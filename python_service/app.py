from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageDraw
import os
from io import BytesIO
from dotenv import load_dotenv
from whisper_processor import WhisperAudioProcessor
from free_image_generator import FreeImageGenerator
from replicate_image_generator import ReplicateImageGenerator

# Load environment variables
load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize processors
audio_processor = WhisperAudioProcessor()

# Try Replicate first, fallback to HuggingFace, then placeholder
replicate_key = os.getenv('REPLICATE_API_KEY')
huggingface_key = os.getenv('HUGGINGFACE_API_KEY')

if replicate_key:
    print("Using Replicate API for image generation")
    image_generator = ReplicateImageGenerator(api_key=replicate_key)
elif huggingface_key:
    print("Using HuggingFace API for image generation")
    image_generator = FreeImageGenerator(api_key=huggingface_key)
else:
    print("No API keys found, using placeholder image generation")
    image_generator = FreeImageGenerator()

@app.route('/process-audio', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400
    audio_file = request.files['audio']
    audio_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(audio_path)

    try:
        # Extract audio features
        features = audio_processor.extract_features(audio_path)
        
        # Transcribe audio (if OpenAI key is available)
        transcription = audio_processor.transcribe_audio(audio_path)
        
        # Create art prompt
        prompt = audio_processor.create_art_prompt(features, transcription)
        
        # Generate image using DALL-E or placeholder
        img = image_generator.generate_image(prompt)
        
        buf = BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)

        return send_file(buf, mimetype='image/png')
        
    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 