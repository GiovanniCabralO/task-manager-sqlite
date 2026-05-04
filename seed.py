import sqlite3
from tasks import add_task, add_category, get_category_id_by_name

# Limpeza do Banco de Dados
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM tasks")
cursor.execute("DELETE FROM categories")
cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('tasks', 'categories')")
conn.commit()
conn.close()

# Criando as Categorias (Necessário para o Relacionamento)
categorias = ["Trabalho", "Estudo", "Pessoal", "Financeiro"]
for cat in categorias:
    add_category(cat)

print("Categorias criadas.")

# Lista de Tarefas (Título, Prioridade, Nome da Categoria)
tarefas = [
    # TRABALHO
    ("Revisar segurança do banco de dados", "alta", "Trabalho"),
    ("Finalizar entrega do projeto principal", "alta", "Trabalho"),
    ("Consertar bug crítico no login", "alta", "Trabalho"),
    ("Backup geral do servidor", "alta", "Trabalho"),
    ("Atualizar documentação do sistema", "média", "Trabalho"),
    
    # ESTUDO
    ("Assistir tutorial de SQL avançado", "baixa", "Estudo"),
    ("Pesquisar novas tecnologias", "média", "Estudo"),
    
    # FINANCEIRO
    ("Pagar impostos da empresa", "alta", "Financeiro"),
    ("Pagar conta de luz", "alta", "Financeiro"),
    
    # PESSOAL
    ("Fazer mercado", "alta", "Pessoal"),
    ("Passear com o cachorro", "média", "Pessoal"),
    ("Organizar estante de livros", "baixa", "Pessoal"),
    ("Caminhada no parque", "baixa", "Pessoal"),
]

# Populando o Banco
for t in tarefas:
    titulo, prioridade, nome_cat = t
    
    cat_id = get_category_id_by_name(nome_cat)
    
    if cat_id:
        add_task(titulo, prioridade, cat_id)

print(f"Banco de dados populado com {len(tarefas)} tarefas com sucesso!")