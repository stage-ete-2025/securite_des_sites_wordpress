

 **AKOUTTIF Imane**
**Date** : 13 juillet 2025
**Outil utilisé** : WPScan v3.8.28
**URL cible** : `http://localhost/wordpress`

---

## 1.  Objectif de l’analyse

L’objectif de cette analyse était d’effectuer un **audit de sécurité sur une installation locale de WordPress** via l’outil WPScan. L’analyse vise à identifier les failles potentielles, configurations à risque et composants obsolètes ou vulnérables.

---

## 2. Commande Utilisée

```bash
wpscan --url http://localhost/wordpress --enumerate vp,vt
```


## 3.  Résultats Détailés

| Élément détecté         | Description                                  | Niveau de Risque | Recommandation                                                                                 |
| ----------------------- | -------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------- |
| **Version WordPress**   | 6.8.1 (à jour)                               |  Faible        | Aucun risque connu, garder le CMS à jour                                                       |
| **Serveur Web**         | Apache/2.4.58, PHP/8.2.12, Perl 5.34.1       |  Moyen         | Masquer les versions via config Apache (`ServerTokens Prod`) et `php.ini` (`expose_php = Off`) |
| **Fichier readme.html** | Présent et accessible                        |  Faible        | Supprimer `readme.html` (`rm readme.html`)                                                     |
| **XML-RPC Activé**      | Interface accessible via `/xmlrpc.php`       |  Moyen         | Désactiver si non utilisé (`functions.php` ou `.htaccess`)                                     |
| **Répertoire Uploads**  | Liste des fichiers activée                   |  Élevé         | Désactiver le listing via `.htaccess` (`Options -Indexes`)                                     |
| **WP-Cron**             | Accès externe autorisé via `wp-cron.php`     |  Moyen         | Limiter son accès ou remplacer par une tâche CRON système                                      |
| **Thème Actif**         | Astra v4.11.5 (à jour)                       |  Faible        | Aucun correctif requis actuellement                                                            |
| **Plugins détectés**    | Aucun plugin vulnérable trouvé (scan limité) |  Incomplet     | j'ai pas utilise API token pour liste complète des vulnérabilités                                 |

---


## 5.  Recommandations Générales

2. **Désactiver ou restreindre XML-RPC** si non nécessaire.
3. **Supprimer les fichiers non essentiels exposés au public** (`readme.html`, etc.).
4. **Désactiver le listing de dossiers** via `.htaccess` dans `wp-content/uploads/`.
5. **Remplacer WP-Cron** par une tâche planifiée en CRON système si besoin de performance ou de sécurité.
6. **Vérifier régulièrement les mises à jour** des thèmes, plugins et WordPress.

---



## 7.  Conclusion

L’instance WordPress auditée est globalement à jour et bien configurée, mais plusieurs points techniques doivent être renforcés pour réduire la surface d’attaque. L’utilisation d’un token WPScan ainsi que la mise en place de configurations serveur renforcées sont vivement recommandées.


