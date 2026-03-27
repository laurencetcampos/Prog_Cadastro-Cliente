# Projeto Integrador I - Grupo 7 - UNIVESP - Eng. de Computação

## Visão Geral
Aplicação web para cadastro de clientes interessados em promoções de uma empresa fictícia. Permite armazenar dados como nome, endereço, telefone e status de interesse em promoções.

**Data da Reunião Inicial:** 05-Mar-26  
**Tecnologias:** Python (Flask), MySQL, HTML, CSS

## Estrutura do Projeto
- `V01 - INICIAL/`: Versão inicial com funcionalidade básica de cadastro via API.
- `V02 - CRUD/`: Versão completa com operações CRUD (Create, Read, Update, Delete) e interface web.
- `Pag-Internet_Proj-Int-I_G7/`: Projeto de página web relacionado (possivelmente landing page).

## Tecnologias Utilizadas
- **Backend:** Python com Flask
- **Banco de Dados:** MySQL
- **Frontend:** HTML, CSS (para V02)
- **Ferramentas:** Postman para testes de API

## Instalação e Configuração
1. **Pré-requisitos:**
   - Python 3.x instalado
   - MySQL Server instalado e rodando
   - Criar um banco de dados MySQL (ex: `clientes_db`)

2. **Clonagem do Repositório:**
   ```
   git clone <url-do-repositorio>
   cd temp_repo
   ```

3. **Instalação de Dependências:**
   ```
   pip install flask mysql-connector-python
   ```

4. **Configuração do Banco de Dados:**
   - Execute as queries em `MySQL_Queries.txt` para criar a tabela `clientes`.
   - Atualize `DB_connection.py` com suas credenciais MySQL.

5. **Execução:**
   - Para V01: `python V01 - INICIAL/app.py`
   - Para V02: `python V02 - CRUD/app.py`
   - Acesse `http://localhost:5000` no navegador.

## Uso
- **V01:** Teste via Postman enviando dados para `/add_cliente`.
- **V02:** Interface web completa para gerenciar clientes.

## Próximos Passos Sugeridos
1. **Configuração Completa do Banco:** Garantir que o MySQL esteja configurado e a tabela criada.
2. **Validação de Dados:** Adicionar validações nos formulários (ex: campos obrigatórios, formato de telefone).
3. **Melhoria da UI:** Estilizar melhor os templates HTML com CSS avançado.
4. **Funcionalidades Adicionais:** Adicionar busca/filtragem de clientes, exportação de dados.
5. **Segurança:** Implementar autenticação de usuários, proteção contra SQL injection (já parcialmente feito com placeholders).
6. **Testes:** Criar testes unitários para as funções de banco.
7. **Deploy:** Configurar para produção (ex: com Gunicorn, Docker).
8. **Documentação de API:** Detalhar endpoints para desenvolvedores.

## Contribuição
- Faça um fork do projeto.
- Crie uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`.
- Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`.
- Push para a branch: `git push origin feature/nova-funcionalidade`.
- Abra um Pull Request.

## Licença
Este projeto é para fins educacionais - UNIVESP.
