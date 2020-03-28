# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:55:57 2020

@author: alkan
"""

class Animal:   # super class
    
    def toString(self):
        print("Animal")
        
class Monkey(Animal):   # subclass
    
    def toString(self):
        print("Monkey")
        

a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString()   # monkey calls overriding method

