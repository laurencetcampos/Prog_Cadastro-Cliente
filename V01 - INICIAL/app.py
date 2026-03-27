# Importações necessárias para o funcionamento da aplicação Flask
from flask import Flask, render_template, request, redirect, jsonify
from cliente_route import post_cliente  # Importa a função para cadastrar cliente

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    # Renderiza o template index.html
    return render_template('index.html')

# Rota para adicionar um cliente, aceita métodos GET e POST
@app.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    # Bloco comentado: Código para uso com interface HTML (formulário web)
    # if request.method == 'POST':
    #     nome = request.form['nome']
    #     whatsapp = request.form['whatsapp']
    #     endereco = request.form['endereco']
    #     cidade = request.form['cidade']
    #     status = request.form['status']

    # Código ativo: Para testes de API via Postman (envio de dados via formulário ou JSON)
    data = request.form  # Obtém os dados do formulário
    nome = data.get('nome')  # Extrai o nome
    whatsapp = data.get('whatsapp')  # Extrai o WhatsApp
    endereco = data.get('endereco')  # Extrai o endereço
    cidade = data.get('cidade')  # Extrai a cidade
    status = data.get('status')  # Extrai o status

    # Chama a função para salvar o cliente no banco de dados
    post_cliente(nome, whatsapp, endereco, cidade, status)
    # Retorna uma resposta JSON de sucesso
    return jsonify({"message": "Cliente cadastrado com sucesso!"})
    # Código comentado: Redirecionamento para a página inicial (para uso com HTML)
    # return redirect('/')
    # Código comentado: Renderiza o template add_cliente.html (para uso com HTML)
    # return render_template('add_cliente.html')

# Executa a aplicação em modo debug se o script for executado diretamente
if __name__ == "__main__":
    app.run(debug=True)
