
class Dog:
    def __init__(self,breed_name,age):
        self.bredd_name = breed_name
        self.age = age

    def action(self):
        print(f"{self.age} is a good one")

class wolf(Dog):
    def __init__(self,breed_name,age,type):
        self.type = type
        Dog.__init__(self,breed_name,age)

    def action(self):
        print(f'{self.type} is cat')

d1 = Dog("pomerian",33)
c1 = wolf('siberian',21,'wolf')
d1.action()
c1.action()


class Animals():
    total_animals = 0
    @classmethod
    def Zoo_animals(cls):
        return (f"{cls.total_animals} is the count")
    
    def __init__(self,name,species,age,diet,sound):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.sound = sound
        Animals.total_animals += 1

    def display_info(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"species : {self.species}")
        print(f"diet : {self.diet}")

class mammals(Animals):
    def __init__(self, name, species, age, diet,sound):
        super().__init__(name, species, age, diet, sound)
    
    def make_sound(self):
        print(f"{self.name} is {self.sound}")
        
    def display_info(self):
        super().display_info()
        self.make_sound()
    
class Birds(Animals):
    def __init__(self, name, species, age, diet, sound,wings):
        self.wings = wings
        super().__init__(name, species, age, diet, sound)

    def make_sound(self):
        print(f"{self.name} is {self.sound}")
        
    def wing_count (self):
        print(f"{self.wings} is there!!")
    
    def display_info(self):
        super().display_info()
        self.make_sound()
        self.wing_count()
    
a1 = mammals("leo","lion", 15 ,"carnivor","roar!!")
a2 = Birds("raj","parrot",2,"herbivores","speek",2)
print(a1.display_info())
print(a2.display_info())
Animals.Zoo_animals()


from abc import ABC,abstractmethod

class Engine(ABC):
    def __init__(self,engine_type,hp):
        self.engine_type = engine_type
        self.hp = hp

    @abstractmethod
    def display_info(self):
        pass

class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color

class Wheels:
    def __init__(self,wheel_type,wheel_size):
        self.wheel_type = wheel_type
        self.wheel_size = wheel_size

    def wheel_info(self):
        print(self.wheel_size,self.wheel_type)

class Electric_car(Wheels):
    def __init__(self, wheel_type, wheel_size,battery_cap):
        super().__init__(wheel_type, wheel_size)
        self.battery_cap = battery_cap

class hatchback(Engine,Wheels,Car):
    def __init__(self, engine_type, hp, wheel_type, wheel_size,model,color):
        Engine.__init__(self,engine_type, hp)
        Wheels.__init__(self,wheel_type,wheel_size)
        Car.__init__(self,model,color)

    def display_info(self):
        print(f"Engine_type : {self.engine_type}")
        print(f"Engine_HP : {self.hp}")        
        print(f"Wheel_type : {self.wheel_type}")        
        print(f"wheel_size : {self.wheel_size}")        
        print(f"Model : {self.model}")
        print(f"Color : {self.color}")

class Electric_sedan(Electric_car,Car):
    def __init__(self, wheel_type, wheel_size, battery_cap,model,color):
        super().__init__(wheel_type, wheel_size, battery_cap)
        Car.__init__(self,model,color)
    
    def display_info(self):       
        print(f"Model : {self.model}")
        print(f"Color : {self.color}")
        print(f"Wheel_type : {self.wheel_type}")        
        print(f"wheel_size : {self.wheel_size}")        
        print(f"Battery_capacity : {self.battery_cap}")

c1 = hatchback("v12",2000,"Alloy",20,"Swift","Red")
c2 = Electric_sedan("Alloy",18,50000,"Punch","Green")
c1.display_info()
print()
c2.display_info()
print()


# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# OOP Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle1:
    pass

# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# OOP Exercise 3: Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class car(Vehicle):
    def __init__(self,name,max_speed,mileage):
        Vehicle.__init__(self,name,max_speed,mileage)
    def display_info(self):
        return (f"name:{self.name},Speed:{self.max_speed},Mileage:{self.mileage},color:{Vehicle.color}")


c1 = car("school volvo",123,12)
print(c1.display_info())
print(c1.seating_capacity())



# Create a Bus child class that inherits from the Vehicle class. 
# The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.


# Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
# You need to override the fare() method of a Vehicle class in Bus class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)
    
    def fare(self):
        old_fare = super().fare()
        old_fare += old_fare*10 / 100
        return  old_fare

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print(type(School_bus))
School_bus.print1()
print(isinstance(School_bus,Bus))


lst = [1,2,3,4]
for i,l in enumerate(lst):
    print(i,l)
