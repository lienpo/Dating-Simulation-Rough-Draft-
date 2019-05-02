class Timeline:
    def __init__(self):
    self.day = 0
    self.day_time = "EARLY MORNING"
    self.weekday = "MONDAY"

    def day_over(self):
        if( self.day <= 100 ):
            self.day = self.day + 1
            self.day_time = "EARLY MORNING"
            self.next_weekday()
        elif (self.day == 100):
            self.end_of_game()
    
    def change_day_time(self):
        if self.day_time == "EARLY MORNING":
            self.day_time = "MID-MORNING"
        if self.day_time == "MID-MORNING":
            self.day_time = "AFTERNOON"
        if self.day_time == "AFTERNOON":
            self.day_time = "EVENING"
        if self.day_time == "EVENING":
            self.day_time = "LATE NIGHT"
        if self.day_time == "LATE NIGHT":
            self.day_over()

    def next_weekday():
        if self.weekday == "MONDAY":
            self.weekday = "TUESDAY"
        if self.weekday == "TUESDAY":
            self.weekday = "WEDNESDAY"
        if self.weekday == "WEDNESDAY":
            self.weekday = "THURSDAY"
        if self.weekday == "THURSDAY":
            self.weekday = "FRIDAY"
        if self.weekday == "FRIDAY":
            self.weekday = "SATURDAY"
        if self.weekday == "SATURDAY":
            self.weekday = "SUNDAY"
        if self.weekday == "SUNDAY":
            self.weekday = "MONDAY"
