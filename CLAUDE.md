DePaso — Descripción del proyecto
Qué es
DePaso es una plataforma digital de logística urbana colaborativa para el AMBA,
orientada a PyMEs, comercios y clientes particulares. Gestiona el ciclo completo
del envío: solicitud, clasificación de la carga, asignación del transportista,
seguimiento e impacto ambiental.
A diferencia de Rappi Favor, PedidosYa Envíos y DiDi Entrega —que operan bajo
un modelo exclusivo de transporte dedicado— DePaso introduce un modelo híbrido
que combina transporte dedicado (tipo flete) con transporte colaborativo basado
en trayectorias habituales de los transportistas, aprovechando la capacidad
ociosa de desplazamientos ya existentes mediante matching con el mínimo desvío.

El problema que resuelve

Costos logísticos elevados para PyMEs y comercios sin flota propia.
Vehículos circulando con espacio disponible sin aprovechamiento.
Baja eficiencia en la última milla en entornos urbanos densos.
Alta emisión de CO₂ por viajes dedicados innecesarios.
Falta de ingresos para personas que realizan trayectos cotidianos.


Roles de usuario
Remitente — PyME, comercio o particular que necesita enviar una encomienda.
Publica el envío, recibe una cotización y elige entre las modalidades disponibles.
Transportista — persona que registra su ruta habitual y recibe pedidos
compatibles con su recorrido sin desvíos significativos. No es repartidor de
tiempo completo: aprovecha un viaje que ya iba a hacer. Puede participar con
cualquier movilidad (auto, moto, bicicleta, a pie, utilitario o camión).
Un mismo usuario puede operar en ambos roles.

Modalidades de envío
Dedicada — se asigna un transportista completo al envío según el tipo de
carga. Fletes y mudanzas van a quienes disponen de camioneta o camión.
Colaborativa — el transportista registra su ruta habitual y recibe pedidos
compatibles sin desvíos significativos. Bicicleta y a pie habilitados solo para
paquetes pequeños y documentos en trayectos cortos.
Tipos de paquete contemplados: pequeños y documentos, medianos,
grandes/voluminosos, mudanzas/fletes.

Funcionalidades principales

Registro multimodal — usuarios y transportistas con distintos tipos de
vehículo (peatón, bicicleta, auto, utilitario, camión).
Carga de solicitudes con imágenes — el remitente fotografía el paquete
para clasificación automática.
Clasificador de carga por visión computacional — modelo de IA propio
entrenado por el equipo con un dataset objetivo de ~1.500 imágenes; la v1 se entrenó con 1.079 al 17-ago-2026 (Google Open Images +
fotos propias de objetos argentinos). Admite objeto de referencia opcional e
ingreso manual alternativo. Evaluado con accuracy, matriz de confusión y
análisis de sesgos por iluminación, ángulo y fondo.
Asignación inteligente de envíos — algoritmo de scoring multivariable
determinístico que combina compatibilidad geoespacial, desvío, carga,
reputación y ventana horaria.
Tracking en tiempo real — seguimiento del estado del envío y gestión
de capacidad disponible del transportista.
Cálculo de CO₂ ahorrado — compara el escenario real contra el viaje
dedicado basándose en factores IPCC.
Panel de monitoreo operativo.
Sistema de calificaciones — ambos roles se califican mutuamente.


Stack tecnológico
CapaTecnologíaBackendPython + FastAPIFrontend / App móvilReact Native + ExpoPanel webReact + TypeScript (Vite)Base de datosPostgreSQL (cloud) — PostGIS NO se usa: los cálculos geográficos se resuelven en Python; queda como optimización futuraIA / MLMobileNetV2 (TensorFlow/Keras), transfer learningDatos geoespacialesOpenStreetMap / OSRMDiseñoFigmaControl de versionesGit / GitHub

Alcance del prototipo (PFI)

Cobertura geográfica: AMBA (~15M de habitantes)
Alcance potencial: +100.000 usuarios
Plataforma: PWA / app móvil
Entrega objetivo: diciembre 2026
Presupuesto total estimado: 85 USD (GPU cloud + DB + hosting backend)


Equipo y datos académicos
AlumnaToffoletto, Martina Ornella — LU 1139965AlumnaBasaez, Candela Pilar — LU 1134260CarreraIngeniería en Informática — UADETutorDos Santos, Maximiliano LuisTipo de proyectoDesarrollo

# DePaso — Proyecto Final UADE

Plataforma digital de logística urbana colaborativa para el AMBA que conecta
remitentes (PyMEs, comercios, particulares) con transportistas que aprovechan
la capacidad ociosa de sus trayectos habituales.

- Alumnas: Toffoletto, Martina Ornella (LU 1139965) · Basaez, Candela Pilar (LU 1134260)
- Carrera: Ingeniería en Informática — UADE FICE
- Tutor: Dos Santos, Maximiliano Luis
- Tipo: Proyecto de Desarrollo
- Entrega: diciembre 2026
- GitHub: https://github.com/martinatoffoletto/DePaso

---

## Stack

| Capa | Tecnología |
|---|---|
| Backend | Python 3.11+ · FastAPI (async) · SQLAlchemy |
| App móvil | React Native + Expo · TypeScript |
| Panel web | React 19 + TypeScript (Vite) |
| Base de datos | PostgreSQL (cloud). **PostGIS NO se usa** — la geo se resuelve en Python (haversine × 1,3) y con OSRM; queda como optimización futura |
| IA / ML | MobileNetV2 (TensorFlow/Keras), aprendizaje por transferencia |
| Geo | OpenStreetMap / OSRM |
| Diseño | Figma |
| Docs | LaTeX / MikTeX — norma de citas ISO 690-2010 |

---

## Convenciones del repo

- Un archivo `.tex` por capítulo en `chapters/`
- Figuras en `figures/`, bibliografía en `biblio.bib` (BibTeX, backend biber)
- Citas con `\parencite{}`, norma ISO 690-2010 (estilo iso-numeric)
- **Stack tecnológico:** en el documento del 25% NO se mencionaba (decisión de
  las autoras: no condicionarse antes de avanzar el desarrollo). **A partir de la
  entrega del 50% el stack SÍ se introduce**, en el Cap. 5 «Metodología de
  desarrollo» (§Tecnologías), como lo exige la rúbrica del 50% (ítem Tecnologías).
- **Estructura del documento (entrega 50%, branch `50%-final`):** Cap. 1
  Introducción · Cap. 2 Antecedentes (marco teórico + estado del arte + análisis
  competitivo FODA/Porter) · Cap. 3 Descripción (contexto + investigación de
  usuarios) · Cap. 4 Análisis de requerimientos (RF/RNF + casos de uso) · Cap. 5
  Metodología de desarrollo (metodología + arquitectura C4 + tecnologías + modelo
  de datos + validación) · Cap. 6 Conclusión. Diagramas hechos en TikZ nativo
  (C4, secuencia, despliegue, DER, casos de uso). Materia prima del código en el
  repo hermano `../DePaso`. **Los diagramas se verifican contra el código fuente
  (`depaso_rest/src/app/modules/*/models.py` y `router.py`), NO contra los `.md`
  del repo** — los `.md` describen la intención, el código es la verdad.
- **Auditoría de diagramas vs. código (ago-2026).** Corregidos:
  - DER: Calificación era 1:N → es 1:0..1 (`UniqueConstraint uq_rating_shipment`);
    Clasificación era 0..1 → es 0..N; Envío–Transportista es 0..1 del lado
    transportista (`carrier_id` nullable); Organización–Transportista es N:M vía
    `organization_carriers`, no 1:N. Agregadas las entidades asociativas
    (`organization_members`, `organization_carriers`) y los verbos de relación.
  - Casos de uso: se eliminó «Sistema» como actor (un actor es externo al
    sistema). CU-02 lo inicia el Administrador —el endpoint de matching es
    admin-only, «inspección»— y se incluye en CU-05 vía «include»; CU-03 se
    incluye en CU-01.
  - Secuencia: el CO₂ definitivo se calcula y persiste **al aceptar**
    (`accept_shipment`), no al entregar; la entrega solo libera el pago. Crear y
    pagar son dos operaciones distintas. El cliente interactúa siempre vía la app.
  - Despliegue: la flecha HTTP de la app móvil atravesaba el nodo PostgreSQL;
    se reubicó la app móvil a la izquierda.
  - Trampa de TikZ: un color suelto dentro de un `/.style` (p. ej. `black!65`)
    pisa el `fill=white` y pinta el nodo entero de gris, dejando el texto
    ilegible. Usar `text=black!70`.
- **Regla: el texto ya entregado NO se toca.** El documento es acumulativo: lo del
  25% se mantiene textual y lo nuevo se agrega marcado con `\nuevo{}`. La única
  excepción son los puntos que la cátedra pidió corregir (la lista de correcciones
  del 25%), que sí se reescriben. Caso concreto: §2.1.6 dice «se estima un volumen
  total del orden de **1.500 imágenes**»; **se deja tal cual** y las autoras
  completarán el dataset hasta esa cifra con más descargas de Open Images, en vez
  de bajar el número en el informe. No «corregirlo» a 1.079.
  - Cap. 5 §Validación sí cita **1.079**, que es el conjunto real con el que se
    entrenó `cargo_classifier_v1`. Al reentrenar con el dataset completo hay que
    actualizar ese número (y solo ese).
- **Alineación informe ↔ repo `../DePaso` (17-ago-2026).** Se auditaron todos los
  `.md` de ambos repos contra el código. Corregido: actores unificados en **cuatro** (Cap. 4 y Cap. 5, con la
  organización desdoblada en fletera/comercio solo dentro del C4); **PostGIS
  fuera del stack declarado** (no se usa: la geo se resuelve en Python con
  haversine×1,3 y OSRM); `README.md` de DePaso reescrito (decía que `depaso_web`
  era la app móvil y no mencionaba `depaso_app`); `ARQUITECTURA.md` (un falso
  «62 % de transportistas sin desviarse» → el real es **91,8 %**; tests 30→177;
  augmentation ±20°/±25 %/0,3); `PLAN_MAESTRO.md` (IA ya no está «al 45 % falta
  entrenar»: v1 entrenado; no existen migraciones 002/003, se usa `create_all()`);
  `ORGANIZACION_CODIGO.md` (la app se organiza por rol: `src/sender|carrier|shared`,
  no por `features/services/utils`). `docs/proy.txt` eliminado.
- **Pendiente conocido:** los códigos `RF-*` citados en los comentarios del código
  NO coinciden con la numeración del informe (el código usa `RF-CAR-07` para la
  penalización por abandono, que en el informe es `RF-CAR-08`, y cita un
  `RF-MAT-05` inexistente). La numeración válida es la del Cap. 4.
- **Verificación de cifras:** `docs/encuesta/verify_numbers.py` contrasta cada
  número de la encuesta citado en el documento contra el CSV. Correrlo tras tocar
  cifras: al 17-ago-2026 pasa completo.
- **Auditoría externa con IA (17-ago-2026).** Se pasó el informe por dos modelos
  con `docs/prompt-auditoria.md`. Correcciones aplicadas: CU-06 ya no dice que el
  CO₂ se persiste al entregar (se calcula al aceptar, coincide con el código y con
  la Fig. de secuencia); RF-MAT-02 explicita el **15 %** de desvío; RF-MAT-03 aclara
  que el listado se ordena por el puntaje de RF-MAT-01 (ese es el uso operativo del
  scoring: el ranking de transportistas es admin-only); RF-SHP-04 separa monto
  retenido / comisión / saldo liberado; la tabla de entidades aclara que el destino
  del Trayecto es nulo en la ventana dedicada; el DER pasa a **0..1** del lado Envío
  en la relación con Clasificación (la clasificación existe antes que el envío); el
  modelo `.keras` deja de ser `c4ext` y se dibuja como artefacto interno (`c4store`);
  el FODA deja de listar datos propios como oportunidades **externas**; y se dejó de
  afirmar que la brecha WTP/WTA «valida la viabilidad económica» (resumen, abstract
  y conclusión) — ahora es «compatibilidad preliminar», pendiente del análisis de
  costos.
  - **Rechazado a propósito:** el ±8,5 % de margen de error del Cap. 3 es texto del
    25% ya entregado y el propio párrafo aclara que el objetivo es exploratorio y
    no estimar la población; no se toca.
  - **Corrección revertida:** la auditoría sugirió detallar en RF-SHP-04 el reparto
    entre comisión y saldo del transportista. **No se hace**: el pago es simulado
    en el MVP (no se integra pasarela) y la comisión se define recién con el
    análisis económico. RF-SHP-04 quedó como retención en garantía + liberación a
    la entrega, sin nombrar la comisión, y el FODA dice «margen disponible para la
    plataforma». La única mención que sobrevive es el hallazgo 5 del Cap. 3
    («no tolera comisiones altas»), que es texto del 25% ya entregado.
- **Rúbrica del 50% (ago-2026).** Los ejemplos entre paréntesis de la rúbrica son
  ilustrativos («etc.»): NO hacen falta matriz BCG (se compara un portafolio y
  DePaso es producto único preoperativo) ni triple P (no se hizo análisis
  económico ni flujo de fondos). Con FODA + Porter + estrategia de diferenciación,
  «Competencias» cumple. Cap. 5 §Tecnologías tiene ahora dos subsecciones:
  «Elección de los lenguajes de programación» (Python por el ecosistema de ML —
  inferencia en el mismo proceso de la API; TypeScript por tipado del contrato de
  la API; alternativas descartadas: Java/C#, Node, nativo por plataforma) y
  «Stack tecnológico por capa». Quedan pendientes solo Mockups y Demo.
- Compilar con `pdflatex` o `latexmk`

---

## Qué es cada sección del documento

### Marco Teórico

Reúne los conceptos, teorías y modelos que sustentan el proyecto. No es un
glosario ni un manual técnico: es una construcción argumentativa donde cada
subtema responde a una pregunta concreta vinculada a los objetivos.

> Responde: *¿con qué conceptos y teorías trabajamos?*

Subtemas implementados en el documento, de lo general a lo específico:

1. **Crowdsourced delivery y logística de última milla** — el CSD delega la
   última milla en personas que integran pedidos en sus propios desplazamientos.
   - Yang, Hyland & Jayakrishnan (2022) — arXiv:2203.14719.

2. **Flotas híbridas y el problema del desvío** — los SPVs reducen el costo
   unitario, pero un desvío excesivo elimina el beneficio ambiental. El desvío
   debe ser variable explícita del matching (filtro duro en DePaso).
   - Yang et al. (2022).

3. **Perfiles de conductores: gig-workers (GW) vs. occasional drivers (OD)** —
   fundamento teórico de la modalidad colaborativa.
   - Luy, Hiermann & Schiffer (2023) — arXiv:2311.17935.

4. **Diseño de mercados de matching y asignación** — el matching como
   optimización combinatoria; subastas y elasticidades requieren datos
   históricos inexistentes en el arranque → justifica el scoring determinístico.
   - Akamatsu & Oyama (2023) — arXiv:2312.01641.
   - Oyama & Akamatsu (2024) — arXiv:2412.20395.

5. **Visión computacional y aprendizaje por transferencia** — clasificar la
   carga en categorías volumétricas desde una foto (transfer learning); la
   estimación 3D exacta desde móviles es inviable.
   - Saleh, Al Hanbali & Baubaid (2024) — arXiv:2402.09961.
   - Naumann et al. (2023) — arXiv:2304.06009.

Referencias conceptuales de respaldo, aún NO incorporadas al documento (posibles
ampliaciones futuras: two-sided markets, sharing economy, confianza P2P,
pricing, UX): Hagiu & Wright (2015); Rochet & Tirole (2003); Botsman & Rogers
(2010); Carbone, Rouquet & Roussat (2017); Arslan et al. (2019); Alnaggar et
al. (2021); Gruber (2020); Le & Ukkusuri et al. (2021); Cooper, Reimann &
Cronin (2014).

---

### Estado del Arte

Sistematización de lo que se investigó, desarrolló y publicó sobre el problema
hasta la fecha. Describe trabajos concretos: qué hicieron, cómo, qué resultados,
qué quedó pendiente.

> Responde: *¿quién hizo qué con este problema y con qué resultado?*

**Brecha que justifica DePaso:** ninguna plataforma argentina combina modelo
híbrido (dedicado + colaborativo), clasificación de carga por IA propia y cálculo
de CO₂ para envíos entre particulares y PyMEs en el AMBA.

Competidores directos analizados: Rappi Favor, PedidosYa Envíos, Uber Flash,
DiDi Entrega, Moova, Treggo, OCA/Andreani, Shipit.

Papers en la matriz de antecedentes (los 7 citados en biblio.bib). En jun-2026
se actualizaron 4 citas a sus versiones formales de journal (regla de la
cátedra: arXiv máx. 2 años sin paper formal posterior); las claves BibTeX no
cambiaron:
- Yang et al. (2024) — Transportation Research Part E, vol. 188, 103633,
  DOI 10.1016/j.tre.2024.103633 (antes arXiv:2203.14719) — flota híbrida
  DVs+SPVs a gran escala.
- Luy et al. (2024) — Production and Operations Management, 33(11), 2177–2200,
  DOI 10.1177/10591478241268602 (antes arXiv:2311.17935) — workforce planning
  GW/OD.
- Akamatsu & Oyama (2024) — Transportation Research Part C, vol. 166, 104738,
  DOI 10.1016/j.trc.2024.104738 (antes arXiv:2312.01641) — matching
  fluido-partícula.
- Oyama & Akamatsu (2024) — arXiv:2412.20395 (sin versión journal; dentro del
  límite de 2 años) — mercado CSD de dos lados con elasticidad y task-bundling.
- Saleh et al. (2026) — Computers & Industrial Engineering, vol. 212, 111693,
  DOI 10.1016/j.cie.2025.111693 (antes arXiv:2402.09961) — deep RL para
  courier scheduling.
- Naumann et al. (2023) — arXiv:2304.06009 — CV en logística (SLR). ÚNICO que
  sigue solo en arXiv sin versión formal (verificado en Crossref/Semantic
  Scholar, jun-2026): si la cátedra lo objeta, justificar que es la única SLR
  del tema.
- OIT (2020) — plataformas de reparto en Argentina (único con foco AMBA).
  URL agregada al bib: ilo.org (.../wcms_759896.pdf).

(Orden de autores verificado contra arXiv: 2312.01641 es Akamatsu→Oyama;
2412.20395 es Oyama→Akamatsu.)

---

### User Research

Proceso sistemático para comprender a los usuarios mediante técnicas empíricas.
Aporta evidencia para tomar decisiones de diseño en lugar de basarlas en supuestos.

Técnicas usadas: encuesta, entrevistas semiestructuradas y user personas.

> **No prometer más instrumentos (ago-2026).** La encuesta (145 respuestas) y
> las 5 entrevistas son lo que hay. El documento habla de ellas **en pasado** y
> no anuncia continuidad: se eliminaron del Cap. 3, la conclusión y el Anexo A
> las frases "permanece abierta", "la muestra continuará ampliándose", "próxima
> ronda de entrevistas" y las user personas "preliminares… serán refinadas".
> Tampoco declarar lo contrario ("cerrado", "definitivo"): en la práctica nunca
> se cierra del todo, así que simplemente no se hace hincapié en ninguna de las
> dos direcciones. El feedback posterior entra por la validación con usuarios
> sobre el prototipo, que ya figura en trabajo futuro.

> **Cambio de decisión (ago-2026).** La entrega del 25% se hizo sin entrevistas
> y esta guía indicaba no reintroducirlas. La devolución de la cátedra las pidió
> explícitamente para la entrega del 50%, así que se incorporaron. **Ciclo
> cerrado (ago-2026):** 5 entrevistas por videollamada, materia prima en
> `docs/entrevistas/entrevistas.txt`.
> - Cap. 3, §3.5 "Entrevistas semiestructuradas": completa y **deliberadamente
>   compacta (~2,5 pp., sin subsecciones), en paralelo a §3.4 Encuesta**. Una
>   primera versión con subsecciones (guion / análisis / conclusiones) ocupaba
>   ~10 pp. y quedaba desbalanceada frente a la encuesta; se comprimió a:
>   párrafo de método + perfiles, párrafo de guion (6 ejes en prosa), tabla
>   `tab:entrevistas` con los 11 hallazgos (Hallazgo | Evidencia | Relación con
>   la encuesta e implicancia) y dos párrafos de síntesis y limitaciones.
>   **No volver a expandirla en subsecciones.**
> - Anexo C (`chapters/appendix/interviews.tex`): las 5 transcripciones
>   (E1–E5) con edición ligera y anonimizadas (E:/P:, sin nombres; comercio de
>   E2 generalizado). Sin campo "Duración" (no se registró).
> - Perfiles cubiertos: E1 remitente particular · E2 remitente PyME · E3
>   transporte de carga (camión) · E4 destinataria particular · E5
>   transportista con recorrido habitual (camioneta).
> - **Requerimientos derivados que aún NO están en el Cap. 4** (el Cap. 3 los
>   declara como planificados para la etapa siguiente): evidencia de custodia
>   (foto en retiro/entrega + confirmación de recepción), declaración
>   obligatoria del contenido, y desglose de peajes/estacionamiento medido en
>   la cotización.
> - Vacíos que orientan la próxima ronda: no se entrevistó a transportistas
>   ocasionales con auto/moto/bici, ni se indagó sobre la clasificación por
>   foto (solo respaldada por la encuesta, 80,2%).

> **Pendientes de material (auditoría ago-2026).** Solo requieren material real
> de las autoras; el andamiaje ya está en el documento:
> - Mockups (Cap. 5 §Diseño de la interfaz): 8 `\marcador` a reemplazar por
>   wireframes/capturas de Figma.
> - Demo (Cap. 5 §Avance de la implementación, sección nueva): 5 `\marcador`
>   para capturas reales (API /docs, corrida de pytest, app móvil ×2, panel web).
>
> Entrevistas: **resueltas** (ver el bloque anterior).
>
> Resueltos en la auditoría: imágenes de arquetipo de las user personas
> (fotos reales en Cap. 3: `figures/persona-juan|maria|carlos.png`, origen en
> `docs/Fotos User Personas/1|2|3.png`, redimensionadas a 400 px y recortadas
> con esquinas redondeadas vía `\clip` de TikZ);
> tabla de tecnologías con nombres concretos (SQLAlchemy, JWT/Argon2,
> OSRM/OSM, MobileNetV2 TF/Keras, React+TS, Docker, pytest) verificados contra
> el código de `../DePaso`; `summary.tex` actualizado de 25%→50% con cifras
> corregidas (69,8% / 75%); cronograma del Anexo A actualizado a ago-2026 con
> barra de entrevistas; métricas verificables en objetivos específicos 4 y 5.

**Encuesta** ✓ completada y CERRADA
- Microsoft Forms, lanzada el 22-may-2026. 145 respuestas completas; 133 (91,7%)
  del AMBA.
- Bifurcaciones por perfil → las bases varían: bloque de uso de servicios
  n = 116; bloque transportista n = 98 (94–98 según pregunta). Todo porcentaje
  citado en el cuerpo debe calcularse sobre la base de quienes respondieron esa
  pregunta.
- En el documento: transcripción de resultados en el Anexo B; en el cuerpo,
  tabla de hallazgos + 7 hallazgos accionables.
- Cifras clave verificadas: predisposición colaborativa 69,8%; usaría
  clasificación por foto 80,2%; interés en transportar 84,5%; motivación
  "ingreso extra sin desvío" 91,8%; preocupación responsabilidad por daños
  73,4%; WTP $3.000–6.000 (68,1%); WTA $2.500–5.000 (51,0%).

**User Personas** — 3, construidas a partir de la encuesta:
Juan García (remitente PyME, Lanús), María Alvarez (transportista colaborativa,
Caballito→Microcentro) y Carlos Gómez (fletero dedicado con camión, Quilmes).
Construidas a partir de la investigación de usuarios ya cerrada; no quedan pendientes.
- Elementos: nombre ficticio, datos demográficos, contexto/rol, objetivos,
  frustraciones, comportamientos, cita representativa.

---

## Clasificador de carga — estado y decisiones abiertas

> **Todo lo de esta sección SIGUE EN ANÁLISIS.** Nada está decidido ni
> comprometido en el informe. Anotado el 17-ago-2026 para no perder el hilo.

**Estado real del modelo.** `cargo_classifier_v1.keras` (20-jul-2026): MobileNetV2
+ GAP + `concat(ref_flag)` + Dense(128) + Dropout(0,3) + Dense(4). Dataset de
1.079 imágenes, split 755/162/162, **66,05 % de accuracy en validación**. El
**conjunto de prueba nunca se evaluó** (sigue congelado): correr
`python evaluate_bias.py --data-dir dataset/ --model-dir models/` en Colab —el
dataset no está en el repo, vive en Drive—. Ojo: el objetivo del Cap. 1 está
declarado **sobre el conjunto de prueba**, así que hasta correrlo no se sabe si
se cumple.

**Objetivo declarado (ya actualizado en el Cap. 1):** accuracy ≥ **70 %** sobre
test + los errores concentrados en **categorías adyacentes**. Se sacó la
justificación anterior («supera la línea base aleatoria del 25 %», que es
defenderse contra el azar) y se reemplazó por dos razones de dominio: la
ambigüedad intrínseca de estimar volumen desde una imagen 2D
\parencite{NaumannEtAl2023} y el carácter *human-in-the-loop* del sistema
(RF-VIS-02 deriva a manual con baja confianza; RF-SHP-03 permite carga manual).

**Debilidad metodológica detectada.** Hoy la etiqueta se deriva del **tipo de
objeto**, no del tamaño: `CATEGORY_TO_OI_CLASSES` mapea `Suitcase→l`,
`Furniture→xl`, etc. Esa asignación la decidió el equipo, no el dato. Consecuencia:
el modelo es un reconocedor de objetos con una tabla de conversión pegada — no
mide nada. Bajo `Furniture` entra tanto una mesita como un ropero.

**Datasets candidatos (EN ANÁLISIS, no adoptados).** Ambos traen medidas reales,
lo que permitiría derivar la categoría del volumen en vez del tipo de objeto:
- **Objectron** (Google, github.com/google-research-datasets/Objectron): 15 k
  videos / 4 M imágenes anotadas con caja 3D (alto × ancho × profundidad reales).
  Categorías: bikes, books, bottles, cameras, cereal boxes, chairs, cups, laptops,
  shoes. **Fotos de celular en entornos reales, 10 países** → mismo dominio que la
  app. Le falta el rango XL (no hay camas, sofás, heladeras).
- **ABO — Amazon Berkeley Objects** (amazon-berkeley-objects.s3.amazonaws.com):
  147.702 productos con **dimensiones y peso** en metadata + 398.212 imágenes, y
  `description` / `product_type` / `material` → material para el multimodal sin
  inventar texto. Cubre XL. Contras: fotos de **catálogo** (fondo blanco, estudio)
  → *domain shift* respecto de la foto real; licencia **CC BY-NC** (uso académico
  OK, hay que declararla).
- Ninguno alcanza solo; la idea sería combinarlos con los dos actuales.
- Si se avanza, el entregable fuerte para la defensa es la **comparación**
  etiquetado-por-tipo-de-objeto vs. etiquetado-por-dimensiones-reales sobre el
  mismo test.

**Objeto de referencia.** El informe dice «objeto de referencia» en genérico
(RF-VIS-03, CU-03), **nunca nombra uno concreto** → se puede cambiar sin tocar el
documento. Decisión de las autoras: botella **de 500 ml**, aclarando el tamaño.
Nota técnica: una tarjeta tipo DNI sería geométricamente superior (plana,
rectangular, tamaño normado ISO/IEC 7810 → permite rectificar perspectiva), pero
la botella se ve mejor en cargas grandes. **Lo crítico es que el objeto sea el
mismo en el dataset de entrenamiento y en producción**: hoy `train_classifier.py`
emite un WARNING porque casi no hay imágenes con `ref_flag=1`, así que la entrada
de referencia probablemente **no está aportando nada** todavía.

**Multimodal (imagen + descripción) — a futuro.** La app ya guarda `description`
en `shipments` y `labels.csv` ya tiene la columna `objeto`; el modelo ya es
multi-entrada, así que sumar un brazo de texto es trivial en código. Dos riesgos:
(1) **fuga de etiqueta** — si se rellena `objeto` con la clase de Open Images de
la que se bajó la imagen, el texto *es* la etiqueta y el accuracy sería ficticio;
(2) el texto de entrenamiento tiene que parecerse al que escribe un usuario real,
no a una etiqueta limpia. Alternativa de bajo riesgo: fusión tardía (el texto
desempata solo cuando la confianza de la imagen es baja). Fundamento: el texto
resuelve la ambigüedad de escala que la foto no puede resolver («heladera» da el
volumen; la imagen sola, no).

---

## Casos de uso ↔ código: pendientes de implementar

Auditoría del 17-ago-2026 de los CU del Cap. 4 contra el código. Se corrigió en el
informe el **orden de creación y pago** (CU-01: el envío se crea primero, `POST
/shipments`, y recién después se paga, `POST /shipments/{id}/pay`; el texto decía
lo inverso). Los tres puntos siguientes **quedan declarados en el informe y hay que
implementarlos** — decisión de las autoras, porque son coherentes con el diseño:

1. **Calificación bidireccional** (CU-06 paso 4, RF-SHP-08, y `CLAUDE.md` del
   proyecto: «ambos roles se califican mutuamente»). Hoy solo el cliente califica
   al transportista: `rate_shipment` exige `shipment.client_id == client_id` y el
   modelo `Rating` tiene `UniqueConstraint("shipment_id")`, que **impide una
   segunda calificación por envío**. Para implementarlo: quitar/ampliar ese
   constraint (p. ej. único por `(shipment_id, rater_role)`), agregar el endpoint
   para que el transportista califique, y **actualizar `User.rating`**, que hoy
   existe en la tabla, arranca en 5.0 y no se escribe nunca. Respaldo en las
   entrevistas: E5 teme la acusación falsa del destinatario; E1 señaló que las
   plataformas evalúan el producto y no el transporte.

2. **Persistir el CO₂ en la entrega** (CU-06 paso 3). Hoy se calcula y guarda en
   `accept_shipment` —ahí se conocen trayecto y vehículo— y `_on_delivered` solo
   libera el pago. **Ojo:** el Cap. 5 tiene un párrafo y el diagrama de secuencia
   que explican *deliberadamente* que el valor definitivo se fija al aceptar. Si se
   pasa a persistir también en la entrega, hay que decidir qué se guarda —lo
   razonable es **recalcular con el recorrido real de las trazas GPS**, que es más
   preciso que el trayecto planificado— y **actualizar ese párrafo y la
   Figura del diagrama de secuencia**, que hoy dicen lo contrario.

3. **Evaluación proactiva al publicar un trayecto** (CU-04 paso 3 y CU-02 alt. 1a:
   «el sistema comienza a evaluar los envíos pendientes compatibles»). Hoy
   `publish_route` solo publica; no hay scheduler ni background job y el matching
   corre **cuando el transportista abre su feed** (pull, no push). Matiz
   importante: el comportamiento observable ya existe —`useShipmentNotifications`
   hace `setInterval` sobre `getFeed()` y avisa de ofertas nuevas—, así que para el
   usuario el sistema «le avisa». Lo que falta para que el CU sea literal es que el
   disparo venga del servidor, y eso exige infraestructura de push que hoy no hay.

**Verificado y correcto** (no tocar): todas las validaciones de CU-05
(`is_verified`, `is_active`, compatibilidad vehículo-carga, XL nunca colaborativo,
capacidad, reserva total del vehículo en dedicado por RF-CAP-02), CU-03 completo
(incluido el registro de RF-VIS-04 y el fallback a manual), filtros duros y scoring
de CU-02, tracking de CU-06, y las dos citas de RNF-AVL-01 (está redactado en
genérico, cubre tanto el ruteo caído como el modelo no disponible).

**Detectado, sin resolver:** CU-01 alt. 5a dice que un envío impago «no se ofrece a
los transportistas», pero el matching **no filtra por `payment_status`** — un envío
sin pagar igual aparece en el feed.

---

## Mejoras para la próxima etapa (post-50%)

Lista consolidada (17-ago-2026), ordenada por prioridad. Es un MVP: nada de esto
bloquea la entrega del 50%.

| # | Mejora | Costo | Prio |
|---|---|---|---|
| 1 | **El feed muestra envíos impagos**: el matching no filtra por `payment_status`, contradice CU-01 alt. 5a | 1 línea en `matching/service.py` | Alta |
| 2 | **Códigos `RF-*` del código desalineados** con el Cap. 4: el código usa `RF-CAR-07` para la penalización (informe: `RF-CAR-08`) y cita un `RF-MAT-05` inexistente. La numeración válida es la del Cap. 4 | ~30 min de grep | Alta |
| 3 | **Correr el test set** (`evaluate_bias.py` en Colab) antes de comprometer cifras: el objetivo del Cap. 1 (≥70 %) está declarado sobre prueba y nunca se evaluó | 1 corrida | Alta |
| 4 | **Fotos propias con la botella de 500 ml** para que `ref_flag` aprenda algo (hoy el WARNING del train indica que no aporta) | sesión de fotos | Media |
| 5 | **Calificación bidireccional** (decidido): quitar `uq_rating_shipment` → único por (shipment, rol), endpoint carrier→cliente, escribir `User.rating` | ~1 día | Media |
| 6 | **`Classification` no guarda la ruta de la imagen**: agregar la columna convierte esa tabla en dataset de reentrenamiento listo (hoy habría que cruzar por `shipment_id`, que suele ser NULL) | 2 líneas | Media |
| 7 | **CO₂ recalculado en la entrega con trazas GPS reales** (decidido) + actualizar párrafo y figura de secuencia del Cap. 5 que hoy dicen «al aceptar» | ~1 día | Media |
| 8 | **Push real** (Expo push) para que CU-04 «el sistema comienza a evaluar» sea literal; hoy es polling del cliente | ~1 día | Media |
| 9 | **Escalada de precio si nadie acepta** (ver §Pricing): destraba el envío huérfano en `pending` y genera los datos de elasticidad | ~2 días | Media |
| 10 | Tracking por polling 15 s → SSE/WebSocket desde FastAPI | ~1 día | Baja |
| 11 | `create_all()` sin migraciones: OK para MVP; introducir Alembic recién si hay datos en producción | — | Baja |
| 12 | **Cursivas RAE en extranjerismos del texto del 25%** (~15 casos de *matching/tracking/scoring/dataset* en redonda): pasada global recién en la **entrega final**, cuando el diff ya no importe | 10 min | Baja |

**Eventos / Kafka — evaluado y descartado (17-ago-2026).** Kafka no se justifica:
(a) contradice la justificación escrita del monolito modular (Cap. 5); (b) rompe
RNF-INF-01 (85 USD); (c) hay un solo consumidor. `ShipmentEvent` ya es un log de
eventos de dominio (auditoría con actor, marca temporal y ubicación) sin broker.
Evolución honesta y en orden de costo: Expo push (#8) → SSE (#10) → Redis Streams
si hiciera falta una cola → Kafka solo si algún día se extraen microservicios.

## Mockups (Cap. 5 §Diseño de la interfaz) — mapeo marcador ↔ pantalla real

Los 8 `\marcador` tienen pantalla ya construida; la recomendación es **capturas
reales de la app, no Figma** (la rúbrica acepta «wireframes **o pantallas** claras
y significativas del frontend», y las mismas capturas sirven para la fila Demo):

| Marcador | Pantalla real |
|---|---|
| Solicitud: origen, destino y fotografía | `send-flow/AddressScreen` + `PackageScreen` |
| Cotización: tres tarifas y CO₂ | `send-flow/RouteOfferScreen` (+ `ProductOptionCard`) |
| Seguimiento del envío en curso | `ShipmentsScreen` + `LiveShipmentCard`/`ShipmentDetailModal` |
| Publicación del trayecto habitual | `carrier/PublishTripScreen` |
| Listado de pedidos con desvío y ganancia | feed en `RiderHomeScreen` + `IncomingOfferModal` |
| Envío en curso: estados y entrega | `CarrierShipmentsScreen` / `ActiveJobPanel` |
| Panel PyME: envíos y finanzas | `depaso_web` `features/dashboard`+`shipments`+`finance` |
| Panel admin: monitoreo y validación | `depaso_web` `features/admin` |

**Estado (17-ago-2026).** Las capturas viven en `docs/mockups/` (16 pantallas; las
que empiezan con `T_`/`t_` son del transportista). **Ya insertadas** —copiadas a
`figures/`, redimensionadas a 620 px de ancho:

| Figura | Archivo en `figures/` | Origen |
|---|---|---|
| Solicitud (foto + categoría IA + descripción) | `mockup-solicitud.png` | `fotopaquete.png` |
| Cotización (Ya/Hoy/De paso + CO₂) | `mockup-cotizacion.png` | `tiposenvios.png` |
| Seguimiento del envío | `mockup-seguimiento.png` | `misenvios.png` |
| Publicación del trayecto | `mockup-trayecto.png` | `t_publicarviaje.png` |

**COMPLETO (17-ago-2026): no queda ningún `\marcador` en el documento.** Se
sumaron `mockup-oferta` (oferta entrante con ganancia y distancia),
`mockup-encurso` (envío en curso con «no puedo llevarlo · penaliza reputación»,
RF-CAR-08 visible), `mockup-impacto` (RF-CO2-01/02 con el contrafactual),
`mockup-pyme` y `mockup-admin` (paneles web, **a ancho completo y una por
figura**: a media página eran ilegibles), y para la fila Demo `demo-api`
(Swagger en `/api/v1/docs`) y `demo-tests` (corrida con 176 passed).

**Descartado a propósito:** la captura de Pagos (`t_mispagos`) **no se usa** —
muestra «− 15 %» en cada cobro y la comisión no se discute hasta el análisis
económico. Tampoco se menciona la comisión con cifra en ningún lado del Cap. 5.

Se usa el comando **`\mockup{ancho}{ruta}`** (definido en `main.tex`): pone borde
fino y alinea al tope para convivir en la misma fila con los `\marcador` que
faltan. Los marcadores móviles se subieron a `9.5cm` de alto para que la fila
quede pareja con las capturas ya puestas.

**Decisión de las autoras:** las direcciones ficticias / de San Francisco que
aparecen en algunas capturas del transportista **no se corrigen** — son pantallas
de diseño, no evidencia del funcionamiento real. No volver a plantearlo.

Sin usar todavía, pero buenos: `T_inicio.png` (comunica la filosofía OD: «listo
cuando vos quieras», «publicar un viaje que voy a hacer igual») e
`impactoambiental.png` (RF-CO2-02, hoy sin figura). Se podría ampliar la figura
del transportista a cuatro pantallas.

---

## Pricing — decisiones abiertas

> **EN ANÁLISIS.** Nada de esto está implementado ni prometido en el informe.
> Anotado el 17-ago-2026.

**Cómo cotiza hoy.** `shipments/pricing.py`: tarifa base por categoría
(s 300 / m 380 / l 520 / xl 900) con descuentos **fijos** —`COLLABORATIVE_DISCOUNT
= 0.43`, `SCHEDULED_DISCOUNT = 0.18`— y comisión `PLATFORM_COMMISSION_RATE = 0.15`.
El propio código marca el 18 % como **`To calibrate`** y el 43 % como
«consistent with survey ranges»: son valores elegidos a ojo, no calibrados.

**Escalada de precio si nadie acepta (idea de las autoras, buena).** No confundir
con *surge pricing*: el surge es **predictivo** (necesita histórico de demanda, por
eso el FODA lo declara como debilidad); la escalada es **reactiva** (solo observa
que pasaron N minutos sin aceptación) y **no necesita datos históricos**, así que
es implementable desde el día uno. Diseño propuesto:
- El remitente ve el rango completo al publicar («desde $X, hasta un máximo de $Y
  si nadie lo toma en 15 min») y **aprueba el techo** → no rompe la transparencia
  del precio (hallazgo 1: 75 % elige por costo, precio antes de confirmar).
- Escalones chicos y temporizados, 2–3 como máximo.
- **El incremento va íntegro al transportista, no a la comisión** (si no, parece
  que la plataforma gana cuando el usuario espera).
- Formularlo como «precio garantizado hasta $Y», no «puede subir».
- Es una subasta ascendente con incrementos temporizados (tiene literatura).
- Beneficio secundario fuerte: **genera los datos de elasticidad que hoy no
  existen** (a qué escalón se aceptó, en qué zona y horario), que son justamente
  los que Oyama & Akamatsu señalan como requisito del pricing dinámico. El
  mecanismo simple arranca al complejo.

**Relevar precios de fletes reales para calibrar.** Es benchmarking de mercado,
**no** user research (no reabre la investigación de usuarios). Cuidado con la
inflación: un precio absoluto relevado envejece en semanas. Usarlo para fijar la
**relación** (cuánto más barato es colaborativo vs. flete tradicional) e indexar
el valor absoluto con el **Índice de Costos Logísticos de CEDOL**, que ya está
citado en la introducción (`CEDOL2025`) — así el pricing queda anclado a una
fuente de la bibliografía y se actualiza solo.

**FODA (ya ajustado en el Cap. 2).** La debilidad «cobertura ante daños» **no se
saca** por declararse intermediaria: el encuadre jurídico delimita la
responsabilidad de la plataforma pero **traslada el riesgo al transportista**, y
el 73,4 % lo señala como su preocupación principal. Sacarla contradiría la
amenaza «barreras de confianza (73,4 %)» que figura en el mismo cuadro. Se
reformuló para que quede explícito. También se separó «tarifa determinística» de
«equipo y presupuesto acotados», que eran dos debilidades de naturaleza distinta
en un mismo bullet.

---

## Fuentes principales

- Hernández-Sampieri & Mendoza (2020). *Metodología de la investigación*. McGraw Hill.
- Kitchenham & Charters (2007). *Guidelines for Systematic Literature Reviews*.
  Keele University.
- Webster & Watson (2002). *Writing a literature review*. MIS Quarterly, 26(2).
- Cooper, Reimann & Cronin (2014). *About Face*. Wiley.
- Pruitt & Adlin (2006). *The Persona Lifecycle*. Morgan Kaufmann.
- Nielsen Norman Group — recursos sobre User Research y Personas.

---

## Ver las diferencias contra otra rama

```bash
./make-diff.sh              # contra main
./make-diff.sh 25%-final    # contra otra rama
```

Genera `diff-vs-main.pdf`: **añadido en azul subrayado, borrado en rojo tachado**.
No modifica el proyecto (trabaja sobre copias en un temporal).

Dos cosas que el script resuelve y que `latexdiff main.tex main.tex` a secas no:
el documento usa `\input` por capítulo (hay que aplanar con `latexpand`), y los
bloques marcados con `{\color{nuevo}...}` pisan el color del markup de latexdiff
dentro del grupo, dejando el texto añadido sin resaltar — por eso el script
neutraliza `\nuevo` en las copias temporales antes de comparar.

**El documento se entrega en negro.** `\definecolor{nuevo}` está en `{0,0,0}`
(main.tex), así que los `\nuevo{...}` no se ven. Para volver a resaltar lo nuevo
mientras se trabaja, ponerlo en `{0,0,205}`; el diff no depende de eso.

Requiere `latexpand` y `latexdiff` (vienen con TeX Live) y `poppler`
(`brew install poppler`) solo si se quieren previsualizar páginas sueltas con
`pdftoppm`. 