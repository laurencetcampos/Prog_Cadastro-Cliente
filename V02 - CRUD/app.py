# Importações necessárias do Flask para renderização web e rotas
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# Importações das funções de banco de dados do arquivo cliente_route.py
from cliente_route import post_cliente, get_clientes, get_cliente_by_id, update_cliente, delete_cliente

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flash_messages' # Chave secreta necessária para as mensagens flash (alertas visuais)

@app.route('/')
def index():
    # Rota raiz: Busca todos os clientes no banco de dados e exibe na página inicial (tabela)
    success, result = get_clientes()
    if success:
        clientes = result
    else:
        clientes = []
        flash(result, 'danger')
        
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

        success, msg = post_cliente(nome, whatsapp, endereco, cidade, status) # Salva no banco
        if success:
            flash(msg, 'success') # Mensagem de sucesso na tela
            return redirect(url_for('index')) # Volta para a página inicial
        else:
            flash(msg, 'danger') # Mensagem de erro na tela (ex: whatsapp duplicado)
            return render_template('add_cliente.html') # Deixa o usuário tentar novamente
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

        success, msg = update_cliente(id, nome, whatsapp, endereco, cidade, status)
        if success:
            flash(msg, 'success')
            return redirect(url_for('index'))
        else:
            flash(msg, 'danger')
            success_id, cliente_or_msg = get_cliente_by_id(id)
            if success_id:
                return render_template('edit_cliente.html', cliente=cliente_or_msg)
            else:
                return redirect(url_for('index'))
    
    # Se for GET, busca os dados atuais do cliente para preencher o formulário
    success_id, cliente_or_msg = get_cliente_by_id(id)
    if not success_id:
        flash(cliente_or_msg, 'danger')
        return redirect(url_for('index'))
    
    return render_template('edit_cliente.html', cliente=cliente_or_msg)

@app.route('/delete_cliente/<int:id>')
def delete_cliente_route(id):
    # Rota para deletar um cliente, recebe o ID na URL
    success, msg = delete_cliente(id)
    if success:
        flash(msg, 'success')
    else:
        flash(msg, 'danger')
    return redirect(url_for('index'))
    
if __name__=="__main__":
    app.run(debug=True)
