import random

verifica_cadastro = {} #Dicionario  Para Verificar Se o Usuario tem Cadastro.
numeros_rifa = list(range(1, 101)) #Lista Criada Para as Rifas, Tem a função de Sortear Numeros de 1 a 100
rifas_participante = [] #Lista que Armazena as Rifas do Usuario
quantia_doada = 0 #variavel que serve Para Armazenar a Quantidade de Dinheiro Doado Pelo Usuario.
estado_competicao = False #Variavel Para Verificar Se o Usuario Está Inscrito ou não na Competição de Pesca

def menu_inicial(): #Função que Imprime O Primeiro Menu. (CADASTRO PESSOAL, LOGIN E ENCERRAR PROGRAMA)
    print("ESCOLHA UMA OPÇÃO:")
    print("DIGITE (1) PARA CADASTRO PESSOAL.")
    print("DIGITE (2) PARA LOGIN.")
    print("DIGITE (3) PARA SAIR.")
    return
    
def pos_login(): #Função que Imprime o Menu pós login. (RIFA, DOAÇÃO, AJUDA BAIRRO, COMPETIÇÃO, CONSULTAR DADOS DO USUARIO. SAIR)
    print("ESCOLHA UMA OPÇÃO:")
    print("DIGITE (4)  RIFAS.")
    print("DIGITE (5)  DOAÇÃO PARA O MEIO AMBIENTE.")
    print("DIGITE (6)  AJUDA BAIRRO.")
    print("DIGITE (7)  PARTICIPAR DA COMPETIÇÃO.")
    print("DIGITE (8)  CONSULTAR | RIFAS | DOAÇÕES FEITAS.")
    print("DIGITE (9)  SAIR.")
    return
  

def cadastro(): #FUNÇÃO CRIADA PARA FAZER E ARMAZENAR O CADASTRO DO USUARIO.
    while True:
        print("Opção Escolhida (1) - Cadastro.")
        nome = input("Digite seu nome: ")
        cel = input("Digite seu Telefone: ")
        email = input("Digite seu E-mail: ")
        senha = input("Digite sua senha: ")
        confirma_senha = input("Confirme sua senha: ")

        if not nome or not email or not senha:
            print("Nome, E-mail e Senha não podem ser vazios.")
            continue

        if senha != confirma_senha:
            print("Senhas não coincidem. Tente novamente.")
            continue

        verifica_cadastro[email] = {'nome': nome, 'email': email, 'senha': senha, 'telefone': cel}
        print(f"Seus Dados estão corretos?\nNome: {nome}\nTelefone: {cel}\nE-mail: {email}\nSenha: {senha}")
        dados()
        break

def login(): #Função Criada Para Verificar se o Usuario Possui Login.
    print("Opção Escolhida (2) - Login.")
    email = input("Digite seu email: ")

    if email in verifica_cadastro:
        senha = input("Digite sua senha: ")
        if senha == verifica_cadastro[email]['senha']:
            print("Logado Com Sucesso!")
            pos_login()
        else:
            print("Senha Incorreta. Tente Novamente.")
            login()
    else:
        print("Email não encontrado. Tente novamente.")
        engano = input("Se Você Selecionou essa Opção Por Engano, Digite (1) Para Voltar Ao Menu Principal.\n"
                       "Caso Queira Tentar Novamente o Email, Digite (2): ")
        if engano == '1':
            return menu_inicial(), escolha_opcao()
    
        elif engano == '2':
            return login()
        else:
            print("Opção Inválida. Tente Novamente.")
            return login()

def dados(): #Função Criada Para o Usuario Verificar Se os Dados Do Cadastro Estão Corretos. 
    try:
        resposta_usuario = int(input("Digite (1)- Para Dados Corretos.\nDigite (2) - Para dados Incorretos.\n"))
        if resposta_usuario == 1:
            print("Cadastrado com Sucesso!")
            return pos_login(), escolha_pos_login()
            
        elif resposta_usuario == 2:
            print("Refazendo Cadastro.")
            return cadastro()
        else:
            print("Opção Inválida. Tente Novamente.")
            return dados()
    except:
        print("Opção Inválida. Tente Novamente.")
        return dados()

def escolha_opcao(): #CRIADA PARA O USUARIO ESCOLHER A OPÇÃO DO MENU INICIAL.
    try:
        opcao = int(input("Digite o Numero Conforme Seu Desejo: "))
        if opcao == 1:
            return cadastro()
        elif opcao == 2:
            return login()
        elif opcao == 3:
            print("Saindo Do Site. Pense Sempre No Meio Ambiente!")
        else:
            print("Opção inválida. Tente novamente.")
            return menu_inicial(), escolha_opcao()
        
    except:
        print("Opção inválida. Tente novamente.")
        return menu_inicial(), escolha_opcao()
    

def escolha_pos_login(): #CRIADA PARA O USUARIO ESCOLHER UMA OPÇÃO DO MENU POS LOGIN.
    try:
        escolha = int(input("Digite o Numero Conforme O Seu Desejo: "))
        if escolha == 4:
            return sorteio_rifa()
        elif escolha == 5:
            return doacao_meio_ambiente()
        elif escolha == 6:
            return ajuda_bairro()
        elif escolha == 7:
            return competicao_pesca()
        elif escolha == 8:
            return consultar_rifas_doacoes()
        elif escolha == 9:
            print("FINALIZANDO. NÃO SE ESQUEÇA DE AJUDAR O MEIO AMBIENTE!")
        else:
            print("Opção Inválida. Tente Novamente.")
            return pos_login(), escolha_pos_login()
            
    except:
        print("Opção Inválida. Tente Novamente.")
        return pos_login(), escolha_pos_login()
        
def sorteio_rifa():#FUNÇÃO QUE SERVE PARA SORTEAR E ARMAZENAR AS RIFAS DO USUARIO
    while True:
        numero_pet = int(input("Digite Quantas Latinhas você vai doar | (Min 10) | (Max 100)"))
        if numero_pet < 10:
            print("Quantidade Insuficiente. Tente Novamente.")
            continue
        elif numero_pet > 100:
            print("Quantidade Excedente. Tente Novamente.")
            continue
        else:
            quantidade_rifa = numero_pet // 10
            resultado = int(quantidade_rifa)
            print(f"Você doou {numero_pet} e Ganhou {resultado} NÚMERO(S) DE RIFAS")
            break
    numeros_sorteados = random.sample(numeros_rifa, resultado)
    print(f"Os Seus Números Da Sorte São: {numeros_sorteados} ")
    print("Agradecemos a Doação! ")
    for num in numeros_sorteados:
        numeros_rifa.remove(num)
        rifas_participante.append(num)
    return pos_login(), escolha_pos_login()
    

def doacao_meio_ambiente(): #FUNÇÃO QUE SERVE PARA O USUARIO DOAR DINHEIRO PARA NOSSO SITE, TAMBEM ARMAZENA A QUANTIDAADE DOADA PELO MESMO.
    while True:
        print("DOAÇÃO PARA O MEIO AMBIENTE")
        quantia = int(input("Qual o Valor (R$) que você deseja doar Hoje?"))
        if quantia <= 0:
            print("Valor Inválido. Tente Novamente.")
            continue
        else:
            print(f"Você Doou {quantia} Reais Para o Meio Ambiente. Obrigado!")
            global quantia_doada
            quantia_doada += quantia
            break
    return pos_login(), escolha_pos_login()
    

def ajuda_bairro(): #FUNÇÃO QUE FAZ O FUNCIONAMENTO DA 'AJUDA AO BAIRRO'
    print("AJUDA MEIO AMBIENTE | LIMPE SEU BAIRRO VANTAGENS E  GANHE RECOMPENSAS JUNTO AOS NOSSOS PARCEIROS! ")
    print("A CADA 150 LATINHAS GANHE VANTAGENS E RECOMPENSAS.")
    quantidade_de_lata = int(input("Quantas Latinhas você Recolheu? "))
    if quantidade_de_lata < 150:
        print("Você não alcançou o objetivo. Tente novamente.")
        return pos_login(), escolha_pos_login()
        
    else:
        recompensa = quantidade_de_lata  * 10
        print(f"Você Ganhou {recompensa} Pontos!")
        if recompensa > 1000:
            print("Recompensas Disponiveis: \n 1 - Cupom 1O Reais Ifood \n 2- Cupom 10 Reais Uber \n 3 - Vale Presente Americanas")
            resgatar = input("DIGITE O NUMERO DO CUPOM PARA RESGATA-LO")
            if resgatar =='1':
                print("Você Resgatou o Cupom de 10 Reais Ifood")
                return pos_login(), escolha_pos_login()
            elif resgatar == '2':
                print("Você Resgatou o Cupom de 10 Reais Uber")
                return pos_login(), escolha_pos_login()
            elif resgatar == '3':
                print("Você Resgatou o Vale Presente Americanas")
                return pos_login(), escolha_pos_login()
            else:
                return pos_login(), escolha_pos_login()
        else:
            return pos_login(), escolha_pos_login()
        

def competicao_pesca(): #FUNÇÃO PARA SE INSCREVER NA COMPETIÇÃO 
    print("COMPETIÇÃO DE PESCA.")
    print("DIGITE (+) PARA CADASTRAR DIA 04/06 - 6 Vagas Disponíveis")
    print("DIGITE (-) PARA CADASTRAR DIA 07/06 - 3 Vagas Disponíveis")
    escolha_competicao = input("DIGITE SUA ESCOLHA: ")
    if escolha_competicao == "+":
        print("Você Foi Cadastrado Para o Dia 04/06. Boa Sorte!")
    elif escolha_competicao == "-":
        print("Você Foi Cadastrado Para o Dia 07/06. Boa Sorte!")
    else:
        print("Opção Inválida. Tente Novamente.")
    return pos_login(), escolha_pos_login()
   

def consultar_rifas_doacoes(): #FUNÇÃO CRIADA PARA VERIFICAR AS RIFAS DO USUARIO AS DOAÇÕES FEITAS PELO MESMO OU PARA VOLTAR AO MENU POS LOGIN.
    print("1 - PARA CONSULTAR RIFAS DO USUÁRIO:  ")
    print("2 - PARA CONSULTAR DOAÇÕES FEITAS PELO USUÁRIO:  ")
    print("3 - PARA VOLTAR AO MENU.  ")
    acao = input("DIGITE AQUI:")
    if acao == "1":
        print("CONSULTAR RIFAS DO USUÁRIO:  ")
        print("NÚMERO(S) DE RIFAS DO USUÁRIO:")
        if not rifas_participante:
            print("Você Não Participou de Nenhuma Rifa.\n")
            return consultar_rifas_doacoes()
        else:
            for rifa in rifas_participante:
                print(f"Rifa Numero: ", rifa)
            return consultar_rifas_doacoes()
    elif acao == '2':
        print("CONSULTAR DOAÇÕES FEITAS PELO USUÁRIO:")
        print(f"DOAÇÕES FEITAS PELO USUÁRIO - {quantia_doada} ")
        consultar_rifas_doacoes()
    elif acao == '3':
        return pos_login(), escolha_pos_login()
        
    else:
        print("Opção Inválida. Tente Novamente.")

def necessario_login(): #FUNÇÃO CASO O USUARIO TENTE LOGAR SEM LOGIN. NÃO UTILIZADA NO MOMENTO
    print("Para Participar do Nosso Site é Necessário Fazer Login.")
    pergunta = input("Você Possui Cadastro? (S/N): ").upper()
    if pergunta == "S":
        return login()
    elif pergunta == "N":
        return cadastro()
    else:
        print("Opção Inválida. Digite (S - Para Sim | N - Para Não)")
        return necessario_login()

def main(): #FUNCÃO QUE RODA TODAS AS OUTRAS 
    menu_inicial()
    escolha_opcao()

if __name__ == "__main__":
    main()
