# Test de déni de service (DoS) sur le formulaire WordPress avec Burp Suite Intruder

## 1. Contexte du test
Dans le cadre de l’audit de sécurité du site WordPress local, un test de robustesse du formulaire a été effectué à l’aide de l’outil **Burp Suite Intruder**.  
L’objectif était d’évaluer la résistance du serveur face à une attaque par **surcharge de champ de saisie (DoS applicatif)**.

---

## 2. Méthodologie
1. Outil utilisé : **Burp Suite Community Edition** (module Intruder).  
2. Cible : formulaire de contact intégré au site WordPress.  
3. Technique : envoi de plusieurs requêtes contenant un **payload constitué d’une chaîne très longue de caractères `"AAAAAAAA..."`** insérée dans le champ `message`.  
4. Nombre de requêtes envoyées : **27** au total dans la séquence du test.  
5. Observation réalisée sur les colonnes : `Status code`, `Response received`, `Length` et contenu de la `Response`.

---

## 3. Résultats obtenus
- **Statut des réponses** :  
  Toutes les requêtes renvoient un code **200 OK**, ce qui signifie que le serveur a accepté et traité chaque soumission.

- **Taille des réponses** :  
  Les réponses ont une taille relativement constante (**~3260 octets**), ce qui montre que le serveur retourne toujours le même type de réponse indépendamment de la taille du champ soumis.

- **Délai de réponse** :  
  - Certaines requêtes ont été traitées rapidement (600–800 ms).  
  - D’autres ont nécessité plus de temps (**jusqu’à 1900 ms**).  
  - Cette augmentation progressive indique une **charge supplémentaire** pour le serveur.

- **Comportement observé** :  
  Le serveur accepte la soumission et retourne une réponse valide, malgré la taille anormale des données envoyées.  
  Aucun mécanisme de limitation ou de filtrage n’a été détecté.

---

## 4. Analyse
- Le serveur **accepte des champs surdimensionnés** sans aucune restriction.  
- Le traitement de ces données entraîne une **augmentation du temps de réponse**, révélant une vulnérabilité potentielle aux attaques par déni de service.  
- Bien que les requêtes soient toutes traitées, la lenteur progressive observée est un **signe de saturation possible** si l’attaque était réalisée à grande échelle.  
- Dans un contexte réel, une attaque massive de ce type pourrait provoquer :  
  - une **saturation de la mémoire** et du CPU du serveur,  
  - une **dégradation des performances**, voire une **indisponibilité du service**.

---

## 5. Conclusion
Le test DoS via Burp Suite Intruder a permis de mettre en évidence une faiblesse importante :  
- **Absence de mécanisme de validation de la taille des entrées utilisateur.**  
- **Risque d’exploitation pour ralentir ou bloquer le site.**

---

## 6. Recommandations
1. Mettre en place une **limitation stricte** de la taille des champs dans les formulaires (par exemple 255 ou 500 caractères maximum).  
2. Activer un mécanisme de **filtrage côté serveur** pour rejeter automatiquement les entrées trop volumineuses.  
3. Utiliser un **WAF (Web Application Firewall)** pour bloquer les requêtes suspectes et limiter le nombre de soumissions répétées.  
4. Surveiller les logs Apache/WordPress pour détecter des tentatives d’attaques DoS similaires.  

---

## 7. Illustrations
Les figures ci-dessous montrent l’exécution du test dans Burp Suite :  

- **Figure 1 :** Résultats de l’attaque Intruder avec des payloads surdimensionnés.  
- **Figure 2 :** Evolution des temps de réponse au fil des requêtes.  

