import os

from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import *

import xml.etree.ElementTree as ET

from utils.input import *
from utils.utils import *

ESDE_theme_path = "/home/insalan/ES-DE/themes/ThemeBorneArcade/"

def make_collection():
    nom_collection = prompt_str("Nom de la collection: ")
    genre = prompt_str("Genre à prendre en compte: ")
    
    retcode = os.system("./utils/gamelist_creator.sh -c {} -g {}".format(nom_collection, genre))
    if(retcode==0):
        print("\nNormallement, tout va bien !!!\n")
    else:
        print("\nTout va mal 😭!!!\n")

    Screen().input('Appuyez sur entrée pour continuer')

def copy_img(img_path):
    img_to_copy = prompt_str("Mettre le chemin de l'image (.webp) pour cette collection: ")
    
    retcode = os.system("cp {} ".format(img_to_copy) + img_path)
    if(retcode==0):
        print("\nNormallement, tout va bien !!!\n")
    else:
        print("\nTout va mal 😭!!!\n")

    Screen().input('Appuyez sur entrée pour continuer')

def make_theme():
    nom_collection = prompt_str("Nom de la collection: ").lower()
    description = prompt_str("Description à mettre (laisser vide si rien): ")
    manufacturer = prompt_str("Constructeur à mettre (laisser vide si rien): ")
    releaseYear = prompt_str("Année de sortie (laisser vide si rien): ")
    couleur = prompt_str("Couleur du thème en hex 6 char (voir google svp): ")
 
    xml_path = ESDE_theme_path + "_inc/systems/metadata-custom/{}.xml".format(nom_collection)
    img_path = ESDE_theme_path + "_inc/systems/images/{}.webp".format(nom_collection)

    xml_exist = os.path.isfile(xml_path)
    img_exist = os.path.isfile(img_path)

    if img_exist: 
        remplace_img = prompt_yn("Une image pour ce thème existe déjà, voullez-vous la remplacer ? ")
        if remplace_img:
            os.remove(img_path)
            copy_img(img_path)
    else:
       copy_img(img_path)

    if xml_exist:
        print("\nVous êtes entrain d'éditer un thème de collection déjà présent.\n")
        Screen().input('Appuyez sur entrée pour continuer')
    else:
        retcode = os.system("cp ./utils/template.xml " + xml_path)
        if(retcode==0): print("\nNormallement, tout va bien !!!\n")
        else: print("\nTout va mal 😭!!!\n")
        Screen().input('Appuyez sur entrée pour continuer')

    xml_tree = ET.parse(xml_path)
    xml_root = xml_tree.getroot()

    xml_root[0][0].text = nom_collection
    xml_root[0][1].text = description
    xml_root[0][3].text = manufacturer
    xml_root[0][4].text = releaseYear
    xml_root[0][8].text = couleur

    xml_tree.write(xml_path)

collec_cmenu = ConsoleMenu("Création de collections/thèmes", 
                         "Non ce n'est pas le collector de lol", 
                         formatter=menu_format)

collec_make = FunctionItem("Créer/Mettre à jour une collection", make_collection)
theme_make = FunctionItem("Créer/Mettre à jour un thème pour une collection", make_theme)

collec_cmenu.append_item(collec_make)
collec_cmenu.append_item(theme_make)