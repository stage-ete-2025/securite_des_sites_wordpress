##################################Étude de cas : Tests de sécurité sur le champ Upload de fichier
#1) Contexte

Dans le cadre de l’audit de sécurité du site WordPress, un test a été effectué sur le champ de téléchargement de fichier présent dans le formulaire de contact.
L’objectif était de vérifier la robustesse des contrôles côté serveur, notamment :

La validation des extensions autorisées.

La validation du type MIME.

La capacité à bloquer des fichiers malveillants déguisés en images.

#2) Méthodologie

Outil utilisé : Burp Suite Community Edition.

Étape 1 : Interception de la requête d’upload d’image.

Étape 2 : Modification du nom et du type MIME du fichier avant l’envoi.

Étape 3 : Vérification si le serveur accepte ou rejette le fichier.

Les tests suivants ont été réalisés :

a) Test d’extension déguisée

Fichier original : image.png.

Noms testés :

shell.php → rejeté.

shell.png;.php → rejeté.

shell.php.png → accepté (puisque l’extension finale est .png).

b) Test du type MIME

Modification du header Content-Type dans Burp :

image/png → accepté.

application/x-php → rejeté, même si le fichier avait une extension image.

c) Test avec fichier PHP pur renommé

Fichier : shell.php contenant du code PHP.

Renommé en shell.php.png.

Résultat : rejeté par le serveur (contrôle correct du type MIME).

d) Test avancé : Upload d’un fichier .htaccess

Tentative d’upload d’un fichier .htaccess avec la règle :

AddType application/x-httpd-php .jpg


→ Résultat : rejeté par le serveur.

#3) Résultats

Le serveur accepte uniquement les fichiers images valides (png, jpg, jpeg, gif).

Les fichiers PHP déguisés sont correctement bloqués.

Les types MIME incorrects (application/x-php) sont rejetés.

Le test avancé avec .htaccess est également rejeté.

 Figure 1 – Test d’upload avec extension modifiée (shell.php.png accepté)
 Figure 2 – Test rejeté avec shell.php (fichier PHP pur)


#4) Analyse de la vulnérabilité

Le seul cas accepté est un fichier image légitime renommé en shell.php.png.
→ Dans ce scénario, le serveur valide uniquement la dernière extension (.png).

Toutefois, comme le fichier reste une image valide, aucune exécution PHP n’est possible.

Cela montre que les contrôles de sécurité sont en place, mais que le serveur pourrait être vulnérable si la validation des extensions n’était pas correctement configurée.

#5) Recommandations

Forcer la validation stricte des extensions côté serveur (seulement jpg, jpeg, png, gif).

Vérifier le contenu du fichier via la librairie PHP finfo_file() pour s’assurer qu’il correspond bien à une image.

Stocker les fichiers uploadés hors du répertoire web et générer un nom aléatoire pour éviter toute exécution accidentelle.

Bloquer les fichiers suspects contenant des signatures PHP (<?php).

Limiter la taille des fichiers pour éviter les attaques DoS via upload massif.

#6) Conclusion

Le champ d’upload d’images testé ne présente pas de vulnérabilité critique dans l’état actuel :

Les fichiers malveillants déguisés sont correctement rejetés.

Le test avec .htaccess n’a pas abouti.

Cependant, l’acceptation d’un fichier nommé shell.php.png montre que la validation repose uniquement sur l’extension finale. Dans un autre contexte (mauvaise configuration Apache/PHP), cela pourrait constituer une faille exploitable.
