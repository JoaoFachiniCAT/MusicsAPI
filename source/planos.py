from flask import Flask, jsonify, request
from ..source.database import Database


class Planos:

    #create
    
    def cria_plano(self):
    
            banco= Database.connection
        
            cursor = banco.cursor()

            data = request.json

            descricao = data.get('descricao')
            valor = data.get('valor')
            limite = data.get('limite')
            
            insert = ('INSERT INTO planos '
                    '(descricao, valor, limite)'
                    ' VALUES'
                    '("' + descricao +'", ' + str(valor) + ', ' + str(limite) +');'
                        )
            cursor.execute(insert)
            banco.commit()
            cursor.close()
            
            return insert, Database.status
        
        #read
    def pega_plano():
        banco = Database.connection
        cursor = banco.cursor()
        
        select = ('SELECT id, descricao, valor, limite FROM planos;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultados = []
        for linha in linhas:
            resultado = {
            'id': linha[0],
            'descricao': linha[1],
            'valor': linha[2],
            'limite': linha[3]
            }
            resultados.append(resultado)
        
        return jsonify(resultados)
        
        #read one
    def pega_plano_por_id(plano_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _plano = plano_id
        
        select = ('SELECT id, descricao, valor, limite '
                'FROM planos as p WHERE p.id =' + str(_plano) + ';')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultados = []
        for linha in linhas:
            resultado = {
            'id': linha[0],
            'descricao': linha[1],
            'valor': linha[2],
            'limite': linha[3]
            }
            resultados.append(resultado)
        
        return jsonify(resultados)

        #update
    def atualiza_plano( plano_id):
                banco = Database.connection
                cursor = banco.cursor()
                
                _plano = plano_id
                
                data = request.json
                
                descricao = data.get('descricao')
                valor = data.get('valor')
                limite = data.get('limite')
            
                update = ('UPDATE planos as p '
            'SET p.descricao = "' + descricao + '", p.valor = ' + str(valor) + ', p.limite = ' + str(limite) +  ' '
            'WHERE p.id = ' + str(_plano) + ';')
                
                cursor.execute(update)
                banco.commit()
                cursor.close()
                
                return update

    #delete
    def deleta_plano(self, plano_id):
        banco = Database.connection
        
        cursor = banco.cursor()

        _plano = plano_id

        delete = ('DELETE FROM planos as p '
                    'WHERE p.id = ' + str(_plano) + ';')


        cursor.execute(delete)
        banco.commit()
        cursor.close()

        return delete
