 
 Outil : WPScan v3.8.27  
 Site analysé : http://localhost/wordpress  
 API WPScan : Activée (plan gratuit)

---

##  1. Informations générales sur le site

| Élément                      | Détail |
|-----------------------------|--------|
| Version WordPress           | 6.8.1 (à jour ) |
| Thème actif                 | Astra v4.11.5 (à jour ) |
| Plugins détectés            | Aucun plugin détecté |
| Utilisateur(s) détecté(s)   | `oumaima` |
| WP-Cron                     | Activé (exécutable publiquement) |

---

## 2. Résultats du scan en détail

###  A. Informations serveur (en-têtes HTTP)

- **Serveur** : Apache/2.4.58 (Unix)
- **PHP** : 8.2.12 (exposé via `X-Powered-By`)

**Risque :** Ces informations techniques peuvent aider un attaquant à cibler des vulnérabilités spécifiques.

**Recommandation :**
- Dans le fichier `php.ini`, désactiver l’exposition de PHP :
  ```ini
  expose_php = Off
  B. wp-cron.php est actif

    URL détectée : http://localhost/wordpress/wp-cron.php

    Statut : Accessible à tous

    Risque :

        Peut être déclenché manuellement

        Risque de spam ou surcharge serveur

Recommandations :

    Désactiver l’exécution automatique dans wp-cron.php :

define('DISABLE_WP_CRON', true);

(Optionnel) Bloquer l’accès via .htaccess :

    <Files "wp-cron.php">
      Require all denied
    </Files>

 C. Thème actif : Astra
Élément	Détail
Nom du thème	Astra
Version	4.11.5
Auteur	Brainstorm Force
URL	https://wpastra.com

Analyse :

    Thème populaire, fiable et à jour

    Aucun fichier listé comme exposé (listing désactivé)

Risque : Aucun risque détecté à cette version

Recommandation : Maintenir le thème à jour
 D. Utilisateur détecté : oumaima

Méthodes de détection utilisées :
Méthode	Détail
REST API JSON	/wp-json/wp/v2/users
Sitemap des utilisateurs	/wp-sitemap-users-1.xml
Redirection via ?author=1	/author/oumaima/
Flux RSS	/feed/
OEmbed API + bruteforce ID	Détection complète confirmée

Risque :

    Le nom d’utilisateur est exposé

    Il peut être ciblé par une attaque par brute-force ou usurpation

Recommandations de sécurité :

    Masquer ou modifier /author/ avec une redirection 404 :

add_action('template_redirect', function () {
    if (is_author()) {
        global $wp_query;
        $wp_query->set_404();
        status_header(404);
        nocache_headers();
    }
});

Désactiver l’endpoint REST :

add_filter('rest_endpoints', function ($endpoints) {
    unset($endpoints['/wp/v2/users']);
    return $endpoints;
});

Désactiver le sitemap des utilisateurs :

add_filter('wp_sitemaps_add_provider', function ($provider, $name) {
    if ('users' === $name) {
        return false;
    }
    return $provider;
}, 10, 2);

Activer 2FA sur /wp-admin
