# Importações necessárias do Flask para renderização web e rotas
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# Importações das funções de banco de dados do arquivo cliente_route.py
from cliente_route import post_cliente, get_clientes, get_cliente_by_id, update_cliente, delete_cliente

import sys
import os
import webbrowser
from threading import Timer

# Verifica se o programa está sendo rodado como um executável pelo PyInstaller e ajusta o diretório de templates
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flash_messages' # Chave secreta necessária para as mensagens flash (alertas visuais)

@app.route('/')
def index():
    # Rota raiz: Busca todos os clientes no banco de dados e exibe na página inicial (tabela)
    clientes = get_clientes()
    return render_template('index.html', clientes=clientes)

@app.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    # Rota para adicionar um novo cliente. Aceita exibição do formulário (GET) e envio de dados (POST)
    if request.method == 'POST':
        # ---------- INÍCIO BLOCO INTERFACE WEB ----------
        # Captura os dados enviados pelo formulário HTML
        nome = request.form['nome']
        whatsapp = request.form['whatsapp']
        endereco = request.form['endereco']
        cidade = request.form['cidade']
        status = 1 if 'status' in request.form else 0

        post_cliente(nome, whatsapp, endereco, cidade, status) # Salva no banco
        flash('Cliente cadastrado com sucesso!', 'success') # Mensagem de sucesso na tela
        return redirect(url_for('index')) # Volta para a página inicial
        # ---------- FIM BLOCO INTERFACE WEB ----------
        
        # ---------- INÍCIO BLOCO TESTE API / POSTMAN (DESCOMENTAR PARA USAR) ----------
        # As linhas abaixo são exclusivamente para testes de API simulando envios JSON via Postman
        '''
        data = request.get_json() if request.is_json else request.form
        nome = data.get('nome')
        whatsapp = data.get('whatsapp')
        endereco = data.get('endereco')
        cidade = data.get('cidade')
        status = data.get('status', 0)

        post_cliente(nome, whatsapp, endereco, cidade, status)
        return jsonify({"message": "Cliente cadastrado com sucesso via API!"})
        '''
        # ---------- FIM BLOCO TESTE API / POSTMAN ----------

    # Se for GET, apenas mostra a página com o formulário vazio
    return render_template('add_cliente.html')

@app.route('/edit_cliente/<int:id>', methods=['GET', 'POST'])
def edit_cliente(id):
    # Rota para editar um cliente existente, recebe o ID na URL
    if request.method == 'POST':
        # Se recebeu dados novos (POST), atualiza no banco
        nome = request.form['nome']
        whatsapp = request.form['whatsapp']
        endereco = request.form['endereco']
        cidade = request.form['cidade']
        status = 1 if 'status' in request.form else 0

        update_cliente(id, nome, whatsapp, endereco, cidade, status)
        flash('Cliente atualizado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    # Se for GET, busca os dados atuais do cliente para preencher o formulário
    cliente = get_cliente_by_id(id)
    if not cliente:
        flash('Cliente não encontrado!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('edit_cliente.html', cliente=cliente)

@app.route('/delete_cliente/<int:id>')
def delete_cliente_route(id):
    # Rota para deletar um cliente, recebe o ID na URL
    delete_cliente(id)
    flash('Cliente removido com sucesso!', 'success')
    return redirect(url_for('index'))
    
if __name__=="__main__":
    # Módulo que executa a abertura automática do navegador
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/")
        
    # Aciona um atraso de 1.25 segundos para abrir o navegador, dando tempo ao Flask de iniciar o servidor
    Timer(1.25, open_browser).start()
    
    # Executa o servidor Flask localmente na porta 5000 (debug=False impede que abra o navegador 2 vezes)
    app.run(debug=False, port=5000)
