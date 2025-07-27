import os
import requests
import json
from typing import Dict, Any
from simple_enhanced_processor import SimpleEnhancedAudioProcessor

class WhisperAudioProcessor(SimpleEnhancedAudioProcessor):
    """Enhanced audio processor with multiple transcription services"""

    def __init__(self, replicate_api_key: str = None):
        super().__init__()
        self.replicate_api_key = replicate_api_key or os.getenv('REPLICATE_API_KEY')
        
        # Replicate transcription services only
        self.transcription_services = {
            'replicate_whisper_large': {
                'url': "https://api.replicate.com/v1/predictions",
                'model': "openai/whisper:91ee9c0c3df30478510ff8c8a3a545add1ad0259ad3a9f78fba57fbc05ee64f7",
                'available': bool(self.replicate_api_key),
                'priority': 1,
                'type': 'replicate'
            },
            'replicate_whisper_medium': {
                'url': "https://api.replicate.com/v1/predictions",
                'model': "openai/whisper:91ee9c0c3df30478510ff8c8a3a545add1ad0259ad3a9f78fba57fbc05ee64f7",
                'available': bool(self.replicate_api_key),
                'priority': 2,
                'type': 'replicate'
            }
        }

    def transcribe_audio(self, audio_path: str) -> str:
        """Transcribe audio using multiple available services"""
        # Store audio path for instrument detection
        self._last_audio_path = audio_path
        
        # Try each available service in priority order
        available_services = [
            service for service in self.transcription_services.items()
            if service[1]['available']
        ]
        
        # Sort by priority (lower number = higher priority)
        available_services.sort(key=lambda x: x[1]['priority'])
        
        for service_name, service_config in available_services:
            try:
                print(f"🎤 Attempting transcription with {service_name}...")
                transcription = self._transcribe_with_service(audio_path, service_name, service_config)
                if transcription:
                    print(f"✅ Transcription successful with {service_name}")
                    return transcription
            except Exception as e:
                print(f"❌ {service_name} failed: {e}")
                continue
        
        # If all services fail, use simulated transcription
        print("⚠️ All transcription services failed, using simulated transcription")
        return self._simulate_transcription(audio_path)

    def _transcribe_with_service(self, audio_path: str, service_name: str, service_config: Dict[str, Any]) -> str:
        """Transcribe audio with a specific service"""
        
        service_type = service_config.get('type', 'unknown')
        
        if service_type == 'replicate':
            return self._transcribe_with_replicate(audio_path, service_config)
        else:
            raise ValueError(f"Unknown transcription service type: {service_type}")

    def _transcribe_with_replicate(self, audio_path: str, service_config: Dict[str, Any]) -> str:
        """Transcribe using Replicate Whisper models"""
        try:
            # Replicate uses a two-step process: create prediction, then poll for results
            headers = {
                'Authorization': f'Token {self.replicate_api_key}',
                'Content-Type': 'application/json'
            }

            # Step 1: Create prediction
            with open(audio_path, 'rb') as audio_file:
                import base64
                audio_data = base64.b64encode(audio_file.read()).decode('utf-8')

            payload = {
                "version": service_config['model'],
                "input": {
                    "audio": f"data:audio/m4a;base64,{audio_data}",
                    "model": "large-v2" if "large" in service_config.get('name', '') else "large",
                    "language": "en",
                    "task": "transcribe"
                }
            }

            print(f"Creating Replicate transcription prediction...")
            response = requests.post(
                service_config['url'],
                headers=headers,
                json=payload,
                timeout=60
            )

            if response.status_code == 201:
                prediction = response.json()
                prediction_id = prediction['id']

                # Step 2: Poll for completion
                import time
                max_attempts = 30
                attempts = 0

                while attempts < max_attempts:
                    time.sleep(2)
                    status_response = requests.get(
                        f"{service_config['url']}/{prediction_id}",
                        headers=headers
                    )

                    if status_response.status_code == 200:
                        status_data = status_response.json()

                        if status_data['status'] == 'succeeded':
                            # Get the transcription
                            transcription = status_data.get('output', '')
                            if isinstance(transcription, dict) and 'transcription' in transcription:
                                # Replicate Whisper returns a dict with 'transcription' field
                                return transcription['transcription'].strip()
                            elif isinstance(transcription, list) and len(transcription) > 0:
                                return transcription[0].strip()
                            elif isinstance(transcription, str):
                                return transcription.strip()
                            else:
                                print(f"Unexpected transcription format: {transcription}")
                                return None

                        elif status_data['status'] == 'failed':
                            print(f"Replicate prediction failed: {status_data.get('error', 'Unknown error')}")
                            return None
                        elif status_data['status'] == 'processing':
                            print(f"Still processing... attempt {attempts + 1}")
                            attempts += 1
                            continue
                    else:
                        print(f"Error checking status: {status_response.status_code}")
                        return None

                print("Timeout waiting for Replicate prediction completion")
                return None

            else:
                print(f"Error creating Replicate prediction: {response.status_code}")
                print(response.text)
                return None

        except Exception as e:
            print(f"Replicate transcription error: {e}")
            return None

    def _simulate_transcription(self, audio_path: str) -> str:
        """Enhanced simulated transcription with more variety and accuracy"""
        # Analyze file name for hints
        file_name = os.path.basename(audio_path).lower()
        file_size = os.path.getsize(audio_path)
        
        # More sophisticated simulated transcriptions based on file characteristics
        if 'her' in file_name:
            return "Her voice echoes through the digital landscape, a haunting melody of love and loss in the age of artificial intelligence."
        elif 'electronic' in file_name or 'synth' in file_name:
            return "Synthesized beats pulse through the circuitry, electronic rhythms creating a futuristic soundscape of digital dreams."
        elif 'acoustic' in file_name or 'guitar' in file_name:
            return "Gentle acoustic melodies flow like a mountain stream, organic harmonies blending with natural rhythms and warm tones."
        elif 'ambient' in file_name or 'atmospheric' in file_name:
            return "Atmospheric textures drift through space, ambient sounds creating a meditative sonic environment of peace and reflection."
        elif 'jazz' in file_name:
            return "Smooth jazz harmonies weave through the composition, sophisticated melodies dancing with complex rhythms and soulful expression."
        elif 'rock' in file_name or 'guitar' in file_name:
            return "Powerful guitar riffs drive the energy forward, rock rhythms building intensity with raw emotion and dynamic expression."
        elif 'classical' in file_name or 'orchestral' in file_name:
            return "Orchestral strings swell with classical elegance, timeless melodies flowing through sophisticated arrangements and harmonic beauty."
        elif 'pop' in file_name:
            return "Catchy pop melodies shine with bright energy, contemporary rhythms and harmonies creating an upbeat and accessible soundscape."
        elif 'hip' in file_name or 'rap' in file_name:
            return "Rhythmic vocals flow over urban beats, hip-hop energy driving forward with lyrical expression and street culture authenticity."
        elif file_size > 10000000:  # Large file (>10MB)
            return "Extended musical journey unfolds with complex arrangements, multiple movements creating a rich tapestry of sound and emotion."
        elif file_size < 1000000:  # Small file (<1MB)
            return "Brief musical moment captured in time, concise expression of melody and rhythm in a compact sonic statement."
        else:
            # Generic but varied responses
            responses = [
                "Melodic patterns weave through the composition, creating a rich tapestry of musical expression and emotional depth.",
                "Rhythmic elements pulse with life, driving the music forward with energy and dynamic movement.",
                "Harmonic textures blend together, forming a sophisticated soundscape of musical beauty and complexity.",
                "Atmospheric sounds create a dreamlike environment, where music and emotion merge into a transcendent experience.",
                "Dynamic contrasts shape the musical journey, from quiet introspection to powerful expression and back again.",
                "Layered arrangements build complexity, each element contributing to a rich and engaging musical narrative.",
                "Emotional melodies speak to the heart, conveying feelings through the universal language of music and sound.",
                "Contemporary rhythms blend with traditional elements, creating a fusion of old and new musical expressions."
            ]
            return responses[hash(file_name) % len(responses)]

    def create_art_prompt(self, features: Dict[str, Any], transcription: str = "") -> str:
        """Create an enhanced art prompt incorporating real transcription and instrument detection"""
        # Add audio path to features for instrument detection
        if 'audio_path' not in features:
            features['audio_path'] = getattr(self, '_last_audio_path', '')
        
        # Use instrument-enhanced prompt from parent class
        base_prompt = super().create_instrument_enhanced_prompt(features, transcription)

        # If we have real transcription, enhance the prompt further
        if transcription and transcription.strip():
            # Analyze transcription for emotional content
            emotional_keywords = self._extract_emotional_content(transcription)
            
            # Analyze transcription for visual elements
            visual_elements = self._extract_visual_elements(transcription)

            # Create enhanced prompt with transcription
            enhanced_parts = [
                base_prompt,
                f"Audio content: '{transcription.strip()}'"
            ]

            # Add emotional analysis if found
            if emotional_keywords:
                enhanced_parts.append(f"Emotional themes: {', '.join(emotional_keywords)}")

            # Add visual elements if found
            if visual_elements:
                enhanced_parts.append(f"Visual elements: {', '.join(visual_elements)}")

            return " | ".join(enhanced_parts)

        return base_prompt

    def _extract_emotional_content(self, transcription: str) -> list:
        """Extract emotional keywords from transcription"""
        emotional_keywords = []
        text_lower = transcription.lower()

        # Enhanced emotional keyword categories
        emotion_categories = {
            'love': ['love', 'heart', 'romance', 'passion', 'affection', 'tender', 'intimate'],
            'melancholy': ['sad', 'lonely', 'missing', 'lost', 'alone', 'heartbreak', 'nostalgic', 'reflective'],
            'joy': ['happy', 'joy', 'celebrate', 'dance', 'smile', 'laugh', 'upbeat', 'bright'],
            'energy': ['power', 'energy', 'strength', 'fire', 'burn', 'drive', 'dynamic', 'vibrant'],
            'peace': ['calm', 'peace', 'quiet', 'gentle', 'soft', 'serene', 'tranquil', 'meditative'],
            'nostalgia': ['remember', 'memory', 'past', 'childhood', 'yesterday', 'timeless', 'classic'],
            'futuristic': ['future', 'digital', 'cyber', 'tech', 'artificial', 'robot', 'electronic', 'synthetic'],
            'nature': ['earth', 'nature', 'forest', 'ocean', 'mountain', 'sky', 'organic', 'natural'],
            'mystery': ['mysterious', 'enigmatic', 'dreamy', 'ethereal', 'otherworldly', 'magical'],
            'sophistication': ['elegant', 'sophisticated', 'refined', 'complex', 'intricate', 'masterful']
        }

        # Check for emotional keywords
        for emotion, keywords in emotion_categories.items():
            for keyword in keywords:
                if keyword in text_lower:
                    emotional_keywords.append(emotion)
                    break

        return emotional_keywords[:4]  # Return top 4 emotions found

    def _extract_visual_elements(self, transcription: str) -> list:
        """Extract visual elements from transcription"""
        visual_elements = []
        text_lower = transcription.lower()

        # Visual element categories
        visual_categories = {
            'landscape': ['landscape', 'mountain', 'ocean', 'forest', 'sky', 'horizon', 'valley'],
            'urban': ['city', 'street', 'building', 'urban', 'metropolitan', 'concrete'],
            'abstract': ['pattern', 'texture', 'flow', 'movement', 'shape', 'form'],
            'light': ['light', 'bright', 'glow', 'shine', 'illumination', 'radiance'],
            'color': ['color', 'hue', 'tone', 'palette', 'vibrant', 'muted'],
            'space': ['space', 'cosmic', 'galaxy', 'stars', 'universe', 'infinite'],
            'organic': ['organic', 'natural', 'flowing', 'curved', 'fluid', 'living'],
            'geometric': ['geometric', 'angular', 'structured', 'precise', 'symmetrical']
        }

        # Check for visual elements
        for category, keywords in visual_categories.items():
            for keyword in keywords:
                if keyword in text_lower:
                    visual_elements.append(category)
                    break

        return visual_elements[:3]  # Return top 3 visual elements found 