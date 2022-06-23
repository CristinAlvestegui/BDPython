import mysql.connector #Acesso ao mysql
from mysql.connector import errorcode #Trata as exceções

def connectar():
    try:
        db_connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database='BaseDados')
        print('Conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as erro: #Guardando as posíveis exceções na variável erro
        if erro.errno == errorcode.ER_BAD_DB_ERROR: #Caso o BD não exista
            print('Banco de Dados não existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Caso usuário ou senha foram inválidos
            print('Usuário ou senha invalidos!, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connect.close()