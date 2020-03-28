# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:05:44 2020

@author: alkan
"""

from abc import ABC, abstractmethod

class Shape:
    """
    Shape = Super class ve Abstract class olacak
    """
    
    #abstract method
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    #overriding and polymorphism  
    def toString(): pass

class Square(Shape):
    
    def __init__(self, edge):
        self.__edge = edge  # encapsulation private attribute
        
    def area(self):
        result = self.__edge**2
        print("Square Area: ", result)
        
    def perimeter(self):
        result = self.__edge**4
        print("Square Perimeter: ", result)
        
    def toString(self):
        print("Square edge: ", self.__edge)
        

class Circle(Shape):
    
    #Constant Variable. Tamamen büyük harflerle yazılmış
    PI = 3.14
    
    def __init__(self, radius):
        self.__radius = radius  # encapsulation private attribute
        
    def area(self): 
        result = self.PI * self.__radius**2
        print("Circle area: ", result)

    def perimeter(self): 
        result = 2 * self.PI * self.__radius
        print("Circle Perimeter: ", result)
        
    def toString(self):
        print("Square edge: ", self.__radius)

c = Circle(5)
c.area()
c.perimeter()
c.toString()

s = Square(5)
s.area()
s.perimeter()
s.toString()