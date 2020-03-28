# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:27:39 2020

@author: alkan
"""


class BankAccount:
    
    def __init__(self, name, money, address):
    
        self.name = name         #global
        self.__money = money    ##iki alttan çizgi eklediğimde money değişkenini artık private yaptım
        self.address = address
        
    ### Encapsulatıon, variablelara dışarıdan erişimin yasaklanmasını sağlar
    
    # get ve set metodları
    
    def getMoney(self):   #objemin içerisinde bulunan money variable ını almamı sağlar
        return self.__money
    
    def setMoney(self, amount):    # moneyimi set etmek sitiyorum. Para çekmek, para yatırmak vs
        self.__money = amount
        
    def __increase(self):
        self.__money = self.__money + 500
        
p1 = BankAccount("messi", 1000, "Barcelona")
p2 = BankAccount("Neymar", 2000, "Paris")        

print("get method: ",p1.getMoney())

p1.setMoney(5000)
print("after set method: ",p1.getMoney())


p1.increase()
print("after raise: ",p1.getMoney())

