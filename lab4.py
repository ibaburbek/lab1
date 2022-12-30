class Person:
    def __init__(self):
        self.fullname: str
        self.age: int
    
    def __str__(self):
        print(f'person full name: {self.fullname} and age is {self.age}')

        
class Driver(Person):
    def __init__(self):
        Person.__init__(self)
        self.experience: int
    
    def __str__(self):
        print(f'driver experience: {self.experience}')
            
class Engine:
    def __init__(self):
        self.power:int
        self.company:str
    def __str__(self):
        print(f'Engine power: {self.power} and was produced by {self.company}')
    

        
        
class Car:
    def __init__(self):
        self.brand: str
        self.category: str
        self.driver: Driver()
        self.motor: Engine()
    def __str__(self):
        print(f'automobile is {self.brand}, engine is {self.motor}.\n
                Driver is {self.driver.fullname} with experience {self.driver.experience}')
            
    def start(self):
        print('go')
    
    def stop(self):
        print('stop')
        
    def turnRight(self):
        print('turn right')
        
    def turnLeft(self):
        print('turn left')
        
   
    
    
    
class Lorry(Car):
    def __init__(self):
        Car.__init__(self)
        self.carrying:int
        
        
class Sportcar(Car):
    def __init__(self):
        Car.__init__(self)
        self.speed:int
        
        