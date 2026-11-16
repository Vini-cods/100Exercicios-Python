
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conec:
    with closing(conec.cursor()) as cursor:
        cursor.execute(""" update agenda
                           set telefone = '1234-5678'""")
        print("Registros alterados: ", cursor.rowcount)
