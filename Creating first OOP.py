#A class with methods

class Instructors: #Class: a blueprint(template) for creating objects.
        
    companyName = "Bluelime"   #Attribute: variables that store the data
    
    """
    __init__() is a built-in function (initializer) in Python. 
    Used to initialize objects with initial values. Alll classes should have them. 
    It is called automatically when a new object is created from a class.
    
    
    (self) parameter is a reference to the current instance of the class.
    It is the first parameter of any method (function) in a class.
    It is used to access variables and methods belonging to the class.
    Also used to add attributes to a method.
    
    """

    def __init__(self, course, duration): #Method: a function defined inside a class.
        self.course = course
        self.duration = duration
        
    
    def printinfo(self):
        print("My company name is: ", Instructors.companyName)
        
#Instantiate process
python = Instructors("Python for beginner", 7)
django = Instructors("Django for beginner", 8)

#Accessing the method [ObjectName.Method]
print(python.printinfo())

#Accessing the atrribute
print(python.course)
print(python.duration)

#To change the value of attributes
python.course = "C++ for beginner"
print(python.course)

#To remove the attribute
del django.duration
print(django.course)
print(django.duration)