class BioState:
    def __init__ (self):
        self.hormones = {"cortisol":0.3, "oxytocin": 0.5, "testosterone": 0.4}
        self.sleep = 0.9
    def update_on_event(self, event_type):
        if "betrayal" in event_type:
            self.hormones["cortisol"]+=0.2
            self.hormones["oxytocin"]-=0.1
        elif "bonding" in event_type:
            self.hormones["oxytocin"]+=0.2
        elif "ambition" in event_type:
            self.hormones["testosterone"]+=0.2
        self.sleep -= 0.05
        self._regulate()
    def get_mood(self):
        if self.hormones["cortisol"]>0.6:
            return "tense"
        elif self.hormones["oxytocin"]>0.7:
            return "soft"
        else:
            return "neutral"
    
    def _regulate(self):
        for key in self.hormones:
            self.hormones[key] = min(max(self.hormones[key], 0), 1)
        self.sleep = min(max(self.sleep, 0), 1)
