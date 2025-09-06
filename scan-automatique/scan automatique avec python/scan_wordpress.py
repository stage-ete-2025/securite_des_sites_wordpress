import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ================================
# CONFIGURATION
# ================================
WORDPRESS_URL = "http://localhost/wordpress"
BACKUP_REPORT = "/home/kali/rapport_scan.txt"

# API Token WPScan (à créer sur https://wpscan.com/profile)
WPSCAN_API_TOKEN = "TON_API_TOKEN_ICI"

# Config Email
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "tonemail@gmail.com"
EMAIL_PASSWORD = "mot_de_passe_application"
EMAIL_RECEIVER = "destinataire@gmail.com"

# ================================
# FONCTIONS
# ================================

def run_command(cmd):
    """Exécute une commande système et retourne la sortie"""
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Erreur lors de l'exécution de {cmd}:\n{e.output}"

def generate_report():
    """Exécute les scans et génère un rapport"""
    report = []
    report.append("===== Rapport de scan WordPress =====")
    report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Scan Nmap
    report.append("### Scan Nmap ###")
    nmap_result = run_command("nmap -sV localhost")
    report.append(nmap_result)

    # Scan WPScan avec API token et enumeration des users
    report.append("\n### Scan WPScan ###")
    wpscan_cmd = (
        f"wpscan --url {WORDPRESS_URL} "
        f"--enumerate vp,vt,u "
        f"--api-token {WPSCAN_API_TOKEN}"
    )
    wpscan_result = run_command(wpscan_cmd)
    report.append(wpscan_result)

    # Écriture dans un fichier
    with open(BACKUP_REPORT, "w") as f:
        f.write("\n".join(report))

    return "\n".join(report)

def send_email(report_content):
    """Envoie le rapport par email"""
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = "Rapport de Scan WordPress"

    msg.attach(MIMEText(report_content, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("✅ Email envoyé avec succès.")
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi de l'email : {e}")


# ================================
# MAIN
# ================================
if __name__ == "__main__":
    contenu = generate_report()
    send_email(contenu)
    print(f"📄 Rapport sauvegardé dans : {BACKUP_REPORT}")
