# Rapport WPScan – 09/07/2025

## Version WordPress :
- 6.8.1 (à jour ✅)

## Thème actif :
- Twenty Twenty-Five v1.2 (à jour ✅)
- Listing activé sur : /wp-content/themes/twentytwentyfive/

## Vulnérabilités / Configurations risquées :
- XML-RPC activé → possible brute force / DDoS
- readme.html exposé → fuite d’infos (version WordPress)
- wp-content/uploads/ listable → fichiers accessibles
- WP-Cron externe activé → doit être limité

## Plugins :
- Non détectés (revoir avec scan agressif et clé API)

## Actions à mener :
- Supprimer readme.html ✅
- Ajouter index.html dans `/uploads` et `/themes/twentytwentyfive/` ✅
- Désactiver XML-RPC ou le limiter
- Relancer WPScan avec `--enumerate ap` + token
