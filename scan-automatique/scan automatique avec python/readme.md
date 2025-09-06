###Automatisation des scans WordPress (Nmap & WPScan) – Guide d’utilisation
#1) Objectif

Mettre en place un processus automatisé qui :

détecte régulièrement les failles réseau et applicatives d’un site WordPress ;

compile les résultats (ports ouverts, versions et vulnérabilités) ;

envoie un rapport par e-mail à l’administrateur ;

peut être planifié avec cron.

#2) Périmètre et cibles

Instance WordPress locale (ex. http://localhost/wordpress) ou distante.

Cible réseau scannée avec Nmap (ex. localhost ou l’IP du serveur).

Cible applicative scannée avec WPScan (URL du site WordPress).

#3) Architecture du script

Le script s’articule en quatre blocs :

+Collecte réseau (Nmap)
Lance un scan de services (détection de versions) pour recenser ports et bannières.

+Collecte applicative (WPScan)
Interroge l’instance WordPress, détecte la version, le thème, les plugins, et retourne les vulnérabilités connues.
+Options activées :

détection des plugins vulnérables ;

énumération des utilisateurs ;

utilisation d’un API token WPScan pour enrichir la base CVE.

+Génération du rapport
Assemble un rapport texte structuré (en-tête horodaté, section Nmap, section WPScan, résumé).

+Notification e-mail (SMTP)
Envoie le rapport à une ou plusieurs adresses ; support de TLS.

#4) Pré-requis

+++Python 3 installé sur la machine d’audit.

+++Nmap installé (outil de scan réseau).

+++WPScan installé (gem Ruby) et API token actif (compte gratuit WPScan).

+++Accès réseau au site cible.

+++Paramètres SMTP valides (serveur, port, identifiant, mot de passe ou mot de passe d’application) pour l’envoi des courriels.

#5) Paramétrage à adapter

Dans la section configuration du script, renseigner :

URL cible WordPress (ex. http://localhost/wordpress).

Cible Nmap (ex. localhost).

Adresse expéditrice, destinataire(s), serveur SMTP, port, identifiant, mot de passe.

Jeton WPScan API.

Drapeaux d’énumération (plugins vulnérables, utilisateurs).

Chemins éventuels si Nmap ou WPScan ne sont pas dans le PATH.

#6) Fonctionnement détaillé

Initialisation : chargement de la configuration et horodatage de l’exécution.

Scan réseau : exécution d’un scan de versions sur la cible ; consolidation de la sortie (ports, services, versions).

Scan WordPress : exécution de WPScan sur l’URL ; récupération de la version WordPress, du thème actif, des plugins détectés et des vulnérabilités (CVE, sévérités). Si l’option est activée, l’outil énumère également les utilisateurs exposés publiquement.

Construction du rapport : insertion des deux résultats dans un document texte structuré, avec résumé exécutif et points d’attention.

Notification : envoi du rapport par e-mail via SMTP (TLS).

Codes de retour : le script logue les erreurs d’exécution (échec Nmap/WPScan, quotas API, erreur SMTP).

#7) Sorties attendues

Le rapport texte contient typiquement :

Résumé exécutif : date/heure, cible, statut d’envoi mail.

Section Nmap : liste des ports ouverts (HTTP/HTTPS, FTP, MySQL, etc.), versions détectées et éventuels services sensibles (TRACE activé, suites TLS faibles si des scripts Nmap dédiés sont ajoutés).

Section WPScan :

version de WordPress et statut de mise à jour ;

thème actif et version ;

plugins repérés, versions et vulnérabilités connues (identifiants CVE quand disponibles) ;

utilisateurs exposés ;

avertissements (ex. XML-RPC activé, WP-Cron, pages sensibles accessibles).


#8) Planification (cron)

Le script est conçu pour être planifié avec cron (exécution quotidienne, horaires creux).
Recommandations :

créer un utilisateur système dédié aux tâches d’audit ;

rediriger la sortie standard et la sortie d’erreur vers un fichier de log (ex. scan_wordpress.log) ;

mettre en place une rotation des logs (via logrotate) si le fichier grossit.

Dans le rapport, ajoute une capture d’écran de l’édition cron (titre de figure proposé ci-dessous).

#9) Sécurité & conformité

Consentement : ne scanner que des systèmes que tu es autorisé à auditer.

Charge : planifier hors heures de pointe ; éviter les options agressives si l’environnement est fragile.

Secrets : ne pas versionner les identifiants SMTP ni l’API token ; droits Unix restreints sur le script et le fichier de configuration.

Quotas : l’API de WPScan gratuite a un quota journalier ; prévoir une gestion d’erreur si la limite est atteinte.

Preuve : archiver les rapports envoyés (mail ou dossier de sortie) pour la traçabilité.

#10) Dépannage (FAQ)

Pas de résultat WPScan : vérifier l’installation Ruby/gem, le chemin binaire, la connectivité HTTP(s) vers la cible, la validité du token et le quota journalier.

Échec SMTP : contrôler serveur/port, TLS, identifiants, pare-feu ; avec Gmail, utiliser un mot de passe d’application.

Nmap introuvable : vérifier le PATH ou indiquer le chemin complet.

Rapport vide : vérifier les droits d’accès et que la cible répond bien (site démarré).

#11) Pistes d’amélioration

Export JSON/CSV pour un tableau de bord ;

Génération d’un rapport HTML avec scores de sévérité (CVSS) ;

Envoi dans Slack/Teams ;

Ajout de scripts Nmap spécialisés (TLS, HTTP-trace, SSL-DH) ;

Corrélation avec un historique pour détecter les régressions.


