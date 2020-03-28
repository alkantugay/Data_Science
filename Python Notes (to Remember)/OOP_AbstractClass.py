# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:56:58 2020

@author: alkan
"""

""" 

Türetilen sınıflara yani child classlara implement etmek zorunda olduğumuz methodlara abstract method denir.


Abstract Class Şartları:
   1- Abstract classımdan obje yaratamam
   2- animal clasında kullandığım methodları child classta kullanmak zorundayım
   
Abstract class kullanmamızın sebebi de şablon oluşturmak. Yani türeteceğimiz tüm sınıflarda kullanacağımız methodları belirlemek
    
"""

from abc import ABC, abstractmethod

class Animal(ABC):  # super class
    
    @abstractmethod  #bunu kullandığım için animal classım artık abstract class haline geldi
    def walk(self): pass

       
    def run(self): pass


class Bird(Animal):
    
    def __init__(self):
        print("bird")
        
        
    def walk(self): 
        print("Walk")


    def run(self): 
        print("run")

b = Bird()
