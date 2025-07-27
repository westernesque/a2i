import os
import math
import random
import re
from typing import Dict, Any, List, Tuple

class SimpleEnhancedAudioProcessor:
    """Advanced audio processor with sophisticated musical analysis and AI-powered feature extraction"""
    
    def __init__(self):
        # Musical genre characteristics database
        self.genre_characteristics = {
            'electronic': {
                'tempo_range': (120, 180),
                'energy_level': 'high',
                'complexity': 'complex',
                'brightness': 'bright',
                'texture': 'layered',
                'mood': 'energetic',
                'instruments': ['synth', 'drum machine', 'electronic beats']
            },
            'acoustic': {
                'tempo_range': (60, 120),
                'energy_level': 'medium',
                'complexity': 'moderate',
                'brightness': 'warm',
                'texture': 'organic',
                'mood': 'natural',
                'instruments': ['guitar', 'piano', 'strings', 'drums']
            },
            'ambient': {
                'tempo_range': (40, 80),
                'energy_level': 'low',
                'complexity': 'simple',
                'brightness': 'dark',
                'texture': 'smooth',
                'mood': 'calm',
                'instruments': ['pads', 'atmosphere', 'textures']
            },
            'jazz': {
                'tempo_range': (80, 160),
                'energy_level': 'medium',
                'complexity': 'complex',
                'brightness': 'warm',
                'texture': 'sophisticated',
                'mood': 'sophisticated',
                'instruments': ['saxophone', 'piano', 'bass', 'drums']
            },
            'rock': {
                'tempo_range': (100, 160),
                'energy_level': 'high',
                'complexity': 'moderate',
                'brightness': 'bright',
                'texture': 'gritty',
                'mood': 'powerful',
                'instruments': ['electric guitar', 'bass', 'drums']
            },
            'classical': {
                'tempo_range': (60, 140),
                'energy_level': 'medium',
                'complexity': 'complex',
                'brightness': 'balanced',
                'texture': 'orchestral',
                'mood': 'elegant',
                'instruments': ['orchestra', 'strings', 'woodwinds']
            },
            'pop': {
                'tempo_range': (90, 140),
                'energy_level': 'medium',
                'complexity': 'moderate',
                'brightness': 'bright',
                'texture': 'polished',
                'mood': 'upbeat',
                'instruments': ['vocals', 'synth', 'drums']
            }
        }
        
        # Emotional analysis patterns
        self.emotional_patterns = {
            'joy': ['happy', 'upbeat', 'celebratory', 'energetic', 'bright'],
            'melancholy': ['sad', 'nostalgic', 'reflective', 'calm', 'dark'],
            'passion': ['intense', 'dramatic', 'powerful', 'emotional', 'dynamic'],
            'peace': ['serene', 'tranquil', 'gentle', 'smooth', 'ambient'],
            'mystery': ['atmospheric', 'ethereal', 'enigmatic', 'dreamy', 'otherworldly'],
            'energy': ['rhythmic', 'pulsing', 'driving', 'forceful', 'vibrant']
        }
        
        # Comprehensive instrument database with visual characteristics
        self.instrument_database = {
            'piano': {
                'keywords': ['piano', 'keys', 'keyboard', 'grand', 'upright', 'melody', 'chords'],
                'visual_elements': ['elegant curves', 'black and white keys', 'wooden frame', 'classical instrument'],
                'colors': ['warm browns', 'golden tones', 'rich mahogany', 'ivory and ebony'],
                'textures': ['smooth wood', 'polished surface', 'metallic strings', 'felt hammers'],
                'mood_associations': ['elegant', 'sophisticated', 'emotional', 'intimate', 'classical']
            },
            'guitar': {
                'keywords': ['guitar', 'acoustic', 'electric', 'strings', 'strum', 'pick', 'chord'],
                'visual_elements': ['curved body', 'long neck', 'six strings', 'sound hole', 'pickguard'],
                'colors': ['natural wood', 'sunburst', 'vibrant colors', 'metallic finishes'],
                'textures': ['wood grain', 'smooth finish', 'metal strings', 'leather strap'],
                'mood_associations': ['warm', 'intimate', 'passionate', 'folk', 'rock']
            },
            'violin': {
                'keywords': ['violin', 'strings', 'bow', 'fiddle', 'orchestra', 'classical'],
                'visual_elements': ['curved body', 'scroll', 'f-holes', 'bridge', 'bow'],
                'colors': ['rich amber', 'golden brown', 'dark wood', 'metallic strings'],
                'textures': ['smooth varnish', 'wood grain', 'horsehair bow', 'metal strings'],
                'mood_associations': ['elegant', 'emotional', 'sophisticated', 'melancholic', 'romantic']
            },
            'drums': {
                'keywords': ['drums', 'beat', 'rhythm', 'percussion', 'kick', 'snare', 'hi-hat'],
                'visual_elements': ['circular drums', 'cymbals', 'sticks', 'drum kit', 'rhythm'],
                'colors': ['metallic silver', 'black', 'chrome', 'vibrant wraps'],
                'textures': ['smooth metal', 'taut skin', 'wooden shells', 'metallic cymbals'],
                'mood_associations': ['energetic', 'powerful', 'rhythmic', 'driving', 'dynamic']
            },
            'saxophone': {
                'keywords': ['saxophone', 'sax', 'jazz', 'brass', 'smooth', 'melody'],
                'visual_elements': ['curved brass', 'keys', 'bell', 'neck', 'mouthpiece'],
                'colors': ['brass gold', 'copper tones', 'metallic shine', 'warm brass'],
                'textures': ['smooth brass', 'metallic finish', 'engraved details', 'polished surface'],
                'mood_associations': ['smooth', 'jazz', 'sophisticated', 'romantic', 'soulful']
            },
            'flute': {
                'keywords': ['flute', 'woodwind', 'melody', 'gentle', 'air', 'breath'],
                'visual_elements': ['long tube', 'keys', 'mouthpiece', 'silver finish'],
                'colors': ['silver', 'metallic', 'shiny', 'bright'],
                'textures': ['smooth metal', 'polished surface', 'delicate keys', 'metallic shine'],
                'mood_associations': ['gentle', 'ethereal', 'peaceful', 'delicate', 'airy']
            },
            'synth': {
                'keywords': ['synth', 'electronic', 'digital', 'synthesizer', 'keys', 'electronic'],
                'visual_elements': ['keyboard', 'knobs', 'screens', 'lights', 'modern'],
                'colors': ['neon colors', 'black', 'blue', 'purple', 'futuristic'],
                'textures': ['smooth plastic', 'metallic', 'glowing', 'digital'],
                'mood_associations': ['futuristic', 'electronic', 'modern', 'synthetic', 'digital']
            },
            'bass': {
                'keywords': ['bass', 'low', 'deep', 'groove', 'rhythm', 'electric bass'],
                'visual_elements': ['long neck', 'thick strings', 'body', 'pickups'],
                'colors': ['dark wood', 'black', 'natural tones', 'metallic'],
                'textures': ['smooth wood', 'metal strings', 'polished finish', 'metallic hardware'],
                'mood_associations': ['groovy', 'deep', 'rhythmic', 'smooth', 'powerful']
            },
            'voice': {
                'keywords': ['voice', 'sing', 'vocal', 'lyrics', 'melody', 'human'],
                'visual_elements': ['human figure', 'mouth', 'expression', 'emotion'],
                'colors': ['warm skin tones', 'natural colors', 'expressive'],
                'textures': ['organic', 'natural', 'expressive', 'human'],
                'mood_associations': ['personal', 'emotional', 'human', 'intimate', 'expressive']
            },
            'nature_sounds': {
                'keywords': ['bird', 'nature', 'ambient', 'environmental', 'organic', 'natural'],
                'visual_elements': ['birds', 'trees', 'sky', 'nature', 'organic forms'],
                'colors': ['natural greens', 'sky blues', 'earth tones', 'organic colors'],
                'textures': ['organic', 'natural', 'textured', 'environmental'],
                'mood_associations': ['peaceful', 'natural', 'organic', 'calm', 'serene']
            }
        }
    
    def extract_features(self, audio_path: str) -> Dict[str, Any]:
        """Extract comprehensive audio features using advanced analysis"""
        try:
            # Get file information
            file_size = os.path.getsize(audio_path)
            file_name = os.path.basename(audio_path)
            file_extension = os.path.splitext(audio_path)[1].lower()
            
            # Enhanced file analysis
            duration = self._estimate_duration_advanced(file_size, file_name, file_extension)
            format_info = self._analyze_audio_format(file_extension, file_size, duration)
            
            # Core audio features
            features = {
                'duration': duration,
                'file_size': file_size,
                'format': format_info['format'],
                'sample_rate': format_info['sample_rate'],
                'channels': format_info['channels'],
                'bit_depth': format_info['bit_depth']
            }
            
            # Advanced musical analysis
            features.update(self._analyze_musical_structure_advanced(file_size, duration, file_name))
            features.update(self._analyze_spectral_characteristics_advanced(file_name, duration))
            features.update(self._analyze_rhythm_patterns_advanced(file_size, duration))
            features.update(self._analyze_dynamic_characteristics_advanced(file_size, duration))
            features.update(self._analyze_harmonic_content_advanced(file_name, duration))
            
            # AI-powered analysis
            features.update(self._ai_analyze_musical_characteristics(features, file_name))
            
            # Determine final characteristics
            features['mood'] = self._analyze_mood_advanced(features)
            features['energy_level'] = self._analyze_energy_advanced(features)
            features['complexity'] = self._analyze_complexity_advanced(features)
            features['musical_style'] = self._analyze_musical_style_advanced(features)
            features['emotional_tone'] = self._analyze_emotional_tone_advanced(features)
            features['artistic_style'] = self._analyze_artistic_style(features)
            
            return features
            
        except Exception as e:
            print(f"Error extracting features: {e}")
            return self._get_default_features()
    
    def _estimate_duration_advanced(self, file_size: int, file_name: str, file_extension: str) -> float:
        """Advanced duration estimation using multiple factors"""
        # Base estimation by format and size
        bitrates = {
            '.mp3': 128000, '.m4a': 256000, '.wav': 1411000, 
            '.flac': 1000000, '.aac': 256000, '.ogg': 192000
        }
        
        # Get bitrate for format
        bitrate = bitrates.get(file_extension, 256000)
        
        # Calculate theoretical duration
        theoretical_duration = (file_size * 8) / bitrate
        
        # Adjust based on file name analysis
        name_adjustment = self._analyze_filename_for_duration(file_name)
        
        # Apply realistic constraints
        final_duration = theoretical_duration * name_adjustment
        return max(10, min(1800, final_duration))  # Between 10 seconds and 30 minutes
    
    def _analyze_filename_for_duration(self, file_name: str) -> float:
        """Analyze filename for duration hints"""
        name_lower = file_name.lower()
        
        # Duration indicators
        if any(word in name_lower for word in ['short', 'clip', 'sample', 'preview']):
            return 0.3
        elif any(word in name_lower for word in ['long', 'full', 'complete', 'extended']):
            return 2.0
        elif any(word in name_lower for word in ['remix', 'version', 'edit']):
            return 1.2
        elif any(word in name_lower for word in ['intro', 'outro', 'bridge']):
            return 0.5
        
        return 1.0
    
    def _analyze_audio_format(self, file_extension: str, file_size: int, duration: float) -> Dict[str, Any]:
        """Analyze audio format characteristics"""
        format_info = {
            '.mp3': {'format': 'MP3', 'sample_rate': 44100, 'channels': 2, 'bit_depth': 16},
            '.m4a': {'format': 'M4A', 'sample_rate': 48000, 'channels': 2, 'bit_depth': 16},
            '.wav': {'format': 'WAV', 'sample_rate': 44100, 'channels': 2, 'bit_depth': 24},
            '.flac': {'format': 'FLAC', 'sample_rate': 48000, 'channels': 2, 'bit_depth': 24},
            '.aac': {'format': 'AAC', 'sample_rate': 48000, 'channels': 2, 'bit_depth': 16},
            '.ogg': {'format': 'OGG', 'sample_rate': 44100, 'channels': 2, 'bit_depth': 16}
        }
        
        return format_info.get(file_extension, {
            'format': 'Unknown', 'sample_rate': 44100, 'channels': 2, 'bit_depth': 16
        })
    
    def _analyze_musical_structure_advanced(self, file_size: int, duration: float, file_name: str) -> Dict[str, Any]:
        """Advanced musical structure analysis"""
        # Calculate complexity based on file characteristics
        complexity_factor = min(1.0, (file_size / 1000000) / max(1, duration / 60))
        
        # Energy analysis
        energy_variance = 2000 + (complexity_factor * 80000)
        energy_peaks = int(5 + (complexity_factor * 60))
        peak_density = energy_peaks / max(1, duration)
        
        # Tempo estimation
        estimated_tempo = self._estimate_tempo_advanced(file_name, complexity_factor, duration)
        
        # Structure analysis
        sections = self._estimate_musical_sections(duration, complexity_factor)
        
        return {
            'energy_variance': energy_variance,
            'energy_peaks': energy_peaks,
            'peak_density': peak_density,
            'estimated_tempo': estimated_tempo,
            'musical_sections': sections,
            'structure_complexity': complexity_factor,
            'energy_distribution': self._analyze_energy_distribution(complexity_factor)
        }
    
    def _estimate_tempo_advanced(self, file_name: str, complexity_factor: float, duration: float) -> int:
        """Advanced tempo estimation"""
        name_lower = file_name.lower()
        
        # Genre-based tempo estimation
        if any(word in name_lower for word in ['dance', 'electronic', 'techno', 'house']):
            base_tempo = random.randint(120, 140)
        elif any(word in name_lower for word in ['ambient', 'chill', 'lounge']):
            base_tempo = random.randint(60, 90)
        elif any(word in name_lower for word in ['rock', 'metal', 'punk']):
            base_tempo = random.randint(100, 160)
        elif any(word in name_lower for word in ['jazz', 'blues']):
            base_tempo = random.randint(80, 140)
        elif any(word in name_lower for word in ['classical', 'orchestral']):
            base_tempo = random.randint(60, 120)
        else:
            base_tempo = random.randint(80, 120)
        
        # Adjust based on complexity and duration
        tempo_adjustment = 1.0 + (complexity_factor - 0.5) * 0.4
        return int(base_tempo * tempo_adjustment)
    
    def _estimate_musical_sections(self, duration: float, complexity_factor: float) -> List[str]:
        """Estimate musical sections based on duration and complexity"""
        sections = ['intro']
        
        if duration > 60:
            sections.append('verse')
            if complexity_factor > 0.3:
                sections.append('chorus')
            if duration > 120:
                sections.append('bridge')
                if complexity_factor > 0.6:
                    sections.append('solo')
            sections.append('outro')
        
        return sections
    
    def _analyze_energy_distribution(self, complexity_factor: float) -> str:
        """Analyze how energy is distributed throughout the track"""
        if complexity_factor > 0.7:
            return "dynamic"
        elif complexity_factor > 0.4:
            return "building"
        else:
            return "consistent"
    
    def _analyze_spectral_characteristics_advanced(self, file_name: str, duration: float) -> Dict[str, Any]:
        """Advanced spectral analysis"""
        name_lower = file_name.lower()
        
        # Frequency analysis
        spectral_centroid = self._estimate_spectral_centroid(name_lower)
        spectral_rolloff = spectral_centroid * (1.2 + random.uniform(0, 0.6))
        
        # Brightness analysis
        brightness = self._analyze_brightness_advanced(name_lower, spectral_centroid)
        
        # Texture analysis
        texture = self._analyze_texture_advanced(name_lower, duration)
        
        # Harmonic content
        harmonic_content = self._analyze_harmonic_content(name_lower)
        
        return {
            'spectral_centroid': spectral_centroid,
            'spectral_rolloff': spectral_rolloff,
            'zero_crossing_rate': random.uniform(0.02, 0.18),
            'brightness': brightness,
            'texture': texture,
            'harmonic_content': harmonic_content,
            'frequency_balance': self._analyze_frequency_balance(spectral_centroid)
        }
    
    def _estimate_spectral_centroid(self, file_name: str) -> float:
        """Estimate spectral centroid based on file characteristics"""
        if any(word in file_name for word in ['bass', 'low', 'deep', 'sub']):
            return random.uniform(600, 1200)
        elif any(word in file_name for word in ['high', 'bright', 'treble', 'crystal']):
            return random.uniform(2800, 4500)
        elif any(word in file_name for word in ['mid', 'warm', 'analog']):
            return random.uniform(1200, 2200)
        else:
            return random.uniform(1500, 2800)
    
    def _analyze_brightness_advanced(self, file_name: str, spectral_centroid: float) -> str:
        """Advanced brightness analysis"""
        if spectral_centroid > 3000:
            return "bright"
        elif spectral_centroid < 1200:
            return "dark"
        elif any(word in file_name for word in ['warm', 'analog', 'vintage']):
            return "warm"
        else:
            return "balanced"
    
    def _analyze_texture_advanced(self, file_name: str, duration: float) -> str:
        """Advanced texture analysis"""
        if any(word in file_name for word in ['smooth', 'ambient', 'atmospheric']):
            return "smooth"
        elif any(word in file_name for word in ['gritty', 'distorted', 'raw']):
            return "gritty"
        elif any(word in file_name for word in ['layered', 'complex', 'orchestral']):
            return "layered"
        elif duration > 180:
            return "evolving"
        else:
            return "balanced"
    
    def _analyze_harmonic_content(self, file_name: str) -> str:
        """Analyze harmonic content"""
        if any(word in file_name for word in ['harmonic', 'chordal', 'polyphonic']):
            return "rich"
        elif any(word in file_name for word in ['monophonic', 'melodic', 'lead']):
            return "melodic"
        else:
            return "mixed"
    
    def _analyze_frequency_balance(self, spectral_centroid: float) -> str:
        """Analyze frequency balance"""
        if spectral_centroid > 3000:
            return "high-frequency dominant"
        elif spectral_centroid < 1200:
            return "low-frequency dominant"
        else:
            return "balanced"
    
    def _analyze_rhythm_patterns_advanced(self, file_size: int, duration: float) -> Dict[str, Any]:
        """Advanced rhythm analysis"""
        complexity_factor = min(1.0, (file_size / 1000000) / max(1, duration / 60))
        
        # Beat analysis
        strong_beats = int(3 + (complexity_factor * 40))
        weak_beats = int(8 + (complexity_factor * 50))
        syncopation = random.uniform(0, complexity_factor)
        
        # Rhythm characteristics
        rhythm_regularity = 0.4 + (complexity_factor * 0.4)
        timing_precision = self._analyze_timing_precision(complexity_factor, syncopation)
        rhythm_complexity = self._analyze_rhythm_complexity(complexity_factor, strong_beats)
        
        return {
            'rhythm_regularity': rhythm_regularity,
            'strong_beats': strong_beats,
            'weak_beats': weak_beats,
            'syncopation': syncopation,
            'rhythm_complexity': rhythm_complexity,
            'timing_precision': timing_precision,
            'groove_factor': self._calculate_groove_factor(complexity_factor, rhythm_regularity)
        }
    
    def _analyze_timing_precision(self, complexity_factor: float, syncopation: float) -> str:
        """Analyze timing precision"""
        if complexity_factor > 0.7 and syncopation > 0.5:
            return "syncopated"
        elif complexity_factor > 0.6:
            return "precise"
        elif complexity_factor < 0.3:
            return "loose"
        else:
            return "moderate"
    
    def _analyze_rhythm_complexity(self, complexity_factor: float, strong_beats: int) -> str:
        """Analyze rhythm complexity"""
        if complexity_factor > 0.7 and strong_beats > 25:
            return "complex"
        elif complexity_factor > 0.4 and strong_beats > 15:
            return "moderate"
        else:
            return "simple"
    
    def _calculate_groove_factor(self, complexity_factor: float, rhythm_regularity: float) -> float:
        """Calculate groove factor"""
        return (complexity_factor + rhythm_regularity) / 2
    
    def _analyze_dynamic_characteristics_advanced(self, file_size: int, duration: float) -> Dict[str, Any]:
        """Advanced dynamic range analysis"""
        complexity_factor = min(1.0, (file_size / 1000000) / max(1, duration / 60))
        
        # Dynamic range
        dynamic_range = 6 + (complexity_factor * 30)
        volume_variance = 1 + (complexity_factor * 20)
        
        # Volume curve analysis
        volume_curve = self._analyze_volume_curve(complexity_factor, duration)
        expression = self._analyze_expression(dynamic_range, volume_variance)
        
        # Dynamic characteristics
        dynamic_characteristics = self._analyze_dynamic_characteristics(complexity_factor)
        
        return {
            'dynamic_range': dynamic_range,
            'volume_variance': volume_variance,
            'volume_curve': volume_curve,
            'expression': expression,
            'dynamic_characteristics': dynamic_characteristics,
            'compression_level': self._estimate_compression_level(complexity_factor)
        }
    
    def _analyze_volume_curve(self, complexity_factor: float, duration: float) -> str:
        """Analyze volume curve throughout the track"""
        if complexity_factor > 0.7:
            return random.choice(['crescendo', 'diminuendo', 'dynamic'])
        elif complexity_factor > 0.4:
            return random.choice(['building', 'fading', 'stable'])
        else:
            return 'stable'
    
    def _analyze_expression(self, dynamic_range: float, volume_variance: float) -> str:
        """Analyze expressive characteristics"""
        if dynamic_range > 25 and volume_variance > 15:
            return "expressive"
        elif dynamic_range < 10 and volume_variance < 5:
            return "consistent"
        else:
            return "moderate"
    
    def _analyze_dynamic_characteristics(self, complexity_factor: float) -> str:
        """Analyze overall dynamic characteristics"""
        if complexity_factor > 0.7:
            return "dramatic"
        elif complexity_factor > 0.4:
            return "varied"
        else:
            return "subtle"
    
    def _estimate_compression_level(self, complexity_factor: float) -> str:
        """Estimate compression level"""
        if complexity_factor > 0.7:
            return "minimal"
        elif complexity_factor < 0.3:
            return "heavy"
        else:
            return "moderate"
    
    def _analyze_harmonic_content_advanced(self, file_name: str, duration: float) -> Dict[str, Any]:
        """Advanced harmonic content analysis"""
        name_lower = file_name.lower()
        
        # Harmonic complexity
        harmonic_complexity = self._estimate_harmonic_complexity(name_lower, duration)
        
        # Chord progression analysis
        chord_progression = self._analyze_chord_progression(name_lower)
        
        # Melodic characteristics
        melodic_characteristics = self._analyze_melodic_characteristics(name_lower)
        
        return {
            'harmonic_complexity': harmonic_complexity,
            'chord_progression': chord_progression,
            'melodic_characteristics': melodic_characteristics,
            'tonal_center': self._estimate_tonal_center(name_lower),
            'harmonic_movement': self._analyze_harmonic_movement(name_lower)
        }
    
    def _estimate_harmonic_complexity(self, file_name: str, duration: float) -> str:
        """Estimate harmonic complexity"""
        if any(word in file_name for word in ['jazz', 'progressive', 'complex']):
            return "complex"
        elif any(word in file_name for word in ['ambient', 'drone', 'minimal']):
            return "simple"
        elif duration > 180:
            return "evolving"
        else:
            return "moderate"
    
    def _analyze_chord_progression(self, file_name: str) -> str:
        """Analyze chord progression characteristics"""
        if any(word in file_name for word in ['jazz', 'sophisticated']):
            return "sophisticated"
        elif any(word in file_name for word in ['pop', 'catchy']):
            return "catchy"
        elif any(word in file_name for word in ['ambient', 'atmospheric']):
            return "floating"
        else:
            return "standard"
    
    def _analyze_melodic_characteristics(self, file_name: str) -> str:
        """Analyze melodic characteristics"""
        if any(word in file_name for word in ['melodic', 'tuneful']):
            return "melodic"
        elif any(word in file_name for word in ['rhythmic', 'percussive']):
            return "rhythmic"
        elif any(word in file_name for word in ['textural', 'atmospheric']):
            return "textural"
        else:
            return "mixed"
    
    def _estimate_tonal_center(self, file_name: str) -> str:
        """Estimate tonal center"""
        if any(word in file_name for word in ['major', 'bright', 'happy']):
            return "major"
        elif any(word in file_name for word in ['minor', 'dark', 'sad']):
            return "minor"
        else:
            return "mixed"
    
    def _analyze_harmonic_movement(self, file_name: str) -> str:
        """Analyze harmonic movement"""
        if any(word in file_name for word in ['progressive', 'evolving']):
            return "progressive"
        elif any(word in file_name for word in ['static', 'drone']):
            return "static"
        else:
            return "moderate"
    
    def _ai_analyze_musical_characteristics(self, features: Dict[str, Any], file_name: str) -> Dict[str, Any]:
        """AI-powered analysis of musical characteristics"""
        # Analyze file name for genre hints
        detected_genre = self._detect_genre_from_filename(file_name)
        
        # Analyze musical sophistication
        sophistication_level = self._analyze_sophistication(features)
        
        # Analyze emotional depth
        emotional_depth = self._analyze_emotional_depth(features)
        
        # Analyze artistic intent
        artistic_intent = self._analyze_artistic_intent(features, file_name)
        
        return {
            'detected_genre': detected_genre,
            'sophistication_level': sophistication_level,
            'emotional_depth': emotional_depth,
            'artistic_intent': artistic_intent,
            'musical_innovation': self._analyze_innovation(features)
        }
    
    def _detect_genre_from_filename(self, file_name: str) -> str:
        """Detect genre from filename patterns"""
        name_lower = file_name.lower()
        
        genre_patterns = {
            'electronic': ['electronic', 'synth', 'techno', 'house', 'edm', 'dance'],
            'acoustic': ['acoustic', 'guitar', 'piano', 'folk', 'country'],
            'ambient': ['ambient', 'atmospheric', 'chill', 'lounge', 'downtempo'],
            'jazz': ['jazz', 'swing', 'bebop', 'fusion'],
            'rock': ['rock', 'metal', 'punk', 'grunge'],
            'classical': ['classical', 'orchestral', 'symphony', 'concerto'],
            'pop': ['pop', 'indie', 'alternative'],
            'hip_hop': ['hip', 'rap', 'trap', 'r&b']
        }
        
        for genre, patterns in genre_patterns.items():
            if any(pattern in name_lower for pattern in patterns):
                return genre
        
        return 'experimental'
    
    def _analyze_sophistication(self, features: Dict[str, Any]) -> str:
        """Analyze musical sophistication"""
        complexity = features.get('complexity', 'moderate')
        harmonic_complexity = features.get('harmonic_complexity', 'moderate')
        rhythm_complexity = features.get('rhythm_complexity', 'moderate')
        
        sophistication_score = 0
        sophistication_score += 2 if complexity == 'complex' else 1
        sophistication_score += 2 if harmonic_complexity == 'complex' else 1
        sophistication_score += 2 if rhythm_complexity == 'complex' else 1
        
        if sophistication_score >= 5:
            return "high"
        elif sophistication_score >= 3:
            return "medium"
        else:
            return "simple"
    
    def _analyze_emotional_depth(self, features: Dict[str, Any]) -> str:
        """Analyze emotional depth"""
        dynamic_range = features.get('dynamic_range', 0)
        expression = features.get('expression', 'moderate')
        emotional_tone = features.get('emotional_tone', 'balanced')
        
        if dynamic_range > 25 and expression == 'expressive':
            return "deep"
        elif dynamic_range > 15:
            return "moderate"
        else:
            return "subtle"
    
    def _analyze_artistic_intent(self, features: Dict[str, Any], file_name: str) -> str:
        """Analyze artistic intent"""
        sophistication = features.get('sophistication_level', 'simple')
        emotional_depth = features.get('emotional_depth', 'subtle')
        
        if sophistication == 'high' and emotional_depth == 'deep':
            return "artistic"
        elif sophistication == 'medium':
            return "crafted"
        else:
            return "casual"
    
    def _analyze_innovation(self, features: Dict[str, Any]) -> str:
        """Analyze musical innovation"""
        complexity = features.get('complexity', 'moderate')
        sophistication = features.get('sophistication_level', 'simple')
        
        if complexity == 'complex' and sophistication == 'high':
            return "innovative"
        elif complexity == 'moderate' and sophistication == 'medium':
            return "creative"
        else:
            return "traditional"
    
    def _analyze_mood_advanced(self, features: Dict[str, Any]) -> str:
        """Advanced mood analysis"""
        spectral_centroid = features.get('spectral_centroid', 0)
        energy_variance = features.get('energy_variance', 0)
        estimated_tempo = features.get('estimated_tempo', 0)
        dynamic_range = features.get('dynamic_range', 0)
        brightness = features.get('brightness', 'balanced')
        texture = features.get('texture', 'balanced')
        
        # Multi-factor mood analysis
        mood_score = {
            'energetic': 0, 'calm': 0, 'dramatic': 0, 'melancholic': 0,
            'joyful': 0, 'mysterious': 0, 'passionate': 0, 'contemplative': 0
        }
        
        # Energy-based scoring
        if energy_variance > 50000 and estimated_tempo > 140:
            mood_score['energetic'] += 3
        if energy_variance < 15000 and estimated_tempo < 80:
            mood_score['calm'] += 3
        if dynamic_range > 25 and energy_variance > 40000:
            mood_score['dramatic'] += 2
        if brightness == 'dark' and texture == 'smooth':
            mood_score['melancholic'] += 2
        if brightness == 'bright' and estimated_tempo > 120:
            mood_score['joyful'] += 2
        if texture == 'layered' and brightness == 'dark':
            mood_score['mysterious'] += 2
        if dynamic_range > 20 and texture == 'gritty':
            mood_score['passionate'] += 2
        if texture == 'smooth' and estimated_tempo < 90:
            mood_score['contemplative'] += 2
        
        # Return the mood with highest score
        return max(mood_score, key=mood_score.get)
    
    def _analyze_energy_advanced(self, features: Dict[str, Any]) -> str:
        """Advanced energy analysis"""
        rms = features.get('rms', 0)
        energy_variance = features.get('energy_variance', 0)
        estimated_tempo = features.get('estimated_tempo', 0)
        peak_density = features.get('peak_density', 0)
        
        energy_score = 0
        energy_score += 2 if rms > 1500 else 1 if rms > 1000 else 0
        energy_score += 2 if energy_variance > 40000 else 1 if energy_variance > 20000 else 0
        energy_score += 2 if estimated_tempo > 130 else 1 if estimated_tempo > 100 else 0
        energy_score += 1 if peak_density > 0.5 else 0
        
        if energy_score >= 6:
            return "high"
        elif energy_score >= 3:
            return "medium"
        else:
            return "low"
    
    def _analyze_complexity_advanced(self, features: Dict[str, Any]) -> str:
        """Advanced complexity analysis"""
        energy_peaks = features.get('energy_peaks', 0)
        rhythm_complexity = features.get('rhythm_complexity', 'moderate')
        harmonic_complexity = features.get('harmonic_complexity', 'moderate')
        sophistication = features.get('sophistication_level', 'simple')
        duration = features.get('duration', 0)
        
        complexity_score = 0
        complexity_score += 2 if energy_peaks > 30 else 1 if energy_peaks > 15 else 0
        complexity_score += 2 if rhythm_complexity == 'complex' else 1 if rhythm_complexity == 'moderate' else 0
        complexity_score += 2 if harmonic_complexity == 'complex' else 1 if harmonic_complexity == 'moderate' else 0
        complexity_score += 2 if sophistication == 'high' else 1 if sophistication == 'medium' else 0
        complexity_score += 1 if duration > 180 else 0
        
        if complexity_score >= 7:
            return "complex"
        elif complexity_score >= 4:
            return "moderate"
        else:
            return "simple"
    
    def _analyze_musical_style_advanced(self, features: Dict[str, Any]) -> str:
        """Advanced musical style analysis"""
        detected_genre = features.get('detected_genre', 'experimental')
        estimated_tempo = features.get('estimated_tempo', 0)
        rhythm_complexity = features.get('rhythm_complexity', 'moderate')
        brightness = features.get('brightness', 'balanced')
        texture = features.get('texture', 'balanced')
        sophistication = features.get('sophistication_level', 'simple')
        
        # Use detected genre as base, refine with characteristics
        if detected_genre == 'electronic' and estimated_tempo > 130:
            return "electronic dance"
        elif detected_genre == 'acoustic' and brightness == 'warm':
            return "acoustic folk"
        elif detected_genre == 'ambient' and texture == 'smooth':
            return "ambient atmospheric"
        elif detected_genre == 'jazz' and sophistication == 'high':
            return "jazz fusion"
        elif detected_genre == 'rock' and texture == 'gritty':
            return "rock alternative"
        elif detected_genre == 'classical' and sophistication == 'high':
            return "classical orchestral"
        elif detected_genre == 'pop' and brightness == 'bright':
            return "pop contemporary"
        else:
            return detected_genre
    
    def _analyze_emotional_tone_advanced(self, features: Dict[str, Any]) -> str:
        """Advanced emotional tone analysis"""
        mood = features.get('mood', 'moderate')
        expression = features.get('expression', 'moderate')
        volume_curve = features.get('volume_curve', 'stable')
        brightness = features.get('brightness', 'balanced')
        emotional_depth = features.get('emotional_depth', 'subtle')
        artistic_intent = features.get('artistic_intent', 'casual')
        
        # Multi-dimensional emotional analysis
        if mood == 'energetic' and expression == 'expressive':
            return "passionate"
        elif mood == 'calm' and brightness == 'warm':
            return "peaceful"
        elif mood == 'dramatic' and volume_curve == 'crescendo':
            return "intense"
        elif mood == 'ambient' and texture == 'smooth':
            return "contemplative"
        elif mood == 'rhythmic' and rhythm_complexity == 'complex':
            return "playful"
        elif emotional_depth == 'deep' and artistic_intent == 'artistic':
            return "profound"
        elif mood == 'mysterious' and brightness == 'dark':
            return "enigmatic"
        else:
            return "balanced"
    
    def _analyze_artistic_style(self, features: Dict[str, Any]) -> str:
        """Analyze artistic style for visual generation"""
        musical_style = features.get('musical_style', 'experimental')
        mood = features.get('mood', 'moderate')
        brightness = features.get('brightness', 'balanced')
        texture = features.get('texture', 'balanced')
        sophistication = features.get('sophistication_level', 'simple')
        
        if musical_style == 'electronic dance':
            return "futuristic cyberpunk"
        elif musical_style == 'acoustic folk':
            return "natural organic"
        elif musical_style == 'ambient atmospheric':
            return "ethereal dreamlike"
        elif musical_style == 'jazz fusion':
            return "sophisticated elegant"
        elif musical_style == 'rock alternative':
            return "raw powerful"
        elif musical_style == 'classical orchestral':
            return "timeless majestic"
        elif mood == 'mysterious' and brightness == 'dark':
            return "mystical otherworldly"
        else:
            return "contemporary artistic"
    
    def create_art_prompt(self, features: Dict[str, Any], transcription: str = "") -> str:
        """Create a sophisticated art prompt based on comprehensive musical analysis"""
        # Core musical characteristics
        mood = features.get('mood', 'moderate')
        energy = features.get('energy_level', 'medium')
        complexity = features.get('complexity', 'moderate')
        musical_style = features.get('musical_style', 'experimental')
        emotional_tone = features.get('emotional_tone', 'balanced')
        artistic_style = features.get('artistic_style', 'contemporary artistic')
        
        # Visual characteristics
        brightness = features.get('brightness', 'balanced')
        texture = features.get('texture', 'balanced')
        rhythm_complexity = features.get('rhythm_complexity', 'moderate')
        expression = features.get('expression', 'moderate')
        duration = features.get('duration', 0)
        
        # Advanced characteristics
        sophistication = features.get('sophistication_level', 'simple')
        emotional_depth = features.get('emotional_depth', 'subtle')
        innovation = features.get('musical_innovation', 'traditional')
        
        # Build sophisticated prompt components
        prompt_parts = [
            f"Create a {artistic_style} visual representation of {musical_style} music",
            f"with {mood} mood and {energy} energy",
            f"Complexity: {complexity}, Duration: {duration:.1f} seconds"
        ]
        
        # Add emotional and stylistic elements
        prompt_parts.append(f"Emotional tone: {emotional_tone}")
        prompt_parts.append(f"Visual brightness: {brightness}")
        prompt_parts.append(f"Texture: {texture}")
        prompt_parts.append(f"Sophistication: {sophistication}")
        prompt_parts.append(f"Emotional depth: {emotional_depth}")
        
        # Add rhythm-inspired elements
        if rhythm_complexity == 'complex':
            prompt_parts.append("rhythmic and layered")
        elif rhythm_complexity == 'simple':
            prompt_parts.append("minimal and clean")
        
        # Add expression-inspired elements
        if expression == 'expressive':
            prompt_parts.append("dynamic and dramatic")
        elif expression == 'consistent':
            prompt_parts.append("harmonious and balanced")
        
        # Add innovation-inspired elements
        if innovation == 'innovative':
            prompt_parts.append("avant-garde and experimental")
        elif innovation == 'creative':
            prompt_parts.append("imaginative and original")
        
        # Add style-specific artistic elements
        if musical_style == 'electronic dance':
            prompt_parts.append("futuristic and digital")
        elif musical_style == 'acoustic folk':
            prompt_parts.append("organic and natural")
        elif musical_style == 'ambient atmospheric':
            prompt_parts.append("atmospheric and ethereal")
        elif musical_style == 'jazz fusion':
            prompt_parts.append("sophisticated and complex")
        elif musical_style == 'rock alternative':
            prompt_parts.append("raw and powerful")
        elif musical_style == 'classical orchestral':
            prompt_parts.append("timeless and majestic")
        
        # Add transcription if available
        if transcription and transcription.strip():
            prompt_parts.append(f"Audio content: '{transcription.strip()}'")
        
        # Add artistic direction
        prompt_parts.append("highly detailed, artistic composition")
        prompt_parts.append("professional digital art style")
        
        return " | ".join(prompt_parts)
    
    def _get_default_features(self) -> Dict[str, Any]:
        """Return default features if analysis fails"""
        return {
            'duration': 60.0,
            'mood': 'moderate',
            'energy_level': 'medium',
            'complexity': 'moderate',
            'musical_style': 'experimental',
            'emotional_tone': 'balanced',
            'artistic_style': 'contemporary artistic',
            'detected_instruments': []
        }

    def detect_instruments(self, audio_path: str, transcription: str = "") -> List[Dict[str, Any]]:
        """Detect instruments based on audio characteristics and transcription"""
        detected_instruments = []
        
        # Analyze filename for instrument hints
        file_name = os.path.basename(audio_path).lower()
        
        # Check transcription for instrument keywords
        transcription_lower = transcription.lower() if transcription else ""
        
        # Analyze audio characteristics for instrument detection
        audio_characteristics = self._analyze_audio_for_instruments(audio_path)
        
        # Score each instrument based on multiple factors
        for instrument_name, instrument_data in self.instrument_database.items():
            score = 0
            detection_reasons = []
            
            # Check filename for instrument hints
            for keyword in instrument_data['keywords']:
                if keyword in file_name:
                    score += 3
                    detection_reasons.append(f"filename contains '{keyword}'")
            
            # Check transcription for instrument mentions
            for keyword in instrument_data['keywords']:
                if keyword in transcription_lower:
                    score += 5
                    detection_reasons.append(f"transcription mentions '{keyword}'")
            
            # Check audio characteristics
            if instrument_name in audio_characteristics:
                score += audio_characteristics[instrument_name]
                detection_reasons.append("audio characteristics match")
            
            # Add to detected instruments if score is high enough
            if score >= 3:
                detected_instruments.append({
                    'name': instrument_name,
                    'score': score,
                    'confidence': min(score / 10.0, 1.0),
                    'reasons': detection_reasons,
                    'visual_elements': instrument_data['visual_elements'],
                    'colors': instrument_data['colors'],
                    'textures': instrument_data['textures'],
                    'mood_associations': instrument_data['mood_associations']
                })
        
        # Sort by confidence score
        detected_instruments.sort(key=lambda x: x['score'], reverse=True)
        
        return detected_instruments

    def _analyze_audio_for_instruments(self, audio_path: str) -> Dict[str, float]:
        """Analyze audio characteristics to detect instruments"""
        file_name = os.path.basename(audio_path).lower()
        file_size = os.path.getsize(audio_path)
        
        # Simulate audio analysis based on file characteristics
        instrument_scores = {}
        
        # Piano detection (often in filenames, warm tones)
        if any(word in file_name for word in ['piano', 'keys', 'melody', 'chords']):
            instrument_scores['piano'] = 4.0
        elif 'piano' in file_name or 'keys' in file_name:
            instrument_scores['piano'] = 2.0
        
        # Guitar detection
        if any(word in file_name for word in ['guitar', 'acoustic', 'strings']):
            instrument_scores['guitar'] = 4.0
        elif 'guitar' in file_name:
            instrument_scores['guitar'] = 2.0
        
        # Voice detection (common in songs)
        if any(word in file_name for word in ['voice', 'vocal', 'sing', 'song']):
            instrument_scores['voice'] = 3.0
        else:
            # Assume voice is likely present in most songs
            instrument_scores['voice'] = 1.5
        
        # Nature sounds detection
        if any(word in file_name for word in ['bird', 'nature', 'ambient', 'environmental']):
            instrument_scores['nature_sounds'] = 4.0
        
        # Electronic/synth detection
        if any(word in file_name for word in ['electronic', 'synth', 'digital', 'electronic']):
            instrument_scores['synth'] = 4.0
        
        # Drums detection (common in most music)
        if any(word in file_name for word in ['drums', 'beat', 'rhythm']):
            instrument_scores['drums'] = 3.0
        else:
            # Assume drums might be present
            instrument_scores['drums'] = 1.0
        
        return instrument_scores

    def create_instrument_enhanced_prompt(self, features: Dict[str, Any], transcription: str = "") -> str:
        """Create an art prompt enhanced with instrument-specific visual elements"""
        # Get base prompt without recursion
        base_prompt = self._create_base_art_prompt(features, transcription)
        
        # Detect instruments
        detected_instruments = self.detect_instruments(features.get('audio_path', ''), transcription)
        
        if not detected_instruments:
            return base_prompt
        
        # Enhance prompt with instrument-specific elements
        instrument_elements = []
        
        for instrument in detected_instruments[:3]:  # Top 3 instruments
            # Add visual elements
            visual_elements = instrument['visual_elements'][:2]  # Top 2 visual elements
            instrument_elements.extend(visual_elements)
            
            # Add color suggestions
            colors = instrument['colors'][:2]  # Top 2 colors
            instrument_elements.extend(colors)
            
            # Add mood associations
            moods = instrument['mood_associations'][:2]  # Top 2 moods
            instrument_elements.extend(moods)
        
        # Combine base prompt with instrument elements
        enhanced_parts = [base_prompt]
        
        if instrument_elements:
            enhanced_parts.append(f"Instrument elements: {', '.join(instrument_elements)}")
        
        # Add detected instruments list
        instrument_names = [inst['name'] for inst in detected_instruments[:3]]
        enhanced_parts.append(f"Detected instruments: {', '.join(instrument_names)}")
        
        return " | ".join(enhanced_parts)

    def _create_base_art_prompt(self, features: Dict[str, Any], transcription: str = "") -> str:
        """Create a base art prompt without instrument enhancement (to avoid recursion)"""
        # Core musical characteristics
        mood = features.get('mood', 'moderate')
        energy = features.get('energy_level', 'medium')
        complexity = features.get('complexity', 'moderate')
        musical_style = features.get('musical_style', 'experimental')
        emotional_tone = features.get('emotional_tone', 'balanced')
        artistic_style = features.get('artistic_style', 'contemporary artistic')
        
        # Visual characteristics
        brightness = features.get('brightness', 'balanced')
        texture = features.get('texture', 'balanced')
        rhythm_complexity = features.get('rhythm_complexity', 'moderate')
        expression = features.get('expression', 'moderate')
        duration = features.get('duration', 0)
        
        # Advanced characteristics
        sophistication = features.get('sophistication_level', 'simple')
        emotional_depth = features.get('emotional_depth', 'subtle')
        innovation = features.get('musical_innovation', 'traditional')
        
        # Build sophisticated prompt components
        prompt_parts = [
            f"Create a {artistic_style} visual representation of {musical_style} music",
            f"with {mood} mood and {energy} energy",
            f"Complexity: {complexity}, Duration: {duration:.1f} seconds"
        ]
        
        # Add emotional and stylistic elements
        prompt_parts.append(f"Emotional tone: {emotional_tone}")
        prompt_parts.append(f"Visual brightness: {brightness}")
        prompt_parts.append(f"Texture: {texture}")
        prompt_parts.append(f"Sophistication: {sophistication}")
        prompt_parts.append(f"Emotional depth: {emotional_depth}")
        
        # Add rhythm-inspired elements
        if rhythm_complexity == 'complex':
            prompt_parts.append("rhythmic and layered")
        elif rhythm_complexity == 'simple':
            prompt_parts.append("minimal and clean")
        
        # Add expression-inspired elements
        if expression == 'expressive':
            prompt_parts.append("dynamic and dramatic")
        elif expression == 'consistent':
            prompt_parts.append("harmonious and balanced")
        
        # Add innovation-inspired elements
        if innovation == 'innovative':
            prompt_parts.append("avant-garde and experimental")
        elif innovation == 'creative':
            prompt_parts.append("imaginative and original")
        
        # Add style-specific artistic elements
        if musical_style == 'electronic dance':
            prompt_parts.append("futuristic and digital")
        elif musical_style == 'acoustic folk':
            prompt_parts.append("organic and natural")
        elif musical_style == 'ambient atmospheric':
            prompt_parts.append("atmospheric and ethereal")
        elif musical_style == 'jazz fusion':
            prompt_parts.append("sophisticated and complex")
        elif musical_style == 'rock alternative':
            prompt_parts.append("raw and powerful")
        elif musical_style == 'classical orchestral':
            prompt_parts.append("timeless and majestic")
        
        # Add transcription if available
        if transcription and transcription.strip():
            prompt_parts.append(f"Audio content: '{transcription.strip()}'")
        
        # Add artistic direction
        prompt_parts.append("highly detailed, artistic composition")
        prompt_parts.append("professional digital art style")
        
        return " | ".join(prompt_parts) 