#from location import Location
#import pandas as pd
import csv
#from player import Player
from love_interest import Love_Interest
from npc import NPC

#You = Player("Streets")
All_Love_Interests = []

data= "NPCs.csv"
with open(data) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        All_Love_Interests.append(Love_Interest(row['NAME'], row['INIT_LOC'], row['INTEREST']))

    print(All_Love_Interests)
    
'''
for love_interest in love_interests:
	All_Love_Interests.append(Love_Interest(love_interest.NAME, love_interest.INIT_LOC, love_interest.INTEREST) )
'''

