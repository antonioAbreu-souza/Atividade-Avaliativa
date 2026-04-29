import json
import Funcoes as f
Id_Global = 1
view = f.Ler_archive("users.json")
view_pacientes = f.Ler_archive("pacientes.json")
view_medicos= f.Ler_archive("consultas.json")
view_prontuarios = f.Ler_archive("prontuarios.json")
view_consultas = f.Ler_archive("consultas.json")
while True:
    f.menu_users()
    op = input("Digite sua opção")
    if op == "1":
        if f.validar_admin(view) == True:
            while True:
                f.options()
                op = input("Digite o que deseja alterar")
                if op == "1":
                    f.op_cadastrar_user()
                    op1 = input("DIgite sua opção")
                    if op1 == "1":
                     f.cadastrar_user(view)
                
                    elif op1 == "3":
                        f.Remove_user(view)
                    elif op1 == "4":
                        f.reset_password(view)
                    elif op1 == "5":
                            f.view_users(view)
                elif op == "2":
                    name = input("Nome do médico: ")
                    especial = input("Digite a especialidade do médico: ")
                    crm = input("digite a crm")
                    dados = { "id_medico": Id_Global,
                            "name": name,
                             "especial": especial,
                             "crm": crm
                            }
                    Id_Global +=1
                    view.append(dados)
                    f.Adicionar_archive(view, "users.json")
                    
        
                            