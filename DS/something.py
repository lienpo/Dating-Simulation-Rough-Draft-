class Additive:
      
    def __init__(self, X, Y):
        self.sum = X + Y

    def give_sum(self):
        print("The sum of the two values is " + str(self.sum) + ".")
 




a = 5
b = 2
Addition = Additive(a, b)
Addition.give_sum()


