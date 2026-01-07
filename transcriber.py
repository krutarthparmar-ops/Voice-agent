import speech_recognition as sr

def listen_to_mic():
    recognizer = sr.Recognizer()
    # Adjust for ambient noise
    with sr.Microphone() as source:
        print("\nListening... (Speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        # Uses Google Speech Recognition (Free tier)
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError:
        print("API unavailable")
        return None
if __name__=="__main__":
    listen_to_mic()

