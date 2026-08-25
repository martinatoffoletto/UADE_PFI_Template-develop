# TODO de código — brecha contra el informe del 50 % (21-ago-2026)

Cambios que el código de `../DePaso` necesita para quedar alineado con el informe
después de la revisión del 21-ago-2026. Cada ítem indica **qué dice el informe**,
**qué hace el código hoy** y **qué hay que tocar**.

Nada de esto bloquea la entrega del 50 %: el Capítulo 4 especifica *qué debe hacer*
el sistema y §5.7 declara el estado real. Es la cola de trabajo hacia el 100 %.

Orden: por relación costo/riesgo, no por número de requerimiento.

---

## 🔴 Alta — barato y con consecuencia visible

### 1. El feed ofrece envíos impagos

- **Informe:** RF-SHP-04 — *«el envío solo se ofrezca a los transportistas una vez
  abonado»*. CU-01 alt. 5a dice lo mismo.
- **Código:** `matching/service.py` → `feed_for_carrier()` filtra por estado
  `pending`, vehículo, capacidad y desvío, pero **nunca mira `payment_status`**.
  Un envío sin pagar aparece en el feed y un transportista puede aceptarlo.
- **Tocar:** agregar el filtro `payment_status == PaymentStatus.PAID` en
  `feed_for_carrier` y en `_rank_collaborative` / `_rank_dedicated`. Sumar un test
  en `tests/test_matching.py` que cree un envío `pending` sin pagar y verifique que
  no aparece.
- **Costo:** ~1 línea + 1 test.

### 2. Las fotos se pierden en cada reinicio

- **Informe:** ahora declara **almacenamiento de objetos** (Cap. 5, §Contenedores,
  Tabla 5.I y Figs. 5.2 / 5.5), justificado por escalabilidad.
- **Código:** `vision/router.py:88` escribe en `uploads/packages/<uuid>.jpg`, el
  disco del contenedor. Ni el `Dockerfile` ni `docker-compose.yml` declaran un
  volumen para `uploads/` (el único volumen es `depaso_pgdata`). El disco es
  **efímero**: al reiniciar o redesplegar, las fotos desaparecen y los
  `shipments.photo_url` quedan apuntando a 404. En el plan free de Render eso pasa
  solo, por inactividad.
- **Tocar, en dos etapas:**
  - **Ya (10 min, asegura la demo):** volumen `./uploads:/app/uploads` en
    `docker-compose.yml` y disco persistente en Render.
  - **Después:** extraer un adaptador de almacenamiento (`shared/storage.py`) con
    dos implementaciones —disco local para desarrollo, objetos para producción—.
    El resto del sistema **no se entera**: ya referencia las imágenes por URL, no
    por ruta. Conservar el nombre `uuid4().hex` (RNF-SEC-03).
- **Costo:** volumen ~10 min · adaptador ~medio día.

### 3. `Classification` no guarda la ruta de la imagen

- **Informe:** RF-VIS-04 — *«Registrar cada estimación realizada… para su auditoría
  y posterior reentrenamiento»*.
- **Código:** `vision/models.py` guarda predicción, confianza, `accepted` y
  `manual_category`, pero **ningún puntero a la imagen**. La foto se escribe a
  disco y la URL vuelve en la respuesta HTTP; en la tabla no queda nada. Resultado:
  existe el registro *«predije M con 0,82 y el usuario corrigió a L»* pero **no se
  sabe qué imagen era** — que es justo lo que el requerimiento promete.
- **Tocar:** columna `image_path = Column(String(500), nullable=True)` en
  `Classification` y asignarla en `vision/router.py` después de escribir el archivo.
- **Costo:** 2 líneas. Convierte esa tabla en dataset de reentrenamiento listo.

---

## 🟡 Media — trabajo real, decidido

### 4. Perfiles separados con conmutación (RF-USR-06 reescrito)

- **Informe:** *«Mantener separados el perfil de remitente y el de transportista,
  cada uno con su propia validación y su propia reputación, y permitir que una
  persona alterne entre sus perfiles sin volver a autenticarse.»* Modelo tipo
  Instagram: una sesión, dos perfiles, cambio rápido.
- **Código:**
  - **Backend: ya lo soporta.** `POST /carriers/me` crea el perfil de transportista
    tomando el `user_id` del JWT, con `carriers.user_id` unique. `User.rating` y
    `Carrier.reputation` ya son dos columnas separadas.
  - **App: no existe.** `carriersService.createProfile` está definido en
    `shared/api/carriers.ts:16` y **no lo llama nadie** (grep: una sola aparición).
    La app decide el rol con `user.user_type` (`ProfileScreen.tsx:42`,
    `useShipmentNotifications.ts:47`), que es un campo único fijado en el registro.
- **Tocar (casi todo frontend):**
  - Estado de «perfil activo» en `authStore`, independiente de `user_type`.
  - Pantalla de alta del perfil de transportista que llame a `createProfile`.
  - Conmutador en `ProfileScreen` y ruteo de tabs por perfil activo en vez de por
    `user_type`.
  - Backend: nada obligatorio. Opcional, dejar de usar `user_type` para decidir
    permisos y derivar la condición de transportista de la existencia del perfil
    `Carrier` — que es lo que dice la Tabla 5.II.
- **Costo:** ~1–2 días.

### 5. Calificación bidireccional y sin comentario

- **Informe:** CU-06 paso 4 — *«**Cada parte** califica a la otra con **una
  puntuación**»* (ya sin comentario). RF-SHP-08 sin cambios.
- **Código:** hoy **solo el cliente califica**: `rate_shipment` exige
  `shipment.client_id == client_id`, y `Rating` tiene
  `UniqueConstraint("shipment_id", name="uq_rating_shipment")`, que **impide
  físicamente una segunda calificación por envío**. `User.rating` existe, arranca en
  5.0 y **nunca se escribe**. La columna `comment` existe y el endpoint la acepta,
  pero `RatingModal.tsx` no tiene campo de texto y llama `rateShipment(id, stars)`
  sin tercer argumento.
- **Tocar:**
  - `Rating`: agregar `rater_role`, reemplazar `uq_rating_shipment` por unique
    `(shipment_id, rater_role)`, **eliminar `comment`**.
  - Endpoint para que el transportista califique al cliente.
  - Escribir `User.rating` al recibir una calificación de transportista → cliente
    (hoy solo se actualiza `Carrier.reputation`).
  - Limpiar `comment` de `RatingCreate`, de `RatingResponse`, y el tercer parámetro
    de `shipments.ts:93` (`rateShipment`).
- **Costo:** ~1 día.
- **Respaldo en la investigación:** E5 teme la acusación falsa del destinatario;
  E1 señaló que las plataformas evalúan el producto y no el transporte.

### 6. La foto y la descripción pasan a ser obligatorias (RF-SHP-01)

- **Informe:** *«…una descripción del contenido y una fotografía del paquete, que se
  conserva como constancia del estado en que se despachó»*.
- **Código:** en `shipments/schemas.py:22-23`, **`photo_url` y `description` son
  ambos opcionales** (`str | None = None`). Se puede crear un envío sin foto.
- **Tocar:** volverlos requeridos en `ShipmentCreate`; en la app, que
  `send-flow/PackageScreen` bloquee el avance sin foto. **Cuidado:** al volverlos
  obligatorios se rompen los fixtures que crean envíos sin foto — hay que revisar
  `tests/conftest.py`, `test_integration_flows.py` y `test_matching.py`.
- **Costo:** ~2 h contando la corrección de los tests.

### 7. La descripción entra al endpoint de visión (RF-VIS-01)

- **Informe:** *«Estimar la categoría volumétrica de la carga y su nivel de
  confianza a partir de la fotografía del paquete **y de la descripción** que aporta
  el remitente.»*
- **Código:** `POST /vision/classify` recibe `image` y `has_reference_object`.
  **La descripción no llega al módulo de visión**: vive en `shipments.description` y
  solo se le muestra al transportista.
- **Tocar:** agregar `description: str = Form("")` al endpoint y pasarla a
  `classify()`. Aunque el modelo todavía la ignore, **el contrato tiene que
  llevarla ya**: cuando v3 la use, no hay que cambiar la app ni la API. Que la app
  la mande desde `sender/vision.ts`.
- **Costo:** ~1 h.
- **Ojo con la fuga de etiqueta** cuando el brazo de texto se entrene: si el campo
  se rellena con la clase del dataset de la que se bajó la imagen, y la categoría se
  deriva de esa misma clase, el texto **es** la etiqueta.

---

## 🟢 Baja — higiene

### 8. Códigos `RF-*` / `RNF-*` del código desalineados con el Cap. 4

Los comentarios del código citan requerimientos con números que no existen o que
corresponden a otro. La numeración válida **siempre** es la del Cap. 4.

| Dónde | Cita | Debería ser |
|---|---|---|
| `vision/service.py:33` | `RNF-PERF-02` (tamaño de imagen) | `RNF-PERF-01` |
| `tracking/service.py:4` | `RNF-PERF-04`, «up to 30 s» | `RNF-PERF-02`, **45 s** |
| `auth/router.py:47` | `RNF-SEC-06` (rate limit) | `RNF-SEC-02` |
| `shipments/router.py:287` | `RF-CAR-07` (penalización) | `RF-CAR-08` |
| `matching/service.py:185` | `RF-MAT-05` | **no existe** |
| `shipments/service.py:258` | docstring: CO₂ «persists on delivery» | el CO₂ se persiste **al aceptar** (`:441`); la entrega no lo toca |
| `shipments/service.py:365` | docstring: «persisted on delivery» | ídem — corregir a «computed and persisted at accept time» |
| `shipments/router.py:281` | `RF-CAR-03/04` en `accept_shipment` | `RF-CAR-04` |

**Costo:** ~30 min de grep.

### 9. Objeto de referencia: la app y `CLAUDE.md` no coinciden

- `CLAUDE.md` dice «botella de **500 ml**, decidido».
- `depaso_app/src/sender/dimensioning.ts:24-27` ofrece **tarjeta (8,56 cm), hoja A4
  (29,7 cm) y "otro"**, con medición geométrica real (`scaleCmPerPx`) y un
  `DimensioningModal` ya conectado a `PackageScreen`.
- **Decidir cuál vale.** Tarjeta y A4 son mejores referencias: planos, estandarizados
  mundialmente y sin ambigüedad sobre qué lado se mide; una botella de 500 ml varía
  de forma entre marcas. **El informe no nombra ninguno** (dice «objeto de
  referencia» en genérico, RF-VIS-03 y CU-03), así que esto no obliga a tocar el
  `.tex` — es solo alinear código y documentación interna.

### 10. `has_reference_object` y las condiciones de captura están vacías

- `has_reference_object` es **0 en los tres splits** y `lighting` / `angle` /
  `background` son `"unknown"` en el **100 %** de las imágenes. El modelo tiene la
  entrada de referencia pero nunca aprendió nada de ella, y el análisis de sesgos
  devuelve cuatro filas idénticas.
- **El informe ya no lo declara como hecho** (§5.6 pasó a futuro), así que esto dejó
  de ser una brecha *del informe*. Sigue siendo la tarea que habilita el análisis de
  sesgos: se cierra con la sesión de fotos propias (`ml/TODO_MARTINA.md`, paso 2).

---

## Sin acción

- **RNF-PERF-02 (45 s):** el peor caso real es 35 s — `useGpsPublisher.ts:28`
  publica cada 20 s y `ShipmentDetailModal.tsx:43` consulta cada 15 s. **Ya se
  cumple** con el número nuevo. Solo actualizar el comentario del punto 8.
- **RNF-OBS-01:** `core/logging.py` ya usa structlog con `JSONRenderer` sobre la
  salida estándar, que es exactamente lo que declara la Tabla 5.I. Nada que tocar.
- **RNF-AVL-01:** las dos degradaciones están implementadas —OSRM cae a
  haversine × 1,3 (`osrm_client.py:44-56`), y sin modelo el stub devuelve siempre
  confianza 0,50, por debajo del umbral, forzando el ingreso manual
  (`vision/service.py:56-59`)—. *(Detalle conocido: el cliente de OSRM **no
  reintenta**; una vez que lo marca caído hay que reiniciar la API.)*
- **HTTPS:** no se implementa en la aplicación. Lo termina el proveedor; por eso el
  `Dockerfile` arranca uvicorn con `--proxy-headers`.
