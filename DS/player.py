from location import Location
#from item import Item

class Player:
    def __init__(self, Location_I):
        self.current_loc = Location(Location_I)
'''
        self.academics = 0
        self.fitness = 0
        self.social = 0
        self.confidence = 0

        self.academics_level = "MEDIUM"
        self.fitness_level = "MEDIUM"
        self.social_level = "MEDIUM"
        self.confidence_level = "MEDIUM"
'''        
    def give_location_and_neighbors(self):
        print("\nYou are in the " + self.current_loc.name.rstrip('\n') + ". There are " + str(len(self.current_loc.neighbors)) + " places nearby, " + str(len(self.current_loc.observances)) + "objects to look at, and " + str(len(self.current_loc.npcs)) + " people to talk to here.\n" )
       
    def verify_selection(self, selection):
	category = " "
        action = " "
        name = " "
        file_with_options = " "
        
        group = []
        

        if(selection == 1):
            category = "npcs"
            action = "talk to"
            name = "people"
            question = "Who"
            group = self.current_loc.npcs

        elif(selection == 2):
            category = "neighbors"
            action = "go to"
            name = "places"
            question = "Where"
            group = self.current_loc.neighbors

        elif(selection == 3):
            category = "observables"
            action = "look at"
            name = "objects"
            question = "What"
            group = self.current_loc.observances
            
            
        if(len(group) > 0):
            print("\nThere are " + str(len(group)) + " " + name + " to " + action + ".\n")
            for that in group:
                print(that.name)

            inner_option = input('\n' + question + " do you want to " + action + "? ")
            if( inner_option > 0 and inner_option <= len(group) ):
                if selection == 1:
                    self.talkto(inner_option)
                elif selection == 2:
                    self.goto(inner_option)
                elif selection == 3:
                    self.lookat(inner_option)
            else:
                print("That is not a valid option.")

        elif(len(group) == 0):
            print("\nBut there are no " + name + " to " + action + " here.\n")

    def goto(self, selection):
        new_place_name = self.current_loc.neighbors[selection - 1].name
        self.current_loc.neighbors = []
        self.current_loc.npcs = []
        self.current_loc.observances = []
        self.current_loc.name = new_place_name
        self.current_loc.give_all_neighbors()
        self.current_loc.give_all_npcs()
        self.current_loc.give_all_observances()
        self.goto_inform()

    def talkto(self, selection):
        talking_npc = self.current_loc.npcs[selection - 1]
        talking_npc.speak()

    def lookat(self, selection):
        the_object = self.current_loc.observances[selection - 1]
        the_object.describe()

    def goto_inform(self):
        print("\nYou went to the " + self.current_loc.name.rstrip('\n') + ".")

    def academics_increase(self, increase):
        self.academics = self.academics + increase
        self.check_levels()

    def fitness_increase(self, increase):
        self.fitness = self.fitness + increase
        self.check_levels()

    def social_increase(self, increase):
        self.social = self.social + increase
        self.check_levels()

    def confidence_increase(self, increase):
        self.confidence = self.confidence + increase
        self.check_levels()

    def check_levels(self, lower_level, higher_level):
        if (self.academics >= higher_level):
            self.academics_level = "HIGH"
        elif (self.academics >= lower_level and self.academics < higher_level ):
            self.academics_level = "MEDIUM"
        elif (self.academics < lower_level):
            self.academics_level = "LOW"

       if (self.fitness >= higher_level):
            self.fitness_level = "HIGH"
        elif (self.fitness >= lower_level and self.fitness < higher_level ):
            self.fitness_level = "MEDIUM"
        elif (self.fitness < lower_level):
            self.fitness_level = "LOW"

        if (self.social >= higher_level):
            self.social_level = "HIGH"
        elif (self.social >= lower_level and self.social < higher_level ):
            self.social_level = "MEDIUM"
        elif (self.social < lower_level):
            self.social_level = "LOW"

        if (self.confidence >= higher_level):
            self.confidence_level = "HIGH"
        elif (self.confidence >= lower_level and self.confidence < higher_level ):
            self.confidence_level = "MEDIUM"
        elif (self.confidence < lower_level):
            self.confidence_level = "LOW"

'''
    def take_item(self, item_name, loc_from):
        self.Items_You_Have.append(Item(item_name))
        self.current.loc.Items_In_Room.remove(Item(item_name)) 
    
    def use_item(self, selection):
        item_used = self.Items_You_Have.Item[selection - 1]
        item_used.effect()
        self.Items_You_Have.remove(item_used)
'''        
    
