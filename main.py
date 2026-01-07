import time
from transcriber import listen_to_mic
from synthesizer import speak
from model import generate_response

def main():
    print("--- Local Voice Agent Started ---")
    print("Press Ctrl+C to stop manually\n")

    while True:
        # 1. LISTEN
        user_text = listen_to_mic()
        
        # If silence or error, skip loop
        if not user_text:
            continue
            
        # 2. THINK (Gemini)
        ai_response_text, action = generate_response(user_text)
        
        # 3. SPEAK (ElevenLabs)
        # We speak BEFORE executing actions to ensure the user hears the goodbye
        speak(ai_response_text)
        
        # 4. ACT
        if action == "hangup":
            print("--- Call Ended by Agent ---")
            break
        elif action == "transfer":
            print("--- [SYSTEM] CALL TRANSFERRED ---")
            break
        elif action == "book_meeting":
            print("--- [SYSTEM] MEETING BOOKED ---")
            # You could add logic here to write to a CSV/Database

if __name__ == "__main__":
    main()
