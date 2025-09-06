#!/bin/bash

# ===============================
# Script de sauvegarde WordPress (Bash) pour XAMPP
# ===============================

# Configuration
SITE_PATH="/opt/lampp/htdocs/wordpress"     # Chemin WordPress
BACKUP_DIR="/home/kali/sauvegardes_wp"           # Répertoire des sauvegardes
DB_NAME="wordpress_local2"                         # Nom de la base (changer si nécessaire)
DB_USER="root"                              # Utilisateur MySQL (souvent root sous XAMPP)
DB_PASS=""                                  # Mot de passe (vide par défaut sous XAMPP)
DATE=$(date +%Y-%m-%d-%H%M%S)
BACKUP_PATH="${BACKUP_DIR}/wordpress-backup-${DATE}"

echo "🚀 Lancement de la sauvegarde de ${SITE_PATH}..."

# Création dossier de sauvegarde
mkdir -p "${BACKUP_PATH}" || { echo "❌ Erreur: Impossible de créer le répertoire."; exit 1; }

# Sauvegarde de la base de données avec mysqldump
echo "[+] Export de la base de données..."
/opt/lampp/bin/mysqldump -u${DB_USER}  ${DB_NAME} > "${BACKUP_PATH}/database.sql" \
    || { echo "❌ Erreur export DB."; exit 1; }
echo "✅ Base exportée : ${BACKUP_PATH}/database.sql"

# Sauvegarde des fichiers WordPress
echo "[+] Sauvegarde des fichiers..."
tar -czf "${BACKUP_PATH}/files.tar.gz" -C "${SITE_PATH}" . \
    || { echo "❌ Erreur sauvegarde fichiers."; exit 1; }
echo "✅ Fichiers compressés : ${BACKUP_PATH}/files.tar.gz"

# Nettoyage des anciennes sauvegardes (> 7 jours)
echo "[+] Nettoyage des anciennes sauvegardes..."
find "${BACKUP_DIR}" -type d -name "wordpress-backup-*" -mtime +7 -exec rm -rf {} \;
echo "✅ Nettoyage terminé."

echo "🎉 Sauvegarde complète réalisée avec succès."
