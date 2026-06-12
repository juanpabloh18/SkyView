# ☁️ SkyView UAO

Sistema web basado en Inteligencia Artificial para la segmentación automática del cielo y el cálculo del **Sky View Factor (SVF)** en entornos urbanos utilizando **YOLOv8-Seg**.

## 📌 Descripción

SkyView UAO es una aplicación desarrollada para analizar la relación entre la morfología urbana y el microclima de la Universidad Autónoma de Occidente (UAO).

El sistema utiliza un modelo de segmentación por instancias entrenado con YOLOv8-Seg para identificar automáticamente las áreas de cielo visibles en una imagen y calcular el **Sky View Factor (SVF)**, una métrica ampliamente utilizada en estudios de:

* Isla de Calor Urbana (ICU)
* Confort térmico
* Ventilación natural
* Planeación urbana sostenible
* Estudios de microclima

---

## 🚀 Características

✅ Carga de imágenes desde navegador web.

✅ Segmentación automática del cielo mediante YOLOv8-Seg.

✅ Visualización de la imagen segmentada.

✅ Cálculo automático del Sky View Factor (SVF).

✅ Interpretación cualitativa del resultado.

✅ Interfaz web desarrollada con Flask y Bootstrap.

---

## 🏗️ Arquitectura del Proyecto

```text
SkyView/
│
├── app.py
├── best.pt
│
├── templates/
│   └── index.html
│
└── README.md
```

### Componentes principales

#### Frontend

* HTML5
* Bootstrap 5
* SweetAlert2

#### Backend

* Flask

#### Inteligencia Artificial

* YOLOv8-Seg
* OpenCV
* NumPy
* Ultralytics

---

## ⚙️ Funcionamiento

1. El usuario carga una imagen urbana.
2. Flask recibe la imagen.
3. YOLOv8-Seg realiza la segmentación.
4. Se extrae la máscara correspondiente a la clase **Cielo**.
5. Se calcula el SVF mediante:

[
SVF = \frac{\text{Píxeles de cielo}}{\text{Píxeles totales}}
]

6. Se muestra la imagen segmentada.
7. El sistema presenta el valor del SVF y su interpretación.

---

## 📊 Interpretación del SVF

| SVF         | Interpretación                                                              |
| ----------- | --------------------------------------------------------------------------- |
| ≥ 0.70      | Alta exposición al cielo, excelente ventilación y baja acumulación de calor |
| 0.45 – 0.69 | Exposición moderada al cielo                                                |
| < 0.45      | Baja exposición al cielo, posible acumulación de calor                      |

---

## 🧠 Modelo de Deep Learning

El proyecto utiliza **YOLOv8-Seg** para segmentación por instancias.

### Clases entrenadas

* Cielo
* Estructuras Urbanas

### Dataset

Las imágenes fueron capturadas en el campus de la Universidad Autónoma de Occidente.

Características del conjunto de datos:

* 150 imágenes de estructuras
* 120 imágenes de cielo
* Resolución: 640x640
* Etiquetado realizado con Roboflow

División:

* 80% Entrenamiento
* 10% Validación
* 10% Pruebas

---

## 📈 Resultados

| Métrica              | Valor  |
| -------------------- | ------ |
| Precisión            | 0.621  |
| Recall               | 0.660  |
| F1-Score             | 0.640  |
| mAP@50               | 0.605  |
| mAP@50-95            | 0.397  |
| Tiempo de inferencia | ~15 ms |

Estos resultados demuestran la viabilidad de utilizar modelos de segmentación para estudios de sostenibilidad urbana y análisis microclimáticos.

---

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/juanpabloh18/SkyView.git

cd SkyView
```

### 2. Instalar dependencias

```bash
pip install flask ultralytics opencv-python numpy
```

---

## ▶️ Ejecución

```bash
python app.py
```

Abrir en el navegador:

```text
http://localhost:3000
```

---

## 📷 Ejemplo de Uso

1. Seleccionar una imagen urbana.
2. Presionar **Procesar imagen**.
3. Visualizar la segmentación generada.
4. Presionar **Calcular SVF**.
5. Consultar el porcentaje de cielo visible.
