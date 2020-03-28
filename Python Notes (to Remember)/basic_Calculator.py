# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:58:01 2020

@author: alkan
"""


#%% Calculator Project

class Calc:
    
    #init metodu
    def __init__(self,a,b):
        "initialize values"
        #attribute
        self.value1 = a
        self.value2 = b
    
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2

 
    def multiply(self):
        "multiplication  a*b = result  -> return result"
        return self.value1 * self.value2
    
    def division(self):
        """"multiplication  a*b = result  -> return result"""
        return self.value1 / self.value2
    
    def substraction(self):
        """substraction a-b = result  ->  return result """
        return self.value1 - self.value2
    

print("Choose add(1), multiply(2), division(3), substraction(4)")
selection = input("Selection: ")    # klavyeden değer girebilmemiz için gerekli olan fonksiyon
 
v1 = int(input("first value: "))    # klavyeden girilen değer string olduğu için onu integer a çeviriyoruz
v2 = int(input("second value: "))

c1 = Calc(v1,v2)
        
if selection == "1":
    add_result = c1.add()
    print("Add: {},".format(add_result))
    
elif selection == "2":
    multiply_result = c1.multiply()
    print("Multiply: {}".format(multiply_result))

elif selection == "3":
    division_result = float(c1.division())
    print("Division: {}".format(division_result))
    
elif selection == "4":
    substraction_result = c1.substraction()
    print("Substraction: {}".format(substraction_result))

else:
    print("Yanlış Seçim Yaptınız Lütfen Yeniden Deneyin")
    
    
