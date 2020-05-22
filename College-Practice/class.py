# Class is an blueprint for instances
class Animal():
    def __init__(self, name):
       self.name = name
       self.species = "Animal"

    # method for class 
    def introduce(self):
        print("I am {} of {} species".format(self.name, self.species))
cat = Animal("Cat")
cat.introduce()