import tkinter as tk
from tkinter import messagebox
from tasks import (
    add_task, list_tasks, delete_task, update_status, 
    list_categories, get_category_id_by_name, get_category_summary
)

# --- CONFIGURAÇÕES DE ESTILO ---
COR_FUNDO = "#f4f4f9"
COR_CARD = "#ffffff"
COR_TEXTO = "#2c3e50" 
AZUL_MODERNO = "#3498db"
VERDE_SUCESSO = "#2ecc71"
FONTE_SANS = ("Arial", 10, "bold")

# --- FUNÇÕES ---
def salvar_tarefa():
    texto = entry_tarefa.get()
    prioridade = prioridade_var.get()
    nome_cat = categoria_var.get()
    
    if texto and nome_cat != "Sem Categorias":
        cat_id = get_category_id_by_name(nome_cat)
        add_task(texto, prioridade, cat_id) 
        
        entry_tarefa.delete(0, tk.END)
        atualizar_lista()

def atualizar_lista():
    lista_visual.delete(0, tk.END)
    tarefas = list_tasks(None)
    
    header = f"{'ID':<4} | {'TAREFA':<35} | {'PRIORIDADE':<10} | {'CATEGORIA':<12} | {'STATUS'}"
    lista_visual.insert(tk.END, header)
    lista_visual.insert(tk.END, "—" * 90)

    for t in tarefas:
        titulo = t[1][:32] + "..." if len(t[1]) > 32 else t[1]
        categoria = t[4]
        linha = f"{str(t[0]):<4} | {titulo:<35} | {t[2]:<10} | {categoria:<12} | {t[3].upper()}"
        lista_visual.insert(tk.END, linha)
    
    atualizar_dashboard()

def atualizar_dashboard():
    stats = get_category_summary()
    if not stats:
        lbl_resumo.config(text="AGUARDANDO DADOS...")
        return
    texto = "  •  ".join([f"{nome}: {qtd}" for nome, qtd in stats])
    lbl_resumo.config(text=f"RESUMO: {texto.upper()}")

def deletar_selecionada():
    try:
        selecao = lista_visual.curselection()
        if not selecao or selecao[0] < 2: return 
        id_tarefa = lista_visual.get(selecao[0]).split("|")[0].strip()
        if messagebox.askyesno("Confirmar", f"Deletar tarefa #{id_tarefa}?"):
            delete_task(int(id_tarefa))
            atualizar_lista()
    except: pass

def concluir_selecionada():
    try:
        selecao = lista_visual.curselection()
        if not selecao or selecao[0] < 2: return 
        id_tarefa = lista_visual.get(selecao[0]).split("|")[0].strip()
        update_status(int(id_tarefa), "finalizada")
        atualizar_lista()
    except: pass

def limpar_placeholder(event):
    if entry_tarefa.get() == "Nova tarefa...":
        entry_tarefa.delete(0, tk.END)

# --- INTERFACE (UI) ---
root = tk.Tk()
root.title("Task Manager Pro")
root.geometry("850x650")
root.configure(bg=COR_FUNDO)

header_frame = tk.Frame(root, bg=AZUL_MODERNO, height=80)
header_frame.pack(fill="x")
tk.Label(header_frame, text="TASK MANAGER PRO", font=("Arial", 18, "bold"), 
         bg=AZUL_MODERNO, fg="white").pack(pady=10)

lbl_resumo = tk.Label(root, text="CARREGANDO...", font=("Arial", 9, "bold"), bg=COR_FUNDO, fg="#7f8c8d")
lbl_resumo.pack(pady=10)

# --- ÁREA DE ENTRADA ---
frame_input = tk.Frame(root, bg=COR_FUNDO)
frame_input.pack(pady=10)

entry_tarefa = tk.Entry(frame_input, width=40, font=("Arial", 12), relief="flat", highlightthickness=1)
entry_tarefa.insert(0, "Nova tarefa...")
entry_tarefa.pack(pady=10, ipady=8)
entry_tarefa.bind("<FocusIn>", limpar_placeholder)

# Menus de Seleção
frame_menus = tk.Frame(frame_input, bg=COR_FUNDO)
frame_menus.pack()

# Prioridade
prioridade_var = tk.StringVar(root, value="média")
tk.Label(frame_menus, text="Prioridade:", bg=COR_FUNDO, font=("Arial", 8)).grid(row=0, column=0)
menu_prio = tk.OptionMenu(frame_menus, prioridade_var, "baixa", "média", "alta")
menu_prio.grid(row=1, column=0, padx=10)

# Categoria (Correção do erro de lista vazia)
lista_bruta = list_categories()
categorias = [c[1] for c in lista_bruta] if lista_bruta else ["Sem Categorias"]
categoria_var = tk.StringVar(root, value=categorias[0])

tk.Label(frame_menus, text="Categoria:", bg=COR_FUNDO, font=("Arial", 8)).grid(row=0, column=1)
menu_cat = tk.OptionMenu(frame_menus, categoria_var, *categorias)
menu_cat.grid(row=1, column=1, padx=10)

# Botão Adicionar 
botao_add = tk.Button(root, text="ADICIONAR TAREFA", command=salvar_tarefa, 
                      bg=VERDE_SUCESSO, fg="white", font=("Arial", 10, "bold"), 
                      relief="flat", width=30, cursor="hand2")
botao_add.pack(pady=20)

# --- LISTA DE TAREFAS ---
lista_visual = tk.Listbox(root, width=95, height=12, font=("Courier", 10), 
                          bg=COR_CARD, fg=COR_TEXTO, borderwidth=0, highlightthickness=1,
                          selectbackground=AZUL_MODERNO)
lista_visual.pack(pady=10, padx=30)

# --- BOTÕES DE CONTROLE ---
frame_btns = tk.Frame(root, bg=COR_FUNDO)
frame_btns.pack(pady=20)

tk.Button(frame_btns, text="✔ CONCLUIR", command=concluir_selecionada, bg="#d4edda", width=15, relief="flat").pack(side="left", padx=10)
tk.Button(frame_btns, text="✖ DELETAR", command=deletar_selecionada, bg="#f8d7da", width=15, relief="flat").pack(side="left", padx=10)

if __name__ == "__main__":
    atualizar_lista()
    root.mainloop()