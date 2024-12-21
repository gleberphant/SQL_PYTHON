from pickletools import pybytes_or_str

"""
 TESTES DE USO DO SQL 3         
 feito por :  GR4V4T1NH4         

"""


import sqlite3

table_name = "my_table"

def search_table(cursor):
    try:
        result = cursor.execute(f"SELECT * FROM {table_name}")
        print("-" * 60)
        print(f"{'row[0]':<20}{'row[1]':<20}{'row[2]':<20}")
        print("- " * 31)
        for row in result:
            print(f"{ row[0] :<20}{ row[1] :<20}{ row[1] :<20}")
        print("-" * 60)

    except Exception as e:
        print (f" ERRO: {str(e)}  ")


def create_table(cursor):

    global table_name

    table_name = input("digite o nome da nova tabela ")

    try:
        cursor.execute(f"CREATE TABLE {table_name} (id INTEGER, name TEXT)")
        cursor.commit()
    except Exception as e:
        print (f" ERRO: {str(e)}  ")

def insert_into(cursor):
    try:
        cursor.execute(f"INSERT INTO {table_name} VALUES('1',' name')")
        cursor.commit()
    except Exception as e:
        print(f" ERRO: {str(e)}  ")


def select_table():
    global table_name
    table_name = input("Informe o nome da tabela: ")
    print(f"Nova tabela selecionada: {table_name}")


def draw_main_menu():
    print(" " + ("-" * 20))
    print(f"{'| 1: Pesquisar':<20} |")
    print(f"{'| 2: Inserir dado':<20} |")
    print(f"{'| 3: Criar Tabela':<20} |")
    print(f"{'| 4: Selecionar Tabela':<20} |")
    print(f"{'| Q: Sair':<20} |")
    print(" " + ("-" * 20))


def main_loop(cursor):

    while True:
        draw_main_menu()
        opt = input(f"{'Digite a opção':<18}: ").upper()

        if opt == 'Q':
            break
        elif opt == '1':
            search_table(cursor)
        elif opt == '2':
            insert_into(cursor)
        elif opt == '3':
            create_table(cursor)
        elif opt == '4':
            select_table()


def main():

    with sqlite3.connect("my_database.db") as connection:

        cursor = connection.cursor()
        main_loop(cursor)
        cursor.close()

if __name__ == "__main__":
    main()

