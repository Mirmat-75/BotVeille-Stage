import feedparser
import requests
import time
import os

# 1. Configuration

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
KEYWORDS = KEYWORDS = [
    "cybersécurité",
    "sécurité informatique",
    "sécurité des systèmes d'information",
    "cyber security",
    "network security",
    "sécurité réseau",
    "sécurité système",
    "SOC",
    "SOC analyst",
    "analyste SOC junior",
    "cybersecurity junior",
    "stage cybersécurité",
    "stage sécurité informatique",
    "stage cyber security internship",
    "pentest",
    "pentester junior",
    "ethical hacking",
    "test d'intrusion",
    "vulnérabilité",
    "scan de vulnérabilités",
    "analyse de logs",
    "incident response",
    "gestion des incidents",
    "SIEM",
    "IDS",
    "IPS",
    "firewall",
    "TCP/IP",
    "DNS",
    "DHCP",
    "HTTP",
    "Linux",
    "Windows",
    "Active Directory",
    "Kali Linux",
    "Wireshark",
    "Nmap",
    "Metasploit",
    "Burp Suite",
    "Splunk",
    "ELK",
    "Nessus",
    "Qualys",
    "Python",
    "Bash",
    "PowerShell",
    "SQL",
    "cloud security",
    "AWS",
    "Azure",
    "Docker",
    "Kubernetes",
    "ISO 27001",
    "RGPD",
    "NIST",
    "gestion des risques",
    "TryHackMe",
    "Hack The Box",
    "Root-Me",
    "CTF",
    "capture the flag",
    "analyse réseau",
    "administration système",
    "sécurité cloud",
    "DevSecOps",
    "blue team",
    "red team",
    "forensic",
    "cyber défense",
    "audit sécurité",
    "conformité",
    "GRC",
    "junior",
    "débutant",
    "bac+2",
    "bac+3",
    "stage informatique"
]

# Liste des sources (ex: Google News Tech, HackerNews, Dev.to)

RSS_URLS = [
    "https://fr.indeed.com/France-Emplois-Stage-Cybers%C3%A9curit%C3%A9",
    "https://fr.linkedin.com/jobs",
    "https://www.welcometothejungle.com/fr/jobs",
    "https://www.hellowork.com/fr-fr/stage/mot-cle_cybersecurite.html",
    "https://www.stage.fr/jobs/stage-cybers%C3%A9curit%C3%A9-jobs/",
    "https://efrei.jobteaser.com/fr/job-offers",
    "https://www.letudiant.fr",
    "https://www.studyrama.com",
    "https://www.apec.fr",
    "https://www.meteojob.com",
    "https://www.jooble.org",
    "https://www.monster.fr",
    "https://www.lesjeudis.com",
    "https://scopecyber.fr/stage",
    "https://www.cyberjobs.fr",
    "https://www.welcometothejungle.com/fr/companies/anssi/jobs",
]


# 2. Fonction pour envoyer sur Discord

def send_discord_alert(title, link):
    data = {
        "content": f"🚨 **Veille Info** : {title}\n{link}"
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data)

# 3. Logique principale

def check_feeds():
    print("🔍 Analyse des flux en cours...")
    
    for url in RSS_URLS:
        feed = feedparser.parse(url)
        
        for entry in feed.entries:
            # On vérifie si un mot-clé est dans le titre (insensible à la casse)
            for keyword in KEYWORDS:
                if keyword.lower() in entry.title.lower():
                    print(f"Trouvé: {entry.title}")
                    send_discord_alert(entry.title, entry.link)
                    # Pause pour éviter le spam et respecter les limites
                    time.sleep(1) 
                    break # On évite les doublons pour le même article

# 4. Exécution

if __name__ == "__main__":

    check_feeds()


