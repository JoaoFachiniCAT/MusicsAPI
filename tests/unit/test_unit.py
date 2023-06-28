from source.api_dao import *
from source.database import Database

import pytest

# fazer mocks para todas as funções de acesso 
# fazer teste de integração criando uma tabela e inserindo dados

@pytest.fixture

def test_conexao_banco():
    status = Database.connection.is_connected()
    assert status == True

# def test_artistas():
    