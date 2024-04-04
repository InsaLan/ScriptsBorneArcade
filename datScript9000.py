import sys

from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import *

from utils.input import *
from utils.utils import *

from utils.collection import *
from utils.steam import *

def main():

    root = ConsoleMenu("La borne d'arcade scripts", 
                       "\"Même si aucun lien de parenté avec élisabeth, je me sent comme une borne\" - Pixelbo",
                       formatter=menu_format)

    collec_smenu = SubmenuItem("Création de collections/thèmes", collec_cmenu)
    steam_smenu = SubmenuItem("Mettre à jour les entrées steam", steam_cmenu)
    
    root.append_item(collec_smenu)
    root.append_item(steam_smenu)

    # Show the menu
    root.start()
    root.join()


if __name__ == "__main__":
    main()