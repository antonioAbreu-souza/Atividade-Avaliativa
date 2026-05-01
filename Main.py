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
                            print(f"id do cliente: {p["id"]}, Nome do cliente: {p["name"]} Idade: {p["idade"]} cpf: {p["cpf"]} telefone: {p["telefone"]} endereço: {p["endereco"]}")                
                    elif op == "2":
                        op = input("Digite o nome do cliente: ")
                        for p in view_pacientes:
                            if op == p["name"]:
                                print(f"id do cliente: {p["id"]}, Nome do cliente: {p["name"]} Idade: {p["idade"]} cpf: {p["cpf"]} telefone: {p["telefone"]} endereço: {p["endereco"]}")                
                    #elif op == "3":

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
                            if p["status"] == "cancelada":
                                status += 1
                            print(f"Total de consultas canceladas: {status}")
                    elif op == "3":
                        print(f"Total de pacientes cadastrados: {len(view_consultas)}")
                    elif op == "4":
                        print(f"total de médicos ativos: {len(view_medico)}")
                    
                        
                            