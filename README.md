# 🗂️ Task Manager Pro (Python + SQLite + Tkinter)

Gerenciador de tarefas com arquitetura de banco de dados relacional. Este projeto demonstra a integração entre Python, SQL e Interfaces Gráficas (GUI), focando em integridade de dados e experiência do usuário.

---

## 🛠️ Especificações Técnicas

### 🗄️ Camada de Dados (SQLite3)

O projeto utiliza um modelo relacional normalizado para garantir a consistência das informações:

* **Relacionamento 1:N:** Vínculo entre as tabelas `tasks` e `categories` via *Foreign Keys*
* **Consultas Avançadas:**

  * `INNER JOIN` para exibição de dados correlacionados
  * `LEFT JOIN` com funções de agregação (`COUNT`, `GROUP BY`) para o dashboard
* **Integridade:** Constraints para evitar duplicidade de categorias e garantir campos obrigatórios

---

### 🖥️ Interface Gráfica (Tkinter)

* **Dashboard de Estatísticas:** Resumo dinâmico no cabeçalho refletindo o estado global das tarefas por categoria
* **UI Reativa:** Atualização automática da listagem após inserção, conclusão ou deleção
* **Input Inteligente:** Seleção de categorias via menus dinâmicos que previnem erros de entrada

---

## 📁 Estrutura do Sistema

```bash
.
├── ui.py          # Interface Gráfica e Gerenciamento de Eventos
├── tasks.py       # Engine de Negócio e Queries SQL
├── database.py    # Definição do Schema e Criação das Tabelas
├── main.py        # Versão CLI (Command Line Interface)
├── seed_db.py     # Script para povoamento automático de dados para teste
```

---

## ⚙️ Como Utilizar

### 1. Inicialização

Configure a estrutura do banco de dados e as tabelas:

```bash
python database.py
```

### 2. Povoamento (Opcional)

Para testar o dashboard e as listagens com dados reais imediatamente:

```bash
python seed_db.py
```

### 3. Execução

Inicie a interface principal:

```bash
python ui.py
```

---

## 👨‍💻 Autor

Desenvolvido por **Giovanni Cabral**

Focado em desenvolvimento Backend, Engenharia de Dados e automação com Python.
