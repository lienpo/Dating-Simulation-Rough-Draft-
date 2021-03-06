import io

class NPC:
    def __init__(self, NAME, INIT_LOC, INTEREST):
        

        self.name = NAME
        self.current_loc = INIT_LOC             
        self.dialogue = self.get_dialogue()
	self.interest = INTEREST
        
        self.get_dialogue()
                
    def get_dialogue(self):
        if self.interest == False:
            file_loc = "NPCs/" + self.name.rstrip('\n') + ".txt"
            with open(file_loc) as f:
                return f.read()

    def speak(self):
        print('\n' + self.name.rstrip('\n') + ": " + self.dialogue)
