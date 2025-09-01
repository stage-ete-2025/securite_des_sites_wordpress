##  Analyse du scan WPScan
### Informations générales

Serveur détecté : Apache/2.4.58 (Unix) avec OpenSSL et mod_perl.

Version WordPress : 6.8.2 (à jour → c’est la dernière version au moment du test).

Thème utilisé : Woostify version 2.4.2 (également à jour).

 Pas de vulnérabilité critique directement liée à la version de WordPress ou au thème → bonne pratique de mise à jour.

### Points sensibles détectés

XML-RPC activé

Le fichier xmlrpc.php est accessible.

Risques : attaques de type brute force distribuées, DoS applicatif, ou utilisation comme relai dans des attaques.

#Recommandation :

Désactiver XML-RPC si non utilisé (via plugin comme Disable XML-RPC).

Sinon, restreindre son usage (exemple : uniquement via Jetpack ou services précis).

readme.html exposé

Fichier par défaut de WordPress accessible publiquement.

Risque : divulgation de version (déjà connue par ailleurs, donc redondant).

#Recommandation : 
supprimer ou restreindre l’accès à readme.html.

Inscription ouverte (wp-login.php?action=register)

Permet à tout utilisateur de s’inscrire librement.

Risque : création de comptes malveillants (spams, escalade de privilèges si plugin vulnérable).

#Recommandation : désactiver l’inscription si inutile, ou ajouter un captcha et une validation manuelle.

Répertoire uploads accessible en listing

wp-content/uploads/ affiche son contenu si on accède directement par l’URL.

Risque : exposition de fichiers sensibles, reconnaissance par un attaquant.

#Recommandation : 
ajouter un fichier .htaccess pour désactiver l’indexation, ou configurer Apache/Nginx pour bloquer le directory listing.

WP-Cron externe activé (wp-cron.php)

Script exécuté à chaque visite pour gérer les tâches planifiées.

Risque : vulnérabilité aux attaques de type DoS (surcharge de ressources).

#Recommandation : 
désactiver WP-Cron par défaut (DISABLE_WP_CRON) et utiliser une tâche CRON système (plus fiable et sécurisé).

### Comptes utilisateurs identifiés

WPScan a pu énumérer des utilisateurs → risque important de brute force.

Utilisateurs trouvés : contributeur, root, client, oumaima.

###Risques :

Les noms d’utilisateurs étant exposés, un attaquant peut lancer un brute force sur leurs mots de passe.

La présence d’un compte root est particulièrement dangereuse (cible privilégiée).

#Recommandations :

Renommer ou supprimer les comptes sensibles (root).

Vérifier la robustesse des mots de passe (forcer une politique de mots de passe forts).

Masquer l’énumération d’utilisateurs via un plugin de sécurité ou une configuration spécifique.
### Conclusion

Le site est bien maintenu à jour (WordPress et thème), mais plusieurs failles d’exposition existent :

XML-RPC ouvert,

inscription publique activée,

uploads listés,

énumération des utilisateurs.

Ces points ne sont pas critiques individuellement, mais ensemble ils augmentent la surface d’attaque et exposent le site à des risques de brute force, de DoS ou de divulgation d’informations.

# En production, il faudrait :

Désactiver les fonctionnalités inutiles (XML-RPC, inscription, cron externe).

Restreindre l’accès aux répertoires et fichiers par défaut.

Appliquer une politique stricte sur les utilisateurs.
