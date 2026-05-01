# 🗂️ Task Manager Pro (Python + SQLite + Tkinter)

Gerenciador de tarefas desenvolvido com foco em praticar a integração
entre banco de dados relacional (**SQLite**) e interfaces gráficas
(**Tkinter**).\
O projeto oferece suporte tanto via **Interface Gráfica (GUI)** quanto
via **Terminal (CLI)**.

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   **Interface Gráfica (GUI)**\
    Ambiente amigável desenvolvido com Tkinter.

-   **Modo Terminal (CLI)**\
    Versão completa para gerenciamento rápido via linha de comando.

-   **Persistência de Dados**\
    Utilização de banco de dados SQLite3.

-   **Organização de Dados**\
    Listagem tabular alinhada e tratamento de textos longos.

------------------------------------------------------------------------

## 📁 Estrutura do Projeto

``` bash
.
├── ui.py          # Ponto de entrada da Interface Gráfica
├── main.py        # Ponto de entrada da versão CLI
├── tasks.py       # Funções CRUD e regras de negócio
├── database.py    # Inicialização e conexão com o banco
├── reports.py     # Geração de relatórios e estatísticas
```

------------------------------------------------------------------------

## ⚙️ Como Executar

### 1. Inicializar o banco de dados

``` bash
python database.py
```

### 2. Executar a Interface Gráfica (recomendado)

``` bash
python ui.py
```

### 3. Executar via Terminal (CLI)

``` bash
python main.py
```

------------------------------------------------------------------------

## 📌 Próximas Melhorias

-  Filtros de prioridade na interface gráfica
-  Janela de relatórios visuais
-  Alertas visuais para tarefas próximas do vencimento

------------------------------------------------------------------------

## 👨‍💻 Autor

Desenvolvido por Giovanni Cabral como projeto de portfólio.