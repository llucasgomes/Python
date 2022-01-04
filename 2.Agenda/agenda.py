def menu():  
    menu_principal = "s"  
    while menu_principal == "s":
        opcao = input('''
        ============================================================
                            PROJETO AGENDA EM PYTHON
        MENU:
        [1] CADASTRAR CONTATO
        [2] LISTAR CONTATOS
        [3] DELETAR CONTATO
        [4] BUSCAR CONTATO
        [5] SAIR

        ============================================================

        O QUE VOCE QUER FAZER,DIGITANDO A OPÇÃO ACIMA: ''') 
        if opcao=="1":
            cadastrar()
        elif opcao=="2":
            listar()
        elif opcao=="3":
            deletar()
        elif opcao=="4":
            buscar()
        elif opcao=="5":
            print('MUITO OBRIGADO POR USAR NOSSO AGENDA!!!\n')
            exit()
        else:
            return print( "Digite uma opcao valida da proxima vez")
        menu_principal = input("Deseja voltar ao menu principal? (s/n): ").lower()
    

        

   

def main():
    menu()

def cadastrar():
    id = str(input("Infome o id: "))
    nome  = str(input("Informe o Nome do Contato: ").capitalize())
    fone = str(input("Informe o numero do mesmo: "))
    email = str(input("Informe um email: "))
        

    try:
        agenda = open("agenda.txt","a") # abrir/criar o arquivo agenda.txt, e ter permisao de "a"(gravar dados)
        dados = f"{id};\t{nome};\t{fone};\t{email} \n"
        agenda.write(dados) #escrever os dados
        agenda.close # fecha o documento
        print('Os dados foram salvos com sucesso!!!!!!!!!\n')
    except:
        print('ERRO na gravação do contato')

def listar():
    agenda = open("agenda.txt","r") # abrir/criar o arquivo agenda.txt, e ter permisao de "r"(leitura)
    for contato in agenda: # ira percorrer todos os contatos da agenda
        print(contato)
    agenda.close # fechar a agenda

def buscar():
    nome = input('Informe o nome a ser procurado: ').capitalize()
    agenda = open("agenda.txt","r") # abrir/criar o arquivo agenda.txt, e ter permisao de "r"(leitura)
    for contato in agenda: # ira percorrer todos os contatos da agenda
        if nome in contato.split(';')[1]: # Se o nome estiver na coluna splitada, ele ira puxar os dados da linha
            print(contato)
    agenda.close # fechar a agenda

def deletar():
    nome = input('Informe o nome a ser DELETADO: ') #Nome a ser deletado / .lower e para tudo ser minusculo
    agenda = open('agenda.txt','r') # abrir/criar o arquivo agenda.txt, e ter permisao de "r"(leitura)
    aux = [] # variavel auxiliar 01
    aux2 = [] # variavel auxiliar 02
    
    for i in agenda: # percorrer toda agenda
        aux.append(i) # adiciona os dados na variavel 01
    for i in range(0, len(aux)): # vai percorrer de 0 ate o numero da lista AUX 01
        if  nome not in aux[i]: #Se o nome deletado nao estive no auxiliar 01 entao
            aux2.append(aux[i]) # irei adicionar o dados da AUX 01(indice) no AUX 02
    agenda = open('agenda.txt','w')# abrir/criar o arquivo agenda.txt, e ter permisao de "w"(escrita) 
    for i in aux2: #Percorrer a AUXILIAR 02
        agenda.write(i) # GRAVAR OS DADOS LINHA POR LINHA NA AGENDA
        listar()





main()