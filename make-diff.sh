#!/bin/bash
# make-diff.sh — genera diff-vs-main.pdf con las diferencias contra otra rama.
#
#   ./make-diff.sh          # compara contra main (por defecto)
#   ./make-diff.sh 25%-final
#
# Añadido = azul subrayado · Borrado = rojo tachado.
#
# Por qué no alcanza con `latexdiff main.tex main.tex`: el documento usa \input
# por capítulo (hay que aplanar con latexpand) y envuelve los bloques nuevos en
# {\color{nuevo}...}. Ese \color pisa el color del markup de latexdiff dentro
# del grupo y deja el texto añadido sin resaltar, así que hay que neutralizarlo
# en las copias temporales antes de comparar. El proyecto no se toca.

set -e

BASE="${1:-main}"
ROOT="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

echo "==> Comparando el árbol de trabajo contra '$BASE'"

# 1. La versión base, en un directorio aparte
mkdir -p "$WORK/base"
git -C "$ROOT" archive "$BASE" | tar -x -C "$WORK/base"

# 2. Aplanar los \input de cada versión (cada uno desde su propio directorio)
(cd "$WORK/base" && latexpand --keep-comments main.tex) > "$WORK/old.tex" 2>/dev/null
(cd "$ROOT"      && latexpand --keep-comments main.tex) > "$WORK/new.tex" 2>/dev/null

# 3. Neutralizar el resaltado \nuevo para que no pise el markup de latexdiff
for f in old new; do
    perl -pe 's/\\nuevo\{/\{/g; s/\\color\{nuevo\}//g' "$WORK/$f.tex" \
        | perl -pe 's/\\newcommand\{\\nuevo\}\[1\]\{\{#1\}\}/\\newcommand{\\nuevo}[1]{#1}/' \
        > "$WORK/${f}_flat.tex"
done

# 4. Diferenciar y compilar (TEXINPUTS apunta al proyecto por figuras y estilos)
latexdiff "$WORK/old_flat.tex" "$WORK/new_flat.tex" > "$WORK/diff.tex" 2>/dev/null
echo "==> $(grep -c 'DIFadd\|DIFdel' "$WORK/diff.tex") bloques con cambios; compilando"

(cd "$WORK" && TEXINPUTS="$ROOT//:" BIBINPUTS="$ROOT//:" \
    latexmk -pdf -interaction=nonstopmode -f diff.tex >/dev/null 2>&1) || true

if [ ! -f "$WORK/diff.pdf" ]; then
    echo "ERROR: no se generó el PDF. Log en $WORK/diff.log" >&2
    cp "$WORK/diff.log" "$ROOT/diff-error.log" 2>/dev/null || true
    exit 1
fi

cp "$WORK/diff.pdf" "$ROOT/diff-vs-main.pdf"
echo "==> Listo: diff-vs-main.pdf ($(pdfinfo "$ROOT/diff-vs-main.pdf" 2>/dev/null | awk '/^Pages/{print $2}') páginas)"
