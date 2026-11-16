import sqlite3
conexao = sqlite3.connect('banco01.db')
cursor = conexao.cursor()
cursor.execute('''
                CREATE TABLE AGENDA(
                nome text,
                telefone text)
                ''') 
conexao.commit()
cursor.close()
conexao.close()