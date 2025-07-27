import requests
import json
import base64
from io import BytesIO
from PIL import Image

class FreeImageGenerator:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.base_url = "https://api-inference.huggingface.co/models"
        
        # Popular free models for image generation
        self.models = {
            "stable-diffusion": "runwayml/stable-diffusion-v1-5",
            "realistic": "stabilityai/stable-diffusion-2-1",
            "anime": "hakurei/waifu-diffusion",
            "artistic": "prompthero/openjourney-v2"
        }
    
    def generate_image(self, prompt: str, model_type: str = "stable-diffusion") -> Image.Image:
        """Generate image using HuggingFace's free API"""
        
        if not self.api_key:
            return self._create_placeholder_image(prompt)
        
        try:
            model = self.models.get(model_type, self.models["stable-diffusion"])
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # HuggingFace expects just the prompt as input
            response = requests.post(
                f"{self.base_url}/{model}",
                headers=headers,
                json={"inputs": prompt}
            )
            
            if response.status_code == 200:
                # HuggingFace returns the image directly
                return Image.open(BytesIO(response.content))
            else:
                print(f"HuggingFace API error: {response.status_code}")
                return self._create_placeholder_image(prompt)
                
        except Exception as e:
            print(f"Error in image generation: {e}")
            return self._create_placeholder_image(prompt)
    
    def _create_placeholder_image(self, prompt: str) -> Image.Image:
        """Create a complex, intricate placeholder image when API is not available"""
        # Create a larger canvas for more detail
        img = Image.new('RGB', (512, 512), color='#0a0a0a')
        
        from PIL import ImageDraw, ImageFont
        import random
        import math
        
        draw = ImageDraw.Draw(img)
        
        # Try to use a default font
        try:
            font = ImageFont.load_default()
        except:
            font = None
        
        # Create a complex, layered design
        
        # 1. Background gradient with multiple layers
        for y in range(0, 512, 4):
            # Create a smooth gradient from dark to light
            intensity = int(20 + (y / 512) * 100)
            color = (intensity, intensity//2, intensity*2)
            draw.line([(0, y), (512, y)], fill=color, width=4)
        
        # 2. Add swirling patterns
        center_x, center_y = 256, 256
        for i in range(0, 360, 5):
            angle = math.radians(i)
            radius = 50 + (i % 100)
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            
            # Vary colors based on angle
            r = int(100 + 155 * math.sin(angle))
            g = int(50 + 100 * math.cos(angle * 2))
            b = int(150 + 105 * math.sin(angle * 3))
            
            size = 3 + (i % 10)
            draw.ellipse([x-size, y-size, x+size, y+size], fill=(r, g, b))
        
        # 3. Add geometric patterns
        for i in range(20):
            x1 = random.randint(0, 512)
            y1 = random.randint(0, 512)
            x2 = random.randint(0, 512)
            y2 = random.randint(0, 512)
            
            # Create lines with varying colors
            color = (
                random.randint(100, 255),
                random.randint(50, 200),
                random.randint(100, 255)
            )
            width = random.randint(1, 4)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
        
        # 4. Add complex shapes
        for i in range(15):
            # Create polygons
            points = []
            num_points = random.randint(3, 8)
            center_x = random.randint(50, 462)
            center_y = random.randint(50, 462)
            radius = random.randint(20, 60)
            
            for j in range(num_points):
                angle = (j / num_points) * 2 * math.pi
                x = center_x + int(radius * math.cos(angle))
                y = center_y + int(radius * math.sin(angle))
                points.append((x, y))
            
            # Fill with semi-transparent color
            color = (
                random.randint(50, 200),
                random.randint(50, 200),
                random.randint(50, 200)
            )
            draw.polygon(points, fill=color, outline=(255, 255, 255), width=1)
        
        # 5. Add wave-like patterns (representing audio)
        for wave in range(5):
            y_base = 100 + wave * 80
            points = []
            for x in range(0, 512, 4):
                # Create sine wave with noise
                y = y_base + 20 * math.sin(x * 0.02 + wave) + random.randint(-5, 5)
                points.append((x, int(y)))
            
            # Draw the wave
            color = (
                random.randint(150, 255),
                random.randint(100, 200),
                random.randint(150, 255)
            )
            for i in range(len(points) - 1):
                draw.line([points[i], points[i+1]], fill=color, width=2)
        
        # 6. Add particle effects
        for i in range(100):
            x = random.randint(0, 512)
            y = random.randint(0, 512)
            size = random.randint(1, 3)
            color = (
                random.randint(200, 255),
                random.randint(200, 255),
                random.randint(200, 255)
            )
            draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
        
        # 7. Add text overlay (smaller and more subtle)
        if font:
            draw.text((10, 10), "🎵 Audio to Image 🎨", fill=(255, 255, 255), font=font)
            draw.text((10, 30), f"Prompt: {prompt[:30]}...", fill=(200, 200, 200), font=font)
            draw.text((10, 50), "Complex AI Art Generation", fill=(180, 180, 180), font=font)
        
        return img 