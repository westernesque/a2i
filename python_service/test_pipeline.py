import os
import sys
from dotenv import load_dotenv
from whisper_processor import WhisperAudioProcessor
from replicate_image_generator import ReplicateImageGenerator

def test_pipeline(audio_file_path):
    """Test the complete audio-to-image pipeline"""
    
    # Load environment variables
    load_dotenv()
    
    # Check if file exists
    if not os.path.exists(audio_file_path):
        print(f"❌ Audio file not found: {audio_file_path}")
        return False
    
    print("🎵🎨 REPLICATE-ONLY PIPELINE TEST")
    print("=" * 40)
    print(f"📁 Audio file: {audio_file_path}")
    print(f"📏 File size: {os.path.getsize(audio_file_path)} bytes")
    
    # Check API keys
    replicate_key = os.getenv('REPLICATE_API_KEY')
    
    print(f"\n🔑 API Keys Status:")
    print(f"  Replicate: {'✅ Found' if replicate_key else '❌ Not found'}")
    
    # Initialize processors
    print(f"\n🔧 Initializing processors...")
    audio_proc = WhisperAudioProcessor()
    
    if replicate_key:
        print("  Using Replicate for AI image generation")
        image_gen = ReplicateImageGenerator(api_key=replicate_key)
    else:
        print("  Using Replicate placeholder for image generation")
        image_gen = ReplicateImageGenerator()
    
    try:
        # Step 1: Audio Analysis
        print(f"\n🎼 STEP 1: Audio Analysis")
        print("-" * 25)
        features = audio_proc.extract_features(audio_file_path)
        
        print(f"📊 Analysis Results:")
        print(f"  Duration: {features.get('duration', 0):.2f} seconds")
        print(f"  Mood: {features.get('mood', 'unknown')}")
        print(f"  Energy: {features.get('energy_level', 'unknown')}")
        print(f"  Style: {features.get('musical_style', 'unknown')}")
        print(f"  Complexity: {features.get('complexity', 'unknown')}")
        
        # Step 2: Transcription
        print(f"\n🎤 STEP 2: Replicate Transcription")
        print("-" * 25)
        transcription = audio_proc.transcribe_audio(audio_file_path)
        
        print(f"📝 Transcription: '{transcription}'")
        
        # Step 3: Art Prompt
        print(f"\n🎨 STEP 3: Art Prompt Generation")
        print("-" * 25)
        prompt = audio_proc.create_art_prompt(features, transcription)
        
        print(f"🎯 Generated Prompt: {prompt}")
        
        # Step 4: Image Generation
        print(f"\n🖼️ STEP 4: Replicate Image Generation")
        print("-" * 25)
        print("Creating AI-generated image...")
        img = image_gen.generate_image(prompt)
        
        # Step 5: Save Result
        print(f"\n💾 STEP 5: Save Result")
        print("-" * 25)
        output_filename = f"replicate_pipeline_result_{os.path.splitext(os.path.basename(audio_file_path))[0]}.png"
        img.save(output_filename)
        print(f"✅ Image saved as: {output_filename}")
        
        # Summary
        print(f"\n🎉 REPLICATE PIPELINE SUCCESS!")
        print("=" * 40)
        print(f"✅ Audio analyzed successfully")
        print(f"✅ Content transcribed: {len(transcription)} characters")
        print(f"✅ Art prompt generated: {len(prompt)} characters")
        print(f"✅ AI image created: {output_filename}")
        print(f"🎵🎨 Audio successfully converted to image using Replicate!")
        
        return True
        
    except Exception as e:
        print(f"❌ Pipeline error: {e}")
        return False

if __name__ == "__main__":
    # Try to find the audio file
    possible_paths = [
        "01 her.m4a",
        "../01 her.m4a",
        "uploads/01 her.m4a",
        "test_files/01 her.m4a"
    ]
    
    audio_found = False
    for path in possible_paths:
        if os.path.exists(path):
            test_pipeline(path)
            audio_found = True
            break
    
    if not audio_found:
        print("❌ Audio file '01 her.m4a' not found")
        print("Please place the audio file in the python_service directory") 