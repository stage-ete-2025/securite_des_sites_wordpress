# Audit applicatif – Tests du formulaire (Burp Suite)

> **Contexte**  
> Les tests ont été réalisés avec **Burp Suite** sur le formulaire MetForm d’un site WordPress local.  
> Objectif : vérifier la **validation des entrées**, la **résistance aux injections (XSS)** et la **protection CSRF**.

---

## 1) Méthodologie

1. Capture des requêtes via Burp Proxy.
2. Rejeu et modification via **Repeater** pour injecter différents payloads dans les champs :
   - `nom`
   - `email`
   - `message`
3. Suppression volontaire des en-têtes et champs liés aux nonces (`form_nonce`, `X-WP-Nonce`) afin de tester la résistance CSRF.
4. Observation des réponses serveur et du contenu affiché après soumission.

---

## 2) Résultats des tests

### 2.1 Injection HTML / XSS

- **Payload :** `<script>alert(1)</script>` (champ *message*)  
  - Résultat : la balise `<script>` a été supprimée, mais le texte **`alert(1)`** est affiché en clair.  
  - Interprétation : pas d’exécution de JavaScript, mais le filtrage est partiel (contenu non encodé).

---

- **Payload :** `<img src=x onerror=alert(1)>` (champ *message*)  
  - Résultat : le champ est resté vide.  
  - Interprétation : tentative XSS bloquée correctement.

---

- **Payload :** `<a href="http://attacker.com">Lien</a>` (champ *message*)  
  - Résultat : seule la chaîne **« Lien »** est affichée, sans lien cliquable.  
  - Interprétation : la balise `<a>` est supprimée, mais le texte est conservé.

---

- **Payload :** `<h1>Test</h1>` (champ *nom*)  
  - Résultat : la séquence s’affiche **telle quelle**, non interprétée comme balise HTML.  
  - Interprétation : protection correcte, les balises sont affichées comme texte brut.

---

### 2.2 Validation des entrées

- **Email invalide (ex. `aaaaaa`)**  
  - Résultat : accepté sans rejet.  
  - Interprétation : absence de validation stricte côté serveur sur le format des e-mails.

- **Caractères spéciaux (ex. `@@@@` dans *nom*)**  
  - Résultat : acceptés et stockés normalement.  
  - Interprétation : pas de filtrage ou de contrainte particulière sur les caractères.

---

### 2.3 Protection CSRF

- **Action :** suppression de `form_nonce` et de `X-WP-Nonce` dans la requête.  
- **Résultat :** le formulaire est quand même accepté et l’entrée est enregistrée.  
- **Interprétation :** absence de vérification CSRF côté serveur → risque de soumission forcée.

---

## 3) Analyse

- Les tentatives **XSS classiques** sont bloquées, mais le filtrage reste **incomplet** : le contenu est affiché partiellement sans encodage.
- Les **entrées invalides** (emails non valides, caractères spéciaux) passent sans rejet → risque d’injection indirecte ou de pollution de données.
- La **protection CSRF** est insuffisante, car le formulaire peut être soumis sans nonce valide.

---

## 4) Recommandations

1. **Validation côté serveur :**
   - Vérifier systématiquement le format des e-mails.
   - Définir des règles de validation (regex, longueurs maximales).
   - Rejeter les caractères inattendus si non nécessaires.

2. **Encodage / échappement :**
   - Appliquer `esc_html()` ou équivalent avant affichage des champs pour éviter toute exécution HTML/JS.
   - Assurer un encodage uniforme pour tous les champs.

3. **CSRF :**
   - Vérifier la présence et la validité des nonces (`wp_verify_nonce`) côté serveur.
   - Rejeter toute requête sans nonce ou avec nonce invalide.

---

## 5) Conclusion

Le formulaire est relativement protégé contre les XSS classiques, mais :
- La **validation des entrées est faible** (emails invalides acceptés, caractères spéciaux libres).  
- La **protection CSRF est absente** ou inefficace.  

Ces deux points représentent un risque de sécurité notable et nécessitent une **correction prioritaire**.
