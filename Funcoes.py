import json
def Ler_archive(arquivo):
    with open(arquivo, "r") as archive:
        resultado = json.load(archive)
    return resultado

def Adicionar_archive(dicionario, arquivo):
    with open(arquivo, "w") as archive:
        json.dump(dicionario, archive, indent=2)

#Menu usuarios.
def menu_users():
    print("1- Adminstrador")
    print("2- Médico")
    print("3- Recepcionista")

def validar_admin(lista):
     login = False
     user = input("Digite seu usuario: ")
     password = input("DIgite sua senha: ")
     for p in lista:
            if user == p["user"] and password == p["password"]:
                print(f"Bem vindo Sr {p["name"]}")
                login = True
            else:
                print("Senha Incorreta! ")
            return login
def cadastrar_user(lista):
    name = input("Digite o nome do Usuario: ")
    password = input("Cadastre a senha: ")
    nivel = input("Digite o nível da área: ")
    dados = {"id": id_users,
            "user": name,
            "password": password,
            "nivel": nivel}
    lista.append(dados)
    id_users(lista)
    Adicionar_archive(lista, "users.json")
def op_cadastrar_user():
    print("--------------O que deseja alterar? --------------")
    print("1-Cadastrar usuários do sistema  ")
    print("2-Editar usuários    ")
    print("3-Excluir usuários   ")
    print("4-Resetar senha de usuários    ")
    print("5-Listar todos os usuários    ")
    print("--------------------------------------------------")
def Remove_user(lista):
    for p in lista:
        print(f"Id: {p["id"]}: Usuario: {p["user"]} Nível: {p["nivel"]}")
    op = int(input("Escolha o id do usuario que deseja excluir "))
    for i in lista:
        if op == i["id"]:
            lista.pop(op-1)
            id_users(lista)
            Adicionar_archive(lista, "users.json")
def options():
    print("--------------------------------------------------")
    print("1- Usuarios")
    print("2- médicos")
    print("3- pacientes")
    print("4- Consultas")
    print("5- Relatorios")
    print("--------------------------------------------------")
def reset_password(lista):
    for i in lista:
        print(f"Id: {i["id"]}: Usuario: {i["user"]} Nível: {i["nivel"]}")
    op = int(input("Digite o Id do usuario que quer alterar a senha: "))
    for i in lista:
        if op == i["id"]:
            print(f"Usuario {i["user"]} escolhido.")
            password = input("Digite a nova senha : ")
            i["password"] = password
                                
            Adicionar_archive(lista, "users.json")
def view_users(lista):
    for i in lista:
        print(f"Nome: {i["user"]} Nível: {i["nivel"]}")
def cadastrar_medico(lista):
    name = input("Nome do médico: ")
    especial = input("Digite a especialidade do médico: ")
    crm = input("digite a crm")
    id_medico = len(lista)+1
    dados = { "id_medico": id_medico,
                "name": name,
                "especial": especial,
                "crm": crm,
                        }
    lista.append(dados)
    Adicionar_archive(lista,"medicos.json")      
def Editar_medico(lista):
    for p in lista:
        print(f"id: {p["id_medico"]}, nome do medico: {p["name"]}, especialidade: {p["especialidade"]} e crm: {p["crm"]}")
        op = int(input("Digite o id do médico que deseja "))
        for p in lista:
           if op == p["id_medico"]:
                print("--------------O que deseja alterar? --------------")
                print("1- Nome")
                print("2- Especialidade")
                print("3- Crm")
                op2 = input("digite a opção: ")
                if op2 == "1":
                    nome = input("DIgite a nova especialidade")
                    p["name"] = nome
                    Adicionar_archive(lista, "medicos.json")
                elif op2 == "2":
                    especialidade = input("DIgite a nova especialidade")
                    p["especialidade"] = especialidade
                    Adicionar_archive(lista, "medicos.json")
                elif op2 == "3":
                    crm = input("Digite o novo crm: ")
                    p["crm"] = crm
                    Adicionar_archive(lista, "medicos.json")

    for p in lista:
        print(f"id: {p["id_medico"]} nome do medico: {p["name"]} especialidade: {p["especialidade"]} crm: {p["crm"]}")


#cadastrar médicos: admin
def medicos_cdt():
    print("--------------O que deseja alterar? --------------")
    print("1-Cadastrar médicos   ")
    print("2-Editar médicos     ")
    print("3-Excluir médicos      ")
    print("4-Listar médicos cadastrados   ")
    print("--------------------------------------------------")





#cadastrar paciente: admin
def pacientes_cdt():
    print("1-Visualizar todos os pacientes     ")
    print("2-Buscar pacientes      ")
    print("3-Editar médicos     ")
    print("4-Excluir médicos      ")
    print("5-Ver histórico completo     ")
def mudanças_admin():
    print("--------------Escolha o que deseja alterar--------------")
    print("1- usuarios")
    print("2- medicos")
    print("3- Pacientes")
    print("-------------- Outras opções--------------")
    print("4- Consultas")
    print("5- Relatórios")


    


#Recepcionista.
def perm_recepcionista():
    print("1- Cadastrar paciente")
    print("2- Editar paciente")
    print("3- Buscar paciente específico")
    print("4- Listar todos os pacientes")
    print("5- Visualizar dados completos")
    print("6- Consultas")
    
    
def consultas():
    print("1- Marcar consultas para médico") #Escolhar data e horario dentro
    print("Escolher data e horário")
    print("Reagendar consulta")
    print("Cancelar consulta")
    print("Confirmar presença do paciente")
    print("Listar todas as consultas do dia")
    print("Listar consultas")
    

def Historico():
    print("1- Visualizar consultas anteriores do paciente")
    print("2- Ver datas de atendimentos anteriores")
def Relatórios():
    print("Agenda do dia")
    print("Consultas por data")
    print("Consultas canceladas no período")
    print("pacientes atendidos no dia")
    
def id_users(lista):
    id = 0
    for i in lista:
        id +=1
        i["id"] = id