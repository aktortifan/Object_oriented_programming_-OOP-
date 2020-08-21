#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABSTRACTION

-Abstraction hides the internal details and shows only functionalties

-Example: 1.) In driving course, the instructor doesn't have to teach you how
              the engine works, he just focuses on how to drive a car
          2.) In electricity, we only know how to switch the light on/off, but
              not necessary know the internal wiring which makes that possible
              
-Abstract classes: - The classes that contain one or more abstract methods
                   - They cannot be instansiated (cannot create an object)
                   - They require sub-classes to provide implementation for the
                     abstract methods
                   - Sub-classes of an abstract class in Python are not required 
                     to implement abstract methods to the parent class
                     
-Abstract methods: - They are methods that are declared but contains no implementation
                   - Requires sub-classes to provide implementation for them
                   
-A B C => Abstract Base Classes

-Decorator: Allows you to add new functionality to an existing object (classes, methods, functions)
            without modifying its structures

"""

from abc import ABC, abstractmethod

#Parent class (as an abstract class)
class Shape(ABC):
    
    #decorator
    @abstractmethod
    def area(self):
        pass
    
    #decorator
    @abstractmethod
    def perimeter(self):
        pass
    
#Sub-class that inherited from parent class
class Square(Shape):
    
    def __init__(self, side):
        self.__side = side
        
    def area(self):
        return self.__side*self.__side
        
    def perimeter(self):
        return 4*self.__side

#Instantiation (you will get an error because you cannot instantiate the abstract class)
myShape = Shape()

#you will not get an error although this class is inherited from the parent class
mySquare = Square(5)

print(mySquare.area())
print(mySquare.perimeter())

