_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.28
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[32m[+][0m URL: http://localhost/wordpress/ [::1]
[32m[+][0m Started: Thu Jul 10 18:30:37 2025

Interesting Finding(s):

[32m[+][0m Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.58 (Unix) OpenSSL/1.1.1w PHP/8.2.12 mod_perl/2.0.12 Perl/v5.34.1
 |  - X-Powered-By: PHP/8.2.12
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[32m[+][0m XML-RPC seems to be enabled: http://localhost/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[32m[+][0m WordPress readme found: http://localhost/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[32m[+][0m Upload directory has listing enabled: http://localhost/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[32m[+][0m The external WP-Cron seems to be enabled: http://localhost/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[32m[+][0m WordPress version 6.8.1 identified (Latest, released on 2025-04-30).
 | Found By: Rss Generator (Passive Detection)
 |  - http://localhost/wordpress/feed/, <generator>https://wordpress.org/?v=6.8.1</generator>
 |  - http://localhost/wordpress/comments/feed/, <generator>https://wordpress.org/?v=6.8.1</generator>

[32m[+][0m WordPress theme in use: twentytwentyfive
 | Location: http://localhost/wordpress/wp-content/themes/twentytwentyfive/
 | Latest Version: 1.2 (up to date)
 | Last Updated: 2025-04-15T00:00:00.000Z
 | Readme: http://localhost/wordpress/wp-content/themes/twentytwentyfive/readme.txt
 | [31m[!][0m Directory listing is enabled
 | Style URL: http://localhost/wordpress/wp-content/themes/twentytwentyfive/style.css?ver=1.2
 | Style Name: Twenty Twenty-Five
 | Style URI: https://wordpress.org/themes/twentytwentyfive/
 | Description: Twenty Twenty-Five emphasizes simplicity and adaptability. It offers flexible design options, suppor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 1.2 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://localhost/wordpress/wp-content/themes/twentytwentyfive/style.css?ver=1.2, Match: 'Version: 1.2'

[32m[+][0m Enumerating Vulnerable Plugins (via Passive Methods)

[34m[i][0m No plugins Found.

[32m[+][0m Enumerating Vulnerable Themes (via Passive and Aggressive Methods)

 Checking Known Locations -: |==============================================|
[32m[+][0m Checking Theme Versions (via Passive and Aggressive Methods)

[34m[i][0m No themes Found.

[32m[+][0m Enumerating Users (via Passive and Aggressive Methods)

 Brute Forcing Author IDs -: |==============================================|

[34m[i][0m User(s) Identified:

[32m[+][0m imane
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - http://localhost/wordpress/wp-json/wp/v2/users/?per_page=100&page=1
 |  Rss Generator (Aggressive Detection)
 |  Author Sitemap (Aggressive Detection)
 |   - http://localhost/wordpress/wp-sitemap-users-1.xml
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[33m[!][0m No WPScan API Token given, as a result vulnerability data has not been output.
[33m[!][0m You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[32m[+][0m Finished: Thu Jul 10 18:32:41 2025
[32m[+][0m Requests Done: 665
[32m[+][0m Cached Requests: 46
[32m[+][0m Data Sent: 183.929 KB
[32m[+][0m Data Received: 316.927 KB
[32m[+][0m Memory used: 268.488 MB
[32m[+][0m Elapsed time: 00:02:03
# Rapport d’analyse WPScan (wpscan-analyse-result2.md)

## Résumé du scan WPScan sur le site http://localhost/wordpress/

**Date du scan :** 10 juillet 2025

---

### Informations intéressantes détectées :

- **Serveur Web :** Apache/2.4.58 (Unix) avec OpenSSL/1.1.1w, PHP 8.2.12 et mod_perl.
- **XML-RPC activé** : Le fichier `xmlrpc.php` est accessible, ce qui peut être une porte d’entrée pour certaines attaques (ex: pingback, brute force).
- **Fichier readme.html présent** : Le fichier `readme.html` de WordPress est accessible publiquement, ce qui peut aider un attaquant à connaître la version exacte.
- **Listing activé sur le dossier Uploads** : L’accès à `wp-content/uploads/` affiche la liste des fichiers, ce qui peut révéler des informations sensibles.
- **WP-Cron externe activé** : Le fichier `wp-cron.php` est accessible, ce qui peut être exploité dans certaines attaques DDoS.
- **Version WordPress détectée : 6.8.1** (dernière version à jour au 30 avril 2025).
- **Thème utilisé :** Twenty Twenty-Five version 1.2 (à jour), avec listing du dossier activé (potentiel risque d’exposition).

---

### Plugins et thèmes vulnérables :

- Aucun plugin vulnérable détecté.
- Aucun thème vulnérable détecté.

---

### Utilisateurs identifiés :

- `imane` — utilisateur trouvé via différentes méthodes (flux RSS, API JSON, sitemap utilisateurs, brute force des IDs).

---

### Notes :

- Le scan n’a pas pu fournir d’informations précises sur les vulnérabilités car aucun token API WPScan n’a été fourni.
- Le nombre de requêtes effectuées est élevé (665), avec un temps total de scan d’environ 2 minutes.

---

## Recommandations

- Désactiver ou limiter l’accès à `xmlrpc.php` si ce n’est pas nécessaire.
- Supprimer ou restreindre l’accès au fichier `readme.html`.
- Désactiver le listing des répertoires (`uploads/` et thème Twenty Twenty-Five).
- Utiliser un token API WPScan pour obtenir des informations de vulnérabilité détaillées.
- Vérifier la sécurité des utilisateurs identifiés et limiter les tentatives de brute force.

