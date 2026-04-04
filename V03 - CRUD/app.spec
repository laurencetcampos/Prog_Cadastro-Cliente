# ==============================================================================
# CONFIGURAÇÃO DE EMPACOTAMENTO PYINSTALLER (app.spec)
# ==============================================================================

# Cria a análise dos arquivos necessários para o executável
a = Analysis(
    ['app.py'], # Arquivo principal do aplicativo
    pathex=[], # Caminhos adicionais para buscar módulos
    binaries=[], # Arquivos binários adicionais
    datas=[], # Arquivos de dados não Python a incluir
    hiddenimports=[], # Módulos que o PyInstaller não detecta
    hookspath=[], # Caminho para hooks personalizados
    hooksconfig={}, # Configuração de hooks específicos
    runtime_hooks=[], # Scripts que rodam antes de iniciar
    excludes=[], # Módulos a serem excluídos do executável
    noarchive=False, # Define se os arquivos entram no build
    optimize=0, # Nível de otimização
)

# Cria o arquivo PYZ com os módulos Python puros
pyz = PYZ(a.pure)

# Cria o executável
exe = EXE(
    pyz, # Arquivos Python compactados
    a.scripts, # Scripts de inicialização
    a.binaries, # Arquivos binários
    a.datas, # Arquivos de dados
    [], # Opções adicionais
    name='app', # Nome do executável final
    debug=False, # Modo de depuração (debug)
    bootloader_ignore_signals=False, # Ignora sinais do sistema no boot
    strip=False, # Remove símbolos de depuração
    upx=True, # Usa UPX para compressão
    upx_exclude=[], # Exclusões de compressão UPX
    runtime_tmpdir=None, # Diretório temporário customizado
    console=True, # Define se abre o console (True = sim)
    disable_windowed_traceback=False, # Desativa tracebacks
    argv_emulation=False, # Emulação de args (macOS)
    target_arch=None, # Arquitetura de destino
    codesign_identity=None, # Assinatura (macOS)
    entitlements_file=None, # Entitlements (macOS)
)
