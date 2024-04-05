from consolemenu import *
from consolemenu.items import *

def prompt_str(msg):
    pu = PromptUtils(Screen())
    result = pu.input(msg)
    valid =pu.confirm_answer(result.input_string, "\nVous avez entré {}, êtes-vous sûr? \n".format(result.input_string))
    if not valid: prompt_str(msg)
    return result.input_string

def prompt_yn(msg):
    pu = PromptUtils(Screen())
    result = pu.prompt_for_yes_or_no(msg)
    return result