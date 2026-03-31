import feedparser
import requests
import time
import os

# 1. Configuration

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
KEYWORDS = ["cybersécurité", "attaque", "faille de sécurité"]

# Liste des sources (ex: Google News Tech, HackerNews, Dev.to)

RSS_URLS = [
    "https://news.google.com/rss/search?q=technology&hl=fr&gl=FR&ceid=FR:fr",
    "https://dev.to/feed",
    "https://feeds.feedburner.com/TheHackersNews"
    "https://www.lemondeinformatique.fr"
    "https://cert.ssi.gouv.fr"
    "https://www.zataz.com"
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


