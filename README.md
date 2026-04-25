# Projeto Integrador I - Grupo 7 - UNIVESP - Eng. de Computação

## Visão Geral
Aplicação web para cadastro de clientes interessados em promoções. Permite armazenar dados como nome, endereço, telefone e status de interesse em promoções.

**Data da Reunião Inicial:** 05-Mar-26  
**Tecnologias:** Python (Flask), MySQL, HTML, CSS

## Estrutura do Projeto
- `V01 - INICIAL/`: Versão inicial com funcionalidade básica de cadastro via API.
- `V02 - CRUD/`: Versão completa com operações CRUD (Create, Read, Update, Delete) e interface web.
- `V03 - CRUD/`: Implementado no codigo script para criação de arquivo executavel e add ao banco de dados 30 cadastro de clientes aleatórios, para testes e validações.

## Tecnologias Utilizadas
- **Backend:** Python com Flask
- **Banco de Dados:** MySQL
- **Frontend:** HTML, CSS (para V02)
- **Ferramentas:** Postman para testes de API

## Instalação e Configuração
1. **Pré-requisitos:**
   - Python 3.x instalado
   - MySQL Server instalado e rodando
      Nota: Em 04-Abr-26, implementada conversão do banco de dados em MySQL para SQlite a cada execução do scrip para criar o arq .exe 
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
   - Para V03: `python V03 - CRUD/app.py ou Oferta-Direta.exe`
   - Acesse `http://localhost:5000` ou `http://127.0.0.1:5000` no navegador.

## Uso
- **V01:** Teste via Postman enviando dados para `/add_cliente`.
- **V02:** Interface web completa para gerenciar clientes.-
- **V03:** Teste com implementação de script para criar arquivo executável.

## Próximos Passos Sugeridos
1. **Configuração Completa do Banco:** Garantir que o MySQL esteja configurado e a tabela criada.
2. **Validação de Dados:** Adicionar validações nos formulários (ex: campos obrigatórios, formato de telefone).
   Nota: formato de telefone (mascara) implementa em V03 - CRUD
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
