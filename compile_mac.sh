#!/bin/bash

# Script para compilar el PDF en macOS
# Uso: ./compile_mac.sh

set -e

echo "Compilando LaTeX (pasada 1)..."
pdflatex -interaction=nonstopmode main.tex

echo "Procesando bibliografia con Biber..."
biber main

echo "Compilando LaTeX (pasada 2)..."
pdflatex -interaction=nonstopmode main.tex

echo "Compilando LaTeX (pasada 3 - índice y referencias cruzadas)..."
pdflatex -interaction=nonstopmode main.tex

echo "Compilacion completada. Abriendo PDF..."
open main.pdf
