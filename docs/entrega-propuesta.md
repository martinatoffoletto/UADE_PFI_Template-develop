# Entrega Propuesta (0%) — DePaso

Documento de definición de la **propuesta del PFI**. Reúne en un solo lugar: (A) la
descripción del proyecto propuesto, (B) los objetivos, alcance y recursos, y (C) la
estructura documental que sustentas la propuesta.

> Este documento **es la Introducción del trabajo final**. Las secciones posteriores
> (Antecedentes, User Research, etc.) constituyen las entregas del 25 % y adelante.

Documento general del proyecto: ver [`../CLAUDE.md`](../CLAUDE.md).

---

## Parte A — Definición del Proyecto

### Datos Administrativos

| Campo | Valor |
|---|---|
| **Título** | DePaso: plataforma digital de logística urbana colaborativa con IA para la zona del AMBA |
| **Tipo de Proyecto** | Desarrollo |
| **Entrega** | 25/4/2026 |
| **Duración estimada** | Diciembre de 2026 |
| **Alumnas** | Toffoletto, Martina Ornella (LU 1139965); Basaez, Candela Pilar (LU 1134260) |
| **Carrera** | Ingeniería en Informática — UADE FICE |
| **Tutor** | Dos Santos, Maximiliano Luis |
| **Alcance de usuarios** | +100.000 usuarios potenciales en el AMBA (~15M habitantes) |

### Qué es DePaso

DePaso es una **plataforma digital de logística urbana colaborativa** para el AMBA, orientada a
PyMEs, comercios y clientes particulares. Gestiona el ciclo completo del envío: solicitud,
clasificación de la carga, asignación del transportista, seguimiento e impacto ambiental.

**Diferenciador clave:** A diferencia de Rappi Favor, PedidosYa Envíos y DiDi Entrega —que
operan bajo un modelo exclusivo de transporte dedicado— DePaso introduce un **modelo híbrido**
que combina:
- **Transporte dedicado** (tipo flete): operadores completos con vehículos especializados.
- **Transporte colaborativo**: transportistas que aprovechan su ruta habitual, aceptando
  pedidos compatibles sin desvíos significativos.

Esto permite capitalizar la **capacidad ociosa de desplazamientos ya existentes**, mediante
matching con el mínimo desvío.

### Problemas que se resuelven

1. **Costos logísticos elevados** para PyMEs y comercios sin flota propia.
2. **Vehículos circulando con espacio disponible** sin aprovechamiento.
3. **Baja eficiencia en la última milla** en entornos urbanos densos.
4. **Alta emisión de CO₂** por viajes dedicados innecesarios.
5. **Falta de ingresos** para personas que realizan trayectos cotidianos.

---

## Parte B — Objetivo, Alcance y Recursos

### 1. Objetivo General

Desarrollar un **prototipo funcional de plataforma de logística urbana colaborativa** para el
AMBA para diciembre de 2026 que, mediante IA y matching inteligente, aproveche la capacidad
ociosa de desplazamientos.

**Objetivos específicos:**
- Entrenar un modelo de visión computacional para clasificar cargas.
- Implementar matching por trayectorias reales.
- Calcular el CO₂ ahorrado por envío.
- Habilitar modalidades dedicada y colaborativa.

### 2. Alcance

Diseño y desarrollo de un **prototipo funcional de plataforma digital (PWA/app móvil)** para
la gestión logística de envíos en el AMBA (~15M habitantes), con alcance potencial superior a
100.000 usuarios.

**Funcionalidades incluidas:**
- Registro de usuarios y transportistas multimodales (peatón, bicicleta, auto, utilitario, camión).
- Carga de solicitudes con imágenes.
- Clasificación automática de carga mediante modelo de IA entrenado por el equipo, con ingreso
  manual alternativo.
- Asignación inteligente por trayectorias geoespaciales.
- Gestión de capacidad en tiempo real.
- Cálculo de CO₂ ahorrado.
- Panel de monitoreo operativo.

### 3. Modalidades de Envío

#### Dedicada
Se asigna un transportista completo al envío según el tipo de carga. Fletes y mudanzas van a
quienes disponen de camioneta o camión.

#### Colaborativa
El transportista registra su ruta habitual y recibe pedidos compatibles sin desvíos
significativos. Pueden participar con cualquier movilidad (auto, moto, bicicleta o a pie;
las dos últimas habilitadas solo para paquetes pequeños y documentos en trayectos cortos).

### 4. Tipos de Paquete

- Pequeños y documentos
- Medianos
- Grandes/voluminosos
- Mudanzas/fletes

### 5. Componente de Inteligencia Artificial

El proyecto incorpora IA como componente central mediante un modelo propio entrenado por el
equipo, documentando dataset, arquitectura, métricas, validación y análisis de sesgos.

**Funcionalidades IA:**

#### Clasificador de tamaño de carga (Visión Computacional)
Modelo entrenado con dataset construido a partir de imágenes públicas seleccionadas y
etiquetadas (~1.500 imágenes de Google Open Images + fotos propias de objetos argentinos).
Admite la selección de un objeto de referencia opcional e ingreso manual como alternativa.
Se evalúa con accuracy, matriz de confusión y análisis de sesgos por iluminación, ángulo y
fondo.

#### Asignación inteligente de envíos
Algoritmo de scoring multivariable determinístico que combina:
- Compatibilidad geoespacial
- Desvío
- Tipo de carga
- Reputación del transportista
- Ventana horaria

#### Cálculo de CO₂ ahorrado
Compara el escenario real (envío colaborativo) contra el viaje dedicado basándose en
factores IPCC.

#### Gestión de capacidad disponible
Actualiza en tiempo real el volumen libre con el que dispone el transportista.

### 6. Recursos y Stack Tecnológico

**Infraestructura:**
- Equipos personales del equipo dedicados al proyecto.
- Infraestructura en la nube.
- Herramientas open source.

**Stack de desarrollo:**
- **Backend:** Python + FastAPI
- **Frontend/Móvil:** React Native + Expo
- **Base de Datos:** PostgreSQL + PostGIS (cloud)
- **IA/ML:** Frameworks de machine learning con GPU en la nube
- **Datos Geoespaciales:** OpenStreetMap / datos de calles AMBA
- **Diseño:** Figma
- **Control de versiones:** Git / GitHub

### 7. Presupuesto Estimado

| Insumo | Descripción | Cantidad | Costo Estimado |
|---|---|---|---|
| Equipos de desarrollo | Computadoras dedicadas para el equipo | 2 | 0 USD |
| GPU en la nube | Entrenamiento del modelo de IA en la nube | 1 x 8 meses | 20 USD |
| Base de Datos en la nube | PostgreSQL + PostGIS hosteada | 1 x 8 meses | 50 USD |
| Hosting del backend FastAPI | Hosting del backend durante el desarrollo | 1 x 8 meses | 15 USD |
| Datos geoespaciales | Datos de calles y ruteo del AMBA | 1 | 0 USD |
| Dataset de imágenes | Google Open Images + fotos propias | ~1.500 imgs | 0 USD |
| Frameworks de IA | Frameworks de ML para entrenamiento | 1 | 0 USD |
| Git/GitHub | Control de versiones y gestión del repo | 1 | 0 USD |
| Figma | Diseño de interfaces y prototipado | 1 | 0 USD |
| Copilot IA (Student Plan) | Asistente de IA como apoyo | 1 x 8 meses | 0 USD |
| **Total Presupuesto** | | | **85 USD** |

**Observación:** El presupuesto es acotado y cubierto por el equipo. No se requieren
laboratorios, equipamiento especializado ni fuentes externas de financiamiento.

---

## Parte C — Estructura Documental de la Propuesta

> La propuesta se estructura en torno a la pregunta central: **¿Por qué este proyecto es
> necesario y viable?**

### 1. Introducción — Definición del Proyecto *(esta sección)*

- Qué es DePaso y cuál es su diferenciador.
- Problemas concretos que resuelve.
- Objetivos y alcance funcional.
- Stack tecnológico y presupuesto.

### 2. Antecedentes *(entrega 25%)*

**Marco Teórico:** conceptos y teorías que sustentan el proyecto.
- Crowdsourced delivery y logística de última milla.
- Flotas híbridas y el problema del desvío.
- Perfiles de conductores: gig-workers vs. occasional drivers.
- Diseño de mercados de matching y asignación.
- Visión computacional y aprendizaje por transferencia.

**Estado del Arte:** qué han hecho otros y dónde está la brecha.
- Métodos académicos para matching masivo.
- Plataformas locales de economía gig (Rappi, PedidosYa, etc.).
- Análisis comparativo con competencia directa.
- Conclusión: diferencial de DePaso.

### 3. Descripción — User Research *(entrega 25%)*

- Encuesta cuantitativa (Microsoft Forms, 145 respuestas, 133 del AMBA).
- Hallazgos clave sobre predisposición colaborativa, WTP, WTA, preocupaciones.
- User Personas preliminares (remitente PyME, transportista colaborativa, fletero dedicado).

### 4. Metodología de Desarrollo *(anticipa 50%)*

- Enfoque ágil (Scrum/Kanban).
- Arquitectura de backend (algoritmo de scoring).
- Módulo de visión computacional (dataset, validación, sesgos).
- Módulo de sostenibilidad (cálculo de CO₂).
- Plan de pruebas (unitarias, integrales, UAT).

### 5. Cronograma y Planificación *(anticipa 25%-100%)*

- Diagrama de Gantt (hitos: 25 % Definición, 50 % Desarrollo, 75 % Validación, 100 % Defensa).
- Justificación de desvíos temporales.

### 6. Conclusión General *(anticipa 100%)*

DePaso aborda simultáneamente las ineficiencias de la logística urbana y las problemáticas
de la economía de plataformas en Argentina, materializando los avances académicos en
crowdsourced delivery y flotas híbridas en un prototipo funcional con clasificación de
carga por IA local y medición transparente de la huella de carbono.

### 7. Bibliografía

Gestionada en [`../biblio.bib`](../biblio.bib) (BibTeX, backend biber, norma ISO 690-2010).
Se actualizará a medida que avance la investigación.

---

## Roles de Usuario

### Remitente
- PyME, comercio o particular que necesita enviar una encomienda.
- Publica el envío, recibe una cotización y elige entre las modalidades disponibles.

### Transportista
- Persona que registra su ruta habitual y recibe pedidos compatibles con su recorrido sin
  desvíos significativos.
- No es repartidor de tiempo completo: aprovecha un viaje que ya iba a hacer.
- Puede participar con cualquier movilidad (auto, moto, bicicleta, a pie, utilitario o camión).

**Nota:** Un mismo usuario puede operar en ambos roles.

---

## Referencias y Documentación Complementaria

- **Documento técnico detallado:** [`proy.txt`](proy.txt)
- **Datos crudos de la encuesta:** [`encuesta/`](encuesta/)
- **Bibliografía:** [`../biblio.bib`](../biblio.bib)
- **Proyecto general:** [`../CLAUDE.md`](../CLAUDE.md)
