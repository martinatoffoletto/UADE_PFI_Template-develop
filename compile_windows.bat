@echo off
REM Script para compilar el PDF en Windows
REM Uso: compile_windows.bat

echo 🔨 Compilando LaTeX...
pdflatex main.tex

echo 📚 Ejecutando Bibtex para referencias...
bibtex main

echo 🔨 Compilando nuevamente...
pdflatex main.tex
pdflatex main.tex

echo ✅ ¡Compilación completada!
echo 📂 Abriendo PDF...
start main.pdf
pause
