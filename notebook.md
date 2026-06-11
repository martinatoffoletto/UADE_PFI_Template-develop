1. Introducción
Objetivos
Objetivos generales: Desarrollar e implementar "DePaso", una plataforma digital de logística urbana colaborativa enfocada en el Área Metropolitana de Buenos Aires (AMBA). El sistema busca optimizar los costos logísticos y reducir la emisión de CO₂ combinando un modelo híbrido de transporte dedicado y transporte colaborativo, aprovechando la capacidad ociosa de los trayectos ciudadanos habituales.
Objetivos específicos:
Desarrollar un modelo de Inteligencia Artificial de Visión Computacional entrenado con imágenes locales para clasificar automáticamente el volumen de la carga.
Diseñar e implementar un algoritmo determinístico de scoring multivariable que empareje de manera óptima las solicitudes con los transportistas minimizando los desvíos geográficos y respetando ventanas horarias.
Integrar un módulo de cálculo en tiempo real que estime el CO₂ ahorrado frente a alternativas de viajes dedicados, utilizando los factores de emisión del IPCC.
Crear una interfaz multimodal que atienda tanto a PyMEs (fletes/mudanzas) como a particulares (envíos pequeños).
Alcance
Características del prototipo funcional: El producto mínimo viable (MVP) o prototipo funcional incluirá el registro diferenciado (multimodal) para remitentes y transportistas (peatones, ciclistas, conductores de autos, utilitarios y camiones). Contará con la carga de imágenes para clasificación automática, el motor de asignación inteligente, el seguimiento (tracking) del envío en tiempo real, el cálculo de impacto ambiental (CO₂) y el sistema bidireccional de calificaciones.
Limitaciones y exclusiones: El proyecto se restringe geográficamente a operaciones dentro del AMBA, excluyendo envíos interprovinciales o internacionales. El motor de Visión Computacional estará acotado a la clasificación volumétrica basada en el dataset entrenado (~1.500 imágenes), requiriendo ingreso manual como alternativa si el objeto no es reconocido. Los pagos y seguros sobre la mercadería podrían quedar como desarrollos para etapas posteriores a la tesis, centrándose la plataforma actual en el matching y la operación logística.
Estructura del documento: El documento se divide en: una introducción al problema logístico urbano; el marco teórico y estado del arte; la descripción funcional y el user research; la metodología técnica implementada (incluyendo el modelo de IA y el algoritmo de matching); las conclusiones del impacto del proyecto; y la bibliografía de referencia.

--------------------------------------------------------------------------------
2. Antecedentes
Marco Teórico ¿Con qué conceptos y teorías trabajamos?
Logística colaborativa y economía de plataforma: DePaso opera en un mercado de dos lados (two-sided markets), donde la plataforma conecta la demanda (remitentes) con la oferta (transportistas). Su éxito depende del efecto de red y de equilibrar la elasticidad de participación de ambos actores
,
.
Economía colaborativa (Capacidad ociosa): Se basa en el acceso sobre la propiedad. En logística, esto significa aprovechar un viaje que ya se iba a realizar para transportar carga, generando valor compartido y mitigando los impactos ambientales negativos
,
.
Crowdsourced Delivery (CSD) y flotas híbridas: Las flotas modernas se componen de vehículos dedicados (DVs) y vehículos personales compartidos (SPVs)
,
. Dentro de los SPVs, DePaso se fundamenta en la teoría de los Occasional Drivers (ODs), quienes solo aceptan solicitudes cuyo origen y destino coinciden con su ruta privada preexistente, logrando el mínimo desvío
,
.
Visión computacional para clasificación de objetos: Conceptos de entrenamiento de redes neuronales orientadas a la clasificación de volumen y peso volumétrico a partir de imágenes, evaluadas a través de métricas como accuracy, matriz de confusión y análisis de sesgos.
Modelos de cotización y emparejamiento (Matching & Pricing): La viabilidad del modelo radica en los mecanismos de subasta o scoring que minimizan el costo del desvío (detour cost) de los conductores ocasionales frente a compensaciones justas
,
. Asimismo, se aborda el concepto de task-bundling (agrupamiento de tareas múltiples) para reducir costos sub-aditivos
,
.
Estado del Arte ¿Quién hizo qué con este problema y con qué resultado?
Temas relevantes a nivel global: La investigación internacional ha avanzado significativamente en métodos matemáticos para resolver el matching masivo entre paquetes y conductores, utilizando heurísticas de descomposición
,
, mecanismos basados en subastas VCG
,
, e Inteligencia Artificial (DQN) para programar turnos y gestionar flotas
,
. Sin embargo, la academia teórica asume por defecto que las cargas son cajas homogéneas y ha descubierto que, si no se controla bien el desvío, la logística colaborativa puede llegar a aumentar las emisiones de carbono totales
,
.
Temas relevantes a nivel local (AMBA): Localmente, operan plataformas de "economía gig" (Rappi, PedidosYa, Glovo) que, de acuerdo con la Organización Internacional del Trabajo, funcionan en la práctica como empleos de tiempo completo no reconocidos, imponiendo ritmos de trabajo extenuantes bajo sistemas de puntaje punitivos y orientados solo a paquetería ligera y comida
,
.
Brecha que justifica DePaso (Conclusión de la sección): DePaso innova rompiendo este esquema al crear una verdadera plataforma híbrida que combina vehículos dedicados (fletes PyME) con verdaderos conductores ocasionales colaborativos, sin requerir exclusividad. Además, supera las limitaciones teóricas del estado del arte internacional al introducir clasificación de carga heterogénea por IA propia y un módulo de cálculo directo de CO₂ ahorrado comparado contra la huella de viajes dedicados.

--------------------------------------------------------------------------------
3. Descripción
User Research (Esta sección demuestra que el problema está validado en la realidad)
Encuesta sobre movilidad y logística (✓ completada, Microsoft Forms, 22-may-2026): 145 respuestas completas, 133 (91,7%) del AMBA. Resultados clave (bases por bifurcación: uso n=116, transportista n=98): 69,8% de predisposición al modelo colaborativo; 84,5% de interés en transportar en su ruta habitual; la motivación dominante es generar un ingreso extra sin desviarse de la rutina (91,8%); el costo es el principal criterio de elección (75,0%) y la responsabilidad por daños la principal preocupación (73,4%). El rango WTP ($3.000–6.000, 68,1%) se superpone con el WTA ($2.500–5.000, 51,0%), dejando margen operativo.
User Personas (3 preliminares construidas a partir de la encuesta; se refinarán a medida que se amplíe la muestra):
Juan (Dueño de PyME, Lanús): Necesita enviar mercadería mediana/voluminosa de forma económica sin pagar un flete exclusivo vacío.
María (Conductora colaborativa, Caballito→Microcentro): Hace el trayecto en auto todos los días; busca monetizar el espacio vacío en el baúl aceptando solo pedidos que le queden de paso.
Carlos (Fletero dedicado, Quilmes): Tiene un camión de mudanzas y busca optimizar sus horas de trabajo recibiendo alertas estructuradas de mudanzas o cargas grandes.

--------------------------------------------------------------------------------
4. Metodología de desarrollo
Metodología El desarrollo del proyecto se ejecutó utilizando metodologías ágiles (Scrum / Kanban), ideales para plataformas de dos lados donde las iteraciones de la interfaz de usuario y las mejoras en el algoritmo de matching requieren pruebas incrementales y adaptación rápida.
Arquitectura y tecnologías utilizadas
Frontend (Aplicación/Web): Interfaz fluida con registro multimodal y flujos diferenciados por rol (Remitente / Transportista). Acceso a cámara para captura de imágenes del paquete.
Backend & Algoritmo de Matching: Implementación de un algoritmo de scoring multivariable determinístico. Este motor procesa compatibilidad geoespacial, cruce de rutas (minimización de desvío), tipo de carga, reputación de las partes y ventanas horarias.
Módulo de Inteligencia Artificial (Computer Vision): Entrenamiento de un clasificador de carga propio utilizando un dataset de ~1.500 imágenes (combinando Google Open Images y fotografías propias de objetos de referencia argentinos). Se implementaron modelos de clasificación de imágenes evaluados bajo métricas de accuracy y matriz de confusión, mitigando sesgos de iluminación, ángulo y fondo.
Módulo de Sostenibilidad: Integración de cálculos ambientales paramétricos utilizando los factores de emisión del IPCC (Intergovernmental Panel on Climate Change) para contrastar el trayecto del conductor ocasional vs. el trayecto que habría hecho un vehículo dedicado exclusivamente a esa tarea.
Validación del sistema Se realizaron pruebas unitarias e integrales del flujo completo:
Validación de IA: Prueba del modelo de visión computacional con imágenes fuera del dataset de entrenamiento para confirmar su robustez al categorizar un paquete en las 4 dimensiones (pequeño/documento, mediano, grande, mudanza).
Validación del Matching: Simulaciones de rutas en el mapa del AMBA demostrando que el algoritmo determinístico asigna efectivamente a un Occasional Driver solo cuando el desvío es menor al umbral estipulado, prefiriendo la modalidad "Dedicada" cuando los parámetros de carga lo requieren.

--------------------------------------------------------------------------------
5. Conclusión general
"DePaso" emerge como una solución tecnológica y organizativa innovadora que aborda simultáneamente las ineficiencias de la logística urbana y las problemáticas de la actual economía de plataformas en Argentina. Mientras que el mercado actual se basa en un modelo precarizado y exclusivo de transporte dedicado
,
, DePaso materializa los últimos avances teóricos en logística (Crowdsourced Delivery y flotas híbridas
,
), demostrando que es posible aprovechar la capacidad ociosa de viajes rutinarios para reducir los costos logísticos de PyMEs y particulares. Al integrar un modelo de clasificación de carga por Inteligencia Artificial entrenado con datos locales y medir de forma transparente el ahorro en la huella de carbono, el proyecto no solo mejora la eficiencia técnica de la última milla, sino que propone un ecosistema digital más justo, rentable y ecológicamente sostenible para el AMBA.

--------------------------------------------------------------------------------
6. Bibliografía
(Aquí colocarás el formato requerido por tu universidad, ej. APA, IEEE. Te presento los datos estructurados):
Alnaggar, A., Gzara, F., & Bookbinder, J. H. (2021). Crowdsourced Delivery: A Review. Omega, 98.
Arslan, A. M., Agatz, N., Kroon, L., & Zuidwijk, R. (2019). Crowdsourced Delivery: A Dynamic Pickup and Delivery Problem. Transportation Science, 53(1).
Botsman, R., & Rogers, R. (2010). Beyond Zipcar: Collaborative Consumption. Harvard Business Review.
Hagiu, A., & Wright, J. (2015). Multi-Sided Platforms. Harvard Business School.
Luy, J., Hiermann, G., & Schiffer, M. (2023). Strategic Workforce Planning in Crowdsourced Delivery with Hybrid Driver Fleets. Technical University of Munich.
Akamatsu, T., & Oyama, Y. (2023). A fluid-particle decomposition approach to matching market design for crowdsourced delivery systems. arXiv:2312.01641.
Oyama, Y., & Akamatsu, T. (2024). A market-based efficient matching mechanism for crowdsourced delivery systems with demand/supply elasticities. arXiv:2412.20395.
Organización Internacional del Trabajo (OIT). (2020). El trabajo en las plataformas digitales de reparto en Argentina: Análisis y recomendaciones de política. Oficina de País de la OIT para Argentina.
Saleh, Z., Al Hanbali, A., & Baubaid, A. (2024). Enhancing Courier Scheduling in Crowdsourced Last-Mile Delivery through Dynamic Shift Extensions: A Deep Reinforcement Learning Approach. King Fahd University.
Yang, D., Hyland, M. F., & Jayakrishnan, R. (2022). Tackling the Crowdsourced Shared-Trip Delivery Problem at Scale with a Novel Decomposition Heuristic. University of California-Irvine.


Parte 1: Resúmenes y Citas de los 6 Documentos para DePaso
1. Yang et al. (2022) - "Tackling the Crowdsourced Shared-Trip Delivery Problem at Scale..."
Resumen: Resuelve el problema de enrutamiento para una flota híbrida a gran escala (vehículos dedicados y vehículos personales compartidos que se desvían de su ruta). Propone un algoritmo heurístico que asigna eficientemente los pedidos y reduce costos, aunque advierte que un mal emparejamiento puede aumentar las millas recorridas y el CO₂.
Cita clave para DePaso: "The CSD problem involves dedicated vehicles (DVs) and shared personal vehicles (SPVs) fulfilling delivery orders, wherein the SPVs have their own trip origins and destinations."
.
2. Luy et al. (2023) - "Strategic Workforce Planning in Crowdsourced Delivery with Hybrid Driver Fleets"
Resumen: Estudia la planificación de una flota híbrida a largo plazo. Distingue teóricamente entre "Gigworkers" (trabajan a tiempo completo para la app) y "Occasional Drivers" (conductores ocasionales que solo aceptan pedidos que coinciden con su ruta personal). Demuestra que anticipar la oferta de conductores ahorra hasta un 19% en costos.
Cita clave para DePaso: "We consider two types of CDs, gigworkers (GWs) and occasional drivers (ODs)... ODs only serve requests whose origin and destination coincide with their own private route’s origin and destination."
.
3. Akamatsu & Oyama (2023) - "A fluid-particle decomposition approach to matching market design..."
Resumen: Aborda el "matching" como un problema de diseño de mercado. Propone un mecanismo de subastas para emparejar tareas con conductores según su costo real de desvío, maximizando el beneficio social y reduciendo emisiones al usar capacidad ociosa.
Cita clave para DePaso: "We consider a crowdsourced delivery (CSD) system that effectively utilizes the existing trips to fulfill parcel delivery as a matching problem between CSD drivers and delivery tasks."
.
4. Saleh et al. (2024) - "Enhancing Courier Scheduling... A Deep Reinforcement Learning Approach"
Resumen: Utiliza Inteligencia Artificial (Deep Q-Network) para la asignación dinámica de turnos. Equilibra el uso de "repartidores comprometidos" (dedicados) y "ocasionales", maximizando la ganancia de la plataforma frente a picos de demanda.
Cita clave para DePaso: "The primary objective is to maximize the platform’s profit over the course of the day by efficiently matching couriers with customer requests."
.
5. Oyama & Akamatsu (2024) - "A market-based efficient matching mechanism... with demand/supply elasticities"
Resumen: Modela un mercado CSD de dos lados (remitentes y conductores) considerando la elasticidad de la demanda/oferta y el task-bundling (agrupamiento de tareas). Transforma el problema en un modelo de asignación de tráfico, resolviéndolo 700 veces más rápido que métodos tradicionales.
Cita clave para DePaso: "This paper presents a general formulation of a larege-scale two-sided CSD matching problem, considering demand/supply elasticity, heterogeneous preferences of both shippers and drivers, and task-bundling."
.
6. Organización Internacional del Trabajo (2020) - "El trabajo en las plataformas digitales de reparto en Argentina..."
Resumen: Analiza la realidad del AMBA con plataformas como Rappi y PedidosYa. Denuncia que el modelo actual impone ritmos extenuantes disfrazados de flexibilidad, controlando a los repartidores mediante sistemas de puntaje punitivos.
Cita clave para DePaso (Original en español): "Para poder acceder a los mejores horarios, pedidos y promociones que permiten generar un ingreso mensual considerado suficiente, los trabajadores mantienen un ritmo de trabajo extenuante."
.