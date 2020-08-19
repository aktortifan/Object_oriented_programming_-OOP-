'''
Polymrphism:
    
    -The ability to take or have various forms
    -Ex: The functionality of smarphone: Phone, Messaging, Camera, Mp3 player
    -Ex: Word "watch" can be "Verb" or "Noun"
    
    -Polymorphism allows us to define methods in child class with some name as 
     methods in parent class, but doing different things.
    -Ex: print(len("hello")) -> len() function can be used in String data type
    -Ex: print(len([20, 40, 80])) -> len() function can be used in List data type
    
'''
    
def addNumbers(a, b, c = 1):
    return a + b + c

#What I am doing here is passing arguments for the function parameters.
print(addNumbers(8, 9))

print(addNumbers(8, 9, 4))

#Polymorphic class with methods

class UK():
    
    def capital_city(self):
        print("London is the capital city of UK")
        
    def language(self):
        print("English is the primary language of UK")
        

class Spain():
    
    def capital_city(self):
        print("Madrid is the capital city of Spain")
        
    def language(self):
        print("Spanish is the primary language of Spain")
        
        
#Instansiate
        
"""
We use the same method name, but they will act in different way
"""
        
queen = UK()
queen.capital_city()

zara = Spain()
zara.capital_city()

#Calling the function with iteration
for country in (queen, zara):
    
    country.capital_city()
    country.language()
    
    
#Create polymorphism by using existing method on a new function
    
def europe(eu):
    
    eu.capital_city()
    eu.language()
      
#Calling the function with different instances
europe(queen)
europe(zara)