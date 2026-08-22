# Discurso — Defensa entrega 50% · DePaso

Guion hablado para la exposición oral de Martina y Candela. Calza slide por slide
con `defensa-50-sketch.md` (mismas 9 láminas). Esto es lo que se **dice**, no lo
que va escrito en la lámina.

---

## Framework elegido: Pixar Pitch, con el usuario como héroe

Evalué los tres que planteaste. Conclusión y por qué:

- **Camino del héroe (clásico, 12 etapas)** — demasiado largo y mítico para 10
  minutos técnicos. Forzado ante un tribunal de ingeniería.
- **Pixar Pitch** (*Había una vez… Todos los días… Un día… Por eso… Por eso…
  Hasta que finalmente*) — es la versión comprimida y "de producto" del mismo
  arco. Seis beats, memorables, que **mapean exactamente a tus 9 slides**. Ganador.
- El toque de **StoryBrand / camino del héroe**: el héroe **no es DePaso**, es el
  usuario (Juan, la PyME). DePaso es el guía que le resuelve el problema. Esto
  evita que la charla suene a folleto de producto y le pone emoción.

**Resultado: Pixar Pitch como columna, Juan y Clara como héroes.** Un tribunal de
ingeniería igual recibe toda la evidencia (encuesta, tests, arquitectura), pero
envuelta en una historia que se sigue sola.

### El hilo narrativo (protégelo al editar)

Dos personajes recurrentes atraviesan toda la charla — es el recurso más fuerte:

- **Juan** — PyME de repuestos en Lanús, paga un flete entero por una caja. *(la demanda)*
- **Clara** — maneja todos los días de Caballito al centro con el baúl vacío. *(la oferta)*

Se **abren** en el problema (slide 2), se **conectan** en la propuesta (slide 4) y
se **cierran** juntos en el final (slide 9). Ese arranque-y-cierre con los mismos
dos personajes es lo que hace que el jurado se lleve la idea. Si editás el guion,
no rompas ese lazo.

Y entre los dos hay un **tercer elemento**, que no es un personaje sino un hueco:
**el mercado no tiene dónde juntarlos.** No existe una opción híbrida, y los
fletes y las mudanzas quedan directamente afuera de las apps que hay. Ese hueco
es lo que convierte la historia en un proyecto: sin él, Juan y Clara son dos
anécdotas; con él, son un mercado desatendido.

| Beat Pixar | Slide | Qué pasa |
|---|---|---|
| Había una vez / Todos los días | 1–2 | Juan paga de más; Clara viaja vacía; nadie los junta |
| Un día | 3 | Preguntamos: ¿y si se encuentran? La evidencia dice que sí |
| Por eso… por eso… | 4–7 | DePaso: modelo híbrido → diferencial → arquitectura → demo |
| Hasta que finalmente | 8–9 | Dos problemas, una sola solución; no creamos viajes, aprovechamos los que existen |

---

## Reparto (M = Martina · C = Candela)

Default abajo; es **intercambiable**, ensayen con el que les salga más natural.
La única regla: quien **no** narra la demo, la **maneja** (conduce el teléfono).

| Slide | Habla | Notas |
|---|---|---|
| 1 Portada | **M** | abre |
| 2 Problema | **M** | cuenta a Juan, presenta a Clara y cierra con el hueco del mercado |
| 3 Validación | **C** | encuesta + entrevistas |
| 4 Qué es DePaso | **M** | frase ancla |
| 5 Diferencial + target | **C** | |
| 6 Arquitectura | **M** | |
| 7 Demo | **C narra · M maneja** | M ya tiene el teléfono en la mano para el slide 8 |
| 8 Resultados | **M** | enlaza desde la demo que venía manejando |
| 9 Cierre | **C** | cierra sola; el "gracias" lo dicen las dos |

Tiempo total objetivo: **≈ 10–11 min** (demo incluida). Ritmo 130–150 palabras/min.

---

## Guion, slide por slide

> Convención: *(pausa)* = silencio deliberado · **[acción]** = qué hacer ·
> **negrita** = frase que hay que "plantar" (decir más lento y mirar al jurado).

---

### Slide 1 — Portada · ~10 s · **[M]**

**[Antes de hablar: 3 segundos de pausa. Parar, respirar, mirar al tribunal.]**

> Buenas tardes. Somos Martina Toffoletto y Candela Basáez, de Ingeniería en
> Informática; nuestro tutor es Maximiliano Dos Santos. Les vamos a presentar
> **DePaso**, una plataforma de logística urbana colaborativa para el AMBA. Esta
> es la entrega del 50%.

*(pausa · handoff mental: entrás directo al problema)*

---

### Slide 2 — El problema · 60–75 s · **[M]** · *Beat: "Todos los días"*

> Quiero que piensen en **Juan**. Juan tiene 34 años y un local de repuestos en
> Lanús. Dos o tres veces por semana necesita mandar un paquete —mediano, a veces
> voluminoso— a un cliente en la otra punta del AMBA. Y cada vez, tiene que pagar
> un flete entero. **Un vehículo completo… para una caja.** *(pausa)*
>
> Ese costo se le come el margen; y si lo traslada al precio, deja de ser
> competitivo. Así que Juan termina coordinando cada envío por WhatsApp, cliente
> por cliente, sin saber siquiera cuándo va a llegar. *(pausa)*
>
> Y Juan no es un caso aislado. En un relevamiento a más de dos mil PyMEs de la
> región, el **44%** dijo que el costo de envío es una de las principales barreras
> para vender online. En Argentina los costos logísticos subieron **22%** solo en
> el primer semestre de este año. Y todos esos viajes dedicados tienen un costo
> ambiental: el transporte explica cerca del **14%** de las emisiones del país.
> *(pausa)*
>
> Ahora, mientras Juan paga por un vehículo entero, a veinte cuadras **Clara**
> hace todos los días el mismo viaje al centro… **con el baúl vacío.** *(pausa)*
>
> Y acá está el tercer problema, que es el que nos decidió a hacer esto. Podrían
> preguntarse: si Juan necesita mandar y Clara ya va para allá, ¿por qué no se
> encuentran? Porque **hoy no hay dónde.** *(pausa)* Las apps de mensajería que
> existen llevan paquetes chicos y siempre con un viaje dedicado: alguien sale
> exclusivamente a llevar tu cosa. No contemplan cargas medianas, grandes ni
> mudanzas. Y los fletes viven en otro mundo, resueltos por WhatsApp y
> recomendación. **No existe una opción híbrida**, ni un solo lugar donde entren
> las dos cosas: el paquete chico y la mudanza. *(pausa)*
>
> Dos problemas que, en realidad, son la solución uno del otro. **Y nadie los
> junta.**

**[Handoff a C: "Antes de construir nada, quisimos comprobar esa intuición."]**

---

### Slide 3 — Cómo lo validamos · 60–90 s · **[C]** · *Beat: "Un día"*

> Antes de escribir una sola línea de código, quisimos saber si esa intuición se
> sostenía. Hicimos una encuesta: **145 respuestas**, casi todas del AMBA. No es
> un estudio de mercado cerrado, es **exploratorio** —y decirlo así es parte del
> rigor, no una debilidad—. Pero los números fueron contundentes. *(pausa)*
>
> Del lado de la **demanda**, casi el **70%** se mostró dispuesto a usar un modelo
> colaborativo. Del lado de la **oferta**, más del **84%** se interesó en
> transportar; y de esos, el **92%** lo haría por un ingreso extra… con una
> condición: **que no lo obligue a desviarse de su rutina.** *(pausa)*
>
> Después hicimos cinco entrevistas en profundidad, para entender el *porqué*
> detrás de esos números. Y ahí apareció el hallazgo que ordenó todo el diseño:
> **el desvío no es negociable.** Un transportista lleva tu paquete si le queda de
> paso; si se tiene que desviar, no hay precio que lo compense. Y una segunda
> condición, igual de tajante: **sin seguimiento en tiempo real, no usan la app.**
> *(pausa)*
>
> Y hubo un tercer hallazgo que nos hizo **cambiar un requerimiento**, y lo
> queremos contar porque es lo que justifica haber hecho las entrevistas. Un
> transportista nos dijo que su miedo no es romper algo: es que lo **acusen** de
> haberlo roto. Del otro lado, el 73% de los encuestados dijo que su principal
> preocupación era justamente que le dañaran el envío. *(pausa)* Es el mismo
> miedo, mirado desde las dos puntas. Y se resuelve con una sola cosa: **la
> fotografía del paquete pasó a ser obligatoria**, como constancia del estado en
> que se despachó. *(pausa)*
>
> Esas tres cosas dejaron de ser opiniones y pasaron a ser **reglas del sistema.**

**[Handoff a M: "Y así nace DePaso."]**

---

### Slide 4 — Qué es DePaso · 45–60 s · **[M]** · *Beat: "Por eso…"*

> Así nace DePaso. *(pausa)* La idea es simple: en vez de **crear** un viaje nuevo
> cada vez que alguien necesita enviar algo, **aprovechamos** los viajes que ya
> están pasando. Clara ya va al centro; que lleve el paquete de Juan de paso.
> *(pausa — plantar la frase ancla, más lento)*
>
> **No creamos viajes nuevos: aprovechamos los que ya existen.** *(pausa)*
>
> Para eso DePaso combina dos modalidades. La **colaborativa**, que conecta el
> envío con alguien que ya iba a hacer ese recorrido, con un desvío que el sistema
> **limita al 15%.** Ese límite es, justamente, la regla dura que nos pidieron las
> entrevistas. Y la **dedicada**, tipo flete, para lo que necesita un vehículo
> entero: una mudanza, algo voluminoso. *(pausa)*
>
> Y ahí está la respuesta al hueco que les mostraba recién: **las dos conviven en
> la misma plataforma.** El paquete chico y la mudanza entran por la misma puerta.

**[Handoff a C: "¿Y en qué nos diferenciamos de lo que ya existe?"]**

---

### Slide 5 — Diferencial + target · 60–75 s · **[C]** · *Beat: "Por eso…"*

> ¿En qué nos diferenciamos? Hoy, plataformas como **Rappi Favor** o **PedidosYa
> Envíos** resuelven envíos, sí, pero todas con un modelo **puramente dedicado**:
> alguien sale exclusivamente a llevar tu paquete. *(pausa)*
>
> Nosotras **no competimos por escala** con ellas. Apuntamos al segmento que hoy
> queda afuera por precio: **las PyMEs y los particulares del AMBA sin flota
> propia** —los Juan. *(pausa)*
>
> Y combinamos tres cosas que **ninguna plataforma local reúne al mismo tiempo**:
> el modelo **híbrido** dedicado y colaborativo; una **clasificación de la carga
> por inteligencia artificial propia**; y el **cálculo del CO₂ ahorrado** en cada
> envío. Ese cruce —híbrido, IA propia y ambiental— es nuestro lugar en el mercado.

**[Handoff a M: "Veamos, en una sola lámina, cómo está construido."]**

---

### Slide 6 — Arquitectura · 60 s · **[M]** · *(la única lámina técnica)*

> En una lámina, así está construido. **[señalar, no leer]** Una **app móvil**
> para remitentes y transportistas, y un **panel web** para las PyMEs y la
> administración. Los dos hablan, sobre **HTTPS**, con una **única API**, que
> concentra toda la lógica. A la derecha, lo que la API usa: la **base de datos**,
> un **almacenamiento de objetos** donde van las fotos de los paquetes, y un
> servicio externo de **ruteo** —ese va punteado porque es reemplazable: si se
> cae, el sistema estima las distancias por su cuenta y sigue funcionando—.
> *(pausa)*
>
> Ahora, lo que quiero que miren de esta lámina. **[señalar los chips]** Adentro
> de la API están los **once módulos de dominio**, y no es un detalle de
> implementación: es la arquitectura. **[señalar los tres verdes]** Estos tres son
> los pilares del proyecto. **Matching**, que decide qué envío le sirve a qué
> transportista; **visión**, que estima la categoría de la carga a partir de la
> foto; y **CO₂**, que calcula lo que se ahorra frente al viaje dedicado. El
> modelo de inteligencia artificial corre **en memoria, dentro de la misma API**.
> *(pausa)*
>
> Y una decisión de diseño que queremos defender de entrada: esto es un **monolito
> modular, no microservicios.** Con un presupuesto de **85 dólares** y un equipo de
> **dos personas**, la complejidad distribuida no se justifica. Pero —y esto es lo
> importante— los once módulos **ya están separados por dominio**: si algún día hay
> que extraer uno como servicio, el límite ya está trazado.

**[Handoff a C: "Pero mejor que contarlo, se los mostramos."]**

---

### Slide 7 — Demo en vivo · 5 s de slide + 3–3,5 min · **[C narra · M maneja]**

**[M ya tiene el teléfono/proyección lista. C narra mientras M toca.]**

> Pero mejor que contarlo, se los mostramos. Este es el flujo del **remitente**.
>
> **[M: sacar/subir la foto del paquete]** Saco una foto del paquete. La foto es
> **obligatoria**, y por dos motivos: alimenta la clasificación, y queda como
> **constancia del estado en que se despachó** —es el requerimiento que salió de
> las entrevistas—. *(pausa)* Y con esa foto, el sistema **propone
> automáticamente la categoría de carga**. Si se equivoca, el remitente la corrige
> a mano: **propone, no impone.** *(pausa)*
>
> **[M: avanzar a la cotización]** Con eso, el sistema **cotiza**. Acá están las
> opciones —dedicada y colaborativa— con su precio, **siempre visible antes de
> confirmar**, porque la encuesta nos dijo que el precio es el factor número uno.
> Y abajo, el dato que nos hace distintos: **cuánto CO₂ ahorra** este envío frente
> a mandar un vehículo dedicado. *(pausa)*
>
> En noventa segundos vieron los **tres pilares** del proyecto funcionando juntos:
> la clasificación de la carga, el matching que cotiza y el cálculo ambiental.

**[Si el clasificador se equivoca en vivo — no taparlo, usarlo]**

> Miren, se equivocó: propuso una categoría más chica. **[M: corregirla a mano]**
> Y eso es exactamente lo que tiene que pasar: el sistema **propone**, la persona
> decide. Por eso el requerimiento dice que si la confianza es baja, deriva a la
> carga manual.

**[Opcional, si el tiempo lo permite — "¿es real o una maqueta?"]**

> Y para que quede claro que esto no es una maqueta de diseño: **[M: abrir la API]**
> esta es la API real, con sus endpoints; **[M: correr pytest o mostrar la corrida]**
> y estas son las **176 pruebas automatizadas** que corren sobre el backend.

> **Plan B (si algo falla en vivo):** "Se nos complicó la conexión, les muestro la
> grabación" → pasar al video de 90 s de backup, sin perder el hilo. No pedir
> disculpas largas; naturalizarlo y seguir.

**[Handoff a M: "En números, ¿dónde estamos hoy?"]**

---

### Slide 8 — Resultados / avance · 30–45 s · **[M]**

> En números, un resumen honesto de dónde estamos. El **backend** ya tiene sus
> **once módulos** funcionando, con **176 pruebas** automatizadas que cubren
> también los flujos de punta a punta; y las **dos aplicaciones cliente** —la app
> móvil y el panel web— corren sobre esa misma API. *(pausa)*
>
> Y dos cosas que preferimos decir nosotras antes de que nos las pregunten. La
> primera: el **clasificador de carga está en entrenamiento**, es el foco de los
> próximos meses, y por eso hoy **no les damos una cifra de precisión**. La
> segunda: el **pago está simulado** —no hay pasarela integrada ni administramos
> fondos—; lo que sí corre es el ciclo de estados del envío. *(pausa)*
>
> No está todo terminado —es un prototipo— pero el ciclo del envío **ya corre de
> punta a punta.**

**[Handoff a C: "Para cerrar, qué nos queda por delante."]**

---

### Slide 9 — Cronograma + cierre · 60–75 s · **[C, y el "gracias" las dos]** · *Beat: "Hasta que finalmente"*

> Para cerrar. De acá a **diciembre** nos queda construir el conjunto de datos y
> evaluar el modelo, integrar las piezas, y —lo más importante— **validarlo con
> usuarios reales** usando el prototipo. *(pausa)*
>
> Empezamos con dos problemas que parecían distintos: **una PyME que paga de más
> y un auto que viaja vacío.** Y con un tercero, que era que no había dónde
> juntarlos. DePaso los convierte en una sola solución. *(pausa)*
>
> Porque no se trata de poner **más** vehículos en la calle. Se trata de aprovechar
> mejor **los que ya están.** *(pausa)*
>
> **[las dos, mirando al tribunal]** Muchas gracias. Quedamos a disposición para
> sus preguntas.

---

## Notas de ensayo

- **Cronometrar en voz alta**, no leyendo mentalmente. El presupuesto de 10–11 min
  solo vale si se prueba hablando (mínimo 5 ensayos, con reloj a la vista).
- **Plantar las 3 frases ancla** (decirlas más lento, con pausa antes y después):
  1. "Un vehículo completo… para una caja."
  2. "No creamos viajes nuevos: aprovechamos los que ya existen."
  3. "No se trata de poner más vehículos; se trata de aprovechar mejor los que ya están."
- **La cuarta frase, la del slide 2:** "*No existe una opción híbrida.*" Es la que
  convierte una anécdota en un proyecto — plantarla igual que las otras tres.
- **Handoffs**: cada cambio de voz tiene una frase-puente ya escrita arriba. Que
  la diga quien **cierra** su parte, no quien empieza — así el pase no queda mudo.
- **Números**: pausa antes de cada cifra clave y pausa después, para que el jurado
  la procese. No encadenar 44% / 22% / 14% de corrido.
- **Adelantarse a las debilidades.** Las tres que conviene decir **ustedes**, sin
  esperar la pregunta: el clasificador está en entrenamiento (slide 8), el pago es
  simulado (slide 8) y la muestra es exploratoria (slide 3). Decirlas primero
  desarma la pregunta y suma criterio; que las descubra el jurado, resta.
- **Preguntas difíciles**: repasar en voz alta las tablas de
  `defensa-50-sketch.md`, que están agrupadas por tema (IA, producto,
  arquitectura, legal). La respuesta madura siempre es: *"no está implementado
  todavía, es trabajo de la próxima etapa"* — nunca inventar.
- **El clasificador no se anuncia como terminado y no se dan cifras.** Está en
  entrenamiento y el conjunto de datos se está construyendo a partir de
  dimensiones reales. **No mencionar ningún *accuracy* en la exposición**: si
  preguntan, va la respuesta de la tabla. El hallazgo del etiquetado es mejor
  carta que un número — muestra que el problema se detectó midiendo. El informe
  entregado dice exactamente esto: "el modelo en desarrollo". No contradecirlo.
- **El pago no se explica de más.** Si sale el tema: *el estado del pago sí está
  modelado y gobierna el envío; el movimiento de fondos está simulado.* No usar
  la palabra "retención" ni "garantía" — el informe dejó de usarlas a propósito,
  porque describen un mecanismo financiero que el prototipo no tiene.
- **Honestidad sobre la rentabilidad**: el informe habla de *compatibilidad
  preliminar* entre lo que el remitente paga y lo que el transportista cobra,
  **no** de viabilidad económica demostrada (falta el análisis de costos). Si
  preguntan por rentabilidad, sostener ese matiz.
- **Coherencia con el informe.** Todo lo que se dice en voz alta tiene que poder
  encontrarse en el informe entregado. Si en un ensayo aparece una frase que suena
  bien pero no está respaldada ahí, se saca: el tribunal tiene el documento.
