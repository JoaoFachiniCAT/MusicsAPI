from app_t import *
from api_dao_t import Artistas

import pytest



# fazer mocks para todas as funções de acesso 
# fazer teste de integração criando uma tabela e inserindo dados
#mockar todoas os testes para imitar banco de dados

#test.database.Database.connect


def test_artistas(mocker):
        mocker.patch('database_t.Database.connect',
                return_value = 200 )        
        response = app.pega_artistas.get('/artistas')
        assert response.status_code == 200

