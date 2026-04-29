from tasks import add_task, list_tasks, delete_task, update_status
from reports import report_by_status, report_by_priority

choice = 1

while choice != 0:
    print("\n\n\n----------------------------------------------------------")
    print("""\n1 - Adicionar tarefa
2 - Listar tarefas
3 - Atualizar status
4 - Deletar tarefa
5 - Relatórios
0 - Sair""")
    try:
        choice = int(input("\nOpção: "))
    except ValueError:
        print("\nErro: Por favor, digite apenas números.")
        continue

    match choice:
        case 1:
            add_title = input("\n\nTítulo da tarefa: ")
            add_priority = input("Prioridade da tarefa [baixa|média|alta]: ").lower()
            add_date = input("Data limite da tarefa: ")
            add_task(add_title, add_priority, add_date)
            print(f"\nTarefa '{add_title}' adicionada com sucesso!")

        case 2:
            priority_or_none = input("\n\nDeseja listar as tarefas com base na prioridade [S | N]? ").capitalize()
            if priority_or_none == 'S':
                list_priority = input("\nDigite a prioridade das tarefas que deseja listar [baixa|média|alta]: ").lower()
                list_tasks(list_priority)
            else:
                list_tasks(None)

        case 3:
            try:
                update_id = int(input("\n\nDigite o ID da tarefa que deseja atualizar: "))
            except ValueError:
                print("\nErro: Por favor, digite apenas números.")
                continue

            update_st = input("Digite o novo status da tarefa [pendente|finalizada]: ").lower()
            update_status(update_id, update_st)
            print(f"Tarefa de ID '{update_id}' atualizada para o status '{update_st}' com sucesso!")

        case 4:
            try:
                delete_id = int(input("\n\nDigite o ID da tarefa que deseja deletar: "))
            except ValueError:
                print("\nErro: Por favor, digite apenas números.")
                continue

            delete_task(delete_id)
            print(f"Tarefa {delete_id} deletada com sucesso!")

        case 5:
            print("\n\n1 - Relatório por prioridade")
            print("2 - Relatório por status")
            try:
                choice_report = int(input("\nOpção: "))
                if choice_report == 1:
                    report_by_priority()
                elif choice_report == 2:
                    report_by_status()
                else:
                    print("Opção de relatório inválida.")
            except ValueError:
                print("Entrada inválida. Digite 1 ou 2.")