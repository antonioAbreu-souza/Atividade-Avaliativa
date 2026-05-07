import json
import Funcoes as f

view = f.Ler_archive("users.json")
view_medico = f.Ler_archive("medicos.json")
view_pacientes = f.Ler_archive("pacientes.json")
view_prontuarios = f.Ler_archive("prontuarios.json")
view_consultas = f.Ler_archive("consultas.json")
while True:
    f.menu_users()
    op = input("Digite sua opção: ")
    if op == "1":
        if f.validar_admin(view) == True:
            while True:
                f.options()
                op = input("Digite o que deseja acessar: ")
                if op == "1":
                    f.op_cadastrar_user()
                    op1 = input("DIgite sua opção: ")
                    if op1 == "1":
                        f.cadastrar_user(view)
                    elif op1 == "2":
                        f.editar_user(view)
                    elif op1 == "3":
                        f.Remove_user(view)
                    elif op1 == "4":
                        f.reset_password(view)
                    elif op1 == "5":
                        f.view_users(view)
                    
                elif op == "2":
                    f.medicos_cdt()
                    op = input("Digite o que deseja alterar: ")
                    if op =="1":
                        f.cadastrar_medico(view_medico)
                    elif op =="2":
                        f.Editar_medico(view_medico)
                    elif op =="3":
                        for p in view_medico:
                            print(f"id: {p["id_medico"]}, nome do medico: {p["name"]}, especialidade: {p["especialidade"]} e crm: {p["crm"]}")
                            
                        op = int(input("Digite o Id do medico que deseja remover"))
                        for i in view_medico:
                            if op == i["id_medico"]:
                                view_medico.pop(op-1)
                                f.Adicionar_archive(view_medico, "medicos.json")
                                print(f"Usuario {p["name"]} excluido com sucesso")
                            else:
                                print("Id inexistente")
                    elif op == "4":
                        for p in view_medico:
                            print(f"id: {p["id_medico"]}, nome do medico: {p["name"]}, especialidade: {p["especialidade"]} e crm: {p["crm"]}")
                elif op == "3":
                    print("1- Visualizar todos os pacientes")
                    print("2- Buscar pacientes")
                    print("3- Ver historico completo")
                    op = input("Digite a opção")
                    if op == "1":
                        for p in view_pacientes:
                            print(f"id do cliente: {p["id_paciente"]}, Nome do cliente: {p["name"]} ")                
                    elif op == "2":
                        op = input("Digite o nome do cliente: ")
                        for p in view_pacientes:
                            if op == p["name"]:
                                print(f"id do cliente: {p["id_paciente"]}, Nome do cliente: {p["name"]} Idade: {p["idade"]} cpf: {p["cpf"]} telefone: {p["telefone"]} endereço: {p["endereco"]}")                
                    elif op == "3":
                        for p in view_pacientes:
                            print(f"id do cliente: {p["id_paciente"]}, Nome do cliente: {p["name"]} Idade: {p["idade"]} cpf: {p["cpf"]} telefone: {p["telefone"]} endereço: {p["endereco"]}")

                elif op == "4":
                    print("1- Visualizar todas as consultas do sistema")
                    print("2- Consultar agenda geral")
                    op = input("Digite uma opção: ")
                    if op == "1":
                        for p in view_consultas:
                            print(f"id: {p["id"]}, id do paciente: {p["id_paciente"]}, id do medico: {p["id_medico"]}, data: {p["data"]}, horario: {p["hora"]} e status: {p["status"]}")
                    #elif op == "2"
                elif op == "5":
                    print("1- Total de consultas realizadas por periodo")
                    print("2- Total de consultas canceladas")
                    print("3- Quantidade de pacientes cadastrados")
                    print("4- Quantidade de médicos ativos")
                    print("5- Consultas por médico")
                    print("6- Atendimentos realizados no dia")
                    print("7- Pacientes mais atendidos")
                    op = input("DIgite uma opção")
                    if op == "1":
                            op = input("Digite o periodo (ex: 2024-01 ou 2024): ")
                            data = 0
                            for p in view_consultas:
                                if p["data"][:len(op)] == op:
                                    data += 1
                            print(f"Total de consultas no período {op}: {data}")
                    elif op == "2":
                        status = 0
                        for p in view_consultas:
                            if p["status"] == "cancelado":
                                status += 1
                        print(f"Total de consultas canceladas: {status}")
                    elif op == "3":
                        print(f"Total de pacientes cadastrados: {len(view_pacientes)}")
                    elif op == "4":
                        print(f"total de médicos ativos: {len(view_medico)}")
                    elif op == "5":
                        print(len(view_consultas))
                    
                    elif op == "6":
                            finalizado = 0
                            op = input("Digite a data de hoje: ")
                            for p in view_consultas:
                                if p["data"][:len(op)] == op:
                                    if p["status"] == "finalizado":
                                        finalizado +=1
                            print(f"Atendimentos finalizados hoje: {finalizado}")
                            
                elif op =="6":
                    print("Saindo")
                    break        
    elif op == "2":
        print("1- Pacientes")
        print("2- Consultas")
        print("3- Historico")
        print("4- Relatorios")
        op =input("digite a opção: ")
        if op == "1":
            print("1- Cadastrar paciente")
            print("2- Editar paciente")
            print("3- Buscar paciente especifico")
            print("4- Listar todos os pacientes")
            op = input("Digite a sua opção")
            if op == "1":
                name = input("nome do paciente: ")
                idade = int(input("idade do paciente: "))
                cpf = input("Cpf do paciente: ")       
                phone = input("Telefone do paciente: ")
                endereco = input("endereço do paciente")
                id_paciente = len(view_pacientes)+1
                dados = {"id_paciente": id_paciente,
                    "name": name, 
                     "idade": idade,
                     "cpf": cpf,
                     "telefone": phone,
                     "endereco": endereco}
                view_pacientes.append(dados)
                f.Adicionar_archive(view_pacientes,"pacientes.json" )
            elif op == "2":
                for p in view_pacientes:
                    print(f"Id do paciente: {p["id_paciente"]}, Nome: {p["name"]}, Idade: {p["idade"]}, cpf: {p["cpf"]} telefone: {p["telefone"]} e endereço: {p["endereco"]} ")
                op = int(input("Digite o nome do paciente que deseja alterar: "))
                for p in view_pacientes:
                    if op == p["id_paciente"]:
                        print("O que deseja alterar?")
                        print("1- Nome do paciente")
                        print("2- Idade do paciente")
                        print("3- Cpf do paciente")
                        print("4- Telefone do paciente")
                        op = input("Digite a opção")
                        if op == "1":
                            name = input("Digite o novo nome: ")
                            p["name"] = name
                            f.Adicionar_archive(view_pacientes, "pacientes.json")
                        elif op == "2":
                                idade = input("Digite a nova idade")
                                p["idade"] = idade
                                f.Adicionar_archive(view_pacientes, "pacientes.json")
                        elif op == "3":
                                cpf = input("Digite o novo cpf")
                                p["cpf"] = cpf
                                f.Adicionar_archive(view_pacientes, "pacientes.json")
                        elif op == "4":
                                phone = input("Digite o novo numero de telefone: ")
                                p["telefone"] = phone
                                f.Adicionar_archive(view_pacientes, "pacientes.json")
                        elif op == "5": 
                                endereco = input("Digite o novo endereço: ")
                                p["endereco"] = endereco
                                f.Adicionar_archive(view_pacientes, "pacientes.json")
            elif op == "3":
             op = input("Digite o nome do cliente: ")
             for p in view_pacientes:
                if op == p["name"]:
                    print(f"Id do paciente: {p["id_paciente"]}, Nome: {p["name"]}, Idade: {p["idade"]}, cpf: {p["cpf"]} telefone: {p["telefone"]} e endereço: {p["endereco"]} ")
            elif op == "4":
                for p in view_pacientes:
                    print(f"Id do paciente: {p["id_paciente"]}, Nome: {p["name"]}, Idade: {p["idade"]}, cpf: {p["cpf"]} telefone: {p["telefone"]} e endereço: {p["endereco"]} ")    
        elif op == "2":
            print("1- marcar consulta para médico: ")
            print("2- reagendar consulta")
            print("3- cancelar consulta")
            print("4- confirmar presença do paciente: ")
            print("5- listar todas as consultas do dia")
            print("6- listar consultas futuras")
            op1 = input("Digite a opção: ")
            if op1 == "1":
                f.agendar_consulta(view_consultas, view_medico, view_pacientes)
            elif op1 == "2":
                f.reagendar_consulta(view_consultas)
    
    
  