from flask import Flask, render_template, request, jsonify
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
