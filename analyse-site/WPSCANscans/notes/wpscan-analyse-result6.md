#  Rapport d’analyse – WPScan sur WordPress local
 
 **Cible** : http://localhost/wordpress  
 **Outil utilisé** : WPScan v3.8.27  
 **Objectif** : Identifier les failles de sécurité présentes sur le site WordPress local (plugins, thèmes, fichiers sensibles, utilisateurs).

---

## 1. Informations générales

- **Serveur web** : Apache 2.4.58 (Unix) avec OpenSSL 1.1.1w et PHP 8.2.12  
- **Version de WordPress** : **6.8.2** (dernière version stable à jour)  
- **Thème actif** : **Astra** (v4.11.5 – obsolète, dernière version disponible v4.11.8)  
- **Plugins installés** :
  - **Contact Form 7** (v5.2.2 – obsolète)
  - **Elementor** (v3.30.2 – obsolète)

---

## 2. Fichiers et fonctionnalités sensibles détectés

###  XML-RPC activé
- Fichier accessible : `http://localhost/wordpress/xmlrpc.php`
- **Risque** : Peut être utilisé pour des attaques par brute-force ou des attaques DDoS par pingback.
- **Référence** : [https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login](https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login)
- **Recommandation** :
  - Désactiver XML-RPC si non utilisé (via le plugin "Disable XML-RPC" ou dans `.htaccess`)

###  WP-Cron activé
- Fichier : `http://localhost/wordpress/wp-cron.php`
- **Risque** : Peut être abusé pour exécuter des scripts en masse ou lancer des DDoS.
- **Recommandation** :
  - Désactiver le cron interne WordPress et utiliser un vrai cron système

###  Fichier readme WordPress exposé
- `http://localhost/wordpress/readme.html`
- **Risque** : Permet aux attaquants de confirmer la version exacte de WordPress utilisée.
- **Recommandation** :
  - Supprimer le fichier `readme.html` du répertoire racine

---

##  3.Thème détecté : Astra (v4.11.5)

- **Version détectée** : 4.11.5  
- **État** : **Obsolète** (dernière version disponible v4.11.8)  
- **Risque** : Les versions non à jour des thèmes peuvent contenir des failles (XSS, LFI, etc.)
- **Recommandation** :  
  - Mettre à jour Astra vers la version 4.11.8  
  - Désactiver les thèmes non utilisés  

---

## 4. Plugins vulnérables détectés

###  Contact Form 7 (v5.2.2 – obsolète)

WPScan a identifié **5 vulnérabilités connues** affectant ta version :

1. **<5.3.2 – Unrestricted File Upload (CVE-2020-35489)**
   - Permet à un attaquant d’uploader un fichier malveillant (shell PHP)
   - Gravité : **critique**
   - Référence : [https://wpscan.com/vulnerability/7391118e](https://wpscan.com/vulnerability/7391118e)

2. **<5.8.4 – Authenticated File Upload (CVE-2023-6449)**  
   - Exploitable par un utilisateur authentifié (rôle Editor+)  
   - Permet l’upload de fichiers arbitraires  

3. **<5.9.2 – Reflected XSS (CVE-2024-2242)**  
   - Injection de scripts via l’URL du formulaire  

4. **<5.9.5 – Unauthenticated Open Redirect (CVE-2024-4704)**  
   - Peut rediriger les visiteurs vers un site malveillant  

5. **<6.0.6 – Order Replay Vulnerability (CVE-2025-3247)**  
   - Exploitable via la fonction de paiement Stripe  

**Recommandation :**
- **Mettre à jour immédiatement** vers la dernière version (v6.1)
- Vérifier les fichiers uploadés récemment (`wp-content/uploads/`) pour déceler des shells

---

###  Elementor (v3.30.2 – obsolète)

1. **<3.30.3 – Contributor+ Stored XSS (CVE-2025-4566)**  
   - Un utilisateur Contributor peut injecter du JavaScript malveillant  
   - Référence : [https://wpscan.com/vulnerability/785a15fe](https://wpscan.com/vulnerability/785a15fe)

**Recommandation :**
- Mettre à jour vers la dernière version v3.30.3

---

## 5. Risques globaux détectés

| Vulnérabilité              | Gravité  |
|----------------------------|----------|
| Plugins obsolètes (Contact Form 7) | 🔴 Critique |
| XML-RPC activé             | 🟠 Moyen |
| WP-Cron activé              | 🟡 Faible |
| Thème obsolète (Astra)      | 🟠 Moyen |
| Elementor obsolète          | 🟠 Moyen |

---

## 6. Recommandations générales

1. **Mettre à jour** :
   - WordPress core (actuellement à jour )
   - Plugins Contact Form 7 et Elementor **immédiatement**
   - Thème Astra vers la dernière version

2. **Désactiver XML-RPC** si non utilisé  
   Dans `.htaccess` :
   ```apache
   <Files xmlrpc.php>
     Order Deny,Allow
     Deny from all
   </Files>
