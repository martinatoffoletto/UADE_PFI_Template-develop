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
entrenado por el equipo con dataset de ~1.500 imágenes (Google Open Images +
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
CapaTecnologíaBackendPython + FastAPIFrontend / App móvilReact Native + ExpoBase de datosPostgreSQL + PostGIS (cloud)IA / MLFrameworks de ML en la nube con GPUDatos geoespacialesOpenStreetMap / datos de calles AMBADiseñoFigmaControl de versionesGit / GitHub

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
| Backend | Python + FastAPI |
| Frontend / móvil | React Native + Expo |
| Base de datos | PostgreSQL + PostGIS (cloud) |
| IA / ML | Frameworks ML con GPU en la nube |
| Geo | OpenStreetMap / datos AMBA |
| Diseño | Figma |
| Docs | LaTeX / MikTeX — norma de citas ISO 690-2010 |

---

## Convenciones del repo

- Un archivo `.tex` por capítulo en `chapters/`
- Figuras en `figures/`, bibliografía en `referencias.bib` (BibTeX)
- Citas con `\cite{}`, norma ISO 690-2010
- Compilar con `pdflatex` o `latexmk`

---

## Qué es cada sección del documento

### Marco Teórico

Reúne los conceptos, teorías y modelos que sustentan el proyecto. No es un
glosario ni un manual técnico: es una construcción argumentativa donde cada
subtema responde a una pregunta concreta vinculada a los objetivos.

> Responde: *¿con qué conceptos y teorías trabajamos?*

Subtemas definidos para DePaso (de lo general a lo específico):

1. **Logística colaborativa y economía de plataforma** — mercados de dos lados
   (two-sided markets). Remitentes en un lado, transportistas en el otro. El valor
   crece con la base de usuarios de ambos lados (efecto de red).
   - Hagiu & Wright (2015) — *Multi-Sided Platforms*. Harvard Business School.
   - Rochet & Tirole (2003) — *Platform Competition in Two-Sided Markets*. JEEA.

2. **Economía colaborativa / sharing economy** — acceso por sobre propiedad:
   aprovechar capacidad ociosa (un viaje que ya se iba a realizar) para generar
   valor compartido.
   - Botsman & Rogers (2010) — *Beyond Zipcar: Collaborative Consumption*. HBR.
   - Carbone, Rouquet & Roussat (2017) — *The Rise of Crowd Logistics*.
     Journal of Business Logistics.

3. **Crowdsourced delivery y last-mile logistics** — conductores ad hoc para
   cubrir el último tramo. Puede reducir costos hasta un 42%, pero requiere
   resolver el matching dinámico en tiempo real.
   - Arslan, Agatz, Kroon & Zuidwijk (2019) — *Crowdsourced Delivery: A Dynamic
     Pickup and Delivery Problem*. Transportation Science, 53(1).
   - Alnaggar, Gzara & Bookbinder (2021) — *Crowdsourced Delivery: A Review*.
     Omega, 98.
   - Oyama (2023) — arXiv:2312.01641.

4. **Visión computacional para clasificación de objetos** — modelos de CV para
   clasificar imágenes de paquetes. Métricas: accuracy, matriz de confusión,
   análisis de sesgos por iluminación, ángulo y fondo. Directamente vinculado
   al clasificador de carga propio del proyecto.

5. **Confianza en plataformas P2P** — confianza personal (reputación) vs.
   sistémica (garantías de la plataforma: seguros, calificaciones, disputas).
   - Gruber (2020) — *Personal Trust and System Trust in the Sharing Economy*.
     Frontiers in Psychology.

6. **Modelos de cotización y pricing** — tarifa fija, por peso/distancia o
   scoring multivariable. Variables críticas: disposición a pagar del remitente
   y compensación mínima aceptable del transportista.
   - Le, Ukkusuri et al. (2021) — Transportation Research Part E, 149.

7. **UX en apps de servicios / matching** — patrones clave: cotización en pasos
   reducidos, tracking en tiempo real, flujos diferenciados por rol.
   - Cooper, Reimann & Cronin (2014) — *About Face*. Wiley.

---

### Estado del Arte

Sistematización de lo que se investigó, desarrolló y publicó sobre el problema
hasta la fecha. Describe trabajos concretos: qué hicieron, cómo, qué resultados,
qué quedó pendiente.

> Responde: *¿quién hizo qué con este problema y con qué resultado?*

**Brecha que justifica DePaso:** ninguna plataforma argentina combina modelo
híbrido (dedicado + colaborativo), clasificación de carga por IA propia y cálculo
de CO₂ para envíos entre particulares y PyMEs en el AMBA.

Competidores directos analizados: Rappi Favor, PedidosYa Envíos, DiDi Entrega,
Moova, Treggo, OCA/Andreani, Shipit.

Papers clave:
- Alnaggar et al. (2021) — Omega 98 — revisión sistemática de plataformas CSD.
- Arslan et al. (2019) — Transportation Science 53(1) — matching dinámico.
- Carbone et al. (2017) — Journal of Business Logistics — crowd logistics.
- Le & Ukkusuri et al. (2021) — TRE 149 — willingness to work como crowd-shipper.
- Oyama (2023) — arXiv:2312.01641 — matching como optimización combinatoria.
- Anónimo (2024) — arXiv:2412.20395 — mercado CSD de dos lados con elasticidad.

Dato de mercado: mercado global CSD valuado en USD 12.500M en 2023, proyectado
a USD 37.500M en 2032 (CAGR 12,5%).

---

### User Research

Proceso sistemático para comprender a los usuarios mediante técnicas empíricas.
Aporta evidencia para tomar decisiones de diseño en lugar de basarlas en supuestos.

Técnicas usadas: encuesta, entrevistas semiestructuradas, user personas.

**Encuesta** ✓ completada
- Bifurcaciones por perfil: remitente / transportista / no usuario.
- En el documento: instrumento va al Anexo; en el cuerpo van visualizaciones
  de resultados + 3–5 hallazgos accionables que impactan decisiones de diseño.

**Entrevistas** — pendiente
- Modalidad semiestructurada, mínimo 5 entrevistas de 30–45 min.
- Transcripciones al Anexo; en el cuerpo solo hallazgos sintetizados.

**User Personas** — pendiente (se construyen post encuesta + entrevistas)
- 2–3 personas: al menos una remitente y una transportista.
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