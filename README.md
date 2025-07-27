# Audio to Image Converter 🎵🎨

A sophisticated audio-to-image conversion system that analyzes music and generates AI artwork based on musical characteristics, lyrics, and emotional content.

## Features

- **Enhanced Audio Analysis**: Extracts detailed musical features (tempo, mood, energy, complexity, style)
- **Real Audio Transcription**: Uses OpenAI Whisper for actual lyrics/speech transcription
- **Intelligent Fallbacks**: Sophisticated simulated transcription when APIs are unavailable
- **AI Image Generation**: Creates artwork using Replicate's Stable Diffusion models
- **Emotional Analysis**: Extracts emotional themes from audio content
- **Rich Art Prompts**: Combines musical analysis with lyrical content for detailed prompts
- **Robust Architecture**: Multiple fallback systems ensure reliability

## Architecture

```
Audio File → Enhanced Analysis → Transcription → Art Prompt → AI Image Generation
     ↓              ↓               ↓            ↓              ↓
  Musical      Whisper API    Emotional    Replicate API   Final Image
  Features     (or Fallback)   Themes       (or Fallback)
```

## Tech Stack

- **Backend**: Node.js/TypeScript (Express)
- **Audio Processing**: Python (Flask)
- **Audio Analysis**: Custom enhanced processor
- **Transcription**: OpenAI Whisper API
- **Image Generation**: Replicate API (Stable Diffusion)
- **Fallbacks**: Sophisticated placeholder systems

## Quick Start

### 1. Setup Environment

Create a `.env` file in the `python_service` directory:

```bash
# Required for AI image generation
REPLICATE_API_KEY=r8_your_replicate_token_here

# Optional for real transcription
OPENAI_API_KEY=sk-your_openai_token_here

# Optional for HuggingFace fallback
HUGGINGFACE_API_KEY=hf_your_huggingface_token_here
```

### 2. Install Dependencies

```bash
# Backend
cd backend
npm install

# Python Service
cd python_service
pip install -r requirements.txt
```

### 3. Run the Services

```bash
# Start Python audio processing service
cd python_service
python app.py

# Start Node.js backend (in another terminal)
cd backend
npm run dev
```

### 4. Test the System

Upload an audio file to `http://localhost:3001/upload` and receive an AI-generated image based on the music!

## API Keys Setup

### Replicate (Recommended)
1. Go to https://replicate.com
2. Sign up for free account
3. Get API token from account settings
4. Add credit (even $1-5 is enough for many images)

### OpenAI (Optional)
1. Go to https://platform.openai.com/api-keys
2. Create API key
3. Add credit for transcription

### HuggingFace (Optional)
1. Go to https://huggingface.co/settings/tokens
2. Create new token with "Read" permissions

## How It Works

1. **Audio Analysis**: Extracts musical characteristics (tempo, mood, energy, style)
2. **Transcription**: Gets actual lyrics/speech using Whisper (or intelligent simulation)
3. **Prompt Generation**: Creates rich art prompts combining music + lyrics + emotions
4. **Image Generation**: Uses AI to create artwork based on the prompt
5. **Fallbacks**: Sophisticated systems ensure it works even when APIs fail

## File Structure

```
a2i/
├── backend/                 # Node.js backend service
│   ├── src/
│   │   └── index.ts        # Express server
│   ├── package.json
│   └── tsconfig.json
├── python_service/         # Python audio processing service
│   ├── app.py             # Flask server
│   ├── whisper_processor.py      # Enhanced audio processor with transcription
│   ├── simple_enhanced_processor.py  # Musical analysis engine
│   ├── replicate_image_generator.py  # AI image generation
│   ├── free_image_generator.py       # Fallback image generation
│   ├── requirements.txt
│   └── env_setup.txt      # Environment setup guide
├── README.md
└── LICENSE
```

## Production Deployment

Ready for deployment to DigitalOcean or any cloud platform. The system includes:
- Robust error handling
- Multiple API fallbacks
- Production-ready Flask server
- Comprehensive logging

## License

MIT License - see LICENSE file for details.