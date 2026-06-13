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
- Figuras en `figures/`, bibliografía en `biblio.bib` (BibTeX, backend biber)
- Citas con `\parencite{}`, norma ISO 690-2010 (estilo iso-numeric)
- **El stack tecnológico NO se menciona en el documento del 25%** (decisión de
  las autoras: no condicionarse antes de avanzar el desarrollo). No nombrar
  frameworks/BD concretos en el documento; se definirá en el Cap. 4 (entrega 50%).
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

Técnicas usadas: encuesta (permanece abierta) y user personas. **No se realizan
entrevistas** — no reintroducirlas en el documento.

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