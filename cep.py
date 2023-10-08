import requests

#URL de acesso da API VIA CEP: https://viacep.com.br/
#URL para acessar um CEP especial: https://viacep.com.br/ws/<cep>/json/

class VerificarCEP:
    def __init__(self, cep):
        self.cep = cep.replace("-", "")
        self.url = f"https://viacep.com.br/ws/{self.cep}/json/"
        self.response = requests.get(self.url)
    

    def RetornoDeCEP(self):
        try:
            if self.response.status_code == 200:
                data = self.response.json()
                retorno_dados = [
                    data['cep'],
                    data['logradouro'],
                    data['bairro'],
                    data['localidade'],
                    data['uf']
                ]
                return retorno_dados
            else:
                d = {"msg": "CEP inválido",
                    "status": self.response.status_code}
                return d
        except Exception as e:
            d = {"msg": "Um erro ocorreu na busca do CEP",
                 "motivo": e}
            return d


if __name__ == "__main__":
    cep = VerificarCEP("03525050")
    print(cep.RetornoDeCEP())

