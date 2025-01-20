import json
from time import sleep
from datetime import datetime, timedelta
import os

class Cores: #definição das cores utilizadas
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'

arquivo = 'produtos.json' 
#############################################################################################################################################################################################
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
#############################################################################################################################################################################################
def cabecalho(texto): #usei para definir um estilo de cabeçalho fixo
   sleep(1)
   limpar_tela()
   print("="*30)
   print(texto)
   print("="*30)
   print()
#############################################################################################################################################################################################
def voltar_menu2(): #ele limpa a tela e faz voltar o menu inicial
   limpar_tela()
   menu_inicial()
#############################################################################################################################################################################################
def Gerar_produtos():#para quando o estoque foi excluido ou se o usuario estiver com preguiça de adicionar
    cabecalho(Cores.MAGENTA + '      GERAR DADOS' + Cores.RESET)

    sleep(1)
    print("ADICIONANDO PRODUTOS...............")
    limpar_tela()
    print("PRODUTOS ADICIONADOS COM SUCESSO....")
    sleep(1)

    produtos = [
         {
            'nome_produto': 'Arroz [01]', 
            'quantidade': 100,
            'data_de_validade': (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')#isso aqui faz com que a data de 
            #validade sempre seja diferente a cada geração
        },
        {
            'nome_produto': 'Feijão [02]',
            'quantidade': 50,
            'data_de_validade': (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')
        },
        {
            'nome_produto': 'Macarrão [03]',
            'quantidade': 200,
            'data_de_validade': (datetime.now() + timedelta(days=270)).strftime('%Y-%m-%d')
        },
        {
            'nome_produto': 'Óleo [04]',
            'quantidade': 30,
            'data_de_validade': (datetime.now() + timedelta(days=450)).strftime('%Y-%m-%d')
        },
        {
            'nome_produto': 'Açúcar [05]',
            'quantidade': 150,
            'data_de_validade': (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')
        }
    ]

    with open(arquivo, 'w') as f: #com o arquivo aberto ele escreve nele os items gerados
        json.dump(produtos, f, indent=3)
    print('DADOS INICIAIS GERADOS COM SUCESSO E SALVOS NO ARQUIVO JSON.')

    opçao = int(input("DIGITE 1 PARA VOLTAR AO MENU \n>>>> "))#toda vez que o algoritmo principal 
    #for utilizado ele coloca a opção de contiuar na função ou voltar ao menu
    if opçao == 1:
        voltar_menu2()
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1  imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido 
        #continuar na função apos isso
        sleep(1)
#############################################################################################################################################################################################
def Deletar_estoque():#deleta todo os produtos da lista(estoque)
    cabecalho(Cores.MAGENTA + '      DELETAR ESTOQUE' + Cores.RESET)
    opcao = int(input("TEM CERTEZA QUE DESEJA DELETAR TODOS OS PRODUTOS DO ESTOQUE? (1- SIM 2 - NÃO): "))#coloquei uma confirmação extra caso o usuário escolha 
    #esssa opção sem querer
    
    if opcao == 1:
        with open(arquivo, 'w') as f:#com o arquivo aberto ele escreve nele
            json.dump([], f, indent=3)
        sleep(1)  
        print("DELETANDO ESTOQUE........")
        sleep(1)
        print(Cores.VERDE + "TODOS OS PRODUTOS FORAM DELETADOS COM SUCESSO" + Cores.RESET)
    elif opcao == 2:
        sleep(1)
        print(Cores.VERDE + "AÇÃO CANCELADA. NENHUM PRODUTO FOI REMOVIDO" + Cores.RESET)
    else:
        print(Cores.VERMELHO + "OPÇÃO INVÁLIDA" + Cores.RESET)

    opçao = int(input("DIGITE 1 PARA VOLTAR AO MENU \n>>>> "))#toda vez que o algoritmo principal for utilizado ele coloca a opção de contiuar na função ou voltar ao menu,aqui, deixei apenas o opção voltar disponivel pois faz mais lógica
    if opçao == 1:
        voltar_menu2()
    else:
        print("OPÇÃO INVÁLIDA......")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)
        print("VOLTANDO....")
        sleep(1)
#############################################################################################################################################################################################
def informações():#um simples resumo sobre o que é
    cabecalho(Cores.MAGENTA + '      INFORMAÇÕES' + Cores.RESET)
    print("O programa criado tem o intuito de ajudar uma empresa a gerenciar o sistema de estoque do atacadão.")
    print("O usuário pode adicionar produtos, listar os produtos, verificar a validade dos produtos, consultar um produto, atualizar os dados de um produto,")
    print("excluir um produto, salvar o estoque no formato txt, excluir todo o estoque e gerar um estoque inicial.")
    print("\nMaria Giullia Lima Lopes Barbosa")
    print("\na22402878")
    
    opçao = int(input("DIGITE 1 PARA VOLTAR AO MENU \n>>>> "))#toda vez que o algoritmo principal for utilizado ele coloca a opção de contiuar na função ou voltar ao menu,
    # aqui, deixei apenas o opção voltar disponivel pois faz mais lógica
    if opçao == 1:
        voltar_menu2()
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1 e 2 imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)
#############################################################################################################################################################################################
def Salvar_estoque():#salva o estoque em um arquivo .txt
    cabecalho(Cores.MAGENTA + '      SALVAR ESTOQUE' + Cores.RESET)
    try:
        with open(arquivo, 'r') as f:#com o arquivo aberto ele lê e carrega 
            produtos = json.load(f)
    except FileNotFoundError:#se o arquivo não existir ele avisa ao usuário
        print(Cores.VERMELHO + "ARQUIVO JSON NÃO ENCONTRADO. NENHUM DADO FOI SALVO." + Cores.RESET)
        return

    if not produtos:#se não existir produtos ele avisa ao usuário
        print(Cores.VERMELHO + "O ESTOQUE ESTÁ VAZIO. NENHUM DADO FOI SALVO." + Cores.RESET)
        return

    arquivo_txt = 'estoque.txt'
    with open(arquivo_txt, 'w') as f: #com o arquivo aberto ele escreve o estoque
        f.write("RELATÓRIO DE ESTOQUE\n")
        f.write("=" * 40 + "\n")
        for produto in produtos: #para produtos dentro de produtos:
            f.write(f"Nome do Produto: {produto['nome_produto']}\n")#referencia o que será escrito, aqui vai ser o nome do produto que é dentro da lista produtos 
            #'nome produto' e assim adiante 
            f.write(f"Quantidade: {produto['quantidade']}\n")
            f.write(f"Data de Validade: {produto['data_de_validade']}\n")
            f.write("=" * 40 + "\n")
    
    print(Cores.VERDE + f"PRODUTOS SALVOS COM SUCESSO NO ARQUIVO '{arquivo_txt}'!" + Cores.RESET)

    opçao = int(input("DIGITE 1 PARA VOLTAR AO MENU \n>>>> "))#toda vez que o algoritmo principal for utilizado ele coloca a 
    #opção de contiuar na função ou voltar ao menu, aqui, deixei apenas o opção voltar disponivel pois faz mais lógica
    if opçao == 1:
        voltar_menu2()
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1 imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)
#############################################################################################################################################################################################              
def adicionar_produto():#adiciona produtos a lista produtos
    cabecalho(Cores.MAGENTA + '      ADICIONAR PRODUTOS' + Cores.RESET)
    nome_produto = input('DIGITE O NOME DO PRODUTO: \n>>> ') #define o nome/quantidade de cada variável
    quantidade = int(input('DIGITE A QUANTIDADE DE PRODUTOS: \n>>> '))
    data_val = input('DIGITE A DATA DE VALIDADE DO PRODUTO [AAAA-MM-DD]: \n>>> ')
    try:
        with open(arquivo, 'r') as f:#com o arquivo aberto ele lê e carrega
            produtos = json.load(f)
    except FileNotFoundError:#se o arquivo não existir ele avisa ao usuário
        produtos = []
        print(Cores.VERMELHO + "ARQUIVO JSON NÃO ENCONTRADO. NENHUM DADO FOI SALVO." + Cores.RESET)
        return

    produtos.append({'nome_produto': nome_produto, 'quantidade': quantidade, 'data_de_validade': data_val})#com as variveis definidas 
    #pelas perguntas ele atribui cada uma delas a uma categoria na lista

    with open(arquivo, 'w') as f:#com o arquivo aberto ele escreve o novo produto na lista
        json.dump(produtos, f, indent=3)
    print(Cores.VERDE + 'PRODUTO CADASTRADO NO SISTEMA.' + Cores.RESET)
    
    opçao = int(input("CONTINUAR?(1- SIM 2-NÃO) \n>>>> "))
    if opçao == 1:
        adicionar_produto()
    elif opçao == 2:
        voltar_menu2 
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1 e 2 imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)     
#############################################################################################################################################################################################
def listar_produtos():#lista todos os produtos da lista produtos
    cabecalho(Cores.MAGENTA + '      LISTAR PRODUTOS' + Cores.RESET)
    try:
        with open(arquivo, 'r') as f:#com o arquivo aberto ele lê e carrega
            produtos = json.load(f)
    except FileNotFoundError:#se o arquivo não existir ele avisa ao usuário
        produtos = []
        print(Cores.VERMELHO + "ARQUIVO JSON NÃO ENCONTRADO. NENHUM DADO FOI SALVO." + Cores.RESET)
        return

    if produtos:
        for produto in produtos:#para produtos dentro da lista produtos:
            print('*' * 30)
            print(f"NOME DO PRODUTO: {produto['nome_produto']}, QUANTIDADE: {produto['quantidade']}, DATA DE VALIDADE: {produto['data_de_validade']}")#forma em que os dados 
            #serão exibidos e as suas referencias dentro da lista
            print('*' * 30)
    else:
        print(Cores.VERMELHO + 'NENHUM PRODUTO ENCONTRADO.' + Cores.RESET)#se não existir nenhum produto na lista ele informa ao usuário
    
    opçao = int(input("DIGITE 1 PARA VOLTAR AO MENU \n>>>> "))#toda vez que o algoritmo principal for utilizado ele coloca a opção de contiuar 
    #na função ou voltar ao menu, aqui, deixei apenas o opção voltar disponivel pois faz mais lógica
    if opçao == 1:
        voltar_menu2()
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1 imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)
#############################################################################################################################################################################################
def atualizar_produto():#atualiza os dados de um produto especifico
    cabecalho(Cores.MAGENTA + '      ATUALIZAR PRODUTOS' + Cores.RESET)
    produto_antigo = input('DIGITE O NOME DO PRODUTO A SER ATUALIZADO: \n>>> ') #variavel produto antigo é criada para poder usar como referencia
    try:
        with open(arquivo, 'r') as f:#com o arquivo aberto ele lê e carrega
            produtos = json.load(f)
    except FileNotFoundError:#se o arquivo não existir ele avisa ao usuário
        produtos = []
        print(Cores.VERMELHO + "ARQUIVO JSON NÃO ENCONTRADO. NENHUM DADO FOI SALVO." + Cores.RESET)
        return
    
    encontrado = False #defini essa variavel encontrado para pode evitar que se possa atualizar um ítem inexistente

    for produto in produtos: #para produtos na lista produtos 
        if produto['nome_produto'] == produto_antigo:#é checado se o nome do produto antigo (que vai ser atualizado para outro) existe na lista produtos
            encontrado = True #se existir o loop acaba e encontrado se torna verdadeiro         
            break

    if encontrado: #se for verdadeiro ele executa isto:
        produto_novo = input('DIGITE O NOVO NOME DO PRODUTO: \n>>> ')#define outras variáveis
        quantidade_nova = int(input('DIGITE A NOVA QUANTIDADE DE PRODUTOS: \n>>> '))
        data_val_nova = input('DIGITE A NOVA DATA DE VALIDADE: \n>>> ')
        produto['nome_produto'] = produto_novo #define que essas novas variáveis vao se transformar nesses parametros na lista
        produto['quantidade'] = quantidade_nova
        produto['data_de_validade'] = data_val_nova 
        with open(arquivo, 'w') as f: #com o arquivo aberto ele escreve a atualização
            json.dump(produtos, f, indent=3)
        print(Cores.VERDE + 'PRODUTO ATUALIZADO COM SUCESSO.' + Cores.RESET)
    else:#se o encontrado continuar como false ele imprime isto:
        print(Cores.VERMELHO + 'ESTE PRODUTO NÃO EXISTE.' + Cores.RESET)
    
    opçao = int(input("CONTINUAR?(1- SIM 2-NÃO) \n>>>> "))#toda vez que o algoritmo principal for utilizado ele coloca a opção de contiuar na função ou voltar ao menu
    if opçao == 1:
        atualizar_produto()
    elif opçao == 2:
        voltar_menu2
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1 imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)
#############################################################################################################################################################################################
def checar_produto(): #mostra os dados de um determinado produto
    cabecalho(Cores.MAGENTA + '      CONSULTAR PRODUTOS' + Cores.RESET)
    nome_produto = input('DIGITE O NOME DO PRODUTO: \n>>> ')
    try:
        with open(arquivo, 'r') as f: #com o arquivo aberto ele lê e carrega 
            produtos = json.load(f)
    except FileNotFoundError:#se o arquivo não existir ele avisa ao usuário
        produtos = []
        print(Cores.VERMELHO + "ARQUIVO JSON NÃO ENCONTRADO. NENHUM DADO FOI SALVO." + Cores.RESET)
        return
    
    encontrado = False #defini essa variavel encontrado para pode evitar que se possa pesquisar um ítem inexistente

    for produto in produtos:#para produtos na lista produtos 
        if produto['nome_produto'] == nome_produto:#é checado se o nome do produto existe na lista produtos
            print(f"NOME DO PRODUTO: {produto['nome_produto']}, QUANTIDADE: {produto['quantidade']}, DATA DE VALIDADE: {produto['data_de_validade']}")#forma em que os 
            #dados serão exibidos e as suas referencias dentro da lista
            encontrado = True#se existir o loop acaba e encontrado se torna verdadeiro  
            break
    if not encontrado:#se o encontrado continuar como false ele imprime isto:
        print('NENHUM PRODUTO CADASTRADO.')
    
    opçao = int(input("CONTINUAR?(1- SIM 2-NÃO) \n>>>> "))#toda vez que o algoritmo principal for utilizado ele coloca a opção de contiuar na função ou voltar ao menu
    if opçao == 1:
        checar_produto()
    elif opçao == 2:
        voltar_menu2
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1  e 2 imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)

###################################################################################################################################################################
def excluir_produto():
    cabecalho(Cores.MAGENTA + '      EXCLUIR PRODUTOS' + Cores.RESET)
    nome_produto = input('DIGITE O NOME DO PRODUTO A SER EXCLUÍDO: \n>>> ')
    try:
        with open(arquivo, 'r') as f:#com o arquivo aberto ele lê e carrega 
            produtos = json.load(f)
    except FileNotFoundError:#se o arquivo não existir ele avisa ao usuário
        produtos = []
        print(Cores.VERMELHO + "ARQUIVO JSON NÃO ENCONTRADO. NENHUM DADO FOI SALVO." + Cores.RESET)
        return
    
    produtos = [produto for produto in produtos if produto['nome_produto'] != nome_produto] #define uma nova lista produtos atualizada com 
    #todos os produtos exceto aquele que foi escrito

    encontrado = False#defini essa variavel encontrado para pode evitar que se possa excluir um ítem inexistente

    for produto in produtos:#para produtos em produtos
        if produto['nome_produto'] == nome_produto:#é checado se o nome do produto existe na lista produtos
            encontrado = True #se existir o loop acaba e encontrado se torna verdadeiro       
            break

    if encontrado:#se o encontrado continuar como false ele imprime  e executa isto:
        with open(arquivo, 'w') as f:#com o arquivo aberto ele escreve a atualização feita
            json.dump(produtos, f, indent=3)
        print(Cores.VERMELHO + 'PRODUTO EXCLUÍDO COM SUCESSO.' + Cores.RESET)      
    else:#se o encontrado continuar como false ele imprime isto:
        print(Cores.VERMELHO + 'ESTE PRODUTO NÃO EXISTE.' + Cores.RESET)
    
    
    opçao = int(input("CONTINUAR?(1- SIM 2-NÃO) \n>>>> "))#toda vez que o algoritmo principal for utilizado ele coloca a opção de contiuar na função ou voltar ao menu
    if opçao == 1:
        excluir_produto()
    elif opçao == 2:
        voltar_menu2
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1 e 2 imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)
#############################################################################################################################################################################################
def verificar_validade():#verifica se a validade dos produtos adicionados
    cabecalho(Cores.MAGENTA + '      VERIFICAR PRODUTOS' + Cores.RESET)
    nome_produto = input('DIGITE O NOME DO PRODUTO: \n>>> ')
    try:
        with open(arquivo, 'r') as f:#com o arquivo aberto ele lê e carrega 
            produtos = json.load(f)
    except FileNotFoundError:#se o arquivo não existir ele avisa ao usuário
        produtos = []
        print(Cores.VERMELHO + "ARQUIVO JSON NÃO ENCONTRADO. NENHUM DADO FOI SALVO." + Cores.RESET)
        return
    
    hoje = datetime.now() #define o dia em que o programa é executado como a data de referencia
    alerta_periodo = timedelta(days=30)# Estabelece um intervalo de 30 dias para verificar produtos próximos ao vencimento.

    encontrado = False

    produtos_vencidos = []#cria uma lista de produtos que vai conter apenas os produtos que estão vencidos 
    produtos_pra_vencer = []#cria uma lista de produtos que vai conter apenas os produtos que estão proximos (há 30 dias) de vencer

    for produto in produtos:#para produtos em produtos
        if produto['nome_produto'] == nome_produto:
            encontrado = True #se existir o loop acaba e encontrado se torna verdadeiro
            if encontrado:
                data_val = datetime.strptime(produto['data_de_validade'], '%Y-%m-%d')#imprime a data de validade do produto
                if data_val < hoje: #se a data de validade do produto for menor que a data atual ele ele executa:
                    produtos_vencidos.append(produto)#é adicionado a lista de produtos vencidos
                elif hoje <= data_val <= hoje + alerta_periodo:#se a data de validade do produto for maior ou igual que a data atual 
                    #mas também menor que a data atual + o alerta de periodo (30 dias) ele:
                    produtos_pra_vencer.append(produto)#ele entra para a lista de produto para vencer

                if produtos_vencidos:#se o produto estiver na lista de vencido:
                    print(Cores.VERMELHO + 'PRODUTOS VENCIDOS:' + Cores.RESET)
                    for produto in produtos_vencidos:#para produtos em produtos
                        print(f"NOME DO PRODUTO: {produto['nome_produto']}, QUANTIDADE: {produto['quantidade']}, DATA DE VALIDADE: {produto['data_de_validade']}")#forma em que os dados serão exibidos e as suas referencias dentro da lista

                if produtos_pra_vencer:
                    print(Cores.VERMELHO + 'PRODUTOS A VENCER:' + Cores.RESET)
                    for produto in produtos_pra_vencer:#para produtos em produtos
                        print(f"NOME DO PRODUTO: {produto['nome_produto']}, QUANTIDADE: {produto['quantidade']}, DATA DE VALIDADE: {produto['data_de_validade']}")#forma em que os dados serão exibidos e as suas referencias dentro da lista

                if not produtos_vencidos: #se não for vencido ou estiver dentro do delta de cuidado:
                    print(Cores.VERDE + 'NENHUM PRODUTO VENCIDO FOI ENCONTRADO.' + Cores.RESET)
            break#neste caso break acontece apos a checagem de tudo
    if not encontrado:#se o encontrado continuar como false ele imprime isto:
        print(Cores.VERMELHO + 'ESTE PRODUTO NÃO EXISTE.' + Cores.RESET)

    opçao = int(input("CONTINUAR?(1- SIM 2-NÃO) \n>>>> "))#toda vez que o algoritmo principal for utilizado ele coloca a opção de contiuar na função ou voltar ao menu
    if opçao == 1:
        verificar_validade()
    elif opçao == 2:
        voltar_menu2
    else:
        print("OPÇÃO INVÁLIDA......")#qualquer outro numero diferente de 1 e 2 imprimie e executa isto:
        sleep(1)
        print("VOLTANDO....")#coloquei pra voltar mesmo na opção inválida pq n acho que faça sentido continuar na função apos isso
        sleep(1)
#############################################################################################################################################################################################
def menu_inicial(): #tela inicial do programa
    print(Cores.VERDE + '-' * 34 + Cores.RESET)
    cabecalho(Cores.MAGENTA + 'BEM-VINDO AO ESTOQUE DO ATACADÃO!' + Cores.RESET)
    print('1 - ABRIR GERENCIAMENTO DE ESTOQUE')
    print('2 - SAIR')
    print(Cores.VERDE + '-' * 34 + Cores.RESET)
#############################################################################################################################################################################################
def exibir_menu(): #tela com as opções possíveis do programa
    cabecalho(Cores.MAGENTA + '          MENU' + Cores.RESET)
    print('1. ADICIONAR UM PRODUTO')
    print('2. LISTAR PRODUTOS')
    print('3. VERIFICAR VALIDADE')
    print('4. CONSULTAR PRODUTO')
    print('5. ATUALIZAR PRODUTO')
    print('6. EXCLUIR PRODUTO')
    print('7. VOLTAR AO MENU INICIAL')
    print("8. GERAR PRODUTOS")
    print("9. DELETAR ESTOQUE TOTAL")
    print("10. iNFORMAÇÕES")
    print("11. SALVAR ESTOQUE")
#############################################################################################################################################################################################
def main():
    while True: 
        menu_inicial()#equanto nenhuma opção for escolhida ela fica com o menu inicial aberto
        opcao_inicial = int(input('INFORME UMA OPÇÃO: \n>>> ')) #variável que vai definir a opcão de abrir ou não o menu

        if opcao_inicial == 1:#se a opção inicial for 1 abre o menu
            while True:
                exibir_menu()
                opcao = input('\nESCOLHA UMA OPÇÃO: \n>>> ')#opção que direciona o usuario a função escolhida

                if opcao == "1": #se a opção for 1 abre adicionar produtos
                   adicionar_produto()
                elif opcao == '2':#se a opção for 2 abre listar produtos
                    listar_produtos()
                elif opcao == '3':#se a opção for 3 abre verificar validade
                    verificar_validade()
                elif opcao == '4':#se a opção for 4 abre verificar checar produto
                    checar_produto()
                elif opcao == '5':#se a opção for 5 abre atualizar produto
                    atualizar_produto()
                elif opcao == '6':#se a opção for 7 abre excluir produto
                    excluir_produto()
                elif opcao == '7':#se a opção for 8 abre o menu inicial
                    print(Cores.MAGENTA + 'VOLTANDO AO MENU INICIAL...' + Cores.RESET)
                    sleep(3)
                    break
                elif opcao == '8': #se a opção for 8 abre gerar produto
                    Gerar_produtos()
                    break
                elif opcao == '9': #se a opção for 9 abre deletar estoque
                    Deletar_estoque()
                    break
                elif opcao == '10': #se a opção for 10 abre informações
                    informações()
                    break
                elif opcao == '11': #se a opção for 11 abre salvar estoque
                    Salvar_estoque()
                    break
                else: #qualquer outro numero diferente das mencionadas imprimie isto:
                    print(Cores.VERMELHO + 'OPÇÃO INVÁLIDA. TENTE NOVAMENTE!' + Cores.RESET)

        elif opcao_inicial == 2: #se a opção inicial for 2 fecha a aplicação
            print(Cores.MAGENTA + 'SAINDO...' + Cores.RESET)
            sleep(3)
            limpar_tela()
            break

        else:#qualquer outro numero diferente de 1 e 2 imprimie isto:
            print(Cores.VERMELHO + 'OPÇÃO INVÁLIDA. TENTE NOVAMENTE!' + Cores.RESET)
#############################################################################################################################################################################################
if __name__ == "__main__":
    main()