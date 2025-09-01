##  Analyse du Scan WPScan (avec API)
###  Informations générales

Serveur : Apache/2.4.58 (Unix) + OpenSSL + mod_perl.

WordPress : Version 6.8.2 (à jour, dernière version disponible).

Thème actif : Woostify 2.4.2 (également à jour, pas de vulnérabilités connues).

### Vulnérabilités détectées
#1. Problèmes généraux de configuration

XML-RPC activé (xmlrpc.php)
🔹 Risque : attaques de brute force, DoS distribué, relais d’attaques.
🔹 Recommandation : désactiver si inutile ou restreindre via un plugin (Disable XML-RPC).

readme.html exposé
🔹 Risque : divulgation d’informations sur la version de WordPress.
🔹 Recommandation : supprimer ou bloquer l’accès à ce fichier.

Inscription publique activée (wp-login.php?action=register)
🔹 Risque : création de comptes malveillants, spams.
🔹 Recommandation : désactiver si inutile ou ajouter Captcha + validation manuelle.

Uploads directory listé (wp-content/uploads/)
🔹 Risque : accès aux fichiers envoyés → fuite d’informations.
🔹 Recommandation : ajouter un .htaccess ou config Apache pour bloquer le directory listing.

WP-Cron externe activé (wp-cron.php)
🔹 Risque : vulnérable à un déni de service (surcharge de requêtes).
🔹 Recommandation : désactiver WP-Cron par défaut et le remplacer par une tâche CRON système.

#2. Plugins vulnérables
-  Elementor (v.3.30.2 — dernière version 3.31.2)

Vulnérabilités :

Stored XSS (Contributor+) → exploitation via widget Text Path.

Arbitrary File Read (Admin+) → permet la lecture de fichiers sensibles.

Risque : prise de contrôle du site si un compte malveillant est créé ou si un admin est compromis.

Recommandation : mettre à jour immédiatement vers 3.31.2.

- Metform (v.3.8.0 — dernière version 4.0.4)

Vulnérabilités multiples (7 failles recensées) :

CSRF non authentifié

Stored XSS (Contributor+)

Exposition d’informations sensibles (non authentifié)

SSRF (Admin+)

Risque :

Vol de sessions, exécution de scripts malveillants, accès à des informations sensibles.

Recommandation : mise à jour immédiate vers 4.0.4.

- Smart Wishlist (v.1.8.7 — dernière version 1.9.5)

Vulnérabilités :

Disclosure non authentifié de wishlists

SQL Injection (Admin+)

Reflected XSS

Risque : fuite de données utilisateurs, injection SQL (critique).

Recommandation : mise à jour vers 1.9.5.

- Woo Variation Swatches (v.1.0.61 — dernière version 2.2.0)

Vulnérabilité :

Reflected XSS (ancienne faille CVE-2019-14774).

Risque : exécution de script malveillant côté utilisateur.

Recommandation : mise à jour vers 2.2.0.

- WooCommerce (v.9.7.0 — dernière version 10.1.0)

Vulnérabilités :

Stored XSS (Shop Manager+)

SQL Injection (Shop Manager+)

Leak de données personnelles (PII leak, multisite)

Risque :

Compromission du site (XSS & SQLi critiques).

Fuite de données sensibles (RGPD).

Recommandation : mise à jour vers 10.1.0.

## Conclusion

Le site est globalement bien configuré (WordPress + thème à jour), mais les plugins vulnérables représentent un risque critique :

Metform, Elementor et WooCommerce contiennent des failles exploitables qui peuvent mener à une compromission totale du site.

Les problèmes de configuration (XML-RPC, uploads listés, inscriptions ouvertes) augmentent la surface d’attaque.

## Priorité absolue :

Mettre à jour tous les plugins à leur dernière version.

Appliquer les correctifs de configuration (désactivation XML-RPC, directory listing, WP-Cron, etc.).

Mettre en place un plugin de sécurité (Wordfence / iThemes Security) pour bloquer l’énumération d’utilisateurs et ajouter un WAF.
