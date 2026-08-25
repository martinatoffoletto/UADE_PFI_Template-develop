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
Los roles no se combinan en un mismo perfil: quien opere en ambos sentidos tiene
un perfil de remitente y otro de transportista, y alterna entre ellos (decidido el
21-ago-2026, ver §Revisión del 50%).

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
  - Cap. 5 §Validación **ya no cita ninguna cifra de dataset**: el 21-ago-2026 se
    quitó el párrafo del v1 (1.079 imágenes) porque el modelo se rehace de cero.
    No volver a poner un número hasta tener v3 evaluado.
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

## Clasificador de carga — v3, decidido el 18-ago-2026

> Antes esta sección decía «todo sigue en análisis». **Ya no**: se auditó el
> dataset y las decisiones están tomadas. El plan completo vive en
> `../DePaso/depaso_rest/ml/PLAN_V3.md` y el paso a paso en `TODO_MARTINA.md`
> del mismo directorio.

**Por qué se rehace.** Se inspeccionó una muestra aleatoria de la clase `xl`:
de 16 imágenes, **2 eran realmente una mudanza o un flete**. El resto eran un
puerto con barcos, un hall de conferencias, un gato dentro de una caja, cajas de
zapatos apiladas. La causa está en una línea de
`dataset/download_open_images.py`: pedía `label_types=["classifications"]`, que
anota *«en esta foto aparece un mueble»* y baja la **escena entera**. Ya
corregido a `["detections"]`, que da el bounding box y permite recortar.

Encima de ese ruido había un problema de diseño: la etiqueta se derivaba del
**tipo de objeto** (`Box → m`, `Suitcase → l`), un mapeo decidido por el equipo.
Una caja de zapatos y una caja de heladera son las dos `Box`. Aunque se limpiara
el ruido, la tarea seguía mal planteada.

**Qué cambia en v3.** La etiqueta sale de una **medida**, no de un diccionario:
`alto × ancho × profundidad (cm) → volumen → umbral → s/m/l/xl`. Los umbrales se
derivan de la **capacidad del vehículo** (`shared/cargo.py`, Tabla 1.I del
informe): `s` entra en una mochila, `m` en el baúl de una moto, `l` en el baúl de
un auto, `xl` requiere vehículo de carga. Los litros exactos quedan por calibrar
contra la distribución real.

**Fuente principal: ABO (Amazon Berkeley Objects)** — verificado en Colab:
**43.002 productos con dimensiones completas**, peso, tipo, material, y **13.990
con nombre en español**. Con umbrales de tanteo (8/50/200 L) las cuatro
categorías quedan pobladas: `s 24.950 · m 7.164 · l 3.572 · xl 7.316`. Contra:
son fotos de **catálogo** (fondo blanco) → *domain shift*, así que hay que
mezclar con imágenes de entornos reales (Objectron, Open Images con
`detections`, fotos propias). Licencia **CC BY-NC**: uso académico correcto,
**hay que declararla en el informe**.

**Impacto en el informe.** El §2.1.6 dice «del orden de 1.500 imágenes» y
**Open Images figura en el plan de datos ya entregado**. Cambiar de fuente es
defendible —es un hallazgo metodológico, no un error de improvisación— y Open
Images no desaparece: sigue sirviendo para `s` con `detections`. El Cap. 5
§Validación ya no cita ninguna cifra (se quitó el 21-ago-2026): el informe habla
del modelo **en futuro** y no declara avances. No reintroducir números hasta
tener v3 evaluado sobre test.

**Objeto de referencia — por las dos vías (decidido).** Botella de **500 ml**.
(1) *Declarada en la descripción*: el remitente escribe «al lado hay una botella
de 500 ml»; usa un campo que ya existe y dice cuál es la referencia, o sea su
medida. (2) *Medición geométrica*: detectar la botella, calcular el factor
píxeles/cm y medir el paquete contra él — visión clásica con OpenCV, no deep
learning, y completamente explicable (se puede mostrar el cálculo), coherente
con la línea de scoring auditable del proyecto. Se cubren mutuamente: la
geometría da precisión, el texto funciona aunque la detección falle. El informe
dice «objeto de referencia» en genérico (RF-VIS-03, CU-03) y **nunca nombra uno
concreto**, así que esto no obliga a tocar el documento.

**Multimodal (imagen + descripción) — decidido, en dos etapas.** Fundamento: la
literatura de estimación monocular indica que, ante la ambigüedad de escala, *si
se conoce la clase del objeto se puede usar el tamaño típico de esa clase*. Un
léxico «heladera → tal volumen» no es una muleta: es la solución reconocida.
- *Arranque — fusión tardía*: el texto no se entrena; un diccionario objeto →
  volumen típico desempata cuando la confianza de la imagen es baja. Sin riesgo
  de fuga de etiqueta y explicable. Es un enfoque publicado (arXiv 2008.06179,
  1611.09534): se cita.
- *Después — brazo de texto entrenado*: el modelo ya es multi-entrada y
  `labels.csv` ya tiene la columna `objeto`. **Ojo con la fuga de etiqueta**: si
  se rellena `objeto` con la clase de Open Images de la que se bajó la imagen, y
  la categoría se deriva de esa misma clase, el texto *es* la etiqueta.

**Qué NO se toca.** (a) `MyDrive/depaso_ml/models/` y `models_v2/` con sus
`reports/`: son la evidencia de la progresión test **0,62 → 0,71** y del
análisis de sesgos; en la defensa sostienen que el problema se detectó
**midiendo**. (b) La **categoría XL se mantiene** —ya está entregada, y sirve
para avisarle a quien no sabe que su sillón de seis cuerpos necesita un flete—.
(c) Las cuatro categorías y el objetivo del Cap. 1 (**≥ 70 % sobre test**, con
los errores en categorías **adyacentes**).

**Dos agujeros medidos que v3 tiene que cerrar.** `has_reference_object` es
**0 en los tres splits** (el modelo tiene la entrada pero nunca aprendió nada de
ella) y los campos `lighting`/`angle`/`background` son `"unknown"` en el **100 %**
de las imágenes, así que **el análisis de sesgos que promete RNF-UADE-01 está
vacío**: las cuatro filas del reporte dan el mismo número. Las dos cosas se
arreglan con la sesión de fotos propias (Paso 2 del `TODO_MARTINA.md`).

**El entregable fuerte para la defensa** no es el accuracy final: es la
**comparación etiquetado-por-tipo-de-objeto (v2) vs. etiquetado-por-dimensiones
-reales (v3)** sobre el mismo test. Muestra método: se detectó un sesgo en el
propio diseño, se midió y se corrigió.

**Colab.** Sesión `depaso-ia` con T4. `colab new -s depaso-ia --gpu T4`,
`colab exec -s depaso-ia -f script.py`, `colab download`, y **siempre**
`colab stop -s depaso-ia` al terminar (si no, consume créditos). `drivemount` y
`auth` exigen una persona en la terminal: **no los puede correr un agente**.

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

## Revisión del 50% — 21-ago-2026 (decisiones de las autoras)

Ronda de auditoría sobre el informe compilado, contrastada contra `../DePaso`.
Se aplicaron **19 ediciones** en Caps. 3, 4 y 5. Compila limpio: 89 pp., sin
referencias ni citas indefinidas, sin `Overfull` mayor a 25 pt.

**Los tres cambios de fondo:**

1. **Roles separados por perfil (RF-USR-06 reescrito).** Antes prometía que «un
   mismo usuario opera como remitente y transportista». Se cambió a **mantener
   separados ambos perfiles**, cada uno con su validación y su reputación, y
   permitir alternar entre ellos sin volver a autenticarse (modelo tipo
   Instagram: una sesión, dos perfiles). Motivo: la app gatea por
   `users.user_type`, que es un campo único, y `User.rating` / `Carrier.reputation`
   ya son dos columnas separadas — la separación es lo que el sistema hace y
   además es lo correcto (son juicios sobre conductas distintas). Tocó también
   §Actores del Cap. 4 y la precondición de CU-04.

2. **El pago deja de ser una retención de fondos (RF-SHP-04 reescrito).**
   `shipments.payment_status` es **una columna de texto**: no hay pasarela, ni
   cuenta, ni fondos. Decir «retención en garantía» describe un *escrow* con
   implicancias regulatorias que el proyecto no tiene. Ahora el RF describe **el
   estado del pago** (pendiente → abonado → liberado → reintegrado) y declara que
   el movimiento de fondos se simula íntegramente. Se barrieron las otras cuatro
   menciones: CU-01 paso 5, CU-06 paso 3, la etiqueta de la Fig. 5.4 y el cierre
   del párrafo del CO₂. **No volver a escribir «retenido» ni «en garantía».**

3. **El informe no declara nada sobre el estado del modelo de IA.** §5.6
   Validación pasó a **futuro** (se quitaron «el procedimiento está implementado
   y automatizado», el detalle del análisis de sesgos y el párrafo del v1 con las
   1.079 imágenes) y §5.7 dice «módulo integrado a la API, **con el modelo en
   desarrollo**». Los RF-VIS se reescribieron a nivel de **qué entra y qué sale**,
   sin mecanismo: RF-VIS-01 = *fotografía + descripción → categoría + confianza*.
   Motivo: v3 arranca de cero y `ml/size_rule.py` ya muestra que la arquitectura
   cambió (la red estima **dimensiones** y una regla las corta en s/m/l/xl, no es
   un clasificador de cuatro salidas). Comprometer el mecanismo obliga a
   defenderlo en diciembre. **Nada de v3, ABO, umbrales ni la comparación v2/v3
   entra al informe hasta tener la medición en la mano.**

**Los otros cambios aplicados:**

- **Foto obligatoria (RF-SHP-01).** Ahora exige «una fotografía del paquete, que
  se conserva como constancia del estado en que se despachó». La obligatoriedad
  es **como registro, no como insumo de la IA**, así sobrevive aunque el
  clasificador falle o no esté. RF-SHP-03 (ingreso manual) queda intacto: es la
  corrección, no un camino que evite la foto.
- **Cap. 3, entrevistas.** De «tres requerimientos derivados» a **dos**, y ya no
  se «planifican»: quedan cubiertos por RF-SHP-01 (foto + descripción). El
  **desglose de peajes y estacionamiento queda fuera del alcance** — sigue
  figurando como hallazgo en la tabla de entrevistas, pero el informe no promete
  implementarlo. No volver a ponerlo como requerimiento.
- **Almacenamiento de objetos.** El informe declara ahora un servicio de
  almacenamiento de objetos para las fotos (no disco local), justificado por
  escalabilidad: no atar las imágenes al ciclo de vida de la instancia ni impedir
  replicarla. Con eso la caja de la Fig. 5.2 **sí** es un contenedor legítimo. Se
  agregó el nodo a la Fig. 5.5 (topología prevista) y al párrafo de topología.
  **Ojo: el código todavía escribe en `uploads/packages/` sin volumen** → las
  fotos se pierden en cada reinicio. Ver el TODO de código.
- **Calificación: solo puntaje.** Se quitó «comentario» de CU-06, de la Tabla 5.II
  y del nodo del DER. La bidireccionalidad **se mantiene declarada** y se va a
  implementar (sigue siendo la mejora #5).
- **RNF-PERF-02: 30 s → 45 s.** El peor caso real es 35 s (`useGpsPublisher`
  publica cada 20 s + `ShipmentDetailModal` consulta cada 15 s), o sea que 30 s
  no se cumplía. 45 deja margen.
- **Tabla 5.I, fila Observabilidad.** «Registro estructurado de eventos» →
  «Registro estructurado en formato JSON (structlog)», con la justificación
  explicitando que es **sobre la salida estándar del servicio, sin depender de una
  plataforma de observabilidad externa**. Decisión de las autoras: que no parezca
  que hay Splunk/Kafka montado. RNF-OBS-01 **no se tocó**.
- **Fig. 3.1.** El pie ya no dice «la barra sin relleno» (era falso: tiene
  `black!12`) — nombra directo la barra de responsabilidad ante daños.
- **Párrafo de la cardinalidad Envío–Clasificación.** Reescrito poniendo la
  conclusión primero: «La clasificación puede existir sin envío asociado, y de ahí
  el mínimo cero en ese extremo».
- **Tabla 5.II, fila Usuario.** Se aclara que el perfil de transportista «se
  administra con independencia del perfil de remitente», para no chocar con el
  nuevo RF-USR-06.

**Verificado y correcto — no volver a revisar:** las 14 cardinalidades del DER una
por una contra los `models.py`; las Figs. 5.1, 5.3 y 5.4; la Tabla 5.III completa
(la separación «servicio de ruteo» vs. «cálculo propio de distancias» está bien
resuelta y es la respuesta a «¿el filtro de desvío mide lo que dice medir?»);
HTTP vs. HTTPS (el informe ya lo explica bien: HTTPS es HTTP dentro de TLS y lo
termina el proveedor, por eso el `Dockerfile` usa `--proxy-headers`); «sitio
estático» para el panel (`vite build` → `dist/`, nginx en el compose);
TypeScript al 100 % (102 archivos `.ts/.tsx` en la app, 39 en el panel, cero
`.js`); el párrafo WTP/WTA de la conclusión («compatibilidad preliminar», no
viabilidad).

**Rechazado a propósito:** «MiPyMEs» en Porter se deja — es el vocabulario del
informe del ICC, que define esa población; cambiarlo a «PyMEs» alteraría a qué
grupo corresponde el 44 %. Y se probó rotular la flecha de la Fig. 5.5 como
«HTTP (red local)»: **colisiona con la etiqueta «red local»** de la flecha
API→PostgreSQL. Quedó en «HTTP».

**Barrido final (21-ago-2026).** Se auditó el documento **entero** —incluidos
resumen, abstract, conclusión y anexos— contra los cinco temas de la revisión.
Aparecieron **dos afirmaciones de avance en IA fuera del Cap. 5**, que habían
quedado sueltas y se corrigieron:
- `conclusion.tex`: «una primera versión **entrenada** del clasificador de carga»
  → «el módulo de estimación de la categoría de carga integrado al servicio».
  También «requerimientos para la etapa siguiente» → «incorporados al Cap. 4»
  (coherencia con el cambio del Cap. 3), y «**Ampliación** del conjunto de datos»
  → «**Construcción** del conjunto de datos» en trabajo futuro.
- `appendix/schedule_of_activities.tex` (Anexo A): «el clasificador de carga
  cuenta con una primera versión **entrenada en julio**; este **adelanto** respecto
  de la planificación original otorga mayor margen…» → se eliminó la afirmación
  entera; ahora dice que la construcción del dataset y el desarrollo del
  clasificador **continúan en curso**.

**Regla que queda:** las afirmaciones sobre el modelo viven en **cuatro** archivos
además del Cap. 5 (`summary.tex`, `abstract.tex`, `conclusion.tex` y el Anexo A).
Al tocar el estado de la IA hay que barrer los cinco, no solo el capítulo.
*(`summary.tex` y `abstract.tex` describen el clasificador como componente de la
plataforma, no como logro; además son texto del 25 % y no se tocan.)*

**Verificación de la regla del 25 % (21-ago-2026).** Se comprobó línea por línea,
contra `25%-final`, que **ninguna de las 39 líneas modificadas en esta ronda
existía en el documento entregado**. Las 22 diferencias del Cap. 3, las 9 del
Cap. 1 y las 8 del Cap. 2 frente al 25 % son **anteriores** a esta sesión y
corresponden a decisiones ya documentadas acá (revisión de estilo del tutor,
mayúsculas en títulos, comillas angulares, `\textperiodcentered` en las fichas de
persona, `[ht]`→`[H]`, métricas verificables en los objetivos específicos, e
inserciones de `\nuevo{}`). Los Caps. 4 y 5 no existían en el 25 %.

Comando para repetir la verificación:

```bash
git diff --unified=0 -- chapters/ | grep '^-[^-]' | while read -r l; do
  git grep -qF "${l:1}" 25%-final -- chapters/ && echo "⚠ 25%: ${l:1}"
done
```

**TODO de código derivado:** `docs/todo-codigo-informe50.md`.

## Mejoras para la próxima etapa (post-50%)

Lista consolidada (17-ago-2026), ordenada por prioridad. Es un MVP: nada de esto
bloquea la entrega del 50%.

| # | Mejora | Costo | Prio |
|---|---|---|---|
| 1 | **El feed muestra envíos impagos**: el matching no filtra por `payment_status`, contradice CU-01 alt. 5a | 1 línea en `matching/service.py` | Alta |
| 2 | **Códigos `RF-*` del código desalineados** con el Cap. 4: el código usa `RF-CAR-07` para la penalización (informe: `RF-CAR-08`) y cita un `RF-MAT-05` inexistente. La numeración válida es la del Cap. 4 | ~30 min de grep | Alta |
| 3 | ~~Correr el test set~~ **HECHO**: v1 da **0,62** y existía un v2 (28-jul) sin documentar que da **0,71**. Reemplazado por → **rehacer el dataset con dimensiones reales (v3)**, ver `ml/PLAN_V3.md` | varios días | Alta |
| 4 | **Fotos propias con la botella de 500 ml**: `has_reference_object` es **0 en los tres splits**, y `lighting`/`angle`/`background` son `"unknown"` en el **100 %** → el análisis de sesgos de RNF-UADE-01 está **vacío** | sesión de fotos | Alta |
| 5 | **Calificación bidireccional** (decidido): quitar `uq_rating_shipment` → único por (shipment, rol), endpoint carrier→cliente, escribir `User.rating` | ~1 día | Media |
| 6 | **`Classification` no guarda la ruta de la imagen**: agregar la columna convierte esa tabla en dataset de reentrenamiento listo (hoy habría que cruzar por `shipment_id`, que suele ser NULL) | 2 líneas | Media |
| 7 | **CO₂ recalculado en la entrega con trazas GPS reales** (decidido) + actualizar párrafo y figura de secuencia del Cap. 5 que hoy dicen «al aceptar» | ~1 día | Media |
| 8 | **Push real** (Expo push) para que CU-04 «el sistema comienza a evaluar» sea literal; hoy es polling del cliente | ~1 día | Media |
| 9 | **Escalada de precio si nadie acepta** (ver §Pricing): destraba el envío huérfano en `pending` y genera los datos de elasticidad | ~2 días | Media |
| 10 | Tracking por polling 15 s → SSE/WebSocket desde FastAPI | ~1 día | Baja |
| 11 | `create_all()` sin migraciones: OK para MVP; introducir Alembic recién si hay datos en producción | — | Baja |
| 12 | **Cursivas RAE en extranjerismos del texto del 25%** (~15 casos de *matching/tracking/scoring/dataset* en redonda): pasada global recién en la **entrega final**, cuando el diff ya no importe | 10 min | Baja |
| 13 | **Espacio fino antes del `\%` en el texto del 25%** (~24 casos de `69,8\%` en `chapter03.tex`, `surveys.tex`, `schedule_of_activities.tex`): el texto nuevo del 50% ya usa `~\%` (norma RAE). Misma lógica que la fila 12: pasada global en la **entrega final** | 5 min | Baja |

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


## Revisión de estilo del tutor (19-ago-2026) — aplicada

Pedido: corregir redundancia y profesionalizar lo nuevo de `50%-final`; auditar
mayúsculas, orden de la bibliografía, ortografía y gramática; y revisar
FODA / cinco fuerzas de Porter.

Existe el skill **`rae-informes`** (`.claude/skills/rae-informes/SKILL.md`) con el
checklist RAE del proyecto: usarlo al redactar o revisar prosa en `chapters/*.tex`.

Correcciones aplicadas (las dos primeras las señaló el tutor por nombre):
- «La muestra se conformó mediante un muestreo…» → «Se aplicó un muestreo…» (Cap. 3).
- «Se dedica a hacer fletes» → «Fletero independiente» (user persona Carlos Gómez);
  su cita representativa repetía «clientes» dos veces, se reescribió.
- Otras redundancias: «el Capítulo 5 desarrolla la metodología de desarrollo»,
  «la transcripción… y la transcripción…», «fotografía el paquete y acompaña la
  fotografía», «mercado de dos lados… de ambos lados», «estado asignado…
  transportista asignado», y tres secciones que abrían repitiendo su propio título
  (Arquitectura de la solución / Diseño de la interfaz / Modelo de datos).
- Extranjerismos del texto **nuevo** a cursiva: *backend*, *frontend*, *stack*,
  *token(s)*, *software*, *matching*, *crowdsourced delivery*, *gig-workers*,
  *user personas*. El texto del 25% queda para la pasada final (fila 12).
- Tipografía: comillas rectas `"…"` → angulares «…» en las citas de las user
  personas; guion corto como separador en las fichas de persona → `\textperiodcentered`;
  `\%` → `~\%` en todo el texto nuevo (fila 13 para el resto).
- Calcos: «a nivel de objeto» → «por objeto»; «contenedorizado» → «en contenedores».

**Verificado y sin cambios:** mayúsculas (los títulos ya usan mayúscula solo en la
primera palabra; los roles van en minúscula); bibliografía (las 17 entradas de
`biblio.bib` están citadas y las 17 claves citadas existen; `sorting=nyt` ordena
alfabéticamente); compilación limpia (87 pp., sin referencias ni citas indefinidas,
sin `Overfull` mayor a 25 pt).

**Detalle cosmético conocido, no se toca:** tres claves BibTeX llevan un año que ya
no coincide con el `YEAR` de la entrada tras la actualización a las versiones de
journal (`AkamatsuOyama2023`→2024, `LuyEtAl2023`→2024, `SalehEtAl2024`→2026,
`OyamaAkamatsu2024`→2025). La clave es una etiqueta interna: no se imprime en
ningún lado con `style=iso-numeric`. Renombrarlas obliga a tocar todos los
`\parencite` sin beneficio visible.

**FODA y Porter:** no hay skill instalado de análisis estratégico (`find-skills`
puede buscar uno). Se revisaron a mano contra la rúbrica: las cinco fuerzas están
completas y cada una cierra con evidencia citada; el FODA tiene los cuatro
cuadrantes más la lectura cruzada, y la estrategia de diferenciación cierra el
apartado. La fila «Competencias» de la rúbrica queda cubierta.

## Auditoría final de la entrega del 50% — 19-ago-2026

Se verificaron los **ocho ítems de la rúbrica** y **todos los diagramas contra el
código de `../DePaso`** (no contra los `.md`). Los ocho ítems quedan cubiertos:
Requerimientos (Tablas 4.I/4.II + 6 CU + Fig 4.1), Mockups (Figs 5.6--5.10),
Diagramas (CU, C4 x3, secuencia, despliegue, DER), Competencias (Porter 2.III,
FODA 2.IV, estrategia), Tecnologías (§5.3.1 lenguajes + §5.2.1 red + Fig 5.5),
Modelo de datos (DER 5.11 + Tabla 5.II + **Tabla 5.III de fuentes de datos**, que
es la que cubre el «datasources» del estándar), Demo (Figs 5.12/5.13) y Tabla
comparativa (2.I).

**Verificado contra el código y correcto — no volver a revisar:** los 11 módulos
de dominio coinciden exactamente con `modules/`; las **12 cardinalidades del DER**
se corresponden una por una con los `models.py` (`carriers.user_id` unique →
`0..1`; `shipments.carrier_id` nullable → `0..1`; `uq_rating_shipment` → `0..1`;
`classifications.shipment_id` nullable → `0..1`/`0..N`; las dos asociativas N:M
con su `UniqueConstraint`); el CO₂ se persiste en `accept_shipment`; se crea un
evento `PENDING` al crear el envío, lo que justifica el `1..N`; las imágenes van a
`uploads/packages` con `uuid4().hex` (RNF-SEC-03).

**Defectos corregidos en los diagramas:**
- **Fig 5.3 dibujaba tres capas y el texto declaraba cuatro.** Se agregó la caja
  *Esquemas*, transversal a enrutamiento y servicios. El repo confirma las cuatro
  (`router/service/repository/schemas`).
- Fig 5.4: las etiquetas no tapaban las líneas de vida y la de «Base de datos»
  atravesaba cuatro textos → estilo `lb` con `fill=white`.
- Fig 5.2: `.\,keras` dejaba un espacio espurio; dos flechas sin rótulo; «o
  alternativa» no nombraba nada.
- Fig 5.11 y su texto: se agregó el verbo «acumula» (única relación binaria sin
  verbo) y se aclaró que **las entidades asociativas no llevan verbo** y **cómo se
  lee la cardinalidad** (la contigua a una entidad cuenta instancias de esa
  entidad). Antes el texto afirmaba que toda relación llevaba verbo y cinco no.
- **`roles` no existe en el código**: `User` solo tiene `user_type`. Ser
  transportista se deriva de tener perfil `Carrier`, que el DER ya muestra con
  «posee perfil de». Se corrigió la caja del DER y la Tabla 5.II.
- **`owner_user_id`** es una cuarta clave foránea omitida en el DER: el texto
  decía «tres».
- La separación en cuatro capas **no rige en los 11 módulos**: `admin`, `auth`,
  `co2` y `vision` no tienen `repository.py`. Se matizó a «los módulos con
  persistencia propia».

**Decisión de despliegue: Docker (19-ago-2026).** El informe afirmaba que la API
corre «dentro de un contenedor sobre una plataforma como servicio» y apoyaba en
eso la portabilidad de RNF-INF-02, pero `render.yaml` declaraba `runtime: python`
con `pip install` — o sea, un build propio de Render que ignoraba el `Dockerfile`
existente. En vez de bajar la afirmación del informe se **alineó el repo**, porque
todavía no está decidido el proveedor y una imagen es el artefacto que no ata a
ninguno: `render.yaml` pasó a `runtime: docker` + `dockerfilePath`, y el CMD del
`Dockerfile` pasó de `--port 8000` fijo a `--port ${PORT:-8000}` (las PaaS
inyectan `$PORT`; en local, sin la variable, sigue en 8000 y `docker-compose` no
se rompe). **El texto del informe no se tocó: ahora es literalmente cierto.**

**Detectados y NO corregidos (decisión de las autoras):**
- `password_reset_tokens` no figura en el DER ni en la Tabla 5.II ni entre las
  omisiones declaradas. Es una tabla técnica, no de dominio.
- `main.py:103` hace `CREATE EXTENSION IF NOT EXISTS postgis` y `docker-compose`
  usa la imagen `postgis/postgis`. **El informe igual es preciso**: no hay
  columnas `geometry` ni funciones `ST_`, la geo se resuelve con haversine, y la
  tabla del stack dice «con extensiones geoespaciales disponibles para una
  eventual optimización». No cambiar el informe por esto.

## Espaciado de títulos y cursivas del índice — 19-ago-2026

**Títulos sin margen superior (resuelto).** `titlesec` aplica el espacio *anterior*
con `\addvspace`, que **solo agrega la diferencia** respecto del espacio ya
acumulado. Con `{0pt}{12pt}{6pt}` un título que venía después de un `enumerate`,
un `longtable` o una figura quedaba **pegado** al bloque anterior (caso visible:
§3.7 «User personas», que tocaba el ítem 7 de los hallazgos accionables). En
`main.tex` el espacio anterior pasó a ser elástico y mayor que el que dejan esos
entornos:

| Nivel | Antes | Ahora |
|---|---|---|
| `\section` | `{0pt}{12pt}{6pt}` | `{0pt}{20pt plus 6pt minus 4pt}{8pt}` |
| `\subsection` | `{0pt}{12pt}{6pt}` | `{0pt}{17pt plus 5pt minus 3pt}{6pt}` |
| `\subsubsection` | `{0pt}{12pt}{6pt}` | `{0pt}{14pt plus 4pt minus 2pt}{6pt}` |

`\chapter` no se tocó (arranca página). Se eliminaron los tres `\vspace{1em}`
sueltos de `chapter01.tex`: eran parches locales a este mismo problema y ahora
duplicarían el espacio. **No volver a parchear con `\vspace` manual**; si un
título aparece pegado, subir el valor en `\titlespacing`.

Nota: un título de sección seguido *inmediatamente* por uno de subsección (p. ej.
1.2 → 1.2.1, sin texto en medio) queda algo justo por el mismo motivo. Es el
comportamiento estándar de LaTeX y se dejó así: separarlos más los desvincula
visualmente.

**Cursivas solo en el cuerpo (decisión de las autoras, 19-ago-2026).** Los
extranjerismos van en cursiva **únicamente en el texto corrido**: nunca en un
título de sección, en un epígrafe de figura o tabla, ni por lo tanto en el índice.
Se probó primero conservarlos en cursiva en el título y limpiarlos del índice con
el argumento corto opcional (`\section[User personas]{\emph{User personas}}`);
**se descartó**: las autoras quieren los encabezados enteros en redonda.

Quedaron así (sin `\emph` y sin argumento corto):

```latex
\section{User personas}
\subsection{Stack tecnológico por capa}
\subsection{CU-02 --- Asignar un transportista mediante matching}
\caption{Componentes del backend: módulos de dominio en cuatro capas (C4, nivel 3)}
```

En el cuerpo esas mismas palabras **sí** llevan cursiva (`\emph{user personas}`,
`\emph{backend}`, `\emph{matching}`, `\emph{stack}`). Comprobación rápida de que
no se coló ninguna:

```bash
grep -rn '\\\(chapter\|section\|subsection\|subsubsection\|caption\)\*\?\(\[[^]]*\]\)\?{[^}]*\\\(emph\|textit\|textsl\)' chapters/
```

## Figura de la encuesta (Cap. 3 §3.4) — 19-ago-2026

`fig:encuesta` en `chapters/chapter03.tex`: barras horizontales en dos bloques,
**DEMANDA (remitentes)** y **OFERTA (transportistas potenciales)**. Es el único
gráfico de la encuesta y está en **TikZ nativo** (sin pgfplots), como el resto de
los diagramas del repo.

**Por qué así y no una torta.** Los indicadores son porcentajes de sí/no sobre
**bases distintas** (n = 116, 98, 94): no son partes de un todo y una torta
obligaría a sumar 100 % falsamente. Las barras horizontales además dejan escribir
el `n` de cada fila, que es lo que §3.4 se compromete a explicitar.

**Por qué dos bloques.** Carga el argumento estructural del proyecto —un mercado
de dos lados necesita ambos validados a la vez— y conecta con la debilidad del
FODA «dependencia de la adopción simultánea de ambos lados». Un ranking único de
ocho barras se evaluó y se descartó: es más legible pero puramente descriptivo.

**Paleta neutra, en grises (decidido el 19-ago-2026).** Se probó primero con los
colores de marca de la app (`forest #0B3B2E`, `emerald #10B981`, `amber #E89E2A`
sobre el crema `#F4EFE3`, tomados de `../DePaso/depaso_app/tailwind.config.js`) y
las autoras lo descartaron: **queda raro** en el informe, se lee como pieza de
marketing y no como figura de datos. Las definiciones `dp*` se retiraron del
preámbulo de `main.tex`; si alguna vez se quiere volver, están en el commit y en
el `tailwind.config.js`. Ahora: demanda `black!78`, oferta `black!50`, guías
`black!18`. **Sin panel de fondo**: el gráfico va directo sobre el blanco de la
página. Se probó un `black!3` de fondo y también se descartó — no agregar
rectángulo de fondo de ningún color.

**La última barra (73,4 % preocupación por daños) va sin relleno, a propósito.**
Es el único indicador **negativo** del gráfico: mide una barrera de adopción, no
una adhesión. En grises no alcanza con un tono distinto —se leería como «otra
categoría más»—, así que lleva relleno claro (`black!12`) **con contorno**
(`black!55`), que la marca como una medida de otra naturaleza, y el pie lo aclara.
No rellenarla como las demás ni moverla junto a las otras dos: leerla como logro
sería un error de lectura.

**Cifras verificadas** con `docs/encuesta/verify_numbers.py` (correrlo desde
`docs/encuesta/`, usa una ruta relativa): las siete pasan.

**Trampa de TikZ encontrada:** `\hyphenpenalty=10000` dentro de la clave `font=`
de un estilo de nodo rompe con «Missing number, treated as zero» (choca con
`\protect`), y `latexmk` queda en estado de error aunque el PDF salga igual. Para
evitar que una etiqueta se parta, usar un `\\` explícito en el texto del nodo.

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