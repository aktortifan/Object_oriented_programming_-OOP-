"""
ENCAPSULATION

-Process of restricting access to methods and variables to prevent direct data
 modification
-Public methods and variables are accessible from anywhere in program
-Private methods and variables are accessible from their own class
-Note: Double underscore prefic before object name makes it private

"""

class Cars:
     
    def __init__(self, speed, color, wheel):
         self.speed = speed
         self.color = color
         
         #double underscore prefix before variable or method names makes them private
         self.__wheel = wheel
         
    def set_speed(self, value):
         self.speed = value
         
    def get_speed(self):
         return self.speed
            
     
    def set_wheel(self, value2):
        self.__wheel = value2
        
    def get_wheel(self):
        return self.__wheel
     
#Instansiate        
ford = Cars(250, "green", 4)
nissan = Cars(300, "red", 4)
toyota = Cars(350, "blue", 4)

#Can be accessible although in different class
ford.set_speed(250)
ford.get_speed()

ford.speed = 500
print(ford.speed)

#Only accessible from their own class
ford.set_wheel(34)
ford.get_wheel()


ford.__wheel = 90
print(ford.__wheel)
