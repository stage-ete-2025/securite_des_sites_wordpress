# 🛡️ Rapport WPScan – Audit de sécurité WordPress (avec test de brute force)

📅 **Date du scan** : 16 juillet 2025  
🧪 **Outil utilisé** : WPScan v3.8.27  
🌐 **Site scanné** : http://localhost/wordpress  
🔐 **Brute force ciblé sur utilisateur `oumaima`**  
📦 **Token API WPScan** : ❌ Non utilisé

---

## 🧾 1. Informations générales

| Élément                        | Détail |
|-------------------------------|--------|
| Version WordPress             | 6.8.1 (à jour ✅) |
| Thème actif                   | Astra v4.11.5 (à jour ✅) |
| Plugin détecté                | Elementor v3.30.2 (à jour ✅) |
| Utilisateur scanné            | `oumaima` (détecté + ciblé) |
| Brute-force effectué via      | `xmlrpc.php` |
| Liste de mots de passe utilisée | Générée avec `crunch` |

---

## 🔍 2. Résultats du scan en détail

### 📌 A. En-têtes HTTP détectés

| En-tête         | Valeur |
|-----------------|--------|
| Server          | Apache/2.4.58 (Unix) |
| X-Powered-By    | PHP/8.2.12 (exposé) |

**Risque :** Ces en-têtes exposent des informations techniques exploitables (version Apache, PHP…).

**Recommandation :**
- Masquer `X-Powered-By` dans `php.ini` :
  ```ini
  expose_php = Off
###📌 B. XML-RPC activé

    URL : http://localhost/wordpress/xmlrpc.php

    Statut : Activé (accessible publiquement)

    Utilisé pour le brute-force : ✅ Oui

    Protocole testé : system.multicall (accélère le bruteforce)

    Risque :

    xmlrpc permet des attaques par bruteforce invisibles à l’œil nu (pas de logs HTTP simples)

    Permet aussi des attaques DDoS (pingback)

Recommandations :

    Si non utilisé, désactiver xmlrpc via .htaccess :

    <Files "xmlrpc.php">
      Require all denied
    </Files>

###📌 C. WP-Cron actif

    URL : http://localhost/wordpress/wp-cron.php

    Statut : Actif publiquement

    Risque : peut être déclenché manuellement, surcharge serveur possible

Recommandation :

    Dans wp-config.php :

         define('DISABLE_WP_CRON', true);

   Et bloquer l’accès public si nécessaire avec :

    <Files "wp-cron.php">
      Require all denied
    </Files>

###📌 D. Thème détecté : Astra
Élément	Valeur
Nom	Astra
Version	4.11.5
Statut	✅ À jour
Auteur	Brainstorm Force
URL	https://wpastra.com

➡️ Aucun problème détecté à ce niveau
📌 E. Plugin détecté : Elementor
Plugin	Version	Statut
Elementor	3.30.2	✅ À jour

➡️ Aucun signe de vulnérabilité identifié (base vulnérabilités non chargée)

###🔓 3. Brute-force WordPress via xmlrpc.php
Élément	                Valeur
Méthode	                system.multicall (via XML-RPC)
Utilisateur ciblé	oumaima
Nombre de tentatives	121 mots de passe
Dictionnaire utilisé	Généré avec crunch
Résultat	        ❌ Aucun mot de passe trouvé
Temps d’attaque	~54 secondes
✅ Analyse :

    L’utilisateur oumaima a été découvert lors d’un scan précédent

    Aucun mot de passe testé ne s’est révélé correct

    Le site n’a pas bloqué ou ralenti l’attaque → ⚠️ Vulnérabilité au brute-force silencieux

✅ Recommandations pour mitigation :
Recommandation	                           Description
🔐 Activer 2FA	                           Avec plugin comme Wordfence ou WP 2FA
🚫 Bloquer xmlrpc.php	                   Via .htaccess si inutilisé
🔄 Changer le nom d’utilisateur	   Ne pas utiliser de nom public = identifiant
🔐 Politique de mot de passe fort	   Minimum 12 caractères, lettres + chiffres + symboles
🛡️ Installer un plugin de sécurité	   Exemple : iThemes Security, All-In-One WP Security, Wordfence
🔒 Ajouter un fail2ban	                    Si serveur réel (pour bloquer l’IP après X tentatives)
📊 4. Statistiques du scan
Élément	                    Valeur
Durée du scan	            1 min 54 sec
Requêtes effectuées	     296
Requêtes mises en cache	      6
Données envoyées	     111.7 KB
Données reçues	             774.7 KB
Mémoire utilisée	     280.9 MB
Plugin API utilisé ?	    ❌ Non
