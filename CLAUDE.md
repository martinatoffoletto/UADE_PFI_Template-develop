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
entrenado por el equipo con un dataset de 1.079 imágenes al 17-ago-2026 (Google Open Images +
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
- **Alineación informe ↔ repo `../DePaso` (17-ago-2026).** Se auditaron todos los
  `.md` de ambos repos contra el código. Corregido: dataset 1.500→**1.079** real
  (Cap. 2 y `CONTEXTO.md`; el E25 sí decía 1.500 como estimación, la progresión es
  legítima); actores unificados en **cuatro** (Cap. 4 y Cap. 5, con la
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

Técnicas usadas: encuesta (permanece abierta), entrevistas semiestructuradas y
user personas.

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

**Encuesta** ✓ completada
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

**User Personas** — 3 preliminares construidas a partir de la encuesta:
Juan García (remitente PyME, Lanús), María Alvarez (transportista colaborativa,
Caballito→Microcentro) y Carlos Gómez (fletero dedicado con camión, Quilmes).
Pendiente: refinarlas a medida que se amplíe la muestra de la encuesta.
- Elementos: nombre ficticio, datos demográficos, contexto/rol, objetivos,
  frustraciones, comportamientos, cita representativa.

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

## Notas temporales de entorno (borrar cuando ya no haga falta)

- Se instaló `poppler` vía Homebrew (`brew install poppler`, comando `pdftoppm`)
  el 2026-08-16 para poder previsualizar páginas específicas de PDFs (usado para
  revisar el render de `latexdiff` contra `main`). No es una dependencia del
  proyecto en sí 