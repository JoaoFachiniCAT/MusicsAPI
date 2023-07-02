from database_t import Database
from flask import Flask, request, jsonify
from api_dao_t import *


    
#criar end points para manipulação de musica has artistas e musicas has clientes
 

app = Flask(__name__)

#-----------------------------------------------Artistas---------------------------------------

@app.route('/artistas', methods=['POST'])
def criar_artista():
     return 'Sucesso!'
 
@app.route('/artistas', methods = ['GET'])
def pega_artistas():
    return Artistas.get_artistas()

@app.route('/artistas/<int:artista_id>', methods=['GET'])
def pega_artista(artista_id):
    return Artistas.get_artista_id(artista_id)

@app.route('/artistas/<int:artista_id>', methods=['PUT'])
def att_artista(artista_id):
    Artistas.atualiza_artista(artista_id)
    return 'Sucesso!'
    
@app.route('/artistas/<int:artista_id>', methods=['DELETE'])
def del_artista(artista_id):
    Artistas.delete_artista(artista_id)
    return 'Artista com id = ' +  str (artista_id) + ' excluído com sucesso!'


#-----------------------------------clientes#----------------------------------
@app.route('/clientes', methods=['POST'])
def insert_cliente():
    Clientes.cria_cliente()
    return 'Cliente Criado com Sucesso!'

@app.route('/clientes', methods=['GET'])
def get_cliente():
    return Clientes.get_clientes()

@app.route('/clientes/has-musicas', methods=['GET'])
def get_chm():
     return Clientes.cliente_has_musica()

@app.route('/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente_id(cliente_id):
    return Clientes.pega_cliente_por_id(cliente_id)

@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def atualiza_cliente(cliente_id):
    Clientes.atualiza_cliente(cliente_id)
    return 'Cliente atualizado com sucesso!'

@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def exclui_cliente(cliente_id):
    Clientes.deleta_cliente(cliente_id)
    return 'Cliente excluido com sucesso!'

#-----------------------------------generos------------------------------------

@app.route('/generos', methods=['POST'])
def insert_genero():
    Generos.cria_generos()
    return 'Genero criado com sucesso!'

@app.route('/generos', methods=['GET'])
def select_generos():
    return Generos.get_generos()

@app.route('/generos/<int:genero_id>', methods=['GET'])
def select_generos_id(genero_id):
    return Generos.get_generos_id(genero_id)

@app.route('/generos/<int:genero_id>', methods=['PUT'])
def update_generos(genero_id):
    Generos.att_generos_id(genero_id)
    return 'Genero Atualizado com sucesso!'

@app.route('/generos/<int:genero_id>', methods=['DELETE'])
def delete_generos(genero_id):
    Generos.deleta_genero(genero_id)
    return "Genero deletado com sucesso!"

# #----------------------------------gravadoras----------------------------------

@app.route('/gravadoras', methods=['POST'])
def cria_gravadora():
    Gravadoras.cria_grav()
    return 'Gravadora criada com sucesso!'

@app.route('/gravadoras', methods=['GET'])
def get_gravadora():
    return Gravadoras.pega_grav()

@app.route('/gravadoras/<int:gravadora_id>', methods=['GET'])
def get_gravadora_id(gravadora_id):
    return Gravadoras.pega_grav_por_id(gravadora_id)

@app.route('/gravadoras/<int:gravadora_id>', methods=['PUT'])
def update_gravadora(gravadora_id):
    Gravadoras.atualiza_grav(gravadora_id)
    return 'Gravadora atualizada com sucesso!'

@app.route('/gravadoras/<int:gravadora_id>', methods=['DELETE'])
def delete_gravadora(gravadora_id):
    Gravadoras.deleta_grav(gravadora_id)
    return 'Gravadora deletada com sucesso!'

# #---------------------------------musicas--------------------------------------

@app.route('/musicas', methods=['POST'])
def insert_musica():
    Musicas.cria_musica()
    return 'Musica criada com sucesso!'

@app.route('/musicas', methods=['GET'])
def get_musica():
    return Musicas.pega_musica()

@app.route('/musicas/<int:musica_id>', methods=['GET'])
def get_musica_id(musica_id):
    return Musicas.pega_musica_por_id(musica_id)

@app.route('/planos/<int:plano_id>', methods=['PUT'])
def update_musica(musica_id):
    Musicas.atualiza_musica(musica_id)
    return 'Musica deletada com sucesso!'

@app.route('/musicas/<int:musica_id>', methods=['DELETE'])
def delete_musica(musica_id):
    Musicas.deleta_musica(musica_id)
    return 'Musica deletada com sucesso!'

# #---------------------------------planos---------------------------------------------

@app.route('/planos', methods=['POST'])
def insert_planos():
    Planos.cria_plano()
    return 'Planos criado com sucesso!'

@app.route('/planos', methods=['GET'])
def select_planos():
    return Planos.pega_plano()
    
@app.route('/planos/<int:plano_id>', methods=['GET'])
def select_planos_id(plano_id):
    return Planos.pega_plano_por_id(plano_id)

@app.route('/planos/<int:plano_id>', methods=['PUT'])
def update_planos(plano_id):
    Planos.atualiza_plano(plano_id)
    return 'Plano atualizado com sucesso!'

@app.route('/planos/<int:plano_id>', methods=['DELETE'])
def delete_planos(plano_id):
    Planos.deleta_plano(plano_id)
    return 'Plano deletado com sucesso!'

app.run(port=5050, host="localhost", debug=True)