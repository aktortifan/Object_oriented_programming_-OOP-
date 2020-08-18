#Parent class/super class/base class
class Person:
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
florist = Person("Jane", "Flower")

print(florist.printname())



#Child class/sub class/derived class (without function)
class Lawyer(Person):

    """
    Please note that if you create a child class without an __init__() method
    it inherits all methods and attributes of the parent class.
    """
    pass

#instantiate the object
happy_lawyers = Lawyer("Jack", "Smiley")

#To access the function
print(happy_lawyers.printname())

#To access the attribute
print(happy_lawyers.firstname)



#Child class/sub class/derived class (with function)
class LawyerTwo(Person):
    
    def __init__(self, fname, lname, casetype):
        Person.__init__(self, fname, lname)
        self.casetype = casetype
        #self.firstname = fname
        #self.lastname = lname
        
    def printinfo(self):
        print("Hello my name is ", self.firstname, self.lastname)
        
#Instantiate the object
happy_lawyers = LawyerTwo("Jack", "Smiley", "Criminal")

#To activate the child-class-function
print(happy_lawyers.printinfo())

#To activate the parent-class-function
print(happy_lawyers.printname())

#To activate the additional attribute in the class "LawyerTwo"
print(happy_lawyers.casetype)
