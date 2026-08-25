---
name: rae-informes
description: Normas RAE y buenas prácticas de redacción académica en español para informes técnicos y tesis. Usar al redactar o revisar texto en .tex de este proyecto (mayúsculas, tildes, extranjerismos, numerales, puntuación, conectores, estilo impersonal, anglicismos).
---

# Redacción académica en español (norma RAE)

Checklist para redactar o revisar prosa académica en este informe (LaTeX, `chapters/*.tex`).
No aplica a nombres propios de código, identificadores, ni a texto ya entregado que
según `CLAUDE.md` **no se toca** salvo en los puntos que la cátedra pidió corregir.

## 1. Extranjerismos y tecnicismos en inglés

- Van en **cursiva** (`\textit{}` o `\emph{}`) si no tienen adaptación al español:
  *matching*, *tracking*, *scoring*, *dataset*, *machine learning*, *feed*,
  *smartphone*, *deep learning*.
- Si existe equivalente asentado en español, preferirlo: *email* → correo
  electrónico; *online* → en línea; *feedback* → retroalimentación (salvo que el
  glosario técnico del proyecto ya fije el término en inglés).
- Siglas de producto o tecnología (API, GPS, IA, CO₂, PWA) no llevan cursiva:
  son siglas, no extranjerismos.
- En este repo hay una pasada pendiente de ~15 casos de *matching/tracking/
  scoring/dataset* en redonda dentro del texto ya entregado del 25%: **no
  tocarlos ahora**, se resuelven recién en la entrega final (ver `CLAUDE.md`).

## 2. Mayúsculas

- Español usa muchas menos mayúsculas que inglés. NO llevan mayúscula inicial:
  meses, días, estaciones, gentilicios, disciplinas (`ingeniería informática`,
  no `Ingeniería Informática`, salvo en nombres propios de carrera/institución
  citados textualmente).
- Cargos y roles en minúscula salvo al inicio de oración: *el transportista*,
  *el remitente*, *el administrador* (no *Transportista*, *Remitente*).
- Títulos de figura/tabla: solo la primera palabra en mayúscula
  («Figura 4. Diagrama de secuencia del envío», no «Diagrama De Secuencia»).

## 3. Tildes

- Nunca omitir tildes por estar en mayúscula (CÓDIGO, no CODIGO) ni en siglas
  que se pronuncian como palabra si corresponde.
- Adverbios y pronombres: *solo* sin tilde (ya no se acentúa como adverbio,
  norma RAE 2010); *este/esta/aquel* sin tilde salvo ambigüedad real.
- Palabras compuestas con guion mantienen la tilde de cada componente:
  *técnico-operativo*.

## 4. Numerales, unidades y símbolos

- Del cero al nueve en letras dentro de prosa corrida, salvo con unidad,
  porcentaje o cuando el informe ya fija el uso numérico (este proyecto cita
  cifras de encuesta siempre en dígitos: `69,8 %`, `145 respuestas` — mantener
  esa convención, no mezclar con letras).
- Separador decimal: coma (`0,71`), no punto. Separador de miles: punto o
  espacio fino, nunca coma (`1.500` u `1 500`, no `1,500`).
- Símbolo de porcentaje separado por espacio fino o normal: `69,8 %` (no
  `69.8%`).
- Rango de páginas/años con guion medio sin espacios: `2019-2020`.

## 5. Puntuación

- Comillas: preferir angulares «así» para citas textuales cortas; comillas
  inglesas “así” para cita dentro de cita.
- Raya (—) para incisos largos, no guion corto (-).
- Sin coma entre sujeto y verbo, nunca (`El sistema calcula` no `El sistema,
  calcula`).
- Punto y coma para unir oraciones relacionadas sin conjunción; no abusar del
  gerundio de posterioridad («...calculando el CO₂» implicando una acción
  posterior no simultánea es incorrecto — usar «y luego calcula»).

## 6. Registro académico impersonal

- Preferir la voz pasiva refleja o impersonal con *se* sobre la primera
  persona: «se relevaron 145 respuestas», no «relevamos 145 respuestas» —
  salvo en secciones metodológicas donde el informe ya declara autoría en
  primera persona plural (verificar el uso ya fijado en el capítulo antes de
  cambiarlo).
- Evitar el «nosotros» mayestático y las muletillas coloquiales.
- Tercera persona para referirse al sistema: «DePaso calcula», «el algoritmo
  determina» — no «nuestro sistema calcula».

## 7. Anglicismos sintácticos a evitar

- No calcar el orden inglés adjetivo-sustantivo cuando el español prefiere lo
  inverso: «algoritmo de scoring multivariable» (correcto) vs. forzar
  «multivariable scoring algoritmo».
- Evitar el gerundio con función de adjetivo («un problema resultando en...»);
  usar «que resulta en» o «que produce».
- Evitar voz pasiva calcada del inglés cuando la refleja es más natural: «fue
  calculado por el sistema» → «el sistema lo calculó» / «se calculó».

## 8. Coherencia de citas y bibliografía

- Este proyecto usa norma **ISO 690-2010** (estilo iso-numeric) con
  `\parencite{}` — no mezclar con formato APA/Harvard en el cuerpo del texto.
- Verificar que cada cita en el texto tenga entrada en `biblio.bib` y
  viceversa antes de dar una sección por cerrada.

## Cómo aplicar este skill

Al revisar un capítulo:
1. Releer solo el texto **nuevo** (marcado `\nuevo{}` o agregado en la sesión
   actual) — el texto ya entregado no se corrige salvo pedido explícito de la
   cátedra (ver `CLAUDE.md`, «Regla: el texto ya entregado NO se toca»).
2. Pasar el checklist de arriba en orden: extranjerismos → mayúsculas →
   tildes → numerales → puntuación → registro → anglicismos → citas.
3. Señalar cada corrección con el motivo (regla RAE puntual), no reescribir
   silenciosamente párrafos enteros.
