from flask import Flask, render_template, request
from ultralytics import YOLO
import numpy as np
import cv2
import base64

app = Flask(__name__)

model = YOLO("best.pt")  # modelo entrenado

@app.route('/', methods=['GET'])
def home():
    success = request.args.get("success")
    return render_template('index.html', success=success)




@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    img_bytes = imagefile.read()

    # Convertir a OpenCV
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Ejecutar YOLO
    results = model(img)[0]

    # Extraer máscara de cielo (clase 0)
    mask_cielo = None
    if results.masks is not None:
        for cls, m in zip(results.boxes.cls, results.masks.data):
            if int(cls) == 0:
                mask_cielo = m.cpu().numpy()
                break

    svf_value = None

    if mask_cielo is not None:
        cielo_pixels = np.sum(mask_cielo > 0.5)
        total_pixels = mask_cielo.size
        svf_value = cielo_pixels / total_pixels

    # Obtener imagen anotada
    annotated = results.plot()  
    _, buffer = cv2.imencode('.png', annotated)
    encoded_result = base64.b64encode(buffer).decode('utf-8')

    return render_template(
        'index.html',
        result_image=encoded_result,
        svf=svf_value,
        success=1
    )

if __name__ == "__main__":
    app.run(port=3000, debug=True)
