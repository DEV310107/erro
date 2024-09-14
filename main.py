from funcoes import *
import os

sair = None
animais = []

while sair != 0:
    try:
        escolha = menu()  
        os.system("cls")

        match escolha:
            case 1:
                animais.append(cadastro())

            case 2:
                listar(animais)

            case 3:
                consulta(animais)

            case 0:
                print("Saindo do sistema...")
                os.system("pause")
                sair = 0

            case _:
                print("OPÇÃO INVÁLIDA")
                os.system("pause")
                os.system("cls")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        os.system("pause")
        os.system("cls")
