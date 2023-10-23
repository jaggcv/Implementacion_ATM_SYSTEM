import json

name_of_file: str = "FILES_ATM_GUI/account_file.json"

def Withdraw(amount: int, account1: dict):
    listWithNames = ["Numero de cuenta", "Contrasenia", "Balance"]
    cash: int = 0

    with open(name_of_file, 'r') as archivojson:
        contenido: list = []
        contenido = json.load(archivojson)

    if(amount <= account1[listWithNames[2]]):
        cash = amount
        indiceObj = contenido.index(account1)
        contenido.pop(indiceObj)
        account1[listWithNames[2]] = account1[listWithNames[2]] - amount
        contenido.append(account1)

        with open(name_of_file, 'w') as archivojson:
            json.dump(contenido, archivojson)

        return [cash, None]
    else:
        return [None, 'No hay fondos suficientes']
    
#if __name__ == "__main__":
#    resultado = Withdraw(200, {"Numero de cuenta": 12345678,"Contrasenia": 1234,"Balance": 4800.50})
#    print(resultado)
