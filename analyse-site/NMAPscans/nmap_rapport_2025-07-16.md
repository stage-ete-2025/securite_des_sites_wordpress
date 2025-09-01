#  Rapport Nmap – Détection de vulnérabilités sur localhost

 **Date** : 16 juillet 2025  
 **Cible** : localhost (127.0.0.1)  
 **Commande utilisée** :  
```bash
nmap --script vuln localhost

 Objectif : Détecter les vulnérabilités connues sur les services exposés localement (HTTP, HTTPS, MySQL).

### Résumé du Scan
| Port     | Service | État   | Vulnérabilités notables                         |
| -------- | ------- | ------ | ----------------------------------------------- |
| 80/tcp   | HTTP    | Ouvert | TRACE activé, Directory listing, SQLi détectées |
| 443/tcp  | HTTPS   | Ouvert | TLS DH faible, TRACE activé, SQLi possibles     |
| 3306/tcp | MySQL   | Ouvert | Script CVE2012-2122 échoué                      |

###1.  Port 80 - HTTP
#Services détectés :
Apache (serveur web)

WordPress détecté via /wordpress/

phpMyAdmin accessible via /phpmyadmin/

#Vulnérabilités détectées :
## HTTP TRACE activé :
Le serveur répond aux requêtes HTTP TRACE.

+ Peut être utilisé dans des attaques XST (Cross-Site Tracing).

Recommandation : désactiver dans Apache :
          TraceEnable Off
## Répertoires listés :
/icons/, /img/, /webalizer/ ont le directory listing activé.

Risque : fuite d’informations sensibles ou de fichiers temporaires.

Recommandation : ajouter Options -Indexes dans .htaccess.

## SQL Injection (via http-sql-injection) :
De nombreuses URLs de phpMyAdmin sont signalées comme potentiellement vulnérables :

      index.php?lang=en' OR sqlspider

      js/messages.php?v=5.2.1' OR sqlspider

      js/dist/ajax.js?v=5.2.1' OR sqlspider

+ Ces résultats indiquent que phpMyAdmin accepte des paramètres GET pouvant être manipulés.

Recommandation :

Restreindre l’accès à phpMyAdmin (via IP ou login HTTP)

Désactiver son accès si non utilisé

### Autres scripts :
http-fileupload-exploiter : échec (pas de point d’upload vulnérable)

http-stored-xss et http-dombased-xss : pas de faille XSS trouvée

2.  Port 443 - HTTPS
###Services détectés :
Apache avec support TLS

WordPress et phpMyAdmin accessibles en HTTPS

# Vulnérabilités détectées :
### HTTP TRACE (aussi activé en HTTPS) :
Même risque que sur le port 80.

Solution : TraceEnable Off (affecte HTTP/HTTPS)

### Weak SSL DH Parameters (ssl-dh-params) :
Le serveur utilise un groupe Diffie-Hellman faible (1024 bits, Oakley Group 2).

CVE concernée : passive eavesdropping (attaque de type Logjam)

Recommandation :

Modifier la configuration Apache pour renforcer les suites cryptographiques :

     SSLOpenSSLConfCmd DHParameters "/etc/ssl/certs/dhparam.pem"
     
Générer un fichier DH fort avec :

         openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
### SQLi sur HTTPS :
Les mêmes URLs vulnérables en HTTP sont également détectées en HTTPS.

Cela signifie que la vulnérabilité est accessible en clair et chiffré.

3.  Port 3306 - MySQL
### Service détecté :
MySQL Server accessible

# Script vulnérabilité échoué :
mysql-vuln-cve2012-2122 : erreur d’exécution

Ce script teste si un bug dans MySQL permet de contourner l’authentification.

# Recommandation :

Restreindre l’accès à localhost uniquement :

     bind-address = 127.0.0.1
     
Vérifier manuellement que le serveur MySQL est à jour

  4. Répertoires et chemins sensibles détectés
| Chemin                            | Type                         | Recommandation                         |
| --------------------------------- | ---------------------------- | -------------------------------------- |
| `/phpmyadmin/`                    | Interface de gestion BDD     | Restreindre IP ou désactiver           |
| `/wordpress/wp-login.php`         | Interface d’authentification | Protéger par CAPTCHA ou Fail2ban       |
| `/icons/`, `/img/`, `/webalizer/` | Dossiers publics             | Désactiver le listing avec `.htaccess` |

  5. Résumé des recommandations
| Vulnérabilité / Élément | Solution recommandée                            |
| ----------------------- | ----------------------------------------------- |
| HTTP TRACE              | `TraceEnable Off` dans Apache                   |
| Directory listing       | Ajouter `Options -Indexes` dans `.htaccess`     |
| phpMyAdmin exposé       | Restreindre via `.htaccess` ou config Apache    |
| SQL Injection via GET   | Bloquer/filtrer les requêtes GET sensibles      |
| DH Group faible (TLS)   | Générer un groupe DH sécurisé (≥ 2048 bits)     |
| Port MySQL ouvert       | Restreindre à 127.0.0.1 (config `bind-address`) |
