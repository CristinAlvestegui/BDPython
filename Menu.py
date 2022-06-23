import Operacoes
import this
this.opcao = -1

def menu():
    print('\nEscolha umas das opções abaixo: \n\n' +
        '1. Cadastrar\n'                           +
        '2. Consultar\n'                           +
        '3. Teste\n'                               +
        '0. Sair\n')
    this.opcao = int(input())

def operacoes():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe seu nome: ')
            nome = input()
            print('Informe seu Telefone: ')
            telefone = input()
            print('Informe seu endereço:')
            endereco = input()
            print('Informe sua data de nascimento: ')
            dataNsc = input()
            #chamar o meétodo inserir da classe Operações
            Operacoes.inserir(nome, telefone, endereco, dataNsc)
        elif this.opcao == 2:
            Operacoes.consultar()
        else:
            print('Opção escolhida não é válida!')