import mysql.connector

class conexaoDB:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="celsadas",
            password="33880188",
            database="ex"
        )
        self.cursor = self.conexao.cursor()

    def select_bd(self, comando, valores):
        self.cursor.execute(comando, valores)
        return self.cursor.fetchall()

    def insert_bd(self, comando, valores):
        self.cursor.execute(comando, valores)
        self.conexao.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
