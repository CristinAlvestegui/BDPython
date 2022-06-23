import mysql.connector
import DAO

db_connection = DAO.connectar()
con = db_connection.cursor()

def inserir(nome,telefone, endereco, dataNsc):
    try:
        sql = "insert into Pessoa(codigo,nome,telefone,endereco,DataNsc) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, pegaData(dataNsc))
        con.execute(sql)
        db_connection.commit() #Comando para inserir dados na BD
        #print(con.rowcount, 'Salvo com sucesso!')
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def pegaData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano, mes, dia)

def consultar():
    try:
        sql = 'select * from Pessoa'
        con.execute(sql)
        for(codigo, nome, telefone, endereco, DataNsc) in con: #usamos for para percorrer
            print('Código: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}'.format(nome, telefone, endereco, DataNsc)) #aqui podemos print o que vc quizer!
            print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cod, campo, novoDado):
    try:
        sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)