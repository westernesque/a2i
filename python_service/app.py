import os
import tempfile
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from whisper_processor import WhisperAudioProcessor
from replicate_image_generator import ReplicateImageGenerator
from improved_audio_analysis import ImprovedAudioAnalyzer
from PIL import Image
import time

app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Initialize processors
audio_processor = WhisperAudioProcessor()
improved_analyzer = ImprovedAudioAnalyzer()
replicate_key = os.getenv('REPLICATE_API_KEY')
if replicate_key:
    image_generator = ReplicateImageGenerator(api_key=replicate_key)
else:
    image_generator = ReplicateImageGenerator()

def two_stage_pipeline(audio_file_path):
    """Two-stage pipeline: colorful abstract -> representational"""
    
    try:
        # Stage 1: Generate Colorful Abstract Art
        print(f"🎨 STAGE 1: Generate Colorful Abstract Art")
        
        # Use improved analyzer for better feature extraction
        features = improved_analyzer.analyze_audio_file(audio_file_path)
        transcription = audio_processor.transcribe_audio(audio_file_path)
        
        # Detect instruments
        detected_instruments = improved_analyzer.detect_instruments(audio_file_path, transcription)
        
        print(f"📊 Analysis: {features.get('mood', 'unknown')} mood, {features.get('energy_level', 'unknown')} energy")
        print(f"📝 Transcription: {transcription[:100]}...")
        print(f"🎵 Detected instruments: {len(detected_instruments)} found")
        for inst in detected_instruments:
            print(f"  • {inst['name']} (confidence: {inst['confidence']:.2f})")
        if not detected_instruments:
            print(f"  • No instruments detected")
        
        # Create colorful abstract prompt (focus on colors, not representational)
        abstract_prompt = create_colorful_abstract_prompt(features, transcription, detected_instruments)
        print(f"🎯 Abstract Prompt: {abstract_prompt[:200]}...")
        
        # Generate colorful abstract image
        print("🖼️ Generating colorful abstract image...")
        abstract_img = image_generator.generate_image(abstract_prompt)
        
        # Save abstract image
        abstract_filename = f"stage1_abstract_{os.path.splitext(os.path.basename(audio_file_path))[0]}.png"
        abstract_img.save(abstract_filename)
        print(f"✅ Abstract image saved: {abstract_filename}")
        
        # Stage 2: Convert to Representational
        print(f"🖼️ STAGE 2: Convert to Representational Art")
        
        # Create representational prompt
        representational_prompt = create_representational_prompt(features, transcription, detected_instruments)
        print(f"🎯 Representational Prompt: {representational_prompt[:200]}...")
        
        # Generate representational image
        print("🖼️ Generating representational image...")
        representational_img = image_generator.generate_image(representational_prompt)
        
        # Save representational image
        representational_filename = f"stage2_representational_{os.path.splitext(os.path.basename(audio_file_path))[0]}.png"
        representational_img.save(representational_filename)
        print(f"✅ Representational image saved: {representational_filename}")
        
        print(f"📤 Response includes {len(detected_instruments)} detected instruments")
        print(f"📤 Response structure: detected_instruments = {type(detected_instruments)}")
        
        return {
            'success': True,
            'abstract_image': abstract_filename,
            'representational_image': representational_filename,
            'features': features,
            'transcription': transcription,
            'abstract_prompt': abstract_prompt,
            'representational_prompt': representational_prompt,
            'detected_instruments': detected_instruments
        }
        
    except Exception as e:
        print(f"❌ Pipeline error: {e}")
        return {
            'success': False,
            'error': str(e)
        }

def create_colorful_abstract_prompt(features, transcription, detected_instruments=None):
    """Create a prompt focused on colorful abstract art"""
    
    # Get color palette from improved analyzer
    color_palette = improved_analyzer.generate_color_palette(features, detected_instruments)
    
    # Build colorful abstract prompt
    prompt_parts = []
    
    # Color emphasis
    if color_palette['final_colors']:
        prompt_parts.append(f"COLORFUL ABSTRACT ARTWORK featuring {', '.join(color_palette['final_colors'])}")
        prompt_parts.append(f"Color style: {color_palette['description']}")
    
    # Mood and energy
    mood = features.get('mood', 'balanced')
    energy = features.get('energy_level', 'medium')
    prompt_parts.append(f"Abstract art with {mood} mood and {energy} energy")
    
    # Abstract style instructions
    prompt_parts.append("FLUID and ORGANIC abstract forms")
    prompt_parts.append("FLOWING and DYNAMIC composition")
    prompt_parts.append("RICH SATURATED COLORS")
    prompt_parts.append("NO BLACK AND WHITE")
    prompt_parts.append("VIBRANT and INTENSE colors")
    
    # Add transcription if available
    if transcription and transcription.strip():
        prompt_parts.append(f"Audio content: '{transcription.strip()}'")
    
    return " | ".join(prompt_parts)

def create_representational_prompt(features, transcription, detected_instruments=None):
    """Create a prompt focused on representational art"""
    
    # Get color palette from improved analyzer
    color_palette = improved_analyzer.generate_color_palette(features, detected_instruments)
    
    # Build representational prompt
    prompt_parts = []
    
    # Color emphasis
    if color_palette['final_colors']:
        prompt_parts.append(f"REPRESENTATIONAL IMAGE featuring {', '.join(color_palette['final_colors'])}")
        prompt_parts.append(f"Color style: {color_palette['description']}")
    
    # Mood and energy
    mood = features.get('mood', 'balanced')
    energy = features.get('energy_level', 'medium')
    prompt_parts.append(f"Representational art with {mood} mood and {energy} energy")
    
    # Representational style instructions
    prompt_parts.append("CONCRETE SCENES with RECOGNIZABLE OBJECTS")
    prompt_parts.append("REALISTIC and REPRESENTATIONAL imagery")
    prompt_parts.append("NO ABSTRACT ART")
    prompt_parts.append("CREATE CONCRETE SCENES WITH REAL OBJECTS")
    # prompt_parts.append("RICH SATURATED COLORS")
    # prompt_parts.append("NO BLACK AND WHITE")
    
    # Add transcription if available
    if transcription and transcription.strip():
        prompt_parts.append(f"Audio content: '{transcription.strip()}'")
    
    return " | ".join(prompt_parts)

@app.route('/upload', methods=['POST'])
def upload_audio():
    """Handle audio file upload and process with two-stage pipeline"""
    
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file:
        try:
            # Save uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            print(f"📁 File uploaded: {filename}")
            
            # Run two-stage pipeline
            result = two_stage_pipeline(filepath)
            
            if result['success']:
                return jsonify({
                    'success': True,
                    'message': 'Two-stage pipeline completed successfully',
                    'abstract_image': result['abstract_image'],
                    'representational_image': result['representational_image'],
                    'features': result['features'],
                    'transcription': result['transcription'],
                    'abstract_prompt': result['abstract_prompt'],
                    'representational_prompt': result['representational_prompt'],
                    'detected_instruments': result.get('detected_instruments', [])
                })
            else:
                return jsonify({
                    'success': False,
                    'error': result['error']
                }), 500
                
        except Exception as e:
            return jsonify({'error': f'Processing error: {str(e)}'}), 500
        finally:
            # Clean up uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    return jsonify({'error': 'File processing failed'}), 500

@app.route('/images/<filename>')
def get_image(filename):
    """Serve generated images"""
    try:
        return send_file(filename, mimetype='image/png')
    except FileNotFoundError:
        return jsonify({'error': 'Image not found'}), 404

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'service': 'audio-to-image-python',
        'timestamp': time.time()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) 