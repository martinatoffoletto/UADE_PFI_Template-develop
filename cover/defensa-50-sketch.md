# Presentación entrega 50% — DePaso

Sketch de la exposición oral. Esto NO es el deck final: es el guion — qué va en
cada lámina, cuánto dura, qué se dice y qué se demuestra en vivo. El deck vive
en el canvas de Claude Design; el guion hablado, en `defensa-50-speech.md`.

**Restricción real:** 10–15 min de exposición (ideal 10, tope 15) **incluyendo
la demo**, + 5 min de preguntas/feedback. Esto es más corto que los 15–20 min
del material genérico de la cátedra (que describe la defensa final completa),
así que el guion de abajo comprime los 5 bloques oficiales en lo que el tutor
pidió puntualmente para esta entrega: storytelling (problema → validación →
propuesta + diferencial + target → cronograma), 7–12 slides, una sola lámina
de arquitectura.

---

## Presupuesto de tiempo (objetivo: 10 min, buffer hasta 15)

| Bloque | Slides | Minutos |
|---|---|---|
| Apertura (equipo + problema) | 1–2 | 1,5 |
| Validación (user research) | 1 | 1,5 |
| Propuesta + diferencial + target | 2 | 2,0 |
| Arquitectura | 1 | 1,0 |
| **Demo en vivo** | 1 (transición) | 3,0–3,5 |
| Cronograma + cierre | 2 | 1,5 |
| **Total** | **9 slides** | **≈ 10,5–11 min** |

Deja 4 min de margen contra el tope de 15 sin tocar nada — si algo se
extiende (una pregunta espontánea del tribunal a mitad de la demo, por
ejemplo) hay colchón. No estirar la teoría para llenar tiempo: si van
sobrando minutos, se los regalan a la demo o a las preguntas.

---

## Lo que gana a un jurado de ingeniería (leer antes de ensayar)

Cuatro cosas, en orden de peso. Todo el guion está construido sobre ellas:

1. **Trazabilidad.** Que cada decisión de diseño tenga una evidencia detrás,
   y que ustedes la nombren. No "elegimos 15% de desvío", sino "el 15% sale
   de las entrevistas y del paper de Yang". Un jurado perdona que algo no
   esté hecho; no perdona que algo esté hecho porque sí.
2. **Anticipar la objeción.** Decir ustedes la debilidad antes de que la
   pregunten desarma la pregunta y suma criterio. Las tres que conviene
   plantar solas: el clasificador está en entrenamiento, el pago es simulado
   y la muestra es exploratoria.
3. **Método por encima de resultado.** El hallazgo del etiquetado del dataset
   (ver Q&A) vale más que un *accuracy* alto: muestra que el problema se
   detectó **midiendo**, no que salió bien de casualidad.
4. **Que funcione de verdad.** Treinta segundos de Swagger o de `pytest`
   corriendo en vivo responden, sin decirlo, la pregunta que todo jurado
   técnico se hace: *¿esto es una maqueta de Figma?*

### Tabla de trazabilidad — evidencia → decisión

Tenerla en la cabeza, no en una lámina. Es la munición para las preguntas.

| Evidencia | Decisión de diseño |
|---|---|
| E5 y encuesta: 91,8% se motiva por ingreso extra **sin desviarse** | Desvío ≤ 15% como **filtro duro**, no como preferencia |
| Entrevistas: sin seguimiento no adoptan la app | Subsistema de tracking (RF-TRK) en el alcance del MVP |
| E5 teme la acusación falsa; 73,4% teme responder por daños | **Foto obligatoria** del paquete como constancia del estado |
| Encuesta: 75% elige por costo | Precio **siempre visible antes de confirmar**, sin cargos ocultos |
| Yang et al. (2024): un desvío excesivo borra el beneficio ambiental | El desvío es variable explícita del *matching*, no un extra |
| Naumann et al. (2023): estimar volumen exacto desde una foto es inviable | Se clasifica en **categorías**, no se mide el volumen |
| Presupuesto de 85 USD, equipo de 2 | Monolito modular; sin microservicios, sin PostGIS, sin broker |

---

## Slide por slide

Regla 6x6 en todas: máximo 6 líneas, 6 palabras por línea. Lo que sigue en
"contenido" es lo que va escrito en la lámina; "se dice" es el guion hablado
— no son lo mismo, la lámina apoya, no lee.

### 1 — Portada (10 s)
- **Contenido:** DePaso — logística urbana colaborativa · Toffoletto, M. ·
  Basaez, C. · Tutor: Dos Santos, M. · UADE, entrega 50%
- **Se dice:** nombres, tutor, una frase de qué es DePaso. Nada más — la
  regla de los 3 segundos de pausa antes de arrancar va acá.
- **Visual:** logo/nombre grande, colores de marca DePaso (forest/emerald
  sobre crema — acá SÍ tiene sentido usar la paleta de la app, es un slide
  de marca, no una figura de datos académica).

### 2 — El problema (60–75 s) · *tres problemas, no dos*
- **Contenido:** tres tarjetas + tres cifras.
  1. **Juan** · PyME de repuestos en Lanús — paga un flete entero por una caja.
  2. **Clara** · Caballito → Microcentro — hace ese viaje todos los días con
     el baúl vacío.
  3. **El mercado · dedicado o nada** — las apps de mensajería solo llevan
     paquetes chicos y siempre con viaje dedicado; los fletes y las mudanzas
     quedan afuera. **No existe una opción híbrida.**
  Cifras: 44% (costo de envío como barrera, ICC 2024) · 22% (suba de costos
  logísticos, 1.º semestre 2026) · 14% (participación del transporte en las
  emisiones del país).
- **Se dice:** el problema **no es solo el costo ni el espacio ocioso**: es
  que hoy no hay dónde juntarlos. Ese tercer punto es el que justifica que el
  proyecto exista, así que se dice explícito, no se insinúa. Arrancar por
  Juan (persona concreta) antes que por los números — el dato refuerza, no
  abre. Pausa después de cada cifra.
- **Visual:** las dos primeras tarjetas son personas y van con relleno; la
  tercera es una **ausencia** y va dibujada distinto (borde punteado, sin
  relleno). Esa diferencia visual es deliberada: comunica que no es un
  tercer personaje sino el hueco del mercado.
- **Respaldo en el informe:** §2.2 — *"no contemplan cargas medianas, grandes
  ni mudanzas"* y *"ninguna cubre el nicho híbrido colaborativo"*. Si el
  jurado lo pregunta, está citado y con fuente.

### 3 — Cómo lo validamos (60–90 s)
- **Contenido:** encuesta, 145 respuestas, AMBA · 69,8% predispuesto al
  modelo colaborativo · 84,5% interesado en transportar · + 5 entrevistas
- **Se dice:** no es un estudio de mercado completo, es exploratorio — decir
  eso explícitamente transmite rigor, no debilidad. Dos hallazgos concretos,
  no "hicimos entrevistas": el desvío como filtro duro y el seguimiento como
  condición de adopción. **Y un tercero que conviene contar porque demuestra
  que la investigación sirvió para algo:** las entrevistas hicieron
  **cambiar un requerimiento**. Un transportista contó que su miedo no es
  romper algo, es que lo **acusen** de haberlo roto; de ahí salió que la
  fotografía del paquete pasara a ser **obligatoria**, como constancia del
  estado en que se despachó. Investigación → requerimiento, en una frase.
- **Visual:** la Figura 3.1 del informe (barras demanda/oferta) sirve tal
  cual, ya está en gris neutro y pensada para leerse en 5 segundos.

### 4 — Qué es DePaso (45–60 s)
- **Contenido:** modelo híbrido: dedicado + colaborativo · el colaborativo
  aprovecha un viaje que el transportista ya iba a hacer · desvío acotado
  al 15%
- **Se dice:** la frase ancla es "no creamos viajes nuevos, aprovechamos los
  que ya existen". Esa frase sola vale más que cualquier bullet. Cerrar
  atando con el slide 2: la modalidad dedicada es **la que cubre fletes y
  mudanzas** — el hueco que se acaba de mostrar.
- **Visual:** un esquema simple de dos cajas (Dedicado / Colaborativo), no
  el diagrama técnico — ese va en la lámina de arquitectura.

### 5 — Diferencial + target (60–75 s)
- **Contenido:** target: PyMEs y particulares del AMBA sin flota propia ·
  diferencial: modelo híbrido + clasificación de carga por IA propia +
  cálculo de CO₂ por envío · ningún competidor local combina los tres
- **Se dice:** nombrar 2-3 competidores (Rappi Favor, PedidosYa Envíos) y
  decir en una frase por qué DePaso no compite por escala sino por el
  segmento que hoy queda afuera por precio. Esto viene directo del capítulo
  de análisis competitivo (Porter + FODA) — no hace falta mostrar esas
  tablas, alcanza con la conclusión.
- **Visual:** un cuadro comparativo mínimo (3 columnas: DePaso / Rappi Favor
  / PedidosYa Envíos, 3 filas: modelo, IA propia, CO₂) — no la Tabla 2.I
  completa del informe, es demasiado densa para pantalla.

### 6 — Arquitectura (60 s) · *la única lámina técnica*
- **Contenido:** app móvil + panel web —**HTTPS**→ **API REST (FastAPI)** con
  sus **11 módulos de dominio** a la vista, y los **tres diferenciales
  resaltados** (matching · visión · CO₂) · a la derecha, lo que la API usa:
  PostgreSQL, almacenamiento de objetos para las fotos, y ruteo OSRM
  **externo y reemplazable** (punteado) · el modelo de IA corre en memoria
  dentro de la API.
- **Se dice:** una frase por caja, no leer el diagrama. El movimiento clave
  es **señalar los tres módulos verdes**: ahí están los tres pilares del
  proyecto, y se ve que no son un agregado sino parte de la arquitectura.
  Cerrar con la decisión que más defiende el proyecto: "monolito modular, no
  microservicios — con 85 dólares y dos personas la complejidad distribuida
  no se justifica, **pero los once módulos ya están separados por dominio**:
  si mañana hay que extraer uno como servicio, el límite ya está trazado".
  Esa frase responde de antemano una pregunta típica del jurado.
- **Visual:** los once módulos se muestran **como chips dentro de la caja de
  la API**. Es el punto entero de la lámina: si el título dice "monolito
  **modular**" y el dibujo muestra una caja opaca, el diagrama contradice al
  título. La etiqueta **HTTPS** se deja a propósito — la rúbrica pide
  "protocolos que son clave en la tesis", y es lo que permite contestar la
  pregunta de seguridad sin abrir otra lámina.

### 7 — Demo en vivo (transición, 5 s de slide + 3–3,5 min de demo real)
- **Contenido:** "Demo" y nada más, o una captura de pantalla como fondo.
- **Qué mostrar (ver sección Demo abajo).**

### 8 — Resultados / avance (30–45 s, puede fusionarse con el cierre de la demo)
- **Contenido:** 176 pruebas automatizadas corriendo · backend con 11 módulos
  funcionando · app móvil y panel web sobre la misma API
- **Se dice:** **no dar cifras de accuracy** — el clasificador está en
  entrenamiento y el dataset se está reconstruyendo desde cero (v3, por
  dimensiones reales). El informe tampoco declara resultados del modelo: dice
  "módulo integrado a la API, con el modelo en desarrollo", y la exposición
  tiene que decir exactamente lo mismo. Si el tribunal pregunta, ver la tabla
  de preguntas difíciles: el hallazgo del etiquetado es mejor respuesta que
  un número.
- **Visual:** si el tiempo aprieta, este slide se saca y el dato se dice
  hablado durante la demo, mostrando el Swagger o la corrida de pytest en
  vivo en vez de una captura.

### 9 — Cronograma + cierre (60–75 s)
- **Contenido:** hitos hasta diciembre 2026 (dataset ampliado, integración,
  validación con usuarios, informe final) · gracias, abiertas a preguntas
- **Se dice:** cerrar con una frase, no con "eso es todo". Algo como
  "la próxima entrega ya tiene el modelo completo y usuarios reales
  probando el prototipo" — deja al jurado con la sensación de que hay
  continuidad, no que el proyecto termina acá.
- **Visual:** una línea de tiempo horizontal simple, 4 hitos, sin fechas
  exactas de cada tarea (eso está en el Anexo A del informe si preguntan).

**Total: 9 slides**, dentro del rango 7–12 que pidió el tutor.

---

## La demo — qué mostrar

No está todo implementado, así que hay que elegir. Recomendación, de mayor
a menor prioridad si el tiempo aprieta:

1. **Flujo del remitente en vivo** (prioridad alta): sacar/subir una foto
   de un paquete → ver la clasificación automática → ver la cotización con
   las tres tarifas y el CO₂ estimado. Es el flujo más terminado, es el que
   tiene mockups reales en el informe (Figuras 5.6), y es el que mejor
   cuenta la historia de los tres pilares del proyecto (IA + matching +
   CO₂) en 90 segundos.
   - Al sacar la foto, decir en media frase que **la fotografía es
     obligatoria**: además de alimentar la clasificación, queda como
     constancia del estado en que se despachó el paquete. Es el requerimiento
     que salió de las entrevistas (slide 3) — cerrar ese círculo en vivo vale
     mucho.
   - Si el clasificador propone una categoría equivocada, **no taparlo**:
     corregirla a mano delante del jurado y decir "propone, no impone". Un
     error asumido y resuelto en pantalla comunica más solidez que un acierto.
2. **Backend real, no simulado** (prioridad media, 30–45 s): abrir
   `/api/v1/docs` (Swagger) y mostrar 2-3 endpoints reales, o correr
   `pytest` en vivo y que el jurado vea las 176 pruebas pasar. Esto
   responde de antemano "¿esto es un mock de Figma o funciona de verdad?".
3. **Feed del transportista** (prioridad baja, si sobra tiempo): mostrar
   una oferta entrante con el desvío y la ganancia calculados.

**No mostrar:** flujos de pago (está **simulado**: no hay pasarela ni fondos,
solo el estado del envío cambia de pendiente a abonado), calificación
bidireccional (especificada en el informe, todavía no implementada — ver
Q&A), nada del panel de administración salvo que pregunten específicamente.

**Plan B, obligatorio:** grabar un video corto (60–90 s) del flujo del
remitente ANTES de la defensa, como backup. El wifi de la facultad o el
backend en la nube pueden fallar en el peor momento — es lo que dice la
sección de logística: "prueben todo antes, la familiaridad reduce la
ansiedad a la mitad". Si el video de backup está listo, esa ansiedad baja
más todavía: si algo falla en vivo, no se pierde la demo entera.

---

## Diseño visual (deck)

- **Paleta:** la de la app (forest `#0B3B2E`, emerald `#10B981`, ámbar
  `#E89E2A`, crema de fondo `#F4EFE3`). A diferencia del gráfico del informe
  académico (que se hizo en gris neutro a propósito), acá SÍ es una
  presentación de marca — usar los colores de DePaso ayuda a que el jurado la
  asocie con el producto real.
- Tipografía: Newsreader para títulos, Manrope para texto. Mínimo 24 pt
  texto / 36 pt títulos, alto contraste.
- Una idea por lámina. Si un slide de este sketch tiene dos ideas al
  ejecutarlo, se separa en dos.
- Regla de los 5 segundos en cualquier diagrama: si el jurado necesita que
  se lo expliquen para entender qué mira, hay que simplificarlo más.
- **El punteado significa siempre lo mismo** en todo el deck: algo que no
  está o que es reemplazable (el hueco del mercado en el slide 2, el ruteo
  externo en el slide 6). Mantener esa convención — un lenguaje visual
  consistente se lee sin explicación.
- Dejar aire: no llenar el espacio vacío con logos o decoración de relleno.

---

## Entrega y voz (resumen accionable, no la teoría completa)

- 3 segundos de pausa antes de arrancar: parar, respirar, mirar al
  tribunal, sonreír, recién ahí hablar.
- Pies al ancho de hombros, manos entre cintura y pecho, palmas hacia
  arriba cuando se explica algo. Nada de brazos cruzados ni manos en los
  bolsillos.
- Mirada en "W" por la sala; sostener 3–5 segundos por persona antes de
  cambiar.
- Ritmo ~130–150 palabras/minuto. Pausa antes de decir una cifra clave,
  pausa después para que se procese.
- Practicar en voz alta para detectar muletillas propias ("eh", "o sea",
  "tipo") y reemplazarlas por silencio.
- Ensayar juntas al menos 5 veces, con cronómetro — el presupuesto de
  tiempo de arriba solo sirve si se prueba en voz alta, no leyendo.
- Ropa sobria, colores sólidos (no hace falta combinar con la paleta de
  DePaso).

---

## Preguntas difíciles esperables — respuestas honestas preparadas

El tribunal puede preguntar por cosas que el propio informe señala como
pendientes. No improvisar: la respuesta madura es "no está implementado
todavía, es trabajo previsto para la próxima etapa" — nunca inventar. Las
respuestas de abajo están alineadas con lo que dice el informe entregado;
si una contradice al informe, gana el informe.

### Sobre la inteligencia artificial

| Si preguntan... | Respuesta corta |
|---|---|
| "¿Cuál es el accuracy del clasificador?" | **Está en entrenamiento, todavía no damos una cifra.** Al auditar el conjunto de datos encontramos que la etiqueta se derivaba del *tipo de objeto* y no de una medida: una caja de zapatos y una caja de heladera caían en la misma categoría. Lo estamos rehaciendo a partir de **dimensiones reales**. El objetivo declarado sigue siendo ≥70 % sobre el conjunto de prueba, con corrección manual como respaldo. |
| "¿Entonces no tienen nada del modelo?" | Tenemos el problema **medido** y el pipeline nuevo escrito. Detectamos el sesgo revisando nuestro propio dataset, no porque fallara en producción: preferimos rehacerlo ahora y no defender un número que sabíamos mal construido. |
| "¿Por qué categorías y no el volumen exacto?" | Porque estimar volumen exacto desde una sola foto es inviable sin sensores 3D — lo dice la literatura de visión en logística (Naumann et al., 2023). Clasificamos en cuatro categorías volumétricas, que es lo que el sistema necesita para elegir vehículo. |
| "¿Qué entra al modelo?" | Fotografía del paquete y descripción del remitente. Opcionalmente, un objeto de referencia de dimensiones conocidas en la toma, para asistir la escala. |
| "¿Y si el modelo no está disponible?" | El sistema degrada: ofrece directamente la carga manual de la categoría. Está declarado como requerimiento (RNF-AVL-01), no es un parche. |

### Sobre el producto y las decisiones de diseño

| Si preguntan... | Respuesta corta |
|---|---|
| "¿Cómo funciona el pago? ¿Retienen el dinero?" | **El pago está simulado: no hay pasarela ni fondos administrados.** Lo que el sistema modela es el **estado** del pago —pendiente, abonado, liberado, reintegrado— que gobierna cuándo el envío se ofrece y cuándo el saldo se marca como liberado. La integración real es trabajo posterior; está declarado así en el alcance desde el Capítulo 1. |
| "¿Un usuario puede ser remitente y transportista?" | Sí, pero con **perfiles separados**, entre los que alterna. Es deliberado: la validación y la reputación de cada rol son juicios sobre conductas distintas y no deben promediarse — al transportista lo valida un administrador, al remitente no. |
| "¿La foto es obligatoria?" | Sí. Alimenta la clasificación, pero sobre todo queda como **constancia del estado en que se despachó** el paquete. Salió de las entrevistas: el transportista teme que lo acusen de un daño que no hizo, y el remitente teme que le rompan el envío. Un mismo mecanismo cubre a los dos. |
| "¿El transportista puede calificar al cliente?" | Está **especificado** en los requerimientos y en el caso de uso —cada parte califica a la otra— pero todavía **no implementado**: hoy solo califica el cliente. La restricción de unicidad de la tabla lo impide y ya está diseñado el cambio. |
| "¿Por qué no calibraron los precios/descuentos?" | Son valores de arranque, declarados como pendientes de calibrar con datos reales de mercado; el análisis económico es la próxima etapa. |
| "¿Es rentable?" | Todavía no lo podemos afirmar. Lo que la encuesta muestra es que **los rangos se solapan**: lo que el remitente declara estar dispuesto a pagar y lo que el transportista pide se cruzan. Eso es **compatibilidad preliminar**, no un margen demostrado — falta incorporar costos variables, tasa de conversión y cobertura. El informe lo dice con esas palabras. |

### Sobre la arquitectura y la técnica

| Si preguntan... | Respuesta corta |
|---|---|
| "¿Por qué no microservicios?" | Monolito modular: la complejidad de microservicios (red, observabilidad distribuida, consistencia eventual) no se justifica con presupuesto de 85 USD y equipo de dos personas. Pero los once módulos ya están separados por dominio: el límite para extraer un servicio ya está trazado. |
| "¿Usan PostGIS / geolocalización avanzada?" | No, decisión deliberada: la geo se resuelve en Python con haversine + factor de corrección urbano, y OSRM para distancias reales por calle. PostGIS queda como optimización futura si el volumen de datos lo justifica. |
| "¿Y si se cae el servicio de ruteo?" | El sistema degrada solo: pasa a la estimación propia de distancias. El *matching* sigue funcionando, con un desvío aproximado en lugar de real. |
| "¿Dónde guardan las fotos de los paquetes?" | En un servicio de almacenamiento de objetos, con identificadores aleatorios para que no sean enumerables — que nadie pueda cambiar un número en la URL y bajarse las fotos de todos. Va aparte de la base para no atar las imágenes a la instancia que atiende la API. |
| "¿Por qué Python en el backend?" | Porque el clasificador es uno de los tres componentes diferenciales, y el ecosistema maduro de aprendizaje profundo es Python. Escribir el servidor en el mismo lenguaje permite que la inferencia corra **dentro del proceso de la API**; cualquier otro lenguaje obligaba a un segundo servicio desplegable, que contradice el monolito y el presupuesto. |
| "¿Y la seguridad?" | Tokens de acceso y refresco, contraseñas con Argon2, límite de intentos de login, validación por esquema de toda solicitud entrante, e imágenes con identificadores no adivinables. En producción, todo el tráfico sobre HTTPS. |

### Sobre lo legal y lo regulatorio

| Si preguntan... | Respuesta corta |
|---|---|
| "¿Cómo manejan la responsabilidad legal por daños?" | DePaso se posiciona como intermediaria tecnológica, no transportista; el vínculo remitente-transportista lo regula el Código Civil y Comercial (contrato de transporte de cosas); es un riesgo regulatorio identificado y en definición para los términos y condiciones. |
| "¿Y los datos personales de las fotos (patentes, caras)?" | Se sujeta a la Ley 25.326 de Protección de Datos Personales; está contemplado en el marco legal del capítulo de descripción. |
| "¿Y la situación laboral del transportista?" | Es una diferencia de fondo con las apps de reparto: el conductor ocasional **no depende** de la plataforma, aprovecha un viaje que ya hacía. No hay puntaje punitivo por rechazar pedidos ni obligación de conexión, que es justamente lo que la OIT señala como problemático en el modelo de *gig-work* dedicado. |

---

## Checklist de logística previa

- [ ] Cargar las slides en el dispositivo que van a usar Y en un pendrive
      de backup.
- [ ] Video de la demo grabado y accesible offline (plan B).
- [ ] Probar el proyector/pantalla y el pasador de diapositivas antes de
      empezar.
- [ ] Confirmar que el backend/API esté arriba y accesible desde la sala
      (wifi de la facultad probado, no asumido).
- [ ] **Comprobar que las fotos de los paquetes se siguen viendo** (si el
      backend se reinició, las imágenes de una demo vieja pueden haberse
      perdido — sacar una foto nueva en el momento y listo).
- [ ] Cronometrar el ensayo completo al menos una vez con reloj visible.
- [ ] Repasar la tabla de preguntas difíciles en voz alta, no solo leída.
