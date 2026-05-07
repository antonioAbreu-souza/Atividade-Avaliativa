import json
import datetime 
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
    print("2- Recepcionista")
    print("3- Médico")
def validar_recepcionista(lista):
     login = False
     user = input("Digite seu usuario: ")
     password = input("Digite sua senha: ")
     for p in lista:
            if user == p["user"] and password == p["password"] and p["nivel"] == "recepcionista":
                print(f"Bem vindo/a Sr {p["user"]}")
                login = True
            else:
                print("Usuario ou Senha incorreta")
            return login
def validar_admin(lista):
     login = False
     user = input("Digite seu usuario: ")
     password = input("DIgite sua senha: ")
     for p in lista:
            if user == p["user"] and password == p["password"] and p["nivel"] == "admin":
                print(f"Bem vindo Sr {p["name"]}")
                login = True
            else:
                print("Usuario ou Senha incorreta ")
            return login
def cadastrar_user(lista):
    name = input("Digite o nome do Usuario: ")
    password = input("Cadastre a senha: ")
    nivel = input("Digite o nível da área: ")
    id_user = len(lista)+1
    dados = {"id": id_user,
            "user": name,
            "password": password,
            "nivel": nivel}
    lista.append(dados)
    Adicionar_archive(lista, "users.json")
def editar_user(lista):
    for p in lista:
        print(f"id: {p["id"]}, nome do usuario: {p["user"]}, password: {p["password"]} e nivel {p["nivel"]}")
    op = int(input("Digite o id do usuario que deseja "))
    for i in lista:
        if op == i["id"]:
            print("1- Novo nome")
            print("2- Nova senha")
            print("3- Alterar nível")
            op = input("DIgite a opção: ")
            if op == "1":
                nome = input("Digite o novo nome")
                i["user"] = nome
                Adicionar_archive(lista, "users.json")
            elif op == "2":
                password = input("DIgite a nova senha: ")
                i["password"] = password
                Adicionar_archive(lista, "users.json")
            elif op == "3":
                nivel = input("Digite a nova area: ")
                i["nivel"] = nivel
                Adicionar_archive(lista, "users.json")

def op_cadastrar_user():
    print("--------------O que deseja alterar? --------------")
    print("1-Cadastrar usuários do sistema  ")
    print("2-Editar usuários    ")
    print("3-Excluir usuários   ")
    print("4-Resetar senha de usuários    ")
    print("5-Listar todos os usuários     ")
    print("--------------------------------------------------")
def Remove_user(lista):
    for p in lista:
        print(f"Id: {p["id"]}: Usuario: {p["user"]} Nível: {p["nivel"]}")
    op = int(input("Escolha o id do usuario que deseja excluir "))
    for i in lista:
        if op == i["id"]:
            lista.pop(op-1)
            Adicionar_archive(lista, "users.json")
def options():
    print("--------------------------------------------------")
    print("1- Usuarios")
    print("2- médicos")
    print("3- pacientes")
    print("4- Consultas")
    print("5- Relatorios")
    print("6- Sair")
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
                "especialidade": especial,
                "crm": crm,
                        }
    lista.append(dados)
    Adicionar_archive(lista,"medicos.json")      
def Editar_medico(lista):
    for p in lista:
        print(f"id: {p["id_medico"]}, nome do medico: {p["name"]}, especialidade: {p["especialidade"]} e crm: {p["crm"]}")
    op = int(input("Digite o id do médico que deseja "))
    for i in lista:
        if op == i["id_medico"]:
            print("--------------O que deseja alterar? --------------")
            print("1- Nome")
            print("2- Especialidade")
            print("3- Crm")
            op2 = input("digite a opção: ")
            if op2 == "1":
                    nome = input("DIgite o novo Nome")
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
    


#Unico codigo feito com IA(Vou rever e estudar melhor depois)
def agendar_consulta(lista1, lista2, lista3):

    # 1. Médico
    for m in lista2:
        print(f"ID: {m['id_medico']} | {m['name']} | {m['especialidade']}")

    id_medico = int(input("Digite o ID do médico: "))

    medico_existe = False
    for m in lista2:
        if m["id_medico"] == id_medico:
            medico_existe = True
            break

    if medico_existe == False:
        print("Médico não encontrado.")
        return

    # 2. Paciente
    for p in lista3:
        print(f"ID: {p['id_paciente']} | {p['name']}")

    id_paciente = int(input("Digite o ID do paciente: "))

    paciente_existe = False
    for p in lista3:
        if p["id_paciente"] == id_paciente:
            paciente_existe = True
            break

    if paciente_existe == False:
        print("Paciente não encontrado.")
        return

    # 3. Data (AAAA-MM-DD)
    hoje = input("Digite a data de hoje (AAAA-MM-DD): ")
    data = input("Digite a data (AAAA-MM-DD): ")

    if data < hoje:
        print("Não é permitido agendar em datas passadas.")
        return

    # 4. Horário
    hora = input("Digite o horário (HH:MM): ")

    # 5. Verificar conflito de horário
    for c in lista1:
        if c["id_medico"] == id_medico and c["data"] == data and c["hora"] == hora and c["status"] != "cancelado":
            print("Esse médico já tem consulta nesse dia e horário.")
            return

    # 6. Salvar
    nova = {
        "id": len(lista1) + 1,
        "id_paciente": id_paciente,
        "id_medico": id_medico,
        "data": data,
        "hora": hora,
        "status": "agendado"
    }
    lista1.append(nova)
    Adicionar_archive(lista1, "consultas.json")
    print("Consulta agendada com sucesso!")
    
 
 

 

def reagendar_consulta(lista1):

    for p in lista1:
        if p["status"] != "cancelado" and p["status"] != "finalizado":
            print(f"ID: {p['id']} | Paciente ID: {p['id_paciente']} | Médico ID: {p['id_medico']} | {p['data']} {c['hora']} | {p['status']}")
            
    id_consulta = int(input("Digite o ID da consulta: "))
    consulta = "nada"
    for c in lista1:
        if c["id"] == id_consulta:
            consulta = c
            break
    if consulta == "nada":
        print("Consulta não encontrada.")
        return
    if consulta["status"] == "cancelado" or consulta["status"] == "finalizado":
        print("Essa consulta não pode ser reagendada.")
        return
    hoje = input("Digite a data de hoje (AAAA-MM-DD): ")
    data = input("Nova data (AAAA-MM-DD): ")
    if data < hoje:
        print("Não é permitido reagendar para datas passadas.")
        return
    hora = input("Novo horário (HH:MM): ")
    for c in lista1:
        if c["id"] != id_consulta and c["id_medico"] == consulta["id_medico"] and c["data"] == data and c["hora"] == hora and c["status"] != "cancelado":
            print("Esse médico já tem consulta nesse dia e horário.")
            return
    consulta["data"] = data
    consulta["hora"] = hora
    consulta["status"] = "reagendado"
    Adicionar_archive(lista1, "consultas.json")
    print("Consulta reagendada com sucesso!")
    
    
    
