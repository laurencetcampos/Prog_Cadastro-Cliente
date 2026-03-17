from flask import Flask, render_template, request, redirect, jsonify
from cliente_route import post_cliente

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
#    if request.method == 'POST':                   #Linha 12 ate 17 e linha 28 e 29 sao para uso de interface .html
#        nome = request.form['nome']
#        whatsapp = request.form['whatsapp']
#        endereco = request.form['endereco']
#        cidade = request.form ['cidade']
#        status = request.form['status']

        data = request.form                         #Linha 19 ate 24 e linha 27 sao exclusivamente para testes de API no postman, anterior a criacao dos arquivos .html
        nome = data.get('nome')
        whatsapp = data.get('whatsapp')
        endereco = data.get('endereco')
        cidade = data.get('cidade')
        status = data.get('status')

        post_cliente(nome, whatsapp, endereco, cidade, status)
        return jsonify({"message": "Cliente cadastrado com sucesso!"})
        #return redirect('/')
    #return render_template('add_cliente.html')
    
if __name__=="__main__":
    app.run(debug=True)
