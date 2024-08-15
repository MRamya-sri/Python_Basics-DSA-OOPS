class Birds:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Birds):
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Birds):
    def flight(self):
        print("Ostriches cannot fly.")

#creating objects

obj_Birds = Birds()
obj_sparrow = sparrow()
obj_ostrich = ostrich()

#overriding parent class and as well as inheriting. 

# inheriting other methods in parent class
obj_sparrow.intro()

# overriding the method which has same methods in parent and child class but child class overrides the parent class  and executes its method
obj_sparrow.flight()
