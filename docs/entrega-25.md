# Entrega 25 % — DePaso

Documento de trabajo de la **entrega del 25 % (Definición)** del PFI. Reúne en un
solo lugar: (A) el resumen de lo efectivamente realizado, (B) la rúbrica y guía
de evaluación de la cátedra, y (C) el esquema de contenidos del documento.

> La **Introducción** (objetivos, alcance, estructura) **no se incluye** acá: ese
> material corresponde a la **propuesta (0 %)**. Las secciones de *Metodología de
> desarrollo* y *Conclusión general* del esquema anticipan las entregas del 50 % y
> 100 % y se conservan solo como referencia.

Documento general del proyecto: ver [`../CLAUDE.md`](../CLAUDE.md).
Especificación funcional/técnica detallada (para 50 % en adelante): ver
[`proy.txt`](proy.txt). Datos crudos y scripts de la encuesta: ver
[`encuesta/`](encuesta/).

---

## Parte A — Resumen de lo realizado en el 25 %

La entrega del 25 % corresponde a los **Antecedentes** (marco teórico + estado del
arte), la **investigación de usuarios** y la **planificación**. Lo concretado:

### Marco Teórico (Cap. 2)
Cinco subtemas, de lo general a lo específico, cada uno ligado a una decisión de
diseño:
1. **Crowdsourced delivery (CSD) y logística de última milla** — el CSD aprovecha
   desplazamientos existentes en lugar de generar viajes nuevos.
2. **Flotas híbridas y el problema del desvío** — los vehículos personales
   compartidos (SPVs) reducen el costo unitario, pero un desvío excesivo elimina
   el beneficio ambiental → el desvío es variable explícita del *matching*.
3. **Perfiles de conductores: gig-workers (GW) vs. conductores ocasionales (OD)** —
   fundamento teórico de la modalidad colaborativa.
4. **Diseño de mercados de matching y asignación** — justifica un *scoring*
   determinístico frente a subastas que exigen datos históricos inexistentes al
   arranque.
5. **Visión computacional y aprendizaje por transferencia** — clasificar la carga
   desde una foto; la estimación 3D exacta desde el móvil es inviable.

Se complementa con la **declaración del plan de datos** del clasificador
(procedencia, volumen ~1.500 imágenes y tratamiento del *dataset*).

### Estado del Arte (Cap. 2)
- **Estrategia de búsqueda documentada**: bases Google Scholar, IEEE Xplore,
  Scopus y arXiv; filtro temporal 2022–2026; cinco preguntas de investigación.
- **Competidores analizados**: Rappi Favor, PedidosYa Envíos, Uber Flash, DiDi
  Entrega, OCA/Andreani, Moova, Treggo, Shipit + tabla comparativa.
- **Matriz de antecedentes**: 7 trabajos (objetivo, enfoque, tecnologías,
  resultados, limitaciones y aporte para DePaso).
- **Brecha que justifica DePaso**: 5 elementos que ninguna solución combina
  simultáneamente en el contexto argentino (híbrido GW+OD, IA de carga, control
  del desvío, CO₂ por envío y adaptación al AMBA).

### Investigación de Usuarios (Cap. 3)
- **Encuesta** (Microsoft Forms, lanzada 22-may-2026): 145 respuestas completas,
  133 (91,7 %) del AMBA. Muestreo no probabilístico por conveniencia; margen de
  error teórico ≈ ±8,5 % (95 % de confianza) para fines exploratorios. Bases por
  bifurcación explicitadas por indicador.
- **Tabla de hallazgos clave + 7 hallazgos accionables**.
- **3 User Personas preliminares**: Juan García (PyME, Lanús), María Álvarez
  (transportista colaborativa, Caballito→Microcentro) y Carlos Gómez (fletero
  dedicado, Quilmes).
- Se descartaron las **entrevistas** por decisión metodológica acordada con el
  tutor (problema transversal a la población general del AMBA).

### Planificación
- **Diagrama de Gantt** en el Apéndice A (cronograma del trabajo).

### Bibliografía y rigor de fuentes
- 7 antecedentes + fuentes metodológicas, norma **ISO 690-2010** (biblatex,
  estilo iso-numeric, backend biber).
- Todas las fuentes provienen de venues académicos confiables (Elsevier, SAGE,
  arXiv) o institucionales (Durham, OIT); **DOIs verificados** y vivos.
- Cuatro citas se actualizaron de su versión arXiv a la versión formal de journal
  (regla de la cátedra: arXiv máx. 2 años sin paper formal posterior).

### Decisión de alcance documental
- El **stack tecnológico no se menciona** en el documento del 25 % (decisión de
  las autoras): se define en el Cap. 4 (entrega 50 %).

---

## Parte B — Rúbrica y guía de evaluación (cátedra)

> Consolidado a partir de la **Guía de Evaluación del 25 % del PFI** y la **Rúbrica
> de Evaluación (Entrega 25 %)** de la cátedra.

### B.1. Rúbrica de evaluación (Entrega 25 %)

| Concepto | Estándar para cumplir | Estándar para no cumplir |
|---|---|---|
| **Estructura general del trabajo** | Respeta la estructura solicitada y presenta organización coherente. | Estructura incompleta, desordenada o fuera del esquema requerido. |
| **Carátula e índices** | Carátula institucional correcta e índices bien implementados. | Carátula con errores o faltan índices / niveles de organización. |
| **Formato académico** | Respeta márgenes, tipografías, encabezados y formato institucional. | No respeta el formato o presenta inconsistencias visuales. |
| **Redacción académica** | Formal, clara, impersonal y sin errores relevantes. | Informal, confusa o con errores frecuentes. |
| **Marco teórico** | Suficiente y contextualiza adecuadamente el tema. | Insuficiente o poco relacionado con el problema. |
| **Hilo conductor y coherencia** | Coherencia y continuidad lógica entre secciones. | Contradicciones o falta de cohesión. |
| **Estado del arte** | Antecedentes relevantes y análisis comparativo adecuado. | Limitado o superficial. |
| **Conclusión del estado del arte** | Síntesis clara del diferencial del proyecto. | Sin conclusión clara o sin evidenciar el diferencial. |
| **Realización de entrevistas** | Aportan valor y están correctamente justificadas. | Escasas, poco relevantes o mal documentadas. |
| **Uso de fuentes y referencias** | Citas conforme a normas académicas y fuentes confiables. | Errores de citación o fuentes poco confiables. |
| **Originalidad académica** | Sin plagios ni usos indebidos de contenido. | Plagios o ausencia de atribución correcta. |
| **Dominio conceptual** | Comprensión sólida y adecuada del tema. | Errores conceptuales o escaso dominio. |
| **Planificación del proyecto** | Cronograma y planificación consistente de actividades. | Sin planificación o inconsistente. |
| **Uso de datasets** | Uso explicitado y justificado cuando corresponde. | No se aclara o se utiliza incorrectamente. |

> **Nota DePaso — Entrevistas:** la técnica de entrevistas fue **deliberadamente
> desestimada y validada con el tutor**. El criterio *"Realización de entrevistas"*
> y el lineamiento del Bloque 04 sobre *"3 a 5 entrevistas transcritas"* **no
> aplican** a esta entrega. La metodología de usuarios se sostiene sobre una
> **encuesta cuantitativa con fundamentación estadística del tamaño de muestra** +
> **User Personas**, en reemplazo justificado de las entrevistas.

### B.2. Guía de evaluación — desglose por bloques

**BLOQUE 01 — Estructura y formato.** La estructura debe coincidir estrictamente
con el temario de nivel 1 (Introducción → Apéndices). Índice de navegación con
profundidad máxima de 4 niveles; carátula institucional oficial. Verificación
estricta de márgenes, pie de página, tipografía y diferenciación de títulos;
títulos extensos con versiones acortadas en encabezados.

**BLOQUE 02 — Redacción y rigor.** Tono impersonal íntegro; sin vocabulario
pretencioso; claridad y síntesis sin errores de redacción/sintaxis/semántica.

*Rigor bibliográfico:*
| Criterio | Requisito | Detalle de corrección |
|---|---|---|
| Origen de fuentes | Estrictamente académicas o reconocidas. | Prohibido blogs genéricos o wikis, salvo que sean objeto de estudio. |
| Referencias en arXiv | Aceptación condicionada. | **Máx. 2 años desde su publicación sin paper formal posterior.** |
| Formato de citas | URL completa y metadatos si no hay DOI/ISBN. | Incorporar **"Disponible en"** + **"última fecha de consulta"**. |
| Integridad académica | Ausencia total de plagio. | Cualquier plagio invalida la entrega. |

**BLOQUE 03 — Fundamentos teóricos.** Marco suficiente que nivele al lector; hilo
conductor fluido; preparar cada concepto antes de usarlo (no referenciar
elementos a definir a futuro). El Estado del Arte concluye con un resumen nítido
del diferencial; tabla comparativa de alto valor visual.

**BLOQUE 04 — Metodología de usuarios.** La **encuesta** es el mecanismo
cuantitativo medular; no se admiten volúmenes planos sin fundamentación
estadística del tamaño de muestra. Consistencia socio-demográfica con el alcance
del proyecto. Técnicas alternativas: workshops, brainstorming, entrevistas
técnicas. *(Entrevistas: no aplican a DePaso — ver nota arriba.)*

**BLOQUE 05 — Planificación temporal.** Diagrama de **Gantt obligatorio**
(Apéndice A); documentar y justificar técnicamente los desvíos temporales. Hitos:
25 % Definición · 50 % Desarrollo · 75 % Validación · 100 % Defensa.

**BLOQUE 06 — Gestión de datasets.** Declarar origen exacto de los datos crudos,
volumen estimado y confiabilidad del origen; detallar saneamiento,
preprocesamiento de nulos y codificación.

---

## Parte C — Contenido del documento (esquema, sin Introducción)

> Esquema condensado del documento. Se omite la sección *1. Introducción*
> (propuesta / 0 %). Las secciones 4 y 5 anticipan las entregas 50 % y 100 %.

### 2. Antecedentes

**Marco Teórico — ¿con qué conceptos y teorías trabajamos?**

- **Logística colaborativa y economía de plataforma:** DePaso opera en un mercado
  de dos lados (*two-sided markets*); su éxito depende del efecto de red y de
  equilibrar la elasticidad de participación de ambos actores.
- **Economía colaborativa (capacidad ociosa):** acceso sobre propiedad; aprovechar
  un viaje que ya se iba a realizar genera valor compartido y mitiga impactos
  ambientales.
- **Crowdsourced Delivery (CSD) y flotas híbridas:** vehículos dedicados (DVs) +
  vehículos personales compartidos (SPVs). Dentro de los SPVs, los *Occasional
  Drivers* (ODs) solo aceptan solicitudes cuyo origen/destino coinciden con su
  ruta privada, logrando el mínimo desvío.
- **Visión computacional para clasificación de objetos:** redes neuronales para
  clasificar volumen a partir de imágenes, evaluadas con *accuracy*, matriz de
  confusión y análisis de sesgos.
- **Matching & Pricing:** mecanismos de subasta o *scoring* que minimizan el costo
  del desvío frente a compensaciones justas; *task-bundling* para reducir costos
  sub-aditivos.

**Estado del Arte — ¿quién hizo qué y con qué resultado?**

- **Nivel global:** métodos matemáticos para el *matching* masivo (heurísticas de
  descomposición, subastas VCG, IA/DQN para *scheduling*). La academia asume
  cargas homogéneas y advierte que, sin control del desvío, la logística
  colaborativa puede aumentar las emisiones.
- **Nivel local (AMBA):** plataformas de economía gig (Rappi, PedidosYa, Glovo)
  que, según la OIT, operan como empleos de tiempo completo no reconocidos, con
  sistemas de puntaje punitivos y foco en paquetería ligera y comida.
- **Brecha (conclusión):** DePaso crea una plataforma híbrida real (DVs + ODs
  colaborativos) sin exclusividad, suma clasificación de carga heterogénea por IA
  propia y cálculo de CO₂ ahorrado.

### 3. Descripción — User Research

- **Encuesta** (Microsoft Forms, 22-may-2026): 145 respuestas, 133 (91,7 %) del
  AMBA. Bases por bifurcación: uso n = 116, transportista n = 98. Hallazgos clave:
  69,8 % predisposición colaborativa; 84,5 % interés en transportar; 91,8 %
  motivado por "ingreso extra sin desvío"; costo como principal criterio (75,0 %);
  responsabilidad por daños como principal preocupación (73,4 %); WTP
  $3.000–6.000 (68,1 %) solapado con WTA $2.500–5.000 (51,0 %).
- **User Personas (3 preliminares):**
  - *Juan García* (dueño de PyME, Lanús): enviar mercadería mediana/voluminosa de
    forma económica sin pagar un flete exclusivo vacío.
  - *María Álvarez* (conductora colaborativa, Caballito→Microcentro): monetizar el
    espacio vacío del baúl aceptando solo pedidos de paso.
  - *Carlos Gómez* (fletero dedicado, Quilmes): optimizar horas recibiendo alertas
    estructuradas de mudanzas o cargas grandes.

### 4. Metodología de desarrollo *(anticipa 50 %)*

Metodologías ágiles (Scrum / Kanban). Frontend con registro multimodal y captura
de imágenes; backend con algoritmo de *scoring* multivariable determinístico
(compatibilidad geoespacial, desvío, tipo de carga, reputación, ventana horaria);
módulo de visión computacional (dataset ~1.500 imágenes, *accuracy* + matriz de
confusión, mitigación de sesgos); módulo de sostenibilidad con factores de
emisión del IPCC. Validación con pruebas unitarias e integrales.

### 5. Conclusión general *(anticipa 100 %)*

DePaso aborda simultáneamente las ineficiencias de la logística urbana y las
problemáticas de la economía de plataformas en Argentina, materializando los
avances en CSD y flotas híbridas en un prototipo funcional con clasificación de
carga por IA local y medición transparente de la huella de carbono.

### 6. Bibliografía

Gestionada en [`../biblio.bib`](../biblio.bib) (BibTeX, backend biber, norma
ISO 690-2010). Antecedentes en la matriz: Yang et al. (2024), Luy et al. (2024),
Akamatsu & Oyama (2024), Oyama & Akamatsu (2025), Saleh et al. (2026), Naumann et
al. (2023) y OIT (2020).
