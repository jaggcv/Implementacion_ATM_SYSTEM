
def Recieve_command(comando: int, ) -> bool:
    if comando==1:
        sel=True
    elif comando==2:
        sel=False
    else:
        sel=None
    return sel