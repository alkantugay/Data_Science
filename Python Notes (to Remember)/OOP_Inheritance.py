# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:32:56 2020

@author: alkan
"""

class Animal:
    
    def __init__(self):
        print("Animal is created")
        
    def toString(self):
        print("Animal")
    
    def walk(self):
        print("Animal walk")
        

class Monkey(Animal):    # Animal classından türettiğimizi gösterir.
    
    def __init__(self):
        super().__init__()            # Animal classının init methodunu kullanmamızı sağlar
        print("Monkey is created")
        
    def toString(self):
        print("monkey")
    
    def climb(self):
        print("Monkey can climb")
        
 
class Bird(Animal):
    
    def __init__(self):
        super().__init__()
        print("Bird is created")
    
    def fly(self):
        print("fly")

       
m1 = Monkey()    # hem animal is created hem de monkey is created yazdırır

m1.toString()
m1.walk()
m1.climb()

print("-----------")

b1 = Bird()
b1.walk()
b1.toString()
b1.fly()