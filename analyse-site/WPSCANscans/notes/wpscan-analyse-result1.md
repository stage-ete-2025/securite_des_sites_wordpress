# 🛡️ Rapport WPScan pour le resultat 1

🔧 **Outil utilisé** : WPScan v3.8.27  
🌐 **URL analysée** : http://localhost/wordpress

---

## 📍 Informations générales

| Élément                     | Détail |
|----------------------------|--------|
| Version WordPress          | 6.8.1 (à jour ✅) |
| Thème actif                | Twenty Twenty-Five v1.2 (à jour ✅) |
| Plugins détectés           | Aucun plugin trouvé ❗ |
| Utilisateurs détectés      | Aucun (non exposés) |

---

## ⚠️ Vulnérabilités et points faibles identifiés

### 🔹 A. Fichier `xmlrpc.php` activé

- **Statut** : Actif ✅
- **URL** : http://localhost/wordpress/xmlrpc.php
- **Risques** :
  - Attaques par brute-force XML-RPC (system.multicall)
  - DDoS par pingbacks
- **Recommandation** :
  Ajouter dans `.htaccess` à la racine :
  ```apache
  <Files xmlrpc.php>
    Order allow,deny
    Deny from all
  </Files>
  
### 🔹 B. Fichier readme.html exposé

    Statut : Présent ✅

    URL : http://localhost/wordpress/readme.html

    Risque : Fuite d’information (version WP visible)

    Recommandation :
    Supprimer ce fichier :

sudo rm /opt/lampp/htdocs/wordpress/readme.html
### 🔹 C. Directory listing activé
1. /wp-content/uploads/

    Statut : Listing activé ❗

    Risque : Accès public à tous les fichiers médias

    Recommandation :
    Ajouter un fichier vide :

touch /opt/lampp/htdocs/wordpress/wp-content/uploads/index.html

Ou ajouter un fichier .htaccess :

    Options -Indexes

2. /wp-content/themes/twentytwentyfive/

    Statut : Listing activé ❗

    Risque : Fuite de structure de fichiers PHP

    Recommandation :
    Ajouter un .htaccess dans ce dossier :

    Options -Indexes

###🔹 D. Fichier wp-cron.php actif

    Statut : Actif ✅

    URL : http://localhost/wordpress/wp-cron.php

    Comportement : Page vide (normal)

    Risque :

        Exécutable trop souvent

        Peut ralentir ou être abusé

    Recommandation :
    Dans wp-config.php :

    define('DISABLE_WP_CRON', true);

### Limites du scan

    Plugins non détectés malgré leur présence :

        Scan passif

        Aucun token API fourni

    Base de vulnérabilités non utilisée




