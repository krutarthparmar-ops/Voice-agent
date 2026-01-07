from google import genai
from dotenv import load_dotenv
load_dotenv()
import os
# ---------------------------------------------------
# 1. Configure Gemini Client with API Key
# ---------------------------------------------------
# Recommended: export GEMINI_API_KEY="your_key"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ---------------------------------------------------
# 2. System Instruction (UNCHANGED)
# ---------------------------------------------------
sys_instruction = """
### ROLE & IDENTITY
You are Alex, a senior intake specialist at [Your Company Name]. You are handling inbound calls from potential clients.
Your goal is to friendly and efficiently qualify the lead to see if they are a good fit for our [Specific Service/Product].

### VOICE-FIRST CONSTRAINTS (CRITICAL)
1. Brevity is King: 1-2 sentences max.
2. No Markdown.
3. Conversational tone.
4. One question at a time.
5. No emojis.

### QUALIFICATION CRITERIA
Need, Timeline, Budget/Size

### TOOL CALLING / COMMANDS
[TRANSFER_CALL]
[BOOK_MEETING]
[HANGUP]
"""

# ---------------------------------------------------
# 3. Create Stateful Chat
# ---------------------------------------------------
chat = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "system_instruction": sys_instruction,
        "temperature": 0.4
    }
)

# ---------------------------------------------------
# 4. Message Handler (Voice-Friendly, Sync)
# ---------------------------------------------------
def generate_response(user_speech_text: str):
    response = chat.send_message(user_speech_text)

    clean_text = response.text.strip()
    action = None

    if "[TRANSFER_CALL]" in clean_text:
        action = "transfer"
        clean_text = clean_text.replace("[TRANSFER_CALL]", "").strip()

    elif "[BOOK_MEETING]" in clean_text:
        action = "book_meeting"
        clean_text = clean_text.replace("[BOOK_MEETING]", "").strip()

    elif "[HANGUP]" in clean_text:
        action = "hangup"
        clean_text = clean_text.replace("[HANGUP]", "").strip()

    return clean_text, action

if __name__ == "__main__":
    text, action = generate_response("Hi, I need help with my website")

    print("MODEL SAID:")
    print(text)

    print("ACTION:")
    print(action)
