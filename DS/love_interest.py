from npc import NPC
#from player import Player
from random import randint

import numpy as np
import pandas as pd

class Love_Interest(NPC):
    def __init__(self, NAME, INIT_LOC, INTEREST):
        NPC.__init__(self, NAME, INIT_LOC, INTEREST)
        self.relation_level = 0
        self.relation = "Neutral"
        self.speech_possibilities = pd.read_csv("Love Interest/" + self.name.rstrip("\n") + "Reactions\Reactions.csv")

    def set_relation(self):
        if (self.relation_level < -60):
            self.relation = "Bitter Enemy"
        elif (self.relation_level >= -60 and self.relation_level < -20):
            self.relation = "Angry"
        elif (self.relation_level >= -20 and self.relation_level < 0):
            self.relation = "Neutral"
        elif (self.relation_level >= 0 and self.relation_level < 20):
            self.relation = "Acquaintance"
        elif (self.relation_level >= 20 and self.relation_level < 40):
            self.relation = "Friend"
        elif (self.relation_level >= 40 and self.relation_level < 60):
            self.relation = "Boyfriend"
        elif (self.reaction_level >= 60 and self.relation_level < 80):
            self.relation = "Lover"
    
    def help_relation(self, amount):
        self.relation = self.relation + amount

    def hurt_relation(self, amount):
        self.relation = self.relation - amount

    def set_speech(self, Player):
        current_action = "Approach"

        possibility = []

        if(Player.academics_level == "MEDIUM" and Player.fitness_level == "MEDIUM" and Player.social_level == "MEDIUM" and Player.confidence_level == "MEDIUM"):
            current_action = "Approach"

        else:
            if Player.academics_level == "LOW":
                possibility[0] = 'Low Academics'
            elif Player.academics_level == "MEDIUM":
                possibility[0] = "Approach"
            elif Player.academics_level == "HIGH":
                possibility[0] = 'High Academics'

            if Player.fitness_level == "LOW":
                possibility[1] = 'Low Fitness'
            elif Player.fitness_level == "MEDIUM":
                possibility[1] = "Approach"
            elif Player.fitness_level == "HIGH":
                possibility[1] = 'High Fitness'

            if Player.social_level == "LOW":
                possiblity[2] = "Low Social"
            elif Player.social_level == "MEDIUM":
                possibility[2] = "Approach"
            elif Player.social_level == "HIGH":
                possibility[2] = "High Social"

            if Player.confidence_level == "LOW":
                possibility[3] = "Low Confidence"
            elif Player.confidence_level == "MEDIUM":
                possibility[3] = "Approach"
            elif Player.confidence_level == "HIGH":
                possibility[3] = "High Confidence"

            selection = randint(0,3)
            current_action = possiblity[selection]

        self.dialogue = self.speech_possibilities.loc[current_action][self.relation]
