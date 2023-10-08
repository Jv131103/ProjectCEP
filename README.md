# ProjectCEP
Código de CEP

# Verificador de CEP utilizando a API Via CEP

Este é um simples script em Python que utiliza a biblioteca requests para consultar informações sobre um CEP através da API Via CEP. A API Via CEP fornece dados de endereços no Brasil com base no CEP informado.

## Uso
Certifique-se de ter o Python instalado em seu ambiente.
Execute o script verificar_cep.py.

``` Python
python verificar_cep.py
```

1. Substitua o CEP padrão no exemplo (03525050) pelo CEP desejado.
``` Python
cep = VerificarCEP("SEU_CEP_AQUI")
print(cep.RetornoDeCEP())
```

## Classe VerificarCEP
### Método __init__(self, cep)
  . Descrição: O método de inicialização da classe. Recebe um CEP como parâmetro, formata-o removendo possíveis hífens, e constrói a URL da API Via CEP.

### Método RetornoDeCEP(self)
  . Descrição: Realiza a solicitação à API Via CEP, trata a resposta e retorna os dados do endereço associados ao CEP informado.
  . Retorno:
    - Se o CEP for válido, retorna uma lista com os seguintes elementos:
      . CEP
      . Logradouro
      . Bairro
      . Localidade
      . UF
  . Se o CEP for inválido, retorna um dicionário com a mensagem de erro e o código de status HTTP.
  . Em caso de erro durante a busca, retorna um dicionário com a mensagem de erro e o motivo.

## Exemplo de Uso

``` Python
if __name__ == "__main__":
    cep = VerificarCEP("SE U_CEP_AQUI")
    print(cep.RetornoDeCEP())
```

Substitua "SEU_CEP_AQUI" pelo CEP desejado e execute o script para obter as informações associadas ao CEP.

### Nota
Certifique-se de ter uma conexão com a internet para realizar a consulta à API Via CEP.

## Observação 
Este README fornece instruções básicas para utilizar o script. Certifique-se de revisar o código-fonte para entender melhor as funcionalidades e adaptá-lo conforme necessário para seus próprios projetos.

# Aplicação Flask para Verificação de CEP

Este é um exemplo simples de uma aplicação web utilizando o framework Flask para verificar informações de um CEP. A aplicação inclui duas rotas:
1. Rota Principal ('/'): Exibe um formulário HTML para inserir o CEP.
2. Rota de Gravação ('/gravar'): Recebe o CEP digitado, verifica as informações usando a classe VerificarCEP e exibe os resultados.

## Requisitos
Certifique-se de ter o Flask instalado. Caso não tenha, você pode instalá-lo usando o seguinte comando:`

``` Terminal
pip install flask
```

## Estrutura de Arquivos
A estrutura de arquivos inclui um diretório templates para armazenar os modelos HTML.

project_folder/
│
├── app.py
├── cep.py
└── templates/
    ├── cep.html
    ├── dados.html
    └── erro.html

### Código Python (app.py)
``` Python
from flask import Flask, render_template, request
from cep import VerificarCEP
import os

app = Flask(__name__)

# Configurar o diretório de templates
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

@app.route('/', methods=['GET', 'POST'])
def Cep():
    return render_template('cep.html')

@app.route("/gravar", methods=['POST'])
def gravar():
    if request.method == 'POST':
        cep_digitado = request.form['cep']
        if cep_digitado == "":
            return render_template("erro.html", msg="Dados não inseridos")
        
        verificador_cep = VerificarCEP(cep_digitado)
        dados_cep = verificador_cep.RetornoDeCEP()

        if 'msg' in dados_cep:
            return render_template("erro.html", msg=dados_cep["msg"])
        else:
            return render_template('dados.html', dados_cep=dados_cep, cep_digitado=cep_digitado)

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
```

## Executando a Aplicação
Execute o script app.py para iniciar o servidor Flask.
``` Python
python app.py
```

Acesse a aplicação em seu navegador usando o endereço http://localhost:5001/.
##
Lembre-se de substituir os modelos HTML (cep.html, dados.html e erro.html) e a classe VerificarCEP conforme necessário para atender aos requisitos específicos da sua aplicação.
##
Certifique-se de que a classe VerificarCEP está implementada no arquivo cep.py no mesmo diretório do app.py.
