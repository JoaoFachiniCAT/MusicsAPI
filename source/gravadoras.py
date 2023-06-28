from flask import Flask, jsonify, request
from ..source.database import Database


class Gravadoras:

#create
    def cria_grav():
        banco= Database.connection
    
        cursor = banco.cursor()

        data = request.json

        nome = data.get('nome')
        valor_contrato = data.get('valor-contrato')
        venc_contrato = data.get('venc-contrato')

        insert = ('INSERT INTO gravadoras '
                '(nome, valor_contrato, vencimento_contrato)'
                ' VALUES '
                '("' + nome +'", ' + str(valor_contrato)+ ', ' + str(venc_contrato) + ');'
                )
        cursor.execute(insert)
        banco.commit()
        cursor.close()
        
        return insert
    
    #read
   
    def pega_grav(self):
        banco = Database.connection
        cursor = banco.cursor()
        
    
        select = ('SELECT g.id AS gravadora_id, g.nome AS gravadoras, a.id AS artista_id, a.nome AS artistas '
                'FROM artistas AS a '
                'join gravadoras AS g ON g.id = a.gravadoras_id ORDER BY g.id asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'gravadora_id': linha[0],
            'gravadoras': linha[1],
            'artista_id': linha[2],
            'artistas': linha[3],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)   
    
    
    
    
    
    #read one
    
    def pega_grav_por_id(gravadora_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _gravadora = gravadora_id
        
        select = ('SELECT g.id AS gravadora_id, g.nome AS gravadoras, a.id AS artista_id, a.nome AS artistas '
                'FROM artistas AS a '
                'join gravadoras AS g ON g.id = a.gravadoras_id WHERE g.id = ' + str(gravadora_id) + ' ORDER BY g.id asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'gravadora_id': linha[0],
            'gravadoras': linha[1],
            'artista_id': linha[2],
            'artistas': linha[3],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
        
    #update
   
    def atualiza_grav(gravadora_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _gravadora = gravadora_id
        
        data = request.json
        
        nome = data.get('nome')
        valor_contrato = data.get('valor_contrato')
        vencimento = data.get('vencimento')

        update = ('UPDATE gravadora AS g '
                'SET g.nome = "' + nome + '", g.valor_contrato = ' + str(valor_contrato) + ', vencimento_contrato = "' + str(vencimento) + '" '
                'WHERE g.id = ' + + ';')

        cursor.execute(update)
        banco.commit()
        cursor.close()
        
        return update
    #delete
    
    def deleta_grav(gravadora_id):
                
                banco = Database.connection
                cursor = banco.cursor()
                
                _gravadora = gravadora_id
            
                delete = ('DELETE FROM gravadoras '
                            'WHERE id = ' + str(_gravadora) + ';')
                
            
                cursor.execute(delete)
                banco.commit()
                cursor.close()
                
                return delete
