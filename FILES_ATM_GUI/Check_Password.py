import json

name_of_file: str = "FILES_ATM_GUI/account_file.json"

def Check_password(card_id: int, sel: bool, passw: int):
    listWithNames = ["Numero de cuenta", "Contrasenia", "Balance"]
    
    with open(name_of_file, 'r') as archivojson:
        contenido: list = []
        contenido = json.load(archivojson)
        
    for dictElemt in contenido:
        if(dictElemt[listWithNames[0]]==card_id and \
            dictElemt[listWithNames[1]]==passw):
            if(sel==False):
                return [dictElemt, None, None]
            else:
                return [None, dictElemt, None]
        else:
            continue
        
    return [None, None, "Reintenta la contraseña o vuelve a introducir el id"]
