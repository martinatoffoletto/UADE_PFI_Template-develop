# -*- coding: utf-8 -*-
"""Recalcula los resultados de la encuesta desde el CSV exportado de MS Forms."""
import csv, io, sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

PATH = "Uso de servicios de logística para envío y recepción de encomiendas en el área del AMBA(1-145).csv"

with open(PATH, encoding="utf-8-sig", newline="") as f:
    text = f.read()

# La primera línea es "Tabla 1"; el resto es CSV con ';'
text = text.split("\n", 1)[1]
rows = list(csv.reader(io.StringIO(text), delimiter=";"))
header = [h.strip().replace("\n", " ") for h in rows[0]]
data = [dict(zip(header, r)) for r in rows[1:] if any(c.strip() for c in r)]
print(f"TOTAL FILAS: {len(data)}")

# Mostrar todas las columnas que son preguntas (sin Puntos/Comentarios/meta)
qcols = [h for h in header if h and not h.startswith(("Puntos", "Comentarios"))
         and h not in ("ID", "Hora de inicio", "Hora de finalización", "Correo electrónico",
                       "Nombre", "Total de puntos", "Comentarios del cuestionario",
                       "Hora de la última modificación")]
print("\n=== PREGUNTAS ===")
for q in qcols:
    print("-", q[:120])

def tally(q, multi=False):
    c = Counter()
    answered = 0
    for d in data:
        v = (d.get(q) or "").strip()
        if not v:
            continue
        answered += 1
        if multi:
            for part in v.split(";"):
                part = part.strip()
                if part:
                    c[part] += 1
        else:
            c[v] += 1
    print(f"\n### {q[:110]}")
    print(f"(respondieron: {answered} de {len(data)})")
    for k, n in c.most_common():
        print(f"  {n:4d}  {n/answered*100:5.1f}% (de respondentes) | {n/len(data)*100:5.1f}% (de {len(data)})  {k[:90]}")

for q in qcols:
    # detectar si es multiple: valores con ';'
    vals = [(d.get(q) or "") for d in data]
    multi = sum(1 for v in vals if ";" in v.strip().rstrip(";")) > 3
    tally(q, multi=multi)
