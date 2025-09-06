###Automatisation des sauvegardes WordPress – Script Bash
#1) Objectif

Assurer la sauvegarde régulière d’un site WordPress afin de :

préserver la base de données MySQL/MariaDB ;

sauvegarder les fichiers critiques (thèmes, plugins, médias, configuration) ;

faciliter la restauration rapide en cas d’incident (erreur, attaque, corruption, panne).

#2) Périmètre

Installation WordPress locale (/opt/lampp/htdocs/wordpress dans notre cas).

Base de données MySQL/MariaDB associée.

Répertoire de sauvegarde distinct (/home/kali/sauvegardes_wp) pour isoler les backups du site actif.

#3) Architecture du script

Le script Bash est organisé en plusieurs étapes :

Initialisation

Définition des chemins (site WordPress, dossier de backup).

Génération d’un nom unique basé sur la date et l’heure (wordpress-backup-YYYY-MM-DD-HHMMSS).

Création du répertoire de sauvegarde

Vérifie si le dossier existe, sinon le crée.

Gestion d’erreur si les droits sont insuffisants.

Sauvegarde de la base de données

Export de la base WordPress via mysqldump.

Stockage dans database.sql.

Arrêt immédiat du script si l’export échoue.

Sauvegarde des fichiers WordPress

Compression (tar.gz) de l’intégralité des fichiers (wp-admin, wp-includes, wp-content, wp-config.php, etc.).

Gestion d’erreur si certains fichiers ne sont pas accessibles (droits Unix).

Nettoyage des sauvegardes anciennes

Suppression des répertoires de sauvegarde plus vieux que 7 jours (find -mtime +7).

Journalisation

Messages clairs dans le terminal (✅ réussite, ❌ échec).

Facilement redirigeable vers un fichier log si exécuté en tâche planifiée.

#4) Pré-requis

Bash (inclus par défaut sous Linux).

mysqldump installé (fourni avec MySQL/MariaDB).

Droits de lecture sur le répertoire WordPress et droits d’accès à la base.

Droits d’écriture dans le répertoire de sauvegarde.

#5) Paramétrage à adapter

Dans la section configuration du script, personnaliser :

SITE_PATH → chemin absolu de ton WordPress.

BACKUP_DIR → dossier de sauvegarde (idéalement en dehors de /htdocs).

CLEANUP_DAYS → nombre de jours avant suppression des anciennes sauvegardes.

Identifiants MySQL si ta base est protégée par mot de passe (mysqldump -u user -p password).


#6) Fonctionnement détaillé

Le script s’exécute (manuel ou automatique via cron).

Un dossier daté est créé dans sauvegardes_wp.

La base WordPress est exportée (database.sql).

Tous les fichiers du site sont archivés (files.tar.gz).

Les sauvegardes plus anciennes que 7 jours sont supprimées.

Résultat affiché à l’écran (ou stocké en log si redirection).

#7) Sorties attendues

Exemple de structure d’une sauvegarde :

sauvegardes_wp/
 ├── wordpress-backup-2025-09-02-201003/
 │   ├── database.sql
 │   └── files.tar.gz
 └── wordpress-backup-2025-08-25-113422/


database.sql → dump SQL complet de la base WordPress.

files.tar.gz → archive contenant tous les fichiers WordPress.

#8) Planification (cron)

Pour automatiser la sauvegarde, ajouter dans crontab -e :

0 2 * * * /home/kali/backup.sh >> /home/kali/backup.log 2>&1


➡️ Sauvegarde tous les jours à 2h du matin et enregistre la sortie dans backup.log.

#⚠️ Recommandations :

vérifier régulièrement l’intégrité des archives ;

tester la restauration (fichiers et base) ;

synchroniser les sauvegardes vers un support externe ou cloud.

#9) Sécurité & bonnes pratiques

Permissions : restreindre l’accès au dossier de sauvegarde (chmod 700).

Rotation : supprimer automatiquement les anciennes sauvegardes pour éviter le remplissage du disque.

Redondance : copier les sauvegardes sur un autre disque ou serveur.

Logs : centraliser les logs pour détecter des erreurs de sauvegarde.

#10) Pistes d’amélioration

Génération de rapports HTML ou e-mail après chaque sauvegarde.

Compression avec chiffrement (gpg ou openssl).

Sauvegarde incrémentielle (rsync) pour réduire la taille.

Intégration avec un plan de reprise après sinistre (DRP).
