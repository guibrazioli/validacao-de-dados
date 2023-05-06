import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.validador_cep(cep):
            self.cep = cep
        else:
            raise ValueError ("CEP Inválido!")
        

    def __str__(self):
        return self.format_cep()
        

    def validador_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
            
        
    def format_cep(self):
        return f"{self.cep[:4]}-{self.cep[4:]}"

    
    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )       