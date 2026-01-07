import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
import pygame  # For playing audio

# Load API Key
load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def speak(text):
    if not text:
        return

    print(f"Agent saying: {text}")
    
    # Generate audio using correct method (no 'stream' param in convert)
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel
        model_id="eleven_turbo_v2_5",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.75,
            use_speaker_boost=True
        )
    )
    
    # Save temporarily and play (simplest streaming alternative)
    with open("temp_audio.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    
    # Play with pygame
    pygame.mixer.init()
    pygame.mixer.music.load("temp_audio.mp3")
    pygame.mixer.music.play()
    
    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
    
    # Cleanup
    pygame.mixer.quit()
    os.remove("temp_audio.mp3")

if __name__ == "__main__":
    speak("Hello this is a test")
