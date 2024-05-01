from Config.Util import *
from Config.Config import *
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from tqdm import tqdm
import time 
from plyer import notification 

try:
    import random
    import string
    import json
    import requests
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Nitro Generator")

# Notification avant l'installation des modules
notification_title = 'Installation des modules'
notification_message = 'Lancement de l\'installation des modules...'
notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)

total_iterations = 100

# Barre de progression pour l'installation des modules
progress_bar = tqdm(total=total_iterations, desc="Installation des modules", unit="itérations")

for i in range(total_iterations):
    time.sleep(0.1)  # Simulation de l'installation des modules
    progress_bar.update(1)

progress_bar.close()
print("Téléchargement réussi.")

# Notification après l'installation des modules
notification_title = 'Installation des modules terminée'
notification_message = 'Les modules nécessaires ont été installés avec succès.'
notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)

# Notification avant le chargement du générateur
notification_title = 'Chargement du générateur'
notification_message = 'Lancement du chargement du générateur...'
notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)

# Barre de progression pour le chargement du générateur
generator_iterations = 200
generator_progress_bar = tqdm(total=generator_iterations, desc="Chargement du générateur", unit="itérations")

for i in range(generator_iterations):
    time.sleep(0.1)  # Simulation du chargement du générateur
    generator_progress_bar.update(1)

generator_progress_bar.close()
print("Générateur chargé.")

# Notification après le chargement du générateur
notification_title = 'Chargement du générateur terminé'
notification_message = 'Le générateur a été chargé avec succès.'
notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)

webhook = input(f"{color.RED}\n{INPUT} Webhook ? (y/n) -> {color.RESET}")
if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
    webhook_url = input(f"{color.RED}{INPUT} Webhook URL -> {color.RESET}")
    CheckWebhook(webhook_url)

try:
    threads_number = int(input(f"{INPUT} Threads Number -> {color.RESET}"))
except:
    ErrorNumber()

def send_webhook(embed_content):
    payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }

    headers = {
        'Content-Type': 'application/json'
    }

    requests.post(webhook_url, data=json.dumps(payload), headers=headers)

def nitro_check():
    code_nitro = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(16)])
    url_nitro = f'https://discord.gift/{code_nitro}'
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
    if response.status_code == 200:
        if webhook in ['y']:
            embed_content = {
                'title': f'Nitro Valid !',
                'description': f"**__Nitro:__**\n```{url_nitro}```",
                'color': color_webhook,
                'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                }
            }
            send_webhook(embed_content)
            print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Nitro: {color.WHITE}{url_nitro}{color.GREEN}{reset}")
        else:
            print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Nitro: {color.WHITE}{url_nitro}{color.GREEN}{reset}")
    else:
        print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Status: {color.WHITE}Invalid{color.RED} | Nitro: {color.WHITE}{url_nitro}{color.RED}{reset}")
    
def request():
    threads = []
    try:
        for _ in range(int(threads_number)):
            t = threading.Thread(target=nitro_check)
            t.start()
            threads.append(t)
    except:
        ErrorNumber()

    for thread in threads:
        thread.join()

while True:
    request()
