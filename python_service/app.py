from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageDraw
import os
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process-audio', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400
    audio_file = request.files['audio']
    audio_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(audio_path)

    # Dummy: generate a simple image
    img = Image.new('RGB', (256, 256), color='white')
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Audio processed!", fill='black')
    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 