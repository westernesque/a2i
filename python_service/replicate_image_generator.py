import os
import requests
import base64
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

class ReplicateImageGenerator:
    """Image generator using Replicate API"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('REPLICATE_API_KEY')
        self.base_url = "https://api.replicate.com/v1/predictions"
        
        # Popular models on Replicate
        self.models = {
            "stable-diffusion": "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
            "realistic": "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            "anime": "cjwbw/anything-v3-better-vae:09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65",
            "artistic": "prompthero/openjourney:ad59ca21177f9e217b907481edde9dacfbdb29d5a0ac332e583b64bd646bffaa"
        }
    
    def generate_image(self, prompt: str, model_type: str = "realistic") -> Image.Image:
        """Generate image using Replicate API"""
        
        if not self.api_key:
            print("No Replicate API key found, using placeholder")
            return self._create_placeholder_image(prompt)
        
        try:
            model = self.models.get(model_type, self.models["realistic"])
            
            headers = {
                "Authorization": f"Token {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Enhance prompt for more colorful, vibrant images
            enhanced_prompt = self._enhance_prompt_for_color(prompt)
            
            # Create prediction with enhanced parameters
            payload = {
                "version": model,
                "input": {
                    "prompt": enhanced_prompt,
                    "width": 1024,
                    "height": 1024,
                    "num_outputs": 1,
                    "guidance_scale": 7.5,
                    "num_inference_steps": 50,
                    "scheduler": "K_EULER"
                }
            }
            
            print(f"Creating prediction with Replicate (SDXL)...")
            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload
            )
            
            if response.status_code == 201:
                prediction = response.json()
                prediction_id = prediction['id']
                
                # Poll for completion
                import time
                max_attempts = 30
                attempts = 0
                
                while attempts < max_attempts:
                    time.sleep(2)
                    status_response = requests.get(
                        f"{self.base_url}/{prediction_id}",
                        headers=headers
                    )
                    
                    if status_response.status_code == 200:
                        status_data = status_response.json()
                        
                        if status_data['status'] == 'succeeded':
                            # Get the image URL
                            image_url = status_data['output'][0]
                            
                            # Download the image
                            img_response = requests.get(image_url)
                            if img_response.status_code == 200:
                                return Image.open(BytesIO(img_response.content))
                            else:
                                print(f"Error downloading image: {img_response.status_code}")
                                break
                                
                        elif status_data['status'] == 'failed':
                            print(f"Prediction failed: {status_data.get('error', 'Unknown error')}")
                            break
                        elif status_data['status'] == 'processing':
                            print(f"Still processing... attempt {attempts + 1}")
                            attempts += 1
                            continue
                    else:
                        print(f"Error checking status: {status_response.status_code}")
                        break
                
                print("Timeout waiting for prediction completion")
                return self._create_placeholder_image(prompt)
                
            else:
                print(f"Error creating prediction: {response.status_code}")
                print(response.text)
                return self._create_placeholder_image(prompt)

        except Exception as e:
            print(f"Error in Replicate image generation: {e}")
            return self._create_placeholder_image(prompt)

    def _enhance_prompt_for_color(self, prompt: str) -> str:
        """Enhance prompt to encourage more colorful, vibrant images"""
        # Add color-enhancing keywords
        color_enhancers = [
            "vibrant colors",
            "rich color palette", 
            "warm tones",
            "bright and colorful",
            "saturated colors",
            "colorful composition",
            "vivid imagery",
            "luminous colors"
        ]
        
        # Add artistic style enhancers
        style_enhancers = [
            "artistic",
            "creative",
            "expressive",
            "dynamic",
            "visually striking"
        ]
        
        # Combine original prompt with enhancements
        enhanced_parts = [prompt]
        
        # Add 2-3 random color enhancers
        import random
        selected_colors = random.sample(color_enhancers, 2)
        enhanced_parts.extend(selected_colors)
        
        # Add 1-2 style enhancers
        selected_styles = random.sample(style_enhancers, 1)
        enhanced_parts.extend(selected_styles)
        
        # Add technical quality enhancers
        enhanced_parts.extend([
            "high quality",
            "detailed",
            "professional digital art"
        ])
        
        return ", ".join(enhanced_parts)

    def _create_placeholder_image(self, prompt: str) -> Image.Image:
        """Create a placeholder image when API is not available"""
        # Create a simple placeholder
        img = Image.new('RGB', (512, 512), color='#2a2a2a')
        
        from PIL import ImageDraw, ImageFont
        import random
        
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.load_default()
        except:
            font = None
        
        # Add some visual elements
        for i in range(50):
            x = random.randint(0, 512)
            y = random.randint(0, 512)
            size = random.randint(2, 8)
            color = (
                random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255)
            )
            draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
        
        # Add text
        if font:
            draw.text((20, 20), "🎵 Audio to Image 🎨", fill=(255, 255, 255), font=font)
            draw.text((20, 50), f"Prompt: {prompt[:40]}...", fill=(200, 200, 200), font=font)
            draw.text((20, 80), "Replicate API Placeholder", fill=(180, 180, 180), font=font)
        
        return img 