# Audio to Image Converter

An experimental project that converts audio files into visual art using AI-powered transcription and image generation.

## Features

- **Audio Analysis**: Sophisticated musical feature extraction and analysis
- **AI Transcription**: Real-time audio-to-text conversion using Replicate's Whisper models
- **AI Image Generation**: Creates visual art from audio content using Replicate's Stable Diffusion
- **Enhanced Prompts**: Generates detailed art prompts incorporating musical characteristics and lyrical content
- **Fallback System**: Intelligent placeholder generation when APIs are unavailable

## Tech Stack

- **Backend**: Node.js with Express and TypeScript
- **Audio Processing**: Python with Flask
- **AI Services**: Replicate API (Whisper for transcription, Stable Diffusion for images)
- **Image Processing**: Pillow (PIL)

## Quick Start

### Prerequisites
- Node.js and npm
- Python 3.8+
- Replicate API key with account credit

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd a2i
   ```

2. **Install backend dependencies**
   ```bash
   cd backend
   npm install
   ```

3. **Install Python dependencies**
   ```bash
   cd ../python_service
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Create .env file in python_service directory
   echo "REPLICATE_API_KEY=your_replicate_api_key_here" > .env
   ```

5. **Start the services**
   ```bash
   # Terminal 1: Start Python service
   cd python_service
   python app.py
   
   # Terminal 2: Start Node.js backend
   cd backend
   npm run dev
   ```

## API Key Setup

### Replicate API Key
1. Go to https://replicate.com/
2. Sign up or log in to your account
3. Go to your account settings
4. Generate a new API token
5. Add $5+ credit to your account (required for API usage)

The system uses Replicate for both:
- **Transcription**: Whisper models for audio-to-text conversion
- **Image Generation**: Stable Diffusion models for creating visual art

## How It Works

1. **Audio Upload**: Audio file is uploaded to the Node.js backend
2. **Audio Analysis**: Python service analyzes musical characteristics (tempo, mood, energy, etc.)
3. **Transcription**: Replicate Whisper converts audio to text, extracting lyrics and content
4. **Prompt Generation**: Creates detailed art prompts combining musical features and lyrical content
5. **Image Generation**: Replicate Stable Diffusion generates visual art from the enhanced prompts
6. **Response**: Returns the generated image to the user

## File Structure

```
a2i/
├── backend/                 # Node.js backend
│   ├── src/
│   │   └── index.ts        # Express server
│   ├── package.json
│   └── tsconfig.json
├── python_service/         # Python audio processing
│   ├── app.py             # Flask server
│   ├── whisper_processor.py # Audio processor with Replicate transcription
│   ├── replicate_image_generator.py # Replicate image generation
│   ├── simple_enhanced_processor.py # Musical analysis
│   ├── requirements.txt
│   └── .env               # API keys
└── README.md
```

## Production Deployment

The system is ready for production deployment on platforms like:
- **DigitalOcean**: Deploy both services on separate droplets
- **Heroku**: Deploy Python service with proper WSGI server
- **Railway**: Easy deployment for both Node.js and Python services

### Environment Variables for Production
```bash
REPLICATE_API_KEY=your_production_replicate_key
FLASK_ENV=production
NODE_ENV=production
```

## Testing

Test the complete pipeline:
```bash
cd python_service
python test_replicate_transcription.py
```

## License

MIT License - see LICENSE file for details.