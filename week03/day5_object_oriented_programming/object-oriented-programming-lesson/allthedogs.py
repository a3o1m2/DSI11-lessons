class AllDogs: 
    """
    Creates AllDogs class with two parameters
    """
    def __init__(self, name="", age=0):
        self.name = name 
        self.age = age
        print("Dog", self.name, "has been created.") # This will run whenever a new object is created
    
    def bark_hello(self):
        print("Yo my name is", self.name)
        return "Hey my name is " + self.name


class FlyingDogs(AllDogs):
      
    def __init__(self, name="", age=0, wings=2):
        # Set the `init` defined in the parent class. 
        AllDogs.__init__(self, name, age)
        # Now self.name and self.age are defined, because that's what happens in the parent AllDogs .__init__ method
        self.wings = wings
        self.flight_minutes = 0
        self.total_flight_time = 0
    
    def fly(self, origin, destination):

        import random
        
        flight_minutes = random.randint(5,59)
        
        print("It only took me", flight_minutes , "minutes to fly from", origin, "to", destination, "!")
        self.flight_minutes = flight_minutes
        self.add_flight_time()
        
    def add_flight_time(self):
        
        self.total_flight_time += self.flight_minutes
        print(self.name + " has flown " + str(self.total_flight_time) + " minutes in total.")

    