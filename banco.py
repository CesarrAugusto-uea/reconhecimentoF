import sqlite3

conexao = sqlite3.connect('banco.db')

c = conexao.cursor()

#SQL


def creatre_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados(id integer primary key autoincrement not null, nome text not null)')

creatre_table()

def dataentry(nome=None):
     c.execute("""INSERT INTO dados(nome,id) VALUES(?,?)""", (id, nome))


