import mysql.connector

class Database:
    
    def connect():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="banco"
        )       
        status = print('Estado da conexão Banco de Dados: ' + str (connection.is_connected()))
        
        