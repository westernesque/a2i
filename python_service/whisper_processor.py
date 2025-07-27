import os
import requests
import json
from typing import Dict, Any
from simple_enhanced_processor import SimpleEnhancedAudioProcessor

class WhisperAudioProcessor(SimpleEnhancedAudioProcessor):
    """Enhanced audio processor with real OpenAI Whisper transcription"""
    
    def __init__(self, openai_api_key: str = None):
        super().__init__()
        self.openai_api_key = openai_api_key or os.getenv('OPENAI_API_KEY')
        self.whisper_url = "https://api.openai.com/v1/audio/transcriptions"
    
    def transcribe_audio(self, audio_path: str) -> str:
        """Transcribe audio using OpenAI Whisper API"""
        if not self.openai_api_key:
            print("No OpenAI API key found, using simulated transcription")
            return self._simulate_transcription(audio_path)
        
        try:
            # Prepare the audio file for upload
            with open(audio_path, 'rb') as audio_file:
                files = {
                    'file': audio_file,
                    'model': (None, 'whisper-1'),
                    'response_format': (None, 'json'),
                    'language': (None, 'en')  # Optional: specify language
                }
                
                headers = {
                    'Authorization': f'Bearer {self.openai_api_key}'
                }
                
                print("🎤 Transcribing audio with OpenAI Whisper...")
                response = requests.post(
                    self.whisper_url,
                    headers=headers,
                    files=files,
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    transcription = result.get('text', '').strip()
                    print(f"✅ Transcription successful: {len(transcription)} characters")
                    return transcription
                else:
                    print(f"❌ Transcription failed: {response.status_code}")
                    print(f"Error: {response.text}")
                    return self._simulate_transcription(audio_path)
                    
        except Exception as e:
            print(f"❌ Transcription error: {e}")
            return self._simulate_transcription(audio_path)
    
    def _simulate_transcription(self, audio_path: str) -> str:
        """Fallback to simulated transcription when Whisper is not available"""
        # Analyze file name for hints
        file_name = os.path.basename(audio_path).lower()
        
        # Return different simulated transcriptions based on file characteristics
        if 'her' in file_name:
            return "Her voice echoes through the digital landscape, a haunting melody of love and loss in the age of artificial intelligence."
        elif 'electronic' in file_name or 'synth' in file_name:
            return "Synthesized beats pulse through the circuitry, electronic rhythms creating a futuristic soundscape."
        elif 'acoustic' in file_name or 'guitar' in file_name:
            return "Gentle acoustic melodies flow like a mountain stream, organic harmonies blending with natural rhythms."
        elif 'ambient' in file_name or 'atmospheric' in file_name:
            return "Atmospheric textures drift through space, ambient sounds creating a meditative sonic environment."
        else:
            return "Melodic patterns weave through the composition, creating a rich tapestry of musical expression."
    
    def create_art_prompt(self, features: Dict[str, Any], transcription: str = "") -> str:
        """Create an enhanced art prompt incorporating real transcription"""
        # Get base prompt from parent class
        base_prompt = super().create_art_prompt(features, transcription)
        
        # If we have real transcription, enhance the prompt
        if transcription and transcription.strip():
            # Analyze transcription for emotional content
            emotional_keywords = self._extract_emotional_content(transcription)
            
            # Create enhanced prompt with transcription
            enhanced_parts = [
                base_prompt,
                f"Audio content: '{transcription.strip()}'"
            ]
            
            # Add emotional analysis if found
            if emotional_keywords:
                enhanced_parts.append(f"Emotional themes: {', '.join(emotional_keywords)}")
            
            return " | ".join(enhanced_parts)
        
        return base_prompt
    
    def _extract_emotional_content(self, transcription: str) -> list:
        """Extract emotional keywords from transcription"""
        emotional_keywords = []
        text_lower = transcription.lower()
        
        # Define emotional keyword categories
        emotion_categories = {
            'love': ['love', 'heart', 'romance', 'passion', 'affection'],
            'melancholy': ['sad', 'lonely', 'missing', 'lost', 'alone', 'heartbreak'],
            'joy': ['happy', 'joy', 'celebrate', 'dance', 'smile', 'laugh'],
            'energy': ['power', 'energy', 'strength', 'fire', 'burn', 'drive'],
            'peace': ['calm', 'peace', 'quiet', 'gentle', 'soft', 'serene'],
            'nostalgia': ['remember', 'memory', 'past', 'childhood', 'yesterday'],
            'futuristic': ['future', 'digital', 'cyber', 'tech', 'artificial', 'robot'],
            'nature': ['earth', 'nature', 'forest', 'ocean', 'mountain', 'sky']
        }
        
        # Check for emotional keywords
        for emotion, keywords in emotion_categories.items():
            for keyword in keywords:
                if keyword in text_lower:
                    emotional_keywords.append(emotion)
                    break
        
        return emotional_keywords[:3]  # Return top 3 emotions found 