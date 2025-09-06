####Étude de cas : Vulnérabilité XSS dans les commentaires WordPress
#1) Contexte

Dans le cadre de l’audit de sécurité réalisé sur une instance locale de WordPress, nous avons analysé différents points d’entrée utilisateurs afin de vérifier la robustesse du CMS contre les attaques applicatives.
L’un des tests a porté sur la fonctionnalité des commentaires des articles.

L’objectif était de vérifier si les données soumises par un utilisateur dans un champ de commentaire étaient correctement validées et échappées avant d’être affichées dans le navigateur.

#2) Méthodologie

Outil utilisé : Burp Suite Community Edition.

Étape 1 : Interception de la requête POST envoyée lors de l’ajout d’un commentaire.

Étape 2 : Modification du champ comment pour y injecter un payload XSS.

Étape 3 : Observation du rendu côté navigateur afin de détecter l’exécution du script.

Payload utilisé :

<script>alert('XSS')</script>

#3) Résultats
a) Capture Burp Suite

La requête interceptée et modifiée montre l’injection du code malveillant dans le champ comment.

Figure 1 – Injection XSS dans le champ commentaire via Burp Suite

b) Capture navigateur

Lors de l’affichage de l’article contenant le commentaire injecté, une boîte de dialogue JavaScript s’est exécutée automatiquement, preuve que le script a été interprété par le navigateur.

Figure 2 – Exécution du script XSS lors de l’affichage du commentaire

#4) Analyse de la vulnérabilité

La faille est un XSS stocké (Stored Cross-Site Scripting) :
Le script malveillant est enregistré dans la base de données WordPress et exécuté à chaque affichage du commentaire.

Impact potentiel :

Vol de cookies de session (compromission de comptes administrateurs).

Défacement du site (insertion de contenu malveillant).

Redirection des utilisateurs vers un site externe contrôlé par un attaquant.

Escalade d’attaques (exfiltration de données, installation de malware).

#5) Recommandations

Pour corriger et prévenir ce type de vulnérabilité :

#Validation côté serveur :

Rejeter toute balise HTML/JavaScript dans les champs de commentaires.

Mettre en place une validation stricte via les fonctions WordPress (sanitize_text_field, esc_html, etc.).

##Échappement des sorties :

S’assurer que tous les champs affichés dans le navigateur sont passés par esc_html() ou wp_kses().

##Utilisation de plugins de sécurité :

Ex : Wordfence, Sucuri, qui incluent des filtres anti-XSS.

##Mise à jour régulière :

Maintenir WordPress, thèmes et plugins à jour afin de bénéficier des correctifs de sécurité.

##Option avancée :

Mettre en place un WAF (Web Application Firewall) pour filtrer les requêtes malveillantes avant qu’elles n’atteignent le serveur.

#6) Conclusion

Le test a démontré la présence d’une vulnérabilité XSS stockée dans le système de commentaires WordPress.
Cette faille peut être exploitée par un attaquant pour compromettre la sécurité des utilisateurs et administrateurs du site.

L’application des recommandations proposées est indispensable pour réduire le risque d’exploitation et renforcer la sécurité globale du CMS.
