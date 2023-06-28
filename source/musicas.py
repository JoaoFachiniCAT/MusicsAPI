from flask import Flask, jsonify, request
from ..source.database import Database


class Musicas:

#create
    def cria_musica():
        
            banco= Database.connection
        
            cursor = banco.cursor()

            data = request.json

            nome = data.get('nome')
            duracao = data.get('duracao')
            genero_id = data.get('genero_id')
            lancamento = data.get('lancamento')

            insert = ('INSERT INTO musicas '
                    '(nome, generos_id, duracao, lancamento)'
                    ' VALUES '
                    '("' + nome + '", ' + str(duracao) +  ', ' +  str(genero_id) +  ', ' + str(lancamento) + ');'
                    )
            cursor.execute(insert)
            banco.commit()
            cursor.close()
            
            return insert
        
    #read
    
    def pega_musica(self):
        banco = Database.connection
        cursor = banco.cursor()
        
        select = ('select m.nome as "nome da musica", a.nome as "nome do artista", g.nome as "nome da gravadora", m.duracao '
                    ' from musicas_has_artistas ma '
                    ' join musicas as m on ma.musicas_id = m.id'
                    ' join artistas as a on ma.artistas_id = a.id'
                    ' join gravadoras as g on a.gravadoras_id = g.id order by a.nome asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'nome_musica': linha[0],
            'nome_artista': linha[1],
            'nome_gravadora': linha[2],
            'duracao': linha[3],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
        
        #read one
    def pega_musica_por_id(self, musica_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _musica = musica_id
        
        select = ('select m.nome as "nome da musica", a.nome as "nome do artista", g.nome as "nome da gravadora", m.duracao '
                    ' from musicas_has_artistas ma '
                    ' join musicas as m on ma.musicas_id = m.id'
                    ' join artistas as a on ma.artistas_id = a.id'
                    ' join gravadoras as g on a.gravadoras_id = g.id where m.id = ' + str(musica_id) +'order by a.nome asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'nome_musica': linha[0],
            'nome_artista': linha[1],
            'nome_gravadora': linha[2],
            'duracao': linha[3],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
    #update
    
    def atualiza_musica(self, musica_id):
                banco = Database.connection
                cursor = banco.cursor()
                
                _musica = musica_id
                
                data = request.json
                
                nome_musica = data.get('nome_musica')
                duracao = data.get('duracao')
                generos_id = data.get('generos_id')
                lancamento = data.get('lancamento')
            
                update = ('UPDATE musicas AS m '
            'SET m.nome = "' + nome_musica + '", m.duracao = "' + duracao + '", m.generos_id = ' + str(generos_id) + ', m.lancamento = "' + str(lancamento) + '" '
            'WHERE m.id = ' + str(_musica) + ';')
                
                cursor.execute(update)
                banco.commit()
                cursor.close()
                
                return update
    #delete
    
    def deleta_musica(self, musica_id):
        banco = Database.connection
        
        cursor = banco.cursor()

        _musica = musica_id

        delete = ('DELETE FROM musicas as m '
                    'WHERE m.id = ' + str(_musica) + ';')


        cursor.execute(delete)
        banco.commit()
        cursor.close()

        return delete