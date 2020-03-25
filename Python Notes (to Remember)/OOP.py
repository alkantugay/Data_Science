# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:21:12 2020

@author: alkan
"""

"""
Self, class içerisindeki değişkenlere, metodlara erişmemizi sağlayan parametredir

"""

#%% Classes

employee1_name = "messi"
employee1_age = 33
employee1_address="aaaaa"


#class Employee(object)
#class ın içerisine yazdığımız obje bundan nesne oluşturucağımızı göstermiş olur. Ama yazmamıza da gerek yok. Python bunu otomatik kabul ediyor.
#

class Employee:    # eğer alta pass yazmazsak  Employee(object) yazdığımızda hata verir. (daha sonra içeriği doldurucam demek)
    # atttribute = age,adress,name
    #behaviour = pass,shot
   pass
    #classın içerisinde olmak istiyorsam bir tab boşluk bırakmam gerek      

employee1 = Employee()

#%%  attribute

#Normalde class iiçnde bu şekilde tanımlamalar olmaz. Burada sadece mantığı göstermek  amaç

class Footballer:
    
    football_club = "Barcelona"   
    age = 30
    
f1 = Footballer()

print(f1)
print(f1.age)
print(f1.football_club)

f1.football_club = "Real Madrid"
print(f1.football_club)

#%%  Method

class Square(object):
    
    edge = 5
    area = 0
    def area(self):   #♦ eğer self demezsek, classın içindeki değişkene erişemeyiz
        self.area = self.edge * self.edge
        print("Area: ",self.area)
    
s1 = Square()

print(s1)
print(s1.edge)

s1.edge = 7
s1.area()

#%% Methods vs Functions 

class Emp(object):
    
    age = 25
    salary = 1000  # $
    
    def ageSalaryRatio(self):       # method
        print(self.age / self.salary)

#methodum self diye bir parametreye sahip, bu da aslında benim classımın objesini ifade ediyor.
#MEthodum class çinde yazılması gereken class depended bir modul fonksiyon ise class dışında yazılır
     
e1 = Emp()
e1.ageSalaryRatio()

###############
def ageSalaryRatio(age,salary):    # function, classla hiçbir alakası yok istediğimiz şekilde fonksiyon yazabiliriz
    print(age/salary)
    
ageSalaryRatio(30, 1000)


def findArea(a,b):  #a = pi,  b = r
    area = a*b*b
    return area
    
pi = 3.14
r = 5
    
result1 = findArea(pi, r)
result2 = findArea(pi, 10)

print(result1 + result2)


#%%  Initializer or contructor

class Animal(object):
    
  
    def __init__(self, a, b):  # (name, age) = ("dog", 2) = (a,b)   #initializer metod.  Yani classın temeline attributelarını tanımlayacak method
        self.name = a  #self.name, içerideki namedir.
        self.age = b
        
    
    def getAge(self):
        return self.age
    
    def getName(self):
        print(self.name)
    
    
a1 = Animal("dog", 2)
a2 = Animal("cat", 3)
a3 = Animal("bird", 4)
