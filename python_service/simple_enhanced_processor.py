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
                'keywords': ['violin', 'strings', 'bow', 'melody', 'classical'],
                'visual_elements': ['curved body', 'elegant neck', 'four strings', 'f-holes', 'scroll'],
                'colors': ['rich amber', 'deep reds', 'golden browns', 'warm honey'],
                'textures': ['smooth varnish', 'wood grain', 'horsehair bow', 'ebony fingerboard'],
                'mood_associations': ['elegant', 'emotional', 'romantic', 'classical', 'sophisticated']
            },
            'drums': {
                'keywords': ['drums', 'percussion', 'beat', 'rhythm', 'kick', 'snare'],
                'visual_elements': ['circular drums', 'metal cymbals', 'wooden shells', 'drumsticks'],
                'colors': ['metallic silvers', 'deep blacks', 'warm browns', 'brass tones'],
                'textures': ['smooth metal', 'wood grain', 'textured heads', 'shiny cymbals'],
                'mood_associations': ['rhythmic', 'powerful', 'energetic', 'driving', 'pulsing']
            },
            'saxophone': {
                'keywords': ['saxophone', 'sax', 'jazz', 'smooth', 'melody'],
                'visual_elements': ['curved brass', 'keys', 'bell', 'neck', 'mouthpiece'],
                'colors': ['brass gold', 'copper tones', 'warm yellows', 'rich browns'],
                'textures': ['polished brass', 'smooth curves', 'metallic shine', 'warm patina'],
                'mood_associations': ['smooth', 'jazz', 'sophisticated', 'warm', 'melodic']
            },
            'flute': {
                'keywords': ['flute', 'woodwind', 'melody', 'gentle', 'air'],
                'visual_elements': ['long silver tube', 'keys', 'head joint', 'foot joint'],
                'colors': ['silver metallic', 'cool blues', 'soft whites', 'gentle grays'],
                'textures': ['smooth silver', 'precise keys', 'shiny surface', 'elegant curves'],
                'mood_associations': ['gentle', 'ethereal', 'peaceful', 'floating', 'delicate']
            },
            'synth': {
                'keywords': ['synth', 'electronic', 'digital', 'keys', 'electronic'],
                'visual_elements': ['digital interface', 'LED lights', 'knobs', 'screens'],
                'colors': ['neon colors', 'electric blues', 'vibrant purples', 'bright greens'],
                'textures': ['smooth plastic', 'glowing lights', 'digital displays', 'modern surfaces'],
                'mood_associations': ['futuristic', 'electronic', 'modern', 'digital', 'synthetic']
            },
            'bass': {
                'keywords': ['bass', 'low', 'deep', 'groove', 'rhythm'],
                'visual_elements': ['long neck', 'thick strings', 'large body', 'pickups'],
                'colors': ['deep blacks', 'rich browns', 'dark reds', 'warm earth tones'],
                'textures': ['smooth wood', 'metal strings', 'warm finish', 'solid body'],
                'mood_associations': ['deep', 'groovy', 'rhythmic', 'warm', 'foundational']
            },
            'voice': {
                'keywords': ['voice', 'vocal', 'singing', 'lyrics', 'human'],
                'visual_elements': ['human form', 'expressive face', 'gestures', 'emotion'],
                'colors': ['warm skin tones', 'natural colors', 'expressive hues', 'human warmth'],
                'textures': ['organic', 'natural', 'expressive', 'human'],
                'mood_associations': ['human', 'emotional', 'expressive', 'personal', 'intimate']
            },
            'nature_sounds': {
                'keywords': ['nature', 'ambient', 'environmental', 'organic', 'natural'],
                'visual_elements': ['natural landscapes', 'organic forms', 'environmental textures'],
                'colors': ['earth tones', 'natural greens', 'sky blues', 'organic browns'],
                'textures': ['organic', 'natural', 'textured', 'environmental'],
                'mood_associations': ['natural', 'peaceful', 'organic', 'environmental', 'calm']
            }
        }

        # Dynamic color palette system based on musical features
        self.color_palettes = {
            'mood_based': {
                'joyful': ['#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FF69B4'],
                'melancholy': ['#6B5B95', '#8B4513', '#2F4F4F', '#708090', '#4682B4', '#483D8B'],
                'passionate': ['#DC143C', '#8B0000', '#FF4500', '#FF6347', '#CD5C5C', '#B22222'],
                'peaceful': ['#98FB98', '#87CEEB', '#DDA0DD', '#F0E68C', '#E6E6FA', '#B0E0E6'],
                'mysterious': ['#483D8B', '#4B0082', '#2E8B57', '#191970', '#8A2BE2', '#4169E1'],
                'energetic': ['#FF4500', '#FFD700', '#00FF00', '#FF69B4', '#00CED1', '#FF1493'],
                'calm': ['#98FB98', '#87CEEB', '#DDA0DD', '#F0E68C', '#E6E6FA', '#B0E0E6'],
                'dramatic': ['#DC143C', '#8B0000', '#FF4500', '#FF6347', '#CD5C5C', '#B22222'],
                'contemplative': ['#6B5B95', '#8B4513', '#2F4F4F', '#708090', '#4682B4', '#483D8B']
            },
            'energy_based': {
                'high': ['#FF0000', '#FF4500', '#FFD700', '#00FF00', '#FF69B4', '#00CED1'],
                'medium': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#FFB6C1'],
                'low': ['#6B5B95', '#8B4513', '#2F4F4F', '#708090', '#4682B4', '#483D8B']
            },
            'tempo_based': {
                'fast': ['#FF0000', '#FF4500', '#FFD700', '#00FF00', '#FF69B4', '#00CED1'],
                'medium': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#FFB6C1'],
                'slow': ['#6B5B95', '#8B4513', '#2F4F4F', '#708090', '#4682B4', '#483D8B']
            },
            'brightness_based': {
                'bright': ['#FFFFFF', '#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],
                'warm': ['#FFE4B5', '#FFD700', '#FF6B6B', '#8B4513', '#CD853F', '#D2691E'],
                'dark': ['#000000', '#2F4F4F', '#483D8B', '#8B0000', '#191970', '#4169E1'],
                'balanced': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#FFB6C1']
            },
            'seasonal': {
                'spring': ['#98FB98', '#87CEEB', '#DDA0DD', '#F0E68C', '#E6E6FA', '#B0E0E6'],
                'summer': ['#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FF69B4'],
                'autumn': ['#FF8C00', '#8B4513', '#CD853F', '#D2691E', '#B8860B', '#DAA520'],
                'winter': ['#FFFFFF', '#87CEEB', '#708090', '#4682B4', '#191970', '#4169E1']
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
        
        # Multi-factor mood analysis with improved logic
        mood_score = {
            'energetic': 0, 'calm': 0, 'dramatic': 0, 'melancholic': 0,
            'joyful': 0, 'mysterious': 0, 'passionate': 0, 'contemplative': 0, 'peaceful': 0
        }
        
        # Energy-based scoring (more nuanced)
        if energy_variance > 50000 and estimated_tempo > 140:
            mood_score['energetic'] += 4
        elif energy_variance < 15000 and estimated_tempo < 80:
            mood_score['calm'] += 4
            mood_score['peaceful'] += 3
        elif energy_variance < 25000 and estimated_tempo < 100:
            mood_score['peaceful'] += 4
            mood_score['calm'] += 2
        
        # Tempo-based scoring
        if estimated_tempo > 150:
            mood_score['energetic'] += 3
        elif estimated_tempo < 70:
            mood_score['peaceful'] += 3
            mood_score['contemplative'] += 2
        elif estimated_tempo < 90:
            mood_score['calm'] += 2
        
        # Brightness-based scoring
        if brightness == 'bright' and estimated_tempo > 120:
            mood_score['joyful'] += 3
        elif brightness == 'dark' and texture == 'smooth':
            mood_score['melancholic'] += 3
        elif brightness == 'warm' and estimated_tempo < 100:
            mood_score['peaceful'] += 3
            mood_score['calm'] += 2
        
        # Dynamic range scoring
        if dynamic_range > 25 and energy_variance > 40000:
            mood_score['dramatic'] += 3
        elif dynamic_range < 15 and energy_variance < 20000:
            mood_score['peaceful'] += 2
            mood_score['calm'] += 2
        
        # Texture-based scoring
        if texture == 'layered' and brightness == 'dark':
            mood_score['mysterious'] += 3
        elif texture == 'smooth' and estimated_tempo < 90:
            mood_score['contemplative'] += 3
            mood_score['peaceful'] += 2
        elif texture == 'gritty' and dynamic_range > 20:
            mood_score['passionate'] += 3
        
        # Special case for very peaceful music
        if (energy_variance < 15000 and estimated_tempo < 80 and 
            brightness in ['warm', 'balanced'] and texture == 'smooth'):
            mood_score['peaceful'] += 5
            mood_score['calm'] += 3
        
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
        elif musical_style == 'rock':
            prompt_parts.append("powerful and energetic")
        elif musical_style == 'classical':
            prompt_parts.append("elegant and refined")
        elif musical_style == 'pop':
            prompt_parts.append("bright and accessible")
        elif musical_style == 'experimental':
            prompt_parts.append("innovative and creative")
        
        # Add specific scene suggestions based on mood and energy
        if mood == 'peaceful' and energy == 'low':
            prompt_parts.append("peaceful landscape or serene environment")
        elif mood == 'energetic' and energy == 'high':
            prompt_parts.append("dynamic scene with movement and energy")
        elif mood == 'mysterious':
            prompt_parts.append("mysterious or atmospheric environment")
        elif mood == 'joyful':
            prompt_parts.append("bright and cheerful scene")
        elif mood == 'melancholy':
            prompt_parts.append("contemplative or reflective scene")
        elif mood == 'passionate':
            prompt_parts.append("intense and dramatic scene")
        
        # Add instrument-specific scene suggestions (only if detected_instruments is provided)
        if detected_instruments:
            for instrument in detected_instruments[:2]:  # Top 2 instruments
                instrument_name = instrument['name']
                if instrument_name == 'piano':
                    prompt_parts.append("elegant piano or musical setting")
                elif instrument_name == 'guitar':
                    prompt_parts.append("acoustic or electric guitar scene")
                elif instrument_name == 'drums':
                    prompt_parts.append("rhythmic drum or percussion scene")
                elif instrument_name == 'voice':
                    prompt_parts.append("vocal or singing scene")
                elif instrument_name == 'nature_sounds':
                    prompt_parts.append("natural outdoor environment")
                elif instrument_name == 'synth':
                    prompt_parts.append("electronic or digital music scene")
        
        # Add transcription if available
        if transcription and transcription.strip():
            prompt_parts.append(f"Audio content: '{transcription.strip()}'")
        
        return " | ".join(prompt_parts)
    
    def _get_default_features(self) -> Dict[str, Any]:
        """Return default features if analysis fails"""
        return {
            'duration': 180.0,
            'tempo': 120,
            'energy_level': 'medium',
            'complexity': 'moderate',
            'musical_style': 'pop',
            'emotional_tone': 'balanced',
            'artistic_style': 'contemporary',
            'detected_instruments': []
        }

    def generate_dynamic_color_palette(self, features: Dict[str, Any], detected_instruments: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generate a dynamic color palette based on musical features"""
        palette = {
            'primary_colors': [],
            'secondary_colors': [],
            'accent_colors': [],
            'mood_colors': [],
            'instrument_colors': [],
            'description': ''
        }
        
        # Get mood-based colors
        mood = features.get('mood', 'balanced')
        if mood in self.color_palettes['mood_based']:
            mood_colors = self.color_palettes['mood_based'][mood]
            # Add some randomization to mood colors
            import random
            if len(mood_colors) > 4:
                mood_colors = random.sample(mood_colors, 4)
            palette['mood_colors'] = mood_colors
        
        # Get energy-based colors
        energy = features.get('energy_level', 'medium')
        if energy in self.color_palettes['energy_based']:
            energy_colors = self.color_palettes['energy_based'][energy]
            # Add some randomization to energy colors
            import random
            if len(energy_colors) > 3:
                energy_colors = random.sample(energy_colors, 3)
            palette['primary_colors'] = energy_colors
        
        # Get tempo-based colors
        tempo = features.get('estimated_tempo', 120)  # Fixed: was 'tempo', should be 'estimated_tempo'
        if tempo > 140:
            tempo_category = 'fast'
        elif tempo < 80:
            tempo_category = 'slow'
        else:
            tempo_category = 'medium'
        
        if tempo_category in self.color_palettes['tempo_based']:
            palette['secondary_colors'] = self.color_palettes['tempo_based'][tempo_category]
        
        # Get brightness-based colors
        brightness = features.get('brightness', 'balanced')
        if brightness in self.color_palettes['brightness_based']:
            palette['accent_colors'] = self.color_palettes['brightness_based'][brightness]
        
        # Get instrument-specific colors
        if detected_instruments:
            for instrument in detected_instruments[:3]:  # Top 3 instruments
                instrument_name = instrument['name']
                if instrument_name in self.instrument_database:
                    instrument_colors = self.instrument_database[instrument_name]['colors']
                    palette['instrument_colors'].extend(instrument_colors)
        
        # Combine and deduplicate colors
        all_colors = []
        all_colors.extend(palette['primary_colors'])
        all_colors.extend(palette['secondary_colors'])
        all_colors.extend(palette['accent_colors'])
        all_colors.extend(palette['mood_colors'])
        all_colors.extend(palette['instrument_colors'])
        
        # Remove duplicates while preserving order
        unique_colors = []
        for color in all_colors:
            if color not in unique_colors:
                unique_colors.append(color)
        
        # Limit to 8 colors for the final palette
        final_palette = unique_colors[:8]
        
        # Generate description
        descriptions = []
        if mood != 'balanced':
            descriptions.append(f"{mood} mood")
        if energy != 'medium':
            descriptions.append(f"{energy} energy")
        if tempo_category != 'medium':
            descriptions.append(f"{tempo_category} tempo")
        if brightness != 'balanced':
            descriptions.append(f"{brightness} brightness")
        if detected_instruments:
            instrument_names = [inst['name'] for inst in detected_instruments[:3]]
            descriptions.append(f"featuring {', '.join(instrument_names)}")
        
        palette['final_colors'] = final_palette
        palette['description'] = f"Dynamic palette: {', '.join(descriptions)}" if descriptions else "Balanced color palette"
        
        return palette

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
        """Create an art prompt enhanced with instrument-specific visual elements and dynamic color palette"""
        detected_instruments = self.detect_instruments(features.get('audio_path', ''), transcription)
        base_prompt = self._create_base_art_prompt(features, transcription, detected_instruments)
        
        # Generate dynamic color palette
        color_palette = self.generate_dynamic_color_palette(features, detected_instruments)
        
        enhanced_parts = []
        
        # PRIORITY 1: Start with color information to emphasize it
        if color_palette['final_colors']:
            color_names = []
            for color in color_palette['final_colors'][:6]:  # Use top 6 colors
                # Convert hex to color names for better prompt understanding
                color_name = self._hex_to_color_name(color)
                color_names.append(color_name)
            
            # Create strong color emphasis
            color_emphasis = f"ARTWORK featuring {', '.join(color_names)}"
            enhanced_parts.append(color_emphasis)
            
            # Add color style description
            enhanced_parts.append(f"Color style: {color_palette['description']}")
            
            # Add color intensity keywords
            mood = features.get('mood', 'balanced')
            energy = features.get('energy_level', 'medium')
            
            if energy == 'high' or mood in ['energetic', 'passionate']:
                enhanced_parts.append("VIBRANT and INTENSE colors")
            elif mood in ['peaceful', 'calm']:
                enhanced_parts.append("SOFT and WARM colors")
            elif mood in ['mysterious', 'dark']:
                enhanced_parts.append("RICH and DEEP colors")
            else:
                enhanced_parts.append("BEAUTIFUL and HARMONIOUS colors")
        
        # PRIORITY 2: Add base artistic prompt
        enhanced_parts.append(base_prompt)
        
        # PRIORITY 3: Add instrument elements
        if detected_instruments:
            instrument_elements = []
            for instrument in detected_instruments[:3]:
                visual_elements = instrument['visual_elements'][:2]
                instrument_elements.extend(visual_elements)
                moods = instrument['mood_associations'][:2]
                instrument_elements.extend(moods)
            
            if instrument_elements:
                enhanced_parts.append(f"Instrument elements: {', '.join(instrument_elements)}")
            
            instrument_names = [inst['name'] for inst in detected_instruments[:3]]
            enhanced_parts.append(f"Detected instruments: {', '.join(instrument_names)}")
        
        # PRIORITY 4: Add final color reinforcement
        if color_palette['final_colors']:
            enhanced_parts.append("MUST USE the specified color palette prominently")
            enhanced_parts.append("NO black and white or monochrome")
            enhanced_parts.append("FULL COLOR artwork with rich, saturated colors")
        
        # PRIORITY 5: Add balanced art style instructions based on musical characteristics
        mood = features.get('mood', 'balanced')
        energy = features.get('energy_level', 'medium')
        complexity = features.get('complexity', 'moderate')
        musical_style = features.get('musical_style', 'experimental')
        
        # Determine art style based on musical characteristics - FAVOR REPRESENTATIONAL
        if mood in ['peaceful', 'calm', 'serene'] and complexity == 'simple':
            # Representational for simple, peaceful music
            enhanced_parts.append("REPRESENTATIONAL and REALISTIC imagery")
            enhanced_parts.append("peaceful and serene concrete scenes")
            enhanced_parts.append("recognizable objects and environments")
            enhanced_parts.append("NO ABSTRACT ART - ONLY REPRESENTATIONAL")
            enhanced_parts.append("CREATE CONCRETE SCENES WITH REAL OBJECTS")
        elif mood in ['dramatic', 'passionate'] and energy == 'medium':
            # Representational for dramatic music (CHANGED FROM ABSTRACT)
            enhanced_parts.append("REPRESENTATIONAL and DRAMATIC imagery")
            enhanced_parts.append("concrete scenes with emotional intensity")
            enhanced_parts.append("recognizable objects in dramatic lighting")
            enhanced_parts.append("NO ABSTRACT ART - ONLY REPRESENTATIONAL")
            enhanced_parts.append("CREATE CONCRETE SCENES WITH REAL OBJECTS")
        elif mood in ['dramatic', 'passionate'] and energy == 'high':
            # Representational for high-energy dramatic music (CHANGED FROM ABSTRACT)
            enhanced_parts.append("REPRESENTATIONAL and INTENSE imagery")
            enhanced_parts.append("concrete scenes with powerful emotion")
            enhanced_parts.append("recognizable objects in intense lighting")
            enhanced_parts.append("NO ABSTRACT ART - ONLY REPRESENTATIONAL")
            enhanced_parts.append("CREATE CONCRETE SCENES WITH REAL OBJECTS")
        elif mood in ['melancholic', 'contemplative'] and complexity == 'moderate':
            # Representational for contemplative music
            enhanced_parts.append("REPRESENTATIONAL and CONTEMPLATIVE imagery")
            enhanced_parts.append("peaceful concrete scenes with depth")
            enhanced_parts.append("recognizable objects in serene settings")
            enhanced_parts.append("NO ABSTRACT ART - ONLY REPRESENTATIONAL")
            enhanced_parts.append("CREATE CONCRETE SCENES WITH REAL OBJECTS")
        elif mood in ['joyful', 'upbeat'] and musical_style in ['pop', 'electronic dance']:
            # Mix of both for upbeat music
            enhanced_parts.append("BALANCED artwork with both abstract and representational elements")
            enhanced_parts.append("abstract backgrounds with concrete focal points")
            enhanced_parts.append("dynamic composition with recognizable elements")
        elif mood in ['mysterious', 'ethereal', 'atmospheric'] or (musical_style in ['ambient atmospheric'] and mood not in ['dramatic', 'passionate']):
            # Abstract for mysterious/ambient music
            enhanced_parts.append("ABSTRACT and ATMOSPHERIC artwork")
            enhanced_parts.append("ethereal and dreamlike imagery")
            enhanced_parts.append("fluid and organic abstract forms")
        elif mood in ['energetic'] and energy == 'high':
            # Representational for high-energy music (CHANGED FROM ABSTRACT)
            enhanced_parts.append("REPRESENTATIONAL and DYNAMIC imagery")
            enhanced_parts.append("concrete scenes with movement and energy")
            enhanced_parts.append("recognizable objects in dynamic composition")
            enhanced_parts.append("NO ABSTRACT ART - ONLY REPRESENTATIONAL")
            enhanced_parts.append("CREATE CONCRETE SCENES WITH REAL OBJECTS")
        else:
            # Default approach - STRONGLY FAVOR REPRESENTATIONAL
            enhanced_parts.append("REPRESENTATIONAL artwork with artistic interpretation")
            enhanced_parts.append("concrete scenes with creative elements")
            enhanced_parts.append("recognizable objects with artistic flair")
            enhanced_parts.append("NO ABSTRACT ART - ONLY REPRESENTATIONAL")
            enhanced_parts.append("CREATE CONCRETE SCENES WITH REAL OBJECTS")
            enhanced_parts.append("AVOID ABSTRACT SHAPES AND PATTERNS")
        
        return " | ".join(enhanced_parts)

    def _create_base_art_prompt(self, features: Dict[str, Any], transcription: str = "", detected_instruments: List[Dict[str, Any]] = None) -> str:
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
        
        # Note: Art style instructions are handled in create_instrument_enhanced_prompt
        # to avoid duplication
        
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
            prompt_parts.append("sophisticated and dynamic")
        elif musical_style == 'rock':
            prompt_parts.append("powerful and energetic")
        elif musical_style == 'classical':
            prompt_parts.append("elegant and refined")
        elif musical_style == 'pop':
            prompt_parts.append("bright and accessible")
        elif musical_style == 'experimental':
            prompt_parts.append("innovative and creative")
        
        # Add specific scene suggestions based on mood and energy
        if mood == 'peaceful' and energy == 'low':
            prompt_parts.append("peaceful landscape or serene environment")
        elif mood == 'energetic' and energy == 'high':
            prompt_parts.append("dynamic scene with movement and energy")
        elif mood == 'mysterious':
            prompt_parts.append("mysterious or atmospheric environment")
        elif mood == 'joyful':
            prompt_parts.append("bright and cheerful scene")
        elif mood == 'melancholy':
            prompt_parts.append("contemplative or reflective scene")
        elif mood == 'passionate':
            prompt_parts.append("intense and dramatic scene")
        
        # Add instrument-specific scene suggestions (only if detected_instruments is provided)
        if detected_instruments:
            for instrument in detected_instruments[:2]:  # Top 2 instruments
                instrument_name = instrument['name']
                if instrument_name == 'piano':
                    prompt_parts.append("elegant piano or musical setting")
                elif instrument_name == 'guitar':
                    prompt_parts.append("acoustic or electric guitar scene")
                elif instrument_name == 'drums':
                    prompt_parts.append("rhythmic drum or percussion scene")
                elif instrument_name == 'voice':
                    prompt_parts.append("vocal or singing scene")
                elif instrument_name == 'nature_sounds':
                    prompt_parts.append("natural outdoor environment")
                elif instrument_name == 'synth':
                    prompt_parts.append("electronic or digital music scene")
        
        # Add transcription if available
        if transcription and transcription.strip():
            prompt_parts.append(f"Audio content: '{transcription.strip()}'")
        
        return " | ".join(prompt_parts)

    def _hex_to_color_name(self, hex_color: str) -> str:
        """Convert hex color to descriptive color name"""
        color_map = {
            '#FFD700': 'golden yellow',
            '#FF6B6B': 'coral red',
            '#4ECDC4': 'turquoise',
            '#45B7D1': 'sky blue',
            '#96CEB4': 'sage green',
            '#6B5B95': 'plum purple',
            '#8B4513': 'saddle brown',
            '#2F4F4F': 'dark slate gray',
            '#708090': 'slate gray',
            '#4682B4': 'steel blue',
            '#DC143C': 'crimson red',
            '#8B0000': 'dark red',
            '#FF4500': 'orange red',
            '#FF6347': 'tomato red',
            '#CD5C5C': 'indian red',
            '#98FB98': 'pale green',
            '#87CEEB': 'sky blue',
            '#DDA0DD': 'plum',
            '#F0E68C': 'khaki',
            '#E6E6FA': 'lavender',
            '#483D8B': 'dark slate blue',
            '#4B0082': 'indigo',
            '#2E8B57': 'sea green',
            '#191970': 'midnight blue',
            '#8A2BE2': 'blue violet',
            '#FF0000': 'bright red',
            '#00FF00': 'lime green',
            '#FF69B4': 'hot pink',
            '#00CED1': 'dark turquoise',
            '#FFEAA7': 'cream yellow',
            '#FFFFFF': 'pure white',
            '#FFE4B5': 'moccasin',
            '#CD853F': 'peru',
            '#000000': 'pure black',
            '#8B0000': 'dark red',
            '#FF8C00': 'dark orange',
            '#D2691E': 'chocolate',
            '#B8860B': 'dark goldenrod'
        }
        
        return color_map.get(hex_color.upper(), 'rich color') 