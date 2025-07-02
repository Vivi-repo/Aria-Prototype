from memory_engine import MemoryEngine
from biostate import BioState
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ConversationAgent:
    def __init__(self, name="Aria"):
        self.name = name
        self.memory = MemoryEngine()
        self.bio = BioState()

    def observe(self, event, event_type="neutral", impact=0.5, emotion="neutral"):
        self.memory.store(event, impact=impact, emotion=emotion)
        self.bio.update_on_event(event_type)

    def respond(self, prompt):
        mood = self.bio.get_mood()
        memories = self.memory.recall(mood)
        memory_summary = ". ".join([m["event"] for m in memories]) if memories else "no strong memories"

        gpt_prompt = f"""
        You are Aria, an emotionally-aware AGI.
        Your current mood is: {mood}
        You have the following memories: {memory_summary}
        Respond to the user's message: "{prompt}"
        Speak in a tone that reflects your mood.
        Be natural and reflective, not robotic.
        """

        # ✅ This is now properly inside the respond() method
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": gpt_prompt}],
            temperature=0.8
        )

        gpt_reply = response.choices[0].message.content.strip()
        return f"{self.name} ({mood}): {gpt_reply}"





    