import os
import hashlib
import re
from typing import Dict, Any, List

class ImprovedAudioAnalyzer:
    """Improved audio analyzer that generates more diverse results based on filename analysis"""
    
    def __init__(self):
        # Mood keywords and their characteristics
        self.mood_keywords = {
            'peaceful': {'energy': 'low', 'tempo': 'slow', 'brightness': 'warm', 'colors': ['sage green', 'sky blue', 'cream yellow']},
            'calm': {'energy': 'low', 'tempo': 'slow', 'brightness': 'balanced', 'colors': ['turquoise', 'lavender', 'pale green']},
            'dramatic': {'energy': 'high', 'tempo': 'medium', 'brightness': 'dark', 'colors': ['crimson red', 'dark slate blue', 'plum purple']},
            'energetic': {'energy': 'high', 'tempo': 'fast', 'brightness': 'bright', 'colors': ['bright red', 'lime green', 'hot pink']},
            'joyful': {'energy': 'medium', 'tempo': 'medium', 'brightness': 'bright', 'colors': ['golden yellow', 'coral red', 'sky blue']},
            'melancholic': {'energy': 'low', 'tempo': 'slow', 'brightness': 'dark', 'colors': ['dark slate gray', 'indigo', 'dark red']},
            'mysterious': {'energy': 'low', 'tempo': 'slow', 'brightness': 'dark', 'colors': ['midnight blue', 'plum', 'dark turquoise']},
            'passionate': {'energy': 'high', 'tempo': 'medium', 'brightness': 'warm', 'colors': ['crimson red', 'orange red', 'steel blue']},
            'contemplative': {'energy': 'low', 'tempo': 'slow', 'brightness': 'balanced', 'colors': ['slate gray', 'sea green', 'lavender']}
        }
        
        # Musical style keywords
        self.style_keywords = {
            'piano': ['piano', 'keys', 'melody', 'ballad'],
            'rock': ['rock', 'guitar', 'electric', 'power'],
            'electronic': ['electronic', 'synth', 'digital', 'tech'],
            'ambient': ['ambient', 'atmospheric', 'dream', 'ethereal'],
            'folk': ['folk', 'acoustic', 'natural', 'organic'],
            'jazz': ['jazz', 'smooth', 'sophisticated', 'fusion'],
            'pop': ['pop', 'catchy', 'bright', 'upbeat'],
            'classical': ['classical', 'orchestral', 'elegant', 'refined']
        }
        
        # Energy keywords
        self.energy_keywords = {
            'high': ['energetic', 'powerful', 'intense', 'dynamic', 'vibrant', 'electric', 'explosive'],
            'medium': ['balanced', 'moderate', 'steady', 'flowing', 'harmonious'],
            'low': ['gentle', 'soft', 'quiet', 'peaceful', 'serene', 'calm', 'tranquil']
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
                'keywords': ['drums', 'percussion', 'beat', 'rhythm', 'kick', 'snare', 'hi-hat'],
                'visual_elements': ['circular drums', 'metal cymbals', 'wooden shells', 'drumsticks'],
                'colors': ['metallic silver', 'deep blacks', 'warm browns', 'brass tones'],
                'textures': ['smooth metal', 'wood grain', 'leather heads', 'brushed steel'],
                'mood_associations': ['rhythmic', 'powerful', 'energetic', 'dynamic', 'pulsing']
            },
            'voice': {
                'keywords': ['voice', 'vocal', 'sing', 'song', 'lyrics', 'singer'],
                'visual_elements': ['human figure', 'expressive face', 'microphone', 'stage presence'],
                'colors': ['warm skin tones', 'expressive colors', 'stage lighting', 'vibrant hues'],
                'textures': ['smooth skin', 'expressive features', 'dynamic movement', 'emotional expression'],
                'mood_associations': ['emotional', 'personal', 'expressive', 'intimate', 'powerful']
            },
            'nature_sounds': {
                'keywords': ['bird', 'nature', 'ambient', 'environmental', 'forest', 'ocean'],
                'visual_elements': ['natural landscapes', 'organic forms', 'environmental elements', 'natural textures'],
                'colors': ['earth tones', 'natural greens', 'sky blues', 'organic browns'],
                'textures': ['organic textures', 'natural patterns', 'environmental elements', 'earthly materials'],
                'mood_associations': ['peaceful', 'natural', 'organic', 'tranquil', 'environmental']
            },
            'synth': {
                'keywords': ['synth', 'electronic', 'digital', 'synthesizer', 'electronic'],
                'visual_elements': ['digital interfaces', 'electronic circuits', 'futuristic elements', 'technological forms'],
                'colors': ['neon colors', 'electric blues', 'digital greens', 'futuristic purples'],
                'textures': ['smooth plastic', 'metallic surfaces', 'digital displays', 'electronic components'],
                'mood_associations': ['futuristic', 'electronic', 'digital', 'modern', 'technological']
            }
        }

    def analyze_audio_file(self, audio_path: str) -> Dict[str, Any]:
        """Analyze audio file and generate diverse, realistic features"""
        file_name = os.path.basename(audio_path)
        file_size = os.path.getsize(audio_path)
        
        # Generate a consistent hash for this file to ensure same results
        file_hash = hashlib.md5(file_name.encode()).hexdigest()
        
        # Extract mood from filename
        mood = self._extract_mood_from_filename(file_name, file_hash)
        
        # Extract musical style
        musical_style = self._extract_musical_style(file_name, file_hash)
        
        # Generate energy level based on mood and filename
        energy_level = self._determine_energy_level(mood, file_name, file_hash)
        
        # Generate tempo based on mood and energy
        estimated_tempo = self._estimate_tempo(mood, energy_level, file_hash)
        
        # Generate complexity based on file characteristics
        complexity = self._determine_complexity(file_size, file_name, file_hash)
        
        # Generate spectral characteristics
        spectral_centroid = self._estimate_spectral_centroid(mood, musical_style, file_hash)
        brightness = self._determine_brightness(spectral_centroid, mood)
        
        # Generate dynamic characteristics
        dynamic_range = self._estimate_dynamic_range(energy_level, mood, file_hash)
        energy_variance = self._estimate_energy_variance(energy_level, file_hash)
        
        # Generate duration
        duration = self._estimate_duration(file_size, file_name)
        
        # Build comprehensive features
        features = {
            'mood': mood,
            'energy_level': energy_level,
            'musical_style': musical_style,
            'complexity': complexity,
            'estimated_tempo': estimated_tempo,
            'spectral_centroid': spectral_centroid,
            'brightness': brightness,
            'dynamic_range': dynamic_range,
            'energy_variance': energy_variance,
            'duration': duration,
            'file_size': file_size,
            'file_name': file_name
        }
        
        return features

    def _extract_mood_from_filename(self, file_name: str, file_hash: str) -> str:
        """Extract mood from filename with more sophisticated analysis"""
        # Priority 1: Explicit mood keywords in filename
        mood_keywords = {
            'peaceful': ['peaceful', 'calm', 'serene', 'gentle', 'soft', 'quiet'],
            'energetic': ['energetic', 'upbeat', 'fast', 'dynamic', 'powerful', 'intense'],
            'joyful': ['joyful', 'happy', 'bright', 'cheerful', 'uplifting', 'positive'],
            'melancholic': ['melancholic', 'sad', 'melancholy', 'sorrowful', 'blue', 'depressed'],
            'mysterious': ['mysterious', 'mystical', 'ethereal', 'atmospheric', 'ambient', 'dreamy'],
            'dramatic': ['dramatic', 'epic', 'intense', 'powerful', 'emotional', 'passionate'],
            'contemplative': ['contemplative', 'thoughtful', 'reflective', 'meditative', 'introspective']
        }
        
        file_lower = file_name.lower()
        for mood, keywords in mood_keywords.items():
            if any(keyword in file_lower for keyword in keywords):
                return mood
        
        # Priority 2: Mood-related words that suggest mood
        mood_hints = {
            'peaceful': ['piano', 'acoustic', 'nature', 'rain', 'ocean', 'wind'],
            'energetic': ['rock', 'dance', 'electronic', 'drums', 'bass', 'guitar'],
            'joyful': ['pop', 'summer', 'sunshine', 'party', 'celebration', 'love'],
            'melancholic': ['winter', 'rain', 'night', 'lonely', 'heartbreak', 'missing'],
            'mysterious': ['dark', 'night', 'moon', 'stars', 'space', 'unknown'],
            'dramatic': ['orchestra', 'strings', 'brass', 'choir', 'epic', 'battle'],
            'contemplative': ['solo', 'instrumental', 'classical', 'minimal', 'simple']
        }
        
        for mood, hints in mood_hints.items():
            if any(hint in file_lower for hint in hints):
                return mood
        
        # Priority 3: Hash-based mood with more variation
        if len(file_hash) >= 8:
            hash_int = int(file_hash[:8], 16)
            mood_index = hash_int % 7
            
            moods = ['peaceful', 'energetic', 'joyful', 'melancholic', 'mysterious', 'dramatic', 'contemplative']
            return moods[mood_index]
        
        return 'balanced'

    def _extract_musical_style(self, file_name: str, file_hash: str) -> str:
        """Extract musical style from filename with more sophisticated analysis"""
        # Priority 1: Explicit style keywords in filename
        style_keywords = {
            'jazz': ['jazz', 'swing', 'bebop', 'smooth', 'fusion'],
            'rock': ['rock', 'metal', 'punk', 'grunge', 'alternative'],
            'pop': ['pop', 'mainstream', 'radio', 'chart', 'hit'],
            'electronic': ['electronic', 'edm', 'techno', 'house', 'trance', 'synth'],
            'classical': ['classical', 'orchestra', 'symphony', 'concerto', 'sonata'],
            'folk': ['folk', 'acoustic', 'traditional', 'country', 'bluegrass'],
            'ambient': ['ambient', 'atmospheric', 'chill', 'lounge', 'downtempo'],
            'hip_hop': ['hip', 'hop', 'rap', 'urban', 'r&b', 'soul']
        }
        
        file_lower = file_name.lower()
        for style, keywords in style_keywords.items():
            if any(keyword in file_lower for keyword in keywords):
                return style
        
        # Priority 2: Instrument-based style hints
        instrument_styles = {
            'jazz': ['piano', 'sax', 'trumpet', 'bass', 'drums'],
            'rock': ['guitar', 'electric', 'drums', 'bass', 'distortion'],
            'classical': ['violin', 'cello', 'orchestra', 'strings', 'brass'],
            'folk': ['acoustic', 'guitar', 'banjo', 'harmonica', 'fiddle'],
            'electronic': ['synth', 'digital', 'electronic', 'computer', 'beats'],
            'ambient': ['piano', 'strings', 'atmospheric', 'pad', 'drone']
        }
        
        for style, instruments in instrument_styles.items():
            if any(instrument in file_lower for instrument in instruments):
                return style
        
        # Priority 3: Hash-based style with more variation
        if len(file_hash) >= 16:
            hash_int = int(file_hash[8:16], 16)
            style_index = hash_int % 8
            
            styles = ['jazz', 'rock', 'pop', 'electronic', 'classical', 'folk', 'ambient', 'hip_hop']
            return styles[style_index]
        
        return 'pop'

    def _determine_energy_level(self, mood: str, file_name: str, file_hash: str) -> str:
        """Determine energy level with more sophisticated analysis"""
        file_lower = file_name.lower()
        
        # Priority 1: Explicit energy keywords in filename
        energy_keywords = {
            'high': ['high', 'energetic', 'powerful', 'intense', 'dynamic', 'fast', 'upbeat'],
            'medium': ['medium', 'moderate', 'balanced', 'steady', 'smooth'],
            'low': ['low', 'quiet', 'soft', 'gentle', 'calm', 'peaceful', 'slow']
        }
        
        for level, keywords in energy_keywords.items():
            if any(keyword in file_lower for keyword in keywords):
                return level
        
        # Priority 2: Mood-based energy (with some variation)
        mood_energy_map = {
            'energetic': 'high',
            'joyful': 'high',
            'dramatic': 'high',
            'passionate': 'high',
            'peaceful': 'low',
            'melancholic': 'low',
            'mysterious': 'low',
            'contemplative': 'low'
        }
        
        if mood in mood_energy_map:
            base_energy = mood_energy_map[mood]
            
            # Add some variation based on hash
            if len(file_hash) >= 24:
                hash_int = int(file_hash[16:24], 16)
                variation = hash_int % 3
                
                # 70% chance of mood-based energy, 30% chance of variation
                if variation < 2:  # 67% chance
                    return base_energy
                else:  # 33% chance of variation
                    energy_levels = ['low', 'medium', 'high']
                    current_index = energy_levels.index(base_energy)
                    # Move one step up or down
                    if variation == 2:
                        return energy_levels[min(current_index + 1, 2)]
                    else:
                        return energy_levels[max(current_index - 1, 0)]
        
        # Priority 3: Hash-based energy with more variation
        if len(file_hash) >= 24:
            hash_int = int(file_hash[16:24], 16)
            energy_index = hash_int % 3
            
            energy_levels = ['low', 'medium', 'high']
            return energy_levels[energy_index]
        
        return 'medium'

    def _estimate_tempo(self, mood: str, energy_level: str, file_hash: str) -> int:
        """Estimate tempo with more sophisticated analysis"""
        # Base tempo ranges by mood and energy
        tempo_ranges = {
            'energetic': {'low': (100, 130), 'medium': (130, 160), 'high': (160, 200)},
            'joyful': {'low': (90, 120), 'medium': (120, 150), 'high': (150, 180)},
            'dramatic': {'low': (60, 90), 'medium': (90, 120), 'high': (120, 160)},
            'passionate': {'low': (70, 100), 'medium': (100, 130), 'high': (130, 170)},
            'peaceful': {'low': (40, 70), 'medium': (70, 100), 'high': (100, 130)},
            'melancholic': {'low': (50, 80), 'medium': (80, 110), 'high': (110, 140)},
            'mysterious': {'low': (60, 90), 'medium': (90, 120), 'high': (120, 150)},
            'contemplative': {'low': (40, 70), 'medium': (70, 100), 'high': (100, 130)}
        }
        
        # Get base tempo range
        if mood in tempo_ranges and energy_level in tempo_ranges[mood]:
            min_tempo, max_tempo = tempo_ranges[mood][energy_level]
        else:
            # Default range
            min_tempo, max_tempo = 80, 120
        
        # Add variation based on hash
        if len(file_hash) >= 32:
            hash_int = int(file_hash[24:32], 16)
            
            # Use hash to determine position within the range
            position = (hash_int % 100) / 100.0  # 0.0 to 1.0
            
            # Calculate tempo with some randomness
            tempo = min_tempo + (max_tempo - min_tempo) * position
            
            # Add some additional variation (±10 BPM)
            variation = (hash_int % 20) - 10
            tempo += variation
            
            return max(40, min(200, int(tempo)))
        
        # Fallback to middle of range
        return int((min_tempo + max_tempo) / 2)

    def _determine_complexity(self, file_size: int, file_name: str, file_hash: str) -> str:
        """Determine complexity based on file characteristics"""
        # Base complexity from file size
        if file_size > 10 * 1024 * 1024:  # > 10MB
            base_complexity = 'complex'
        elif file_size > 5 * 1024 * 1024:  # > 5MB
            base_complexity = 'moderate'
        else:
            base_complexity = 'simple'
        
        # Check for complexity indicators in filename
        name_lower = file_name.lower()
        if any(word in name_lower for word in ['complex', 'layered', 'rich', 'sophisticated']):
            return 'complex'
        elif any(word in name_lower for word in ['simple', 'minimal', 'basic']):
            return 'simple'
        
        # Use hash for variation
        hash_int = int(file_hash[32:40], 16) if len(file_hash) >= 40 else 0
        if hash_int % 10 < 3:  # 30% chance to vary
            complexities = ['simple', 'moderate', 'complex']
            current_index = complexities.index(base_complexity)
            return complexities[(current_index + 1) % len(complexities)]
        
        return base_complexity

    def _estimate_spectral_centroid(self, mood: str, musical_style: str, file_hash: str) -> float:
        """Estimate spectral centroid (brightness indicator)"""
        # Base values from mood
        base_values = {
            'peaceful': 2000, 'calm': 2500, 'dramatic': 3500, 'energetic': 4500,
            'joyful': 4000, 'melancholic': 1800, 'mysterious': 2200, 'passionate': 3800, 'contemplative': 2000
        }
        
        base_value = base_values.get(mood, 3000)
        
        # Adjust for musical style
        style_adjustments = {
            'piano': -500, 'rock': 1000, 'electronic': 800, 'ambient': -300,
            'folk': -200, 'jazz': 200, 'pop': 500, 'classical': 0
        }
        
        adjusted_value = base_value + style_adjustments.get(musical_style, 0)
        
        # Add variation
        hash_int = int(file_hash[40:48], 16) if len(file_hash) >= 48 else 0
        variation = (hash_int % 2000) - 1000  # ±1000 Hz variation
        
        return max(500, min(8000, adjusted_value + variation))

    def _determine_brightness(self, spectral_centroid: float, mood: str) -> str:
        """Determine brightness based on spectral centroid and mood"""
        if spectral_centroid > 4000:
            return 'bright'
        elif spectral_centroid < 2000:
            return 'dark'
        elif mood in ['joyful', 'energetic']:
            return 'bright'
        elif mood in ['melancholic', 'mysterious']:
            return 'dark'
        else:
            return 'balanced'

    def _estimate_dynamic_range(self, energy_level: str, mood: str, file_hash: str) -> float:
        """Estimate dynamic range"""
        base_ranges = {'low': 10, 'medium': 20, 'high': 30}
        base_range = base_ranges.get(energy_level, 20)
        
        # Adjust for mood
        mood_adjustments = {
            'dramatic': 10, 'passionate': 8, 'energetic': 5,
            'peaceful': -5, 'calm': -3, 'melancholic': -2
        }
        
        adjusted_range = base_range + mood_adjustments.get(mood, 0)
        
        # Add variation
        hash_int = int(file_hash[48:56], 16) if len(file_hash) >= 56 else 0
        variation = (hash_int % 20) - 10  # ±10 dB variation
        
        return max(5, min(50, adjusted_range + variation))

    def _estimate_energy_variance(self, energy_level: str, file_hash: str) -> float:
        """Estimate energy variance"""
        base_variances = {'low': 10000, 'medium': 30000, 'high': 60000}
        base_variance = base_variances.get(energy_level, 30000)
        
        # Add variation
        hash_int = int(file_hash[56:64], 16) if len(file_hash) >= 64 else 0
        variation = (hash_int % 40000) - 20000  # ±20000 variation
        
        return max(5000, min(100000, base_variance + variation))

    def _estimate_duration(self, file_size: int, file_name: str) -> float:
        """Estimate duration based on file size and name"""
        # Base estimation by format
        bitrates = {
            '.mp3': 128000, '.m4a': 256000, '.wav': 1411000, 
            '.flac': 1000000, '.aac': 256000, '.ogg': 192000
        }
        
        file_extension = os.path.splitext(file_name)[1].lower()
        bitrate = bitrates.get(file_extension, 256000)
        
        # Calculate theoretical duration
        theoretical_duration = (file_size * 8) / bitrate
        
        # Adjust based on filename hints
        name_lower = file_name.lower()
        if any(word in name_lower for word in ['short', 'clip', 'sample']):
            return min(60, theoretical_duration * 0.3)
        elif any(word in name_lower for word in ['long', 'full', 'complete']):
            return min(600, theoretical_duration * 2.0)
        
        return max(10, min(600, theoretical_duration))

    def detect_instruments(self, audio_path: str, transcription: str = "") -> List[Dict[str, Any]]:
        """Detect instruments based on filename and transcription analysis"""
        detected_instruments = []
        file_name = os.path.basename(audio_path).lower()
        transcription_lower = transcription.lower() if transcription else ""
        
        # Score each instrument based on filename and transcription
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
            
            # Add to detected instruments if score is high enough
            if score >= 2:  # Lowered from 3 to 2 for more sensitivity
                detected_instruments.append({
                    'name': instrument_name,
                    'score': score,
                    'confidence': min(score / 10.0, 1.0),
                    'reasons': detection_reasons
                    # Note: visual_elements, colors, textures, mood_associations are available
                    # in instrument_data but not included in the response to maintain compatibility
                })
        
        # If no instruments detected, make some intelligent assumptions
        if not detected_instruments:
            # Assume voice is likely present in most songs (lower confidence)
            detected_instruments.append({
                'name': 'voice',
                'score': 2,
                'confidence': 0.3,
                'reasons': ['assumed presence in vocal music']
            })
            
            # Check for subtle hints in filename
            if any(word in file_name for word in ['melody', 'song', 'music', 'track']):
                detected_instruments.append({
                    'name': 'piano',
                    'score': 2,
                    'confidence': 0.25,
                    'reasons': ['melodic content suggested']
                })
        
        # Add common instruments with low confidence based on general music patterns
        if len(detected_instruments) <= 1:  # If we only have voice or nothing
            # Add common instruments with low confidence based on general music patterns
            common_instruments = [
                ('piano', 0.2, 'common melodic instrument'),
                ('drums', 0.2, 'rhythmic foundation'),
                ('guitar', 0.15, 'common accompaniment')
            ]
            
            for inst_name, confidence, reason in common_instruments:
                if not any(inst['name'] == inst_name for inst in detected_instruments):
                    detected_instruments.append({
                        'name': inst_name,
                        'score': 2,
                        'confidence': confidence,
                        'reasons': [reason]
                    })
        
        # Sort by confidence score
        detected_instruments.sort(key=lambda x: x['score'], reverse=True)
        
        return detected_instruments

    def generate_color_palette(self, features: Dict[str, Any], detected_instruments: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generate color palette based on analyzed features and detected instruments"""
        mood = features.get('mood', 'balanced')
        energy_level = features.get('energy_level', 'medium')
        musical_style = features.get('musical_style', 'pop')
        
        # Get base colors from mood
        base_colors = self.mood_keywords.get(mood, {}).get('colors', ['sage green', 'sky blue', 'cream yellow'])
        
        # Add style-specific colors
        style_colors = {
            'piano': ['warm brown', 'cream yellow', 'sage green'],
            'rock': ['crimson red', 'steel blue', 'dark slate gray'],
            'electronic': ['hot pink', 'lime green', 'electric blue'],
            'ambient': ['lavender', 'dark turquoise', 'plum'],
            'folk': ['sage green', 'warm brown', 'sky blue'],
            'jazz': ['steel blue', 'plum purple', 'sage green'],
            'pop': ['coral red', 'golden yellow', 'sky blue'],
            'classical': ['cream yellow', 'sage green', 'lavender']
        }
        
        style_specific = style_colors.get(musical_style, [])
        
        # Add instrument-specific colors if instruments are detected
        instrument_colors = []
        if detected_instruments:
            for instrument in detected_instruments[:2]:  # Top 2 instruments
                inst_name = instrument['name']
                if inst_name in self.instrument_database:
                    instrument_colors.extend(self.instrument_database[inst_name]['colors'])
        
        # Combine all color sources
        all_colors = base_colors + style_specific + instrument_colors
        unique_colors = list(dict.fromkeys(all_colors))  # Preserve order while removing duplicates
        
        # Limit to 6 colors
        final_colors = unique_colors[:6]
        
        # Generate description
        descriptions = {
            'peaceful': 'soft and harmonious',
            'calm': 'gentle and balanced',
            'dramatic': 'rich and intense',
            'energetic': 'vibrant and dynamic',
            'joyful': 'bright and cheerful',
            'melancholic': 'deep and contemplative',
            'mysterious': 'ethereal and dreamy',
            'passionate': 'warm and intense',
            'contemplative': 'subtle and refined'
        }
        
        description = descriptions.get(mood, 'balanced and harmonious')
        
        # Add instrument influence to description
        if detected_instruments:
            top_instrument = detected_instruments[0]['name']
            if top_instrument == 'piano':
                description += ' with elegant piano tones'
            elif top_instrument == 'guitar':
                description += ' with warm guitar textures'
            elif top_instrument == 'voice':
                description += ' with expressive vocal elements'
            elif top_instrument == 'nature_sounds':
                description += ' with natural environmental elements'
            elif top_instrument == 'synth':
                description += ' with electronic digital elements'
        
        return {
            'final_colors': final_colors,
            'description': description,
            'mood': mood,
            'energy_level': energy_level,
            'musical_style': musical_style,
            'detected_instruments': detected_instruments or []
        } 