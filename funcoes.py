import os
from classes import Gato, Cachorro

def menu():
    print("---- SISTEMA DE VETERINÁRIA ----")
    print("01 - CADASTRAR ANIMAIS")
    print("02 - LISTAR ANIMAIS")
    print("03 - CONSULTA")
    print("00 - SAIR")
    print("")

    while True:
        try:
            escolha = int(input("Qual opção deseja? \n--> "))
            return escolha
        except Exception as e:
            print(f"Valor incorreto, erro: {e}")
            os.system("pause")
            os.system("cls")


def cadastro():
    while True:
        print("---- CADASTRO DE ANIMAIS ----")
        print("01 - CACHORRO")
        print("02 - GATO")
        print("00 - VOLTAR")
        print("")

        try:
            animal = int(input("Qual opção deseja? \n--> "))
        except Exception as e:
            print(f"Valor incorreto, erro: {e}")
            os.system("pause")
            os.system("cls")
            continue

        match animal:
            case 1:
                os.system("cls")
                print("---- CADASTRO DE CACHORRO ----")
                nome = input("Informe o nome do seu cachorro\n--> ")
                raca = input("Informe a raça do seu cachorro\n--> ")
                dono = input("Informe o seu nome\n--> ")
                idade = int(input("Informe a idade do seu cachorro\n--> "))

                cachorro = Cachorro(nome, raca, dono, idade)

                print("\nCACHORRO CADASTRADO COM SUCESSO")
                os.system("pause")
                os.system("cls")
                return cachorro

            case 2:
                os.system("cls")
                print("---- CADASTRO DE GATO ----")
                nome = input("Informe o nome do seu gato\n--> ")
                cor = input("Informe a cor do seu gato\n--> ")
                dono = input("Informe o seu nome\n--> ")
                idade = int(input("Informe a idade do seu gato\n--> "))

                gato = Gato(nome, cor, dono, idade)

                print("\nGATO CADASTRADO COM SUCESSO")
                os.system("pause")
                os.system("cls")
                return gato

            case 0:
                print("Voltando ao menu anterior...")
                os.system("pause")
                os.system("cls")
                return None

            case _:
                print("Opção inválida")
                os.system("pause")
                os.system("cls")


def listar(lista):
    while True:
        print("---- LISTA DE ANIMAIS ----")
        print("01 - LISTAR TODOS OS ANIMAIS")
        print("02 - LISTAR TODOS OS CACHORROS")
        print("03 - LISTAR TODOS OS GATOS")
        print("00 - VOLTAR")

        try:
            escolha = int(input("Qual opção deseja? \n--> "))
            os.system("cls")
        except Exception as e:
            print(f"Valor incorreto, erro: {e}")
            os.system("pause")
            os.system("cls")
            continue

        match escolha:
            case 1:
                print("---- LISTA DE TODOS OS ANIMAIS ----\n")
                print("ID\tNOME\tIDADE\tESPECIE")
                for i, animal in enumerate(lista, start=1):
                    print(f"{i}\t{animal.getNome()}\t{animal.getIdade()}\t{animal.getEspecie()}")
                os.system("pause")
                os.system("cls")

            case 2:
                print("---- LISTA DE TODOS OS CACHORROS ----\n")
                print("ID\tNOME\tIDADE\tRAÇA\tDONO")
                for i, animal in enumerate(lista, start=1):
                    if animal.getEspecie() == "Cachorro":
                        print(f"{i}\t{animal.getNome()}\t{animal.getIdade()}\t{animal.getRaca()}\t{animal.getDono()}")
                os.system("pause")
                os.system("cls")

            case 3:
                print("---- LISTA DE TODOS OS GATOS ----\n")
                print("ID\tNOME\tIDADE\tCOR\tDONO")
                for i, animal in enumerate(lista, start=1):
                    if animal.getEspecie() == "Gato":
                        print(f"{i}\t{animal.getNome()}\t{animal.getIdade()}\t{animal.getCor()}\t{animal.getDono()}")
                os.system("pause")
                os.system("cls")

            case 0:
                print("Voltando ao menu anterior...")
                os.system("pause")
                os.system("cls")
                break

            case _:
                print("Opção inválida")
                os.system("pause")
                os.system("cls")


def consulta(lista):
    while True:
        print("---- CONSULTA DE ANIMAIS ----")
        print("01 - DIAGNOSTICAR O ANIMAL")
        print("02 - VERIFICAR DIAGNÓSTICO DO ANIMAL")
        print("00 - VOLTAR")

        try:
            escolha = int(input("Qual opção deseja? \n--> "))
        except Exception as e:
            print(f"Valor incorreto, erro: {e}")
            os.system("pause")
            os.system("cls")
            continue

        match escolha:
            case 1:
                print("---- DIAGNOSTICANDO OS ANIMAIS ----")
                print("ID\tNOME\tESPECIE")
                for i, animal in enumerate(lista, start=1):
                    print(f"{i}\t{animal.getNome()}\t{animal.getEspecie()}")
                id_sel = int(input("Qual animal deseja consultar? \n--> "))
                diag = input("Informe o diagnóstico do animal\n--> ")
                lista[id_sel - 1].setDiag(diag)

                print("\nDIAGNÓSTICO CADASTRADO COM SUCESSO")
                os.system("pause")
                os.system("cls")

            case 2:
                print("---- VERIFICANDO DIAGNÓSTICO DO ANIMAL ----")
                print("ID\tNOME\tESPECIE")
                for i, animal in enumerate(lista, start=1):
                    print(f"{i}\t{animal.getNome()}\t{animal.getEspecie()}")
                id_sel = int(input("Qual animal deseja verificar? \n--> "))
                print(f"O diagnóstico do animal é: {lista[id_sel - 1].getDiag()}")
                os.system("pause")
                os.system("cls")

            case 0:
                print("Voltando ao menu anterior...")
                os.system("pause")
                os.system("cls")
                break

            case _:
                print("OPÇÃO INVÁLIDA")
                os.system("pause")
                os.system("cls")
