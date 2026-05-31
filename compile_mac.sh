#!/bin/bash

# Script para compilar el PDF en macOS
# Uso: ./compile_mac.sh

echo "🔨 Compilando LaTeX..."
pdflatex main.tex

echo "📚 Ejecutando Bibtex para referencias..."
bibtex main

echo "🔨 Compilando nuevamente..."
pdflatex main.tex
pdflatex main.tex

echo "✅ ¡Compilación completada!"
echo "📂 Abriendo PDF..."
open main.pdf
