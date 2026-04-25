@echo off
:: ==============================================================================
:: SCRIPT DE ATUALIZAÇAO DO EXECUTAVEL (Update-Executavel.bat)
:: Descricao: Este script apaga as compilacoes antigas (pastas 'build' e 'dist') 
:: e executa o PyInstaller novamente de forma limpa para gerar um novo 
:: aplicativo (.exe) atualizado com o codigo mais recente.
:: ==============================================================================
echo ========================================================
echo   Limpando compilacoes e executaveis anteriores...
echo ========================================================
if exist "build" rmdir /s /q "build"
if exist "dist\Oferta-Direta" rmdir /s /q "dist\Oferta-Direta"

echo.
echo ========================================================
echo   Iniciando o PyInstaller para gerar um novo executavel...
echo ========================================================
pyinstaller Oferta-Direta.spec --clean --noconfirm

echo.
echo ========================================================
echo   Processo finalizado! 
echo   Verifique a pasta "dist\Oferta-Direta" para o resultado.
echo ========================================================
pause
