import mysql.connector
def conectar():
    conexao = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="xocolate123",
        database ="estoque"
    )
    return conexao 
def cadastro_tamanho(): 
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()

    print('-' * 22)
    print('tamanhos para escolha')
    print('-' * 22)
    print()
    print('opcoes: ')
    print('tamanho - [P]')
    print('tamanho - [M]')
    print('tamanho - [G]')
    print('tamanho - [GG]')
    tamanho = str(input ( 'Digite o tamanho da blusa:'))
    quantidade = str(input('digite a quantidade:'))

    sql = "INSERT INTO tamanhos (tamanho, quantidade) VALUES (%s, %s)"
    valores = (tamanho, quantidade)
    cursor.execute(sql, valores)
    print(cursor.rowcount, "arquivos inseridos.")
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_tamanhos():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    print(conexao)

    cursor = conexao.cursor()
    sql= "SELECT * FROM tamanhos"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    print(f'| {"id":^10} | {"tamanho":^10} | {"quantidade":^10} |'.format('id', 'tamanho', 'quantidade'))
    print('-' * 40)
    for id, tamanho, quantidade in myresult:
            print('| {:^10} | {:^10} | {:^10} |'.format(id, tamanho, quantidade))
    conexao.commit()
    cursor.close()
    conexao.close()


def alterar_tamanho():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xocolate123",
    database="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor= conexao.cursor()
    print('Os dados disponiveis para serem alterados são:\n')
    listar_tamanhos()
    tamanho = input('digite o novo tamanho: ')
    id = int(input('Qual o id que você deseja atualizar os dados? '))
    sql = "UPDATE tamanhos SET tamanho = %s WHERE id = %s"
    valores = (tamanho, id)
        
    cursor.execute(sql, valores)
    print(cursor.rowcount, "ID atualizado com sucesso!")
    conexao.commit()
    cursor.close()
    conexao.close()


def apagar_tamanho():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    cursor = conexao.cursor()
    print('Os dados disponiveis para serem deletados são:\n')
    listar_tamanhos()
    id = int(input('\nQuais dados você deseja apagar? selecione um ID: '))
    print("\nInformações com ID {} foram deletadas com sucesso!\nTabela atualizada com sucesso!\n".format(id))
    sql = "DELETE FROM tamanhos WHERE id = %s"
    valores = (id,)

    cursor.execute(sql,valores)
    print(cursor.rowcount, "arquivo deletado")
    conexao.commit()
    cursor.close()
    conexao.close()


def sair():
    print("Saindo...")


def menu_tamanhos():
        enter = input("\n===============================================\nTabela selecionada com sucesso!!\nPress Enter para continuar..\n===============================================\n")
        while True:
            menu = input("\n================\nTabela tamanhos\n================\n1-Cadastrar\n2-Listar\n3-Alterar\n4-Apagar\n5-Sair\n")

            if menu =='1':
                cadastro_tamanho()
    
            elif menu =='2':
                listar_tamanhos()

            elif menu =='3':
                alterar_tamanho()

            elif menu =='4':
                apagar_tamanho()

            elif menu =='5':
                sair()
                break      
            
            else:
                print("\nError")


def cadastro_tecido():
    conexao = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="xocolate123",
        database ="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()

    print('-' * 20)
    print('tecidos para escolha')
    print('-' * 20)
    print()
    print('opcoes: ')
    print('[Malha] - ')
    print('[Lycra] - ')
    tipo = input ( 'Digite o tecido da blusa:')
    sql = "INSERT INTO tecidos (tipo) VALUES (%s)"
    valores = (tipo,)
    cursor.execute(sql, valores)

    print(cursor.rowcount, "arquivos inseridos.")
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_tecidos():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()
    sql= "SELECT * FROM tecidos"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    print(f'| {"id":^10} | {"tipo":^10} |'.format('id', 'tipo'))
    print("-" * 25)
    for id, tipo in myresult:
            print('| {:^10} | {:^10} |'.format(id, tipo))
    conexao.commit()
    cursor.close()
    conexao.close()


def alterar_tecido():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xocolate123",
    database="estoque"
    )
    conexao = conectar()
    cursor= conexao.cursor()
    print('Os dados disponiveis para serem alterados são:\n')
    listar_tecidos()
    tecido = input('digite o novo tecido: ')
    id = int(input('Qual o id que você deseja atualizar os dados? '))
    sql = "UPDATE tecidos SET tipo = %s WHERE id = %s"
    valores = (tecido, id)
    cursor.execute(sql, valores) 
    
    print(cursor.rowcount, "ID atualizado com sucesso!") 
    conexao.commit()
    cursor.close()
    conexao.close()


def apagar_tecido():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    cursor = conexao.cursor()
    print('Os dados disponiveis para serem deletados são:\n')
    listar_tecidos()
    id = int(input('\nQuais dados você deseja apagar? selecione um ID: '))
    print("\nInformações com ID {} foram deletadas com sucesso!\nTabela atualizada com sucesso!\n".format(id))
    sql = "DELETE FROM tecidos WHERE id = %s"
    valores = (id,)
    cursor.execute(sql,valores)

    print(cursor.rowcount, "arquivos deletados")
    conexao.commit()
    cursor.close()
    conexao.close()


def sair():
    print("Saindo...")


import mysql.connector
def menu_tecidos():
        enter = input("\n===============================================\nTabela selecionada com sucesso!!\nPress Enter para continuar..\n===============================================\n")
        while True:
            menu = input("\n================\nTabela tecidos\n================\n1-Cadastrar\n2-Listar\n3-Alterar\n4-Apagar\n5-Sair\n")

            if menu =='1':
                cadastro_tecido()
    
            elif menu =='2':
                listar_tecidos()

            elif menu =='3':
                alterar_tecido()

            elif menu =='4':
                apagar_tecido()

            elif menu =='5':
                sair()
                break      
            
            else:
                print("\nError")


def cadastro_cores():
    conexao = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="xocolate123",
        database ="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()
   
    nome = input ( 'Digite a cor da blusa:')
    sql = "INSERT INTO cores (nome) VALUES (%s)"
    valores = (nome,)
    cursor.execute(sql, valores)
    print(cursor.rowcount, "arquivos inseridos.")
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_cores():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()
    sql= "SELECT * FROM cores"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    print(f'| {"id":^10} | {"nome":^10} |'.format('id', 'nome'))
    print("-" * 22)
    for id, nome in myresult:
            print('| {:^10} | {:^10} |'.format(id, nome))
    conexao.commit()
    cursor.close()
    conexao.close()


def alterar_cor():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xocolate123",
    database="estoque"
    )
    conexao = conectar()
    cursor= conexao.cursor()
    print('Os dados disponiveis para serem alterados são:\n')
    listar_cores()
    nome = input('digite a nova cor: ')
    id = int(input('Qual o id que você deseja atualizar os dados? '))
    sql = "UPDATE cores SET nome = %s WHERE id = %s"
    valores = (nome, id)        
    cursor.execute(sql, valores) 
        
    print(cursor.rowcount, "ID atualizado com sucesso!") 
    conexao.commit()
    cursor.close()
    conexao.close()


def apagar_cor():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    cursor = conexao.cursor()
    print('Os dados disponiveis para serem deletados são:\n')
    listar_cores()
    id = int(input('\nQuais dados você deseja apagar? selecione um ID: '))
    print("\nInformações com ID {} foram deletadas com sucesso!\nTabela atualizada com sucesso!\n".format(id))
    sql = "DELETE FROM cores WHERE id = %s"
    valores = (id,)

    cursor.execute(sql,valores)
    print(cursor.rowcount, "arquivos deletados")
    conexao.commit()
    cursor.close()
    conexao.close()


def sair():
    print("Saindo...")


import mysql.connector
def menu_cores():
        enter = input("\n===============================================\nTabela selecionada com sucesso!!\nPress Enter para continuar..\n===============================================\n")
        while True:
            menu = input("\n================\nTabela cores\n================\n1-Cadastrar\n2-Listar\n3-Alterar\n4-Apagar\n5-Sair\n")

            if menu =='1':
                cadastro_cores()
    
            elif menu =='2':
                listar_cores()

            elif menu =='3':
                alterar_cor()

            elif menu =='4':
                apagar_cor()

            elif menu =='5':
                sair()
                break      
            
            else:
                print("\nError")


def cadastrar_blusa():
    conexao = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="xocolate123",
        database ="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()
    listar_blusas()
    id = int(input ( 'Digite o novo ID da blusa:'))

    sql = "INSERT INTO blusas (id) VALUES (%s)"
    valores = (id,)
    cursor.execute(sql, valores)
    print(cursor.rowcount, "ID inserido.")
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_blusas():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    print(conexao)

    cursor = conexao.cursor()
    sql= "SELECT * FROM blusas"
    cursor.execute(sql)

    myresult = cursor.fetchall()
    print()
    print('Lista da tabelas blusas')
    print()
    print('| {:^10} | {:^10} | {:^10} | {:^10} |'.format('id_blusas', 'id_tamanho', 'id_tecido', 'id_cor'))
    print("-" * 22)
    for id_blusas, id_tamanho, id_tecido, id_cor in myresult:
            print('| {:^10} | {:^10} | {:^10} | {:^10} |'.format(str(id_blusas), str(id_tamanho), str(id_tecido), str(id_cor)))
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_blusas_tamanhos():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()
    sql= "SELECT * FROM tamanhos left join blusas  on id_tamanho=tamanhos.id"
    cursor.execute(sql)

    myresult = cursor.fetchall()
    print()
    print('Lista das tabelas blusas e tamanhos')
    print()
    print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'.format('id_tamanhos', 'tamanho', 'quantidade', 'id_blusas', 'id_tamanho', 'id_tecido', 'id_cor'))
    print("-" * 86)
    for id, tamanho, quantidade, id_blusas, id_tamanho, id_tecido, id_cor in myresult:
            print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'. format(str(id), tamanho, quantidade, str(id_blusas), str(id_tamanho), str(id_tecido), str(id_cor)))
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_blusas_tecidos():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()
    sql= "SELECT * FROM tecidos left join blusas on id_tecido=tecidos.id"
    cursor.execute(sql)

    myresult = cursor.fetchall()
    print()
    print('lista das tabelas blusas e tecidos')
    print()
    print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'.format('id_tecidos', 'tipo', 'id_blusas', 'tamanho', 'tecido', 'cor'))
    print("-" * 80)
    for id, tipo, id_blusas, id_tamanho, id_tecido, id_cor in myresult:
            print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'.format(str(id), tipo, str(id_blusas), str(id_tamanho), str(id_tecido), str(id_cor)))
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_blusas_cores():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    print(conexao)
    cursor = conexao.cursor()
    sql= "SELECT * FROM cores left join blusas on id_cor=cores.id"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    print()
    print('Lista das tabelas blusas e cores')
    print()
    print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'.format('id_cores', 'nome', 'id_blusas', 'tamanho', 'tecido', 'cor'))
    print("-" * 80)
    for id, nome, id_blusas, id_tamanho, id_tecido, id_cor in myresult:
            print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'. format(str(id), nome, str(id_blusas), str(id_tamanho), str(id_tecido), str(id_cor)))
    conexao.commit()
    cursor.close()
    conexao.close()


def alterar_blusa():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xocolate123",
    database="estoque"
    )
    conexao = conectar()
    cursor= conexao.cursor()
    print('Os dados disponiveis para serem alterados são:\n')
    listar_blusas()
    id = int(input('Qual o id que você deseja atualizar os dados? '))
    sql = "UPDATE blusas SET id = %s WHERE id = %s"
    valores = (id,)
        
    cursor.execute(sql, valores) 
    print(cursor.rowcount, "ID atualizado com sucesso!") 
    conexao.commit()
    cursor.close()
    conexao.close()


def apagar_blusa():
    conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="xocolate123",
      database="estoque"
    )
    conexao = conectar()
    cursor = conexao.cursor()
    print('Os dados disponiveis para serem deletados são:\n')
    listar_blusas()
    id = int(input('\nQuais dados você deseja apagar? selecione um ID: '))
    print("\nInformações com ID {} foram deletadas com sucesso!\nTabela atualizada com sucesso!\n".format(id))
    sql = "DELETE FROM blusas WHERE id = %s"
    valores = (id,)

    cursor.execute(sql,valores)
    print(cursor.rowcount, "arquivo deletado")
    conexao.commit()
    cursor.close()
    conexao.close()


def sair():
    print("Saindo...")


import mysql.connector
def menu_blusas():
        enter = input("\n===============================================\nTabela selecionada com sucesso!!\nPress Enter para continuar..\n===============================================\n")
        while True:
            menu = input("\n================\nTabela blusas\n================\n1-Cadastrar\n2-Listar\n3-Alterar\n4-Apagar\n5-Sair\n")

            if menu =='1':
                cadastrar_blusa()
    
            elif menu =='2':
                listar_blusas()
                listar_blusas_tamanhos()
                listar_blusas_tecidos()
                listar_blusas_cores()

            elif menu =='3':
                alterar_blusa()

            elif menu =='4':
                apagar_blusa()

            elif menu =='5':
                sair()
                break      
            
            else:
                print("\nError")


while True:
            menu = input("Qual tabela você deseja acessar?\nDigite....\n1- Tamanhos\n2- Tecidos\n3- Cores\n4- blusas\n5 - Sair\n")
            if menu =='1':
                menu_tamanhos()
            
            elif menu =='2':
                menu_tecidos()

            elif menu =='3':
                menu_cores()

            elif menu =='4':
                menu_blusas()

            elif menu =='5':
                print("Saindo.....\n==========================================\nObrigado por utilizar o nosso Programa :)\n==========================================\n")
                break
            else:
                print('\n\nERRO, OPÇÃO INVÁLIDA....\n\n')
