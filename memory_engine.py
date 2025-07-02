import datetime
class MemoryEngine:
    def __init__(self):
        self.episodes=[]
    def store(self, event, impact= 0.5, emotion ="neutral"):
        self.episodes.append({"timestamp": str(datetime.datetime.now()), "event" : event, "impact" :float (impact),"emotion" :emotion })
    def recall(self, mood ="neutral"):
          return[
               m for m in self.episodes
               if m["emotion"] == mood or m["impact"] > 0.7
          ][-5:]
    