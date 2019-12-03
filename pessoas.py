from banco import Banco

class Pessoas(object):

    def __init__(self, id = 0, nome = ""):
        self.id = id
        self.nome = nome


    def insertUser(self):
        print(self.nome)
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c.execute("insert into pessoas(nome)) values ('" + self.nome+"')")
            banco.conexao.commit()
            c.close()

            return "aa"
        except:
            return"bb"

    def selectUser(self,id):
        banco = Banco()
        try:

            c= banco.conexao.cursor()
            c.execute("select * from pessoas where id = " + id + "   ")
            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]

            c.close()

            return"a"
        except:
            return"b"

    def getTable (self):
        banco = Banco()
        try:
            c= banco.conexao.cursor()
            c.execute("select * from pessoas")
            for linha in c:
                print(linha)


            c.close()

            return "pessoas"
        except:
            return "nao deu"






