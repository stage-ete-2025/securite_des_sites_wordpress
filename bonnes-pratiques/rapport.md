#### Mise en place des bonnes pratiques de sécurité WordPress
#1.Installer un plugin de sécurité

Les deux plus utilisés : Wordfence ou iThemes Security.

##Avec Wordfence (exemple) :

Dans le tableau de bord WordPress → Extensions → Ajouter.

Recherche Wordfence Security.

Clique sur Installer → Activer.

Configure :

Active le pare-feu (Web Application Firewall).

Active les scans automatiques pour détecter fichiers suspects / malwares.

Active l’option bloquer les IP après X tentatives de connexion.

Objectif : ajouter une couche de protection (détection + prévention).

#2.Désactivation de l’éditeur de fichiers (wp-config.php)

Par défaut, WordPress permet d’éditer les fichiers de thème/plugin depuis le dashboard (Apparence → Éditeur).
# Risque : si un attaquant accède à l’admin, il peut injecter du code.

# Solution : dans wp-config.php, ajoute :

define('DISALLOW_FILE_EDIT', true);


#Objectif : empêcher la modification directe du code depuis l’admin.

# 3.Changement du préfixe des tables dans la base de données

Par défaut, WordPress utilise le préfixe wp_.
# Risque : les attaques SQL Injection ciblent souvent wp_users, wp_options, etc.

#Solution :

Sauvegarde ta base (phpMyAdmin ou mysqldump).

Dans phpMyAdmin, renomme toutes les tables :

wp_users → secure_users (ou wpabc_users).

wp_posts → secure_posts, etc.

Mets à jour le fichier wp-config.php :

$table_prefix = 'secure_';


#Objectif : compliquer les attaques SQL automatiques.

# 4.Politique de mots de passe forts

 Par défaut, WordPress propose déjà un générateur de mots de passe forts.
Pour renforcer :

Installe le plugin Force Strong Passwords (ou active l’option dans Wordfence/iThemes).

Exige des mots de passe avec :

au moins 12 caractères,

majuscules, minuscules, chiffres, caractères spéciaux.

Sensibilise les utilisateurs/admins à changer régulièrement leurs mots de passe.

#Objectif : réduire les risques de brute force.

# 5. Activer HTTPS avec un certificat SSL (Let’s Encrypt)

# Si ton site est local, tu peux tester avec un certificat auto-signé.
# Si en ligne : utilise Let’s Encrypt (gratuit).

Exemple avec Apache :

Installe Certbot :

sudo apt install certbot python3-certbot-apache


Génére le certificat :

sudo certbot --apache


Certbot configure automatiquement Apache et WordPress pour forcer HTTPS.

Vérifie dans ton site : http:// → https:// (cadenas vert).

# Dans wp-config.php, tu peux forcer HTTPS dans l’admin :

define('FORCE_SSL_ADMIN', true);


#Objectif : protéger les communications (mots de passe, cookies, données).
