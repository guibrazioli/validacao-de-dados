import requests
from acesso_cep2 import BuscaEndereco

cep = "01001000"
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)

