@echo off
REM Script para compilar el PDF en Windows
REM Uso: compile_windows.bat

SET MIKTEX=C:\Users\matof\AppData\Local\Programs\MiKTeX\miktex\bin\x64

echo Compilando LaTeX...
"%MIKTEX%\pdflatex.exe" -interaction=nonstopmode main.tex

echo Ejecutando Biber para referencias...
"%MIKTEX%\biber.exe" main

echo Compilando nuevamente...
"%MIKTEX%\pdflatex.exe" -interaction=nonstopmode main.tex
"%MIKTEX%\pdflatex.exe" -interaction=nonstopmode main.tex

echo Compilacion completada!
echo Abriendo PDF...
start main.pdf
pause
