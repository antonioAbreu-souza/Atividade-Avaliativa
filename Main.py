import json
import Funcoes as f

view = f.Ler_archive("users.json")
view_medico = f.Ler_archive("medicos.json")
view_pacientes = f.Ler_archive("pacientes.json")
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
                    f.medicos_cdt()
                    op = input("Digite o que deseja alterar: ")
                    if op =="1":
                        f.cadastrar_medico(view_medico)
                    elif op =="2":
                        f.Editar_medico(view_medico)
        
                            