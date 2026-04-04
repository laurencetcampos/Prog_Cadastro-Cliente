# -*- mode: python ; coding: utf-8 -*-
# Acima: Define que este arquivo Spec deve ser tratado como um script Python com codificação UTF-8.

# --- ETAPA 1: ANÁLISE ---
# Inicia a Análise, descobrindo as dependências e arquivos que o programa precisa para rodar.
a = Analysis(
    # Script principal do aplicativo, o ponto de virada/entrada para o executável.
    ['app.py'],
    # Diretórios adicionais a serem pesquisados para procurar bibliotecas ou pacotes (vazio neste caso).
    pathex=[],
    # Arquivos binários extras a serem incluídos no programa (como arquivos .dll no Windows).
    binaries=[],
    # Documentos ou pastas extras a serem copiados para o programa final.
    # Neste caso: está enviando a pasta 'templates' e também o banco 'database.sqlite'.
    datas=[('templates', 'templates'), ('database.sqlite', '.')],
    # Módulos Python em que o PyInstaller falhou em encontrar automaticamente; eles podem ser inseridos listados aqui.
    hiddenimports=[],
    # Caminhos para arquivos de "hooks" (scripts criados para corrigir problemas de bibliotecas específicas).
    hookspath=[],
    # Configurações que podem ser passadas especificamente para customizar seus arquivos de "hooks".
    hooksconfig={},
    # Módulos Python secundários que precisam rodar antes do aplicativo base 'app.py' iniciar.
    runtime_hooks=[],
    # Módulos que você quer explicitamente informar ao PyInstaller que NÃO devem ser importados pelo executável.
    excludes=[],
    # Se ativado (True), não empacota arquivos de bytecodes dentro do executável em modo compatível e rápido. Causa aumento no tamanho.
    noarchive=False,
    # Controle do nível de otimização de bytecode que o programa terá no final (0 significa nenhuma otimização extra do CPython ou PyInstaller).
    optimize=0,
)

# --- ETAPA 2: ARCHIVE (Geração PYZ) ---
# Criação do "Python Zipped", um arquivo compacto (estilo .zip) interno que agrupa os módulos e cópias dos códigos Python "puros" que o PyInstaller preparou durante a Análise.
pyz = PYZ(a.pure)

# --- ETAPA 3: GERAR O EXECUTÁVEL ---
# Define como o arquivo Executável real (o .exe no Windows) em si será construído usando blocos passados abaixo.
exe = EXE(
    # Adiciona o agrupamento compacto do pacote PYZ que foi gerado no passo de cima.
    pyz,
    # Scripts básicos extraídos que o executável precisa rodar.
    a.scripts,
    # Um array que, em pacotes maiores, normalmente abrigam bibliotecas se você deseja gerar um único-arquivo .exe exclusivo (modo One-File).
    [],
    # True = Evita incorporar binários (dependências) dentro do .exe. Em vez disso, envia tudo solto em uma pasta. É conhecido como (Modo Um-Diretório/Pasta Múltipla).
    exclude_binaries=True,
    # Nome do arquivo final executável que será impresso para uso (Oferta-Direta.exe).
    name='Oferta-Direta',
    # Se modificado para True, imprime informações no terminal detalhadas de depuração no momento exato em que o executável estiver rodando.
    debug=False,
    # Ficar definido como False significa que os sinais padrões de boot do sistema operacional e de interface não vão ser ignorados antes do boot principal.
    bootloader_ignore_signals=False,
    # Comandos para extrair ou preservar descrições de tabelas de símbolos (para análise nativa no UNIX, geralmente deixado nativo ou em False).
    strip=False,
    # Permite a utilização de compactação de bibliotecas pelo software universal UPX (se UPX estiver instalado na máquina que compila).
    upx=True,
    # False = Esconde a janela de comando do MS-DOS / CMD. Opcionamente configurado aqui como True, ele abrirá um console preto atrás da tela em aplicativos de interface ou terminal puro.
    console=True,
    # O PyInstaller não tentará proibir falhas que tentem gerar exceções via mensagens de janelas do SO quando isto for False.
    disable_windowed_traceback=False,
    # Comando útil para uso em sistemas Mac/Apple e MacOS para interceptar sinais emitidos do SO sobre arquivo. Ignore isso no Windows.
    argv_emulation=False,
    # Target de arquitetura para compilação multiplataforma (ex: x86, amd64). None usa o seu próprio OS padrão do momento.
    target_arch=None,
    # Assinatura de pacote e de certificado Apple para rodar app seguro no OS X. Windows não é afetado.
    codesign_identity=None,
    # Ficheiro customizado Apple Developer Entitlements para autorizar coisas à nível do sistema no Mac.
    entitlements_file=None,
)

# --- ETAPA 4: ARMAZENAR NO DIRETÓRIO ---
# O COLLECT é responsável por empacotar a versão diretório e pasta múltipla. É a fase final se não constratar Modo arquivo Unico (.exe tudo-em-um). Ele ajuntará tudo isso na pasta "dist".
coll = COLLECT(
    # Junta o aplicativo executável que foi preparado logo acima dele.
    exe,
    # Agrupa as extensões .dll (no Windows), .so (no Linux) que sua análise preparou.
    a.binaries,
    # Agrupa e anexa junto os seus anexos complementares referenciados lá em cima (as 'templates' e a 'database.sqlite').
    a.datas,
    # Nenhuma limpeza nativa profunda em pacotes .so (deixa igual na parte superior).
    strip=False,
    # Reforça uso do compactador externo UPX caso ele exista nas pastas extras também além do EXECUTÁVEL .exe.
    upx=True,
    # Configura-se caso quiser ignorar um DLL/arquivo específico para impedir compactação externa que vá quebrá-lo.
    upx_exclude=[],
    # O Nome da pasta final, que hospedará todos seus recursos e executável lá dentro do diretório `/dist`.
    name='Oferta-Direta',
)
