from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import *

from utils.input import *
from utils.utils import *

collec_cmenu = ConsoleMenu("Création de collections/thèmes", 
                         "Non ce n'est pas le collector de lol", 
                         formatter=menu_format)

collec_item1 = MenuItem("Créer/Mettre à jour une collection")

collec_cmenu.append_item(collec_item1)