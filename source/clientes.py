from flask import Flask, jsonify, request
from ..source.database import Database

class Clientes:
    
#create
    def cria_cliente():
        
            banco= Database.connection
        
            cursor = banco.cursor()

            data = request.json

            login = data.get('nome')
            senha = data.get('senha')
            planos_id = data.get('gravadora_id')
            email = data.get('email')

            insert = ('INSERT INTO clientes '
                    '(login, senha, planos_id, email)'
                    ' VALUES '
                    '("' + login +'", ' + str(senha) + ', ' + str(planos_id) + ', ' + str(email) +');'
                        )
            cursor.execute(insert)
            banco.commit()
            cursor.close()
            
            return insert, Database.status
        
    #read
    def get_clientes():
        banco = Database.connection
        cursor = banco.cursor()
        
        data = request.json
        
        select = ('select  c.id as user_id, p.id as plano_id, c.login, p.descricao, p.valor, p.limite, m.nome as nome_musica'
                    'from musicas_has_clientes mc '
                    'join clientes c on mc.clientes_id = c.id'
                    'join musicas m on mc.musicas_id = m.id '
                    'join planos p on c.planos_id = p.id order by c.login asc;')
        
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'user_id': linha[0],
            'plano_id': linha[1],
            'login': linha[2],
            'descrição': linha[3],
            'valor': linha[4],
            'limite': linha[5],
            'nome_musica': linha[6],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)

        
    #read one 
    def pega_cliente_por_id(cliente_id):  
        banco = Database.connection
        cursor = banco.cursor()
        
        _cliente = cliente_id
        
        select = ('select c.id as user_id, p.id as plano_id, c.login, p.descricao, p.valor, p.limite, m.nome as nome_musica'
                    'from musicas_has_clientes mc' 
                    'join clientes c on mc.clientes_id = c.id'
                    'join musicas m on mc.musicas_id = m.id '
                    'join planos p on c.planos_id = p.id where c.id = ' + _cliente + ' order by c.login asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'user_id': linha[0],
            'plano_id': linha[1],
            'login': linha[2],
            'descrição': linha[3],
            'valor': linha[4],
            'limite': linha[5],
            'nome_musica': linha[6],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)

    #update
    def atualiza_cliente(cliente_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _cliente = cliente_id
        
        data = request.json
        
        login = data.get('login')
        senha = data.get('senha')
        planos_id = data.get('planos_id')
        email = data.get('email')
        

        update = ('UPDATE clientes as c '
    'SET c.login = "' + login + '", c.senha = "' + senha + '", c.planos_id = ' + str(planos_id) + ', c.email = "' + email + '" '
    'WHERE p.id = ' + str(_cliente) + ';')
            
        cursor.execute(update)
        banco.commit()
        cursor.close()
        
        return update

        #delete
    def deleta_cliente(self, cliente_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _cliente = cliente_id

        delete = ('DELETE FROM cliente '
                        'WHERE id = ' + str(_cliente) + ';')
        
        
        cursor.execute(delete)
        banco.commit()
        cursor.close()
                
        return delete