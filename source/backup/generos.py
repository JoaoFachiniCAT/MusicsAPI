from flask import Flask, jsonify, request
from source.database import Database

class Generos:
   #create
    def cria_generos(self):
    
            banco = Database.connection
            
            cursor = banco.cursor()

            data = request.json

            descricao = data.get('descricao')
            

            insert = ('INSERT INTO generos '
                    '(descricao)'
                    ' VALUES ("' + descricao + '");'
                        )
            cursor.execute(insert)
            banco.commit()
            cursor.close()
            
            return insert


    def get_generos():
        banco = Database.connection
        cursor = banco.cursor()
        
        select = '(SELECT id, descricao FROM generos)'
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'ID': linha[0],
            'descrição': linha[1],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
        
    #read one 
    def get_generos_id(genero_id): 
        banco = Database.connection
        cursor = banco.cursor()
        
        _genero = genero_id
        
        select = ('SELECT id, descricao  FROM generos as g where g.id = ' + str(_genero) +';')
        
        cursor.execute(select)
        linhas = cursor.fetchone()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'ID': linha[0],
            'descrição': linha[1],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
        
        
    #update
    
    def att_generos_id(self, genero_id):
            banco = Database.connection
            cursor = banco.cursor()
            
            _genero = genero_id
            
            data = request.json
            
            descricao = data.get('descricao')
        
            update = ('UPDATE generos AS g '
                    'SET g.descricao = "' + _genero + '";')
        
            cursor.execute(update)
            banco.commit()
            cursor.close()
            
            return update

    #delete
    def deleta_genero(self, genero_id):
        
        banco = Database.connection
        cursor = banco.cursor()
        
        _genero = genero_id

        delete = ('DELETE FROM generos '
                    'WHERE id = ' + str(_genero) + ';')
        
        
        cursor.execute(delete)
        banco.commit()
        cursor.close()
        
        return delete