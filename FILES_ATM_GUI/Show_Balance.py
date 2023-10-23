
def Show_balance(account2: dict):
    listWithNames = ["Numero de cuenta", "Contrasenia", "Balance"]
    return [account2[listWithNames[0]], account2[listWithNames[2]]]


#if __name__ == "__main__":
#    result = Show_balance({"Numero de cuenta": 12345678,"Contrasenia": 1234,"Balance": 4800.50})
#    print(result)
    