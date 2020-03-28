# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:46:50 2020

@author: alkan
"""


class Website:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name + " " + self.surname)
        
        
class Website1(Website):
    
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)   #super() metodu ile aynı işlevi görür
        self.ids = ids
         
         
    def login(self):
        print(self.name + " " + self.surname+ " " + self.ids)
        
     

class Website2(Website):
    
    def __init__(self,name,surname,email):
        Website.__init__(self, name, surname)s
        self.email = email
        
    def login(self):
        print(self.name + " " + self.surname+ " " + self.email)

p1 = Website("name", "surname")

p2 = Website1("name","surname","123")

p3 = Website2("Tugay","Alkan", "alkantugay@gmail.com")