# 📦 Sistema de Gerenciamento de Estoque

> Sistema desenvolvido em Python para controle de estoque de produtos, permitindo gerenciar inventário, verificar prazos de validade e exportar relatórios.

---

## 🚀 Funcionalidades

O sistema oferece um menu interativo completo com as seguintes opções:

1. **Adicionar Produto:** Cadastra um novo item informando nome, quantidade e data de validade (`AAAA-MM-DD`).
2. **Listar Produtos:** Exibe todos os produtos cadastrados atualmente no sistema.
3. **Verificar Validade:** Analisa a validade de um produto específico, alertando se está vencido ou próximo do vencimento (janela de 30 dias).
4. **Consultar Produto:** Busca e exibe os detalhes de um produto específico pelo nome.
5. **Atualizar Produto:** Permite modificar o nome, a quantidade e a validade de um item existente.
6. **Excluir Produto:** Remove um item específico do estoque.
7. **Gerar Produtos:** Preenche o estoque automaticamente com produtos de exemplo (ideal para testes rápidos).
8. **Deletar Estoque Total:** Esvazia todo o banco de dados de produtos (com confirmação de segurança).
9. **Informações:** Exibe uma breve descrição do projeto e dados da autora.
10. **Salvar Estoque:** Exporta os dados atuais do estoque para um relatório formatado em arquivo de texto (`estoque.txt`).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Módulos Nativos:**
  * `json` (Manipulação e armazenamento de dados)
  * `os` (Comandos do sistema operacional, como limpeza de tela)
  * `time` (`sleep` para pausas visuais e fluidez na interface)
  * `datetime` (Manipulação de datas e prazos de validade)

---

## ⚙️ Como Executar o Projeto

1. Certifique-se de ter o **Python** instalado em sua máquina.
2. Baixe ou copie o código fonte do programa (por exemplo, salve como `estoque.py`).
3. Abra o terminal ou prompt de comando na pasta onde o arquivo está salvo.
4. Execute o script com o seguinte comando:

```bash
python estoque.py
