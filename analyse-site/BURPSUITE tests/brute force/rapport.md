#  Test de Brute Force avec Burp Suite

##  Objectif
Évaluer la résistance du mécanisme d’authentification WordPress face à une attaque par brute force ciblant l’utilisateur **oumaima** identifié lors de la phase d’énumération.



##   Méthodologie

1. **Préparation de l’attaque**  
   - Capture de la requête d’authentification envoyée à `/wp-login.php`.  
   - Envoi de cette requête dans l’outil **Intruder** de Burp Suite.  
   - Sélection du champ `password` comme paramètre à tester.  

2. **Liste de mots de passe**  
   - Utilisation de la même wordlist que celle exploitée précédemment dans **WPScan** pour tester différents mots de passe.  

3. **Lancement de l’attaque**  
   - Injection de la liste de mots de passe.  
   - Observation des réponses renvoyées par le serveur afin de détecter un éventuel succès (différence de taille, redirection, ou changement de statut HTTP).



##  Résultats

- **Utilisateur ciblé** : `oumaima`  
- **Nombre de mots de passe testés** : équivalent à la wordlist déjà utilisée dans WPScan.  
- **Résultat** : aucune authentification réussie.  
- **Temps de réponse** : stable, aucune variation significative détectée.  


##   Analyse

- L’attaque brute force **n’a pas permis de trouver un mot de passe valide** pour l’utilisateur `oumaima`.  
- Cependant, l’absence de mécanismes de protection visibles (comme une limitation de tentatives ou un verrouillage temporaire du compte) suggère que le site reste **vulnérable à une attaque prolongée**.  
- En conditions réelles, un attaquant disposant d’une liste de mots de passe plus adaptée pourrait potentiellement compromettre le compte.


## Recommandations

1. **Limiter les tentatives de connexion** à l’aide d’un plugin WordPress (Wordfence, iThemes Security, Limit Login Attempts Reloaded, etc.).  
2. **Mettre en place l’authentification à deux facteurs (2FA)** pour les comptes utilisateurs sensibles.  
3. **Imposer une politique de mots de passe robustes** (longueur minimale, complexité, interdiction d’utiliser des informations personnelles).  
4. **Configurer un mécanisme de blocage côté serveur** (par exemple avec Fail2Ban) pour restreindre les attaques automatisées.  

