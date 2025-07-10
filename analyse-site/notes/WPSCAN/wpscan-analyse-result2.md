
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

