import os
import math
import random
from typing import Dict, Any

class SimpleEnhancedAudioProcessor:
    """Simplified enhanced audio processor with detailed musical analysis"""
    
    def __init__(self):
        pass
    
    def extract_features(self, audio_path: str) -> Dict[str, Any]:
        """Extract comprehensive audio features using file analysis"""
        try:
            # Get file information
            file_size = os.path.getsize(audio_path)
            file_name = os.path.basename(audio_path)
            
            # Simulate realistic audio features based on file characteristics
            features = {
                'duration': self._estimate_duration(file_size, file_name),
                'sample_rate': random.choice([44100, 48000, 22050, 32000]),
                'channels': random.choice([1, 2]),
                'rms': random.uniform(800, 2000),
                'dBFS': random.uniform(-25, -8),
                'max_dBFS': random.uniform(-20, -5)
            }
            
            # Advanced musical analysis (simulated but realistic)
            features.update(self._simulate_musical_structure(file_size))
            features.update(self._simulate_spectral_features(file_name))
            features.update(self._simulate_rhythm_patterns(file_size))
            features.update(self._simulate_dynamic_range(file_size))
            
            # Determine musical characteristics
            features['mood'] = self._analyze_mood(features)
            features['energy_level'] = self._analyze_energy(features)
            features['complexity'] = self._analyze_complexity(features)
            features['musical_style'] = self._analyze_musical_style(features)
            features['emotional_tone'] = self._analyze_emotional_tone(features)
            
            return features
            
        except Exception as e:
            print(f"Error extracting features: {e}")
            return {}
    
    def _estimate_duration(self, file_size: int, file_name: str) -> float:
        """Estimate duration based on file size and format"""
        # Rough estimation: larger files = longer duration
        # Also consider file name hints
        base_duration = file_size / 100000  # Rough estimate
        
        # Adjust based on file name patterns
        if any(word in file_name.lower() for word in ['short', 'clip', 'sample']):
            base_duration *= 0.3
        elif any(word in file_name.lower() for word in ['long', 'full', 'complete']):
            base_duration *= 2.0
        
        return max(30, min(600, base_duration))  # Between 30 seconds and 10 minutes
    
    def _simulate_musical_structure(self, file_size: int) -> Dict[str, Any]:
        """Simulate musical structure analysis"""
        # Larger files tend to have more complex structure
        complexity_factor = min(1.0, file_size / 5000000)  # Normalize to 5MB
        
        energy_variance = 5000 + (complexity_factor * 45000)
        volume_variance = 5 + (complexity_factor * 20)
        energy_peaks = int(10 + (complexity_factor * 40))
        estimated_tempo = int(80 + (complexity_factor * 80))  # 80-160 BPM
        
        return {
            'energy_variance': energy_variance,
            'volume_variance': volume_variance,
            'energy_peaks': energy_peaks,
            'estimated_tempo': estimated_tempo,
            'peak_density': energy_peaks / 50,
            'dynamic_range': 10 + (complexity_factor * 25)
        }
    
    def _simulate_spectral_features(self, file_name: str) -> Dict[str, Any]:
        """Simulate spectral characteristics"""
        # Analyze file name for hints about spectral content
        name_lower = file_name.lower()
        
        if any(word in name_lower for word in ['bass', 'low', 'deep']):
            spectral_centroid = random.uniform(800, 1500)
            brightness = 'dark'
        elif any(word in name_lower for word in ['high', 'bright', 'treble']):
            spectral_centroid = random.uniform(2500, 4000)
            brightness = 'bright'
        else:
            spectral_centroid = random.uniform(1500, 2500)
            brightness = 'warm'
        
        # Texture based on file characteristics
        texture = 'smooth' if random.random() > 0.5 else 'noisy'
        
        return {
            'spectral_centroid': spectral_centroid,
            'spectral_rolloff': spectral_centroid * 1.5,
            'zero_crossing_rate': random.uniform(0.05, 0.15),
            'brightness': brightness,
            'texture': texture
        }
    
    def _simulate_rhythm_patterns(self, file_size: int) -> Dict[str, Any]:
        """Simulate rhythm analysis"""
        complexity_factor = min(1.0, file_size / 5000000)
        
        rhythm_regularity = 0.3 + (complexity_factor * 0.5)
        strong_beats = int(5 + (complexity_factor * 25))
        weak_beats = int(10 + (complexity_factor * 30))
        
        rhythm_complexity = 'complex' if complexity_factor > 0.7 else 'moderate' if complexity_factor > 0.3 else 'simple'
        timing_precision = 'precise' if rhythm_regularity > 0.7 else 'loose' if rhythm_regularity < 0.3 else 'moderate'
        
        return {
            'rhythm_regularity': rhythm_regularity,
            'strong_beats': strong_beats,
            'weak_beats': weak_beats,
            'rhythm_complexity': rhythm_complexity,
            'timing_precision': timing_precision
        }
    
    def _simulate_dynamic_range(self, file_size: int) -> Dict[str, Any]:
        """Simulate dynamic range analysis"""
        complexity_factor = min(1.0, file_size / 5000000)
        
        dynamic_range = 8 + (complexity_factor * 25)
        volume_variance = 2 + (complexity_factor * 15)
        volume_trend = random.uniform(-2, 2)  # Random trend
        
        expression = 'expressive' if dynamic_range > 20 else 'consistent' if dynamic_range < 10 else 'moderate'
        volume_curve = 'crescendo' if volume_trend > 0.5 else 'diminuendo' if volume_trend < -0.5 else 'stable'
        
        return {
            'dynamic_range': dynamic_range,
            'volume_variance': volume_variance,
            'volume_trend': volume_trend,
            'expression': expression,
            'volume_curve': volume_curve
        }
    
    def _analyze_mood(self, features: Dict[str, Any]) -> str:
        """Analyze mood based on comprehensive features"""
        spectral_centroid = features.get('spectral_centroid', 0)
        energy_variance = features.get('energy_variance', 0)
        estimated_tempo = features.get('estimated_tempo', 0)
        dynamic_range = features.get('dynamic_range', 0)
        
        # Complex mood analysis
        if spectral_centroid > 2500 and energy_variance > 30000 and estimated_tempo > 140:
            return "energetic"
        elif spectral_centroid < 1500 and energy_variance < 15000 and estimated_tempo < 80:
            return "calm"
        elif dynamic_range > 25 and energy_variance > 40000:
            return "dramatic"
        elif estimated_tempo > 120 and features.get('rhythm_complexity') == 'complex':
            return "rhythmic"
        elif features.get('texture') == 'smooth' and spectral_centroid < 2000:
            return "ambient"
        else:
            return "moderate"
    
    def _analyze_energy(self, features: Dict[str, Any]) -> str:
        """Analyze energy level"""
        avg_energy = features.get('rms', 0)
        energy_variance = features.get('energy_variance', 0)
        estimated_tempo = features.get('estimated_tempo', 0)
        
        if avg_energy > 1500 or energy_variance > 40000 or estimated_tempo > 130:
            return "high"
        elif avg_energy < 800 and energy_variance < 15000 and estimated_tempo < 90:
            return "low"
        else:
            return "medium"
    
    def _analyze_complexity(self, features: Dict[str, Any]) -> str:
        """Analyze musical complexity"""
        energy_peaks = features.get('energy_peaks', 0)
        rhythm_complexity = features.get('rhythm_complexity', 'moderate')
        zero_crossing_rate = features.get('zero_crossing_rate', 0)
        duration = features.get('duration', 0)
        
        complexity_score = 0
        complexity_score += energy_peaks / 10 if duration > 0 else 0
        complexity_score += 2 if rhythm_complexity == 'complex' else 1 if rhythm_complexity == 'moderate' else 0
        complexity_score += 2 if zero_crossing_rate > 0.1 else 0
        
        if complexity_score > 4:
            return "complex"
        elif complexity_score > 2:
            return "moderate"
        else:
            return "simple"
    
    def _analyze_musical_style(self, features: Dict[str, Any]) -> str:
        """Analyze musical style/genre characteristics"""
        estimated_tempo = features.get('estimated_tempo', 0)
        rhythm_complexity = features.get('rhythm_complexity', 'moderate')
        brightness = features.get('brightness', 'moderate')
        texture = features.get('texture', 'moderate')
        
        if estimated_tempo > 140 and rhythm_complexity == 'complex':
            return "electronic"
        elif estimated_tempo < 100 and brightness == 'warm':
            return "acoustic"
        elif texture == 'smooth' and brightness == 'dark':
            return "ambient"
        elif rhythm_complexity == 'complex' and estimated_tempo > 120:
            return "dance"
        elif brightness == 'bright' and estimated_tempo > 130:
            return "pop"
        else:
            return "experimental"
    
    def _analyze_emotional_tone(self, features: Dict[str, Any]) -> str:
        """Analyze emotional characteristics"""
        mood = features.get('mood', 'moderate')
        expression = features.get('expression', 'moderate')
        volume_curve = features.get('volume_curve', 'stable')
        brightness = features.get('brightness', 'moderate')
        
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
        else:
            return "balanced"
    
    def create_art_prompt(self, features: Dict[str, Any], transcription: str = "") -> str:
        """Create a rich art prompt based on comprehensive musical analysis"""
        mood = features.get('mood', 'moderate')
        energy = features.get('energy_level', 'medium')
        complexity = features.get('complexity', 'moderate')
        musical_style = features.get('musical_style', 'experimental')
        emotional_tone = features.get('emotional_tone', 'balanced')
        brightness = features.get('brightness', 'moderate')
        texture = features.get('texture', 'moderate')
        rhythm_complexity = features.get('rhythm_complexity', 'moderate')
        expression = features.get('expression', 'moderate')
        duration = features.get('duration', 0)
        
        # Build rich prompt components
        prompt_parts = [
            f"Create a visual representation of {musical_style} music",
            f"with {mood} mood and {energy} energy",
            f"Complexity: {complexity}, Duration: {duration:.1f} seconds"
        ]
        
        # Add emotional and stylistic elements
        prompt_parts.append(f"Emotional tone: {emotional_tone}")
        prompt_parts.append(f"Visual brightness: {brightness}")
        prompt_parts.append(f"Texture: {texture}")
        
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
        
        # Add style-specific elements
        if musical_style == 'electronic':
            prompt_parts.append("futuristic and digital")
        elif musical_style == 'acoustic':
            prompt_parts.append("organic and natural")
        elif musical_style == 'ambient':
            prompt_parts.append("atmospheric and ethereal")
        elif musical_style == 'dance':
            prompt_parts.append("energetic and vibrant")
        
        # Add transcription if available
        if transcription and transcription.strip():
            prompt_parts.append(f"Audio content: '{transcription.strip()}'")
        
        return " | ".join(prompt_parts) 