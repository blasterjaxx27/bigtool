import os

def display_big_tool():
    # Afficher "BigTool" en caractères spéciaux
    big_tool = """
BBBBB  III  GGGG  TTTTT  OOO    OOO   L
B   B   I   G       T   O   O  O   O  L
BBBBB   I   G  GG   T   O   O  O   O  L
B   B   I   G   G   T   O   O  O   O  L
BBBBB  III   GGG    T    OOO    OOO   LLLLL
"""
    print(big_tool)

def download_youtube_video():
    # Ouvrir ip_info.py
    os.system("python ip_info.py")

def open_number_info():
    # Ouvrir number_info.py
    os.system("python number_info.py")

def open_server_info():
    # Ouvrir server_info.py
    os.system("python token_force.py")

def open_spam():
    # Ouvrir spam.py
    os.system("python spam.py")

def open_raid_raid():
    #ouvrir raid-raid.py
    os.system("python raid_raid.py")

def open_nitro():
    # ouvrir nitro.py
    os.system("python nitro.py")

def open_illegal():
    #ouvrir illegal.py
    os.system("python illegal.py")

def open_gen_token():
    # ouvrir gen_token.py
    os.system("python gen_token.py")

def main():
    # Afficher le titre "BigTool" en caractères spéciaux
    display_big_tool()

    # Afficher le menu
    print("\nMenu:")
    print("1) IP info")
    print("2) Number info ")
    print("3) id to token")
    print("4) Spam message")
    print("5) bot raid")
    print("6) nitro generator")
    print("7) illegal website")
    print("8) token generator")

    # Demander à l'utilisateur de faire un choix
    choice = input("\nChoisissez une option: ")

    # Exécuter l'action correspondante au choix de l'utilisateur
    if choice == "1":
        download_youtube_video()
    elif choice == "2":
        open_number_info()
    elif choice == "3":
        open_server_info()
    elif choice == "4":
        open_spam()
    elif choice == "5":
        open_raid_raid()
    elif choice == "6":
        open_nitro()
    elif choice == "7":
        open_illegal()
    elif choice == "8":
        open_gen_token()
    else:
        print("Choix invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
