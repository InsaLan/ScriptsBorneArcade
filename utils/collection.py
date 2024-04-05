import os

from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import *

from utils.input import *
from utils.utils import *


def make_collection():
    nom_collection = prompt_str("Nom de la collection: ")
    genre = prompt_str("Genre à prendre en compte: ")
    
    retcode = os.system("gamelist_creator.sh -c {} -g {}".format(nom_collection, genre))
    if(retcode==0):
        print("\nNormallement, tout va bien !!!\n")
    else:
        print("\nTout va mal 😭!!!\n")

    Screen().input('Appuyez sur entrée pour continuer')

collec_cmenu = ConsoleMenu("Création de collections/thèmes", 
                         "Non ce n'est pas le collector de lol", 
                         formatter=menu_format)

collec_make = FunctionItem("Créer/Mettre à jour une collection", make_collection)

collec_cmenu.append_item(collec_make)