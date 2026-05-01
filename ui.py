import tkinter as tk
from tasks import add_task, list_tasks, delete_task, update_status

# --- CONFIGURAÇÕES DE ESTILO ---
COR_FUNDO = "#f4f4f9"
COR_CARD = "#ffffff"
COR_TEXTO = "#000000" 
AZUL_MODERNO = "#4a90e2"
FONTE_SANS = ("Arial", 10, "bold")

# --- FUNÇÕES ---
def salvar_tarefa():
    texto = entry_tarefa.get()
    prioridade = prioridade_var.get()
    if texto:
        add_task(texto, prioridade, "2026-04-30")
        entry_tarefa.delete(0, tk.END)
        atualizar_lista()

def atualizar_lista():
    lista_visual.delete(0, tk.END)
    tarefas = list_tasks(None)
    
    # Cabeçalho 
    header = f"{'ID':<4} | {'TAREFA':<50} | {'PRIORIDADE':<10} | {'STATUS'}"
    lista_visual.insert(tk.END, header)
    lista_visual.insert(tk.END, "-" * 85)

    for t in tarefas:
        titulo = t[1]
        # Se o título for maior que 50, corta e coloca "..."
        if len(titulo) > 50:
            titulo = titulo[:47] + "..."
            
        linha = f"{str(t[0]):<4} | {titulo:<50} | {t[2]:<10} | {t[3]}"
        lista_visual.insert(tk.END, linha)

def deletar_selecionada():
    try:
        selecao = lista_visual.curselection()
        if not selecao: return
        
        # Se for a linha do cabeçalho ou do traçado "---", ignora
        if selecao[0] < 2: return 

        texto_linha = lista_visual.get(selecao[0])
        
        # Pega o que está antes da primeira barra
        id_tarefa = texto_linha.split("|")[0].strip()
        
        delete_task(int(id_tarefa))
        atualizar_lista()
        print(f"Tarefa {id_tarefa} deletada!")
    except Exception as e: 
        print(f"Erro ao deletar: {e}")

def concluir_selecionada():
    try:
        selecao = lista_visual.curselection()
        if not selecao: return
        if selecao[0] < 2: return 

        texto_linha = lista_visual.get(selecao[0])

        id_tarefa = texto_linha.split("|")[0].strip()
        
        update_status(int(id_tarefa), "finalizada")
        atualizar_lista()
        print(f"Tarefa {id_tarefa} concluída!")
    except Exception as e: 
        print(f"Erro ao concluir: {e}")

# --- INTERFACE (UI) ---
root = tk.Tk()
root.title("Task Manager Pro")
root.geometry("800x650")
root.configure(bg=COR_FUNDO)

# Título Principal
tk.Label(root, text="GERENCIADOR DE TAREFAS", font=("Arial", 16, "bold"), 
         bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=(20, 15))

# --- ÁREA DE ENTRADA ---
frame_input = tk.Frame(root, bg=COR_FUNDO)
frame_input.pack(pady=5)

tk.Label(frame_input, text="O que precisa ser feito?", bg=COR_FUNDO, fg=COR_TEXTO, font=FONTE_SANS).pack()
entry_tarefa = tk.Entry(frame_input, width=45, font=("Arial", 11), relief="flat", 
                        highlightthickness=1, highlightbackground="#333333")
entry_tarefa.pack(pady=5, ipady=5)

# Prioridade (OptionMenu com tamanho fixo)
tk.Label(frame_input, text="Prioridade:", bg=COR_FUNDO, fg=COR_TEXTO, font=FONTE_SANS).pack(pady=(10, 0))
prioridade_var = tk.StringVar(root)
prioridade_var.set("média")

menu_prio = tk.OptionMenu(frame_input, prioridade_var, "baixa", "média", "alta")
menu_prio.config(bg=COR_CARD, fg=COR_TEXTO, width=22, relief="groove", font=("Arial", 10))
menu_prio.pack(pady=5)

botao_add = tk.Button(root, text="+ Adicionar Tarefa", command=salvar_tarefa, 
                      width=25, bg=AZUL_MODERNO, fg="white", font=("Arial", 10, "bold"), 
                      relief="flat", cursor="hand2")
botao_add.pack(pady=15)

# --- SEÇÃO DA LISTA ---
tk.Label(root, text="SUAS TAREFAS ATUAIS", font=FONTE_SANS, 
         bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=(10, 0))

lista_visual = tk.Listbox(root, width=90, height=12, font=("Courier", 10), 
                          bg=COR_CARD, fg=COR_TEXTO, borderwidth=0, highlightthickness=1, 
                          highlightbackground="#333333", selectbackground=AZUL_MODERNO)
lista_visual.pack(pady=10, padx=30, fill=tk.BOTH, expand=True)

# --- BOTÕES DE AÇÃO ---
frame_acoes = tk.Frame(root, bg=COR_FUNDO)
frame_acoes.pack(pady=15)

botao_concluir = tk.Button(frame_acoes, text="✔ Concluir", command=concluir_selecionada,
                            bg="#ccffcc", fg=COR_TEXTO, width=18, relief="groove", font=("Arial", 9, "bold"))
botao_concluir.pack(side=tk.LEFT, padx=10)

botao_deletar = tk.Button(frame_acoes, text="✖ Deletar", command=deletar_selecionada, 
                          bg="#ffcccb", fg=COR_TEXTO, width=18, relief="groove", font=("Arial", 9, "bold"))
botao_deletar.pack(side=tk.LEFT, padx=10)

# Botão Atualizar
botao_att = tk.Button(root, text="🔄 Atualizar Lista", command=atualizar_lista, 
                      bg=COR_FUNDO, fg=COR_TEXTO, relief="flat", font=("Arial", 9))
botao_att.pack(pady=10)

atualizar_lista()
root.mainloop()