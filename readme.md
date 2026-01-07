### File structure
```
local_agent/
├── .env                # Your API keys
├── main.py             # The core logic loop
├── model.py            # Gemini configuration (Your code)
├── transcriber.py      # Microphone-to-Text logic
├── synthesizer.py      # Text-to-Speech (ElevenLabs) logic
└── requirements.txt    # List of dependencies
```

### Installation
```
brew install portaudio
pip install -r requirements.txt
```

### configuration

GEMINI_API_KEY=your_google_gemini_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

### 🚀 RUN
```
python main.py
```
