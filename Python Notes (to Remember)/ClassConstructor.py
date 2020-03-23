# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:04:02 2020

@author: alkan
"""

class Calisan:
    
    zamOrani = 1.8
    counter = 0
    
    def __init__(self,isim,soyisim,maas):  # Constructor
    #Self dışardan gelen ismi, calısan classımız içinde kullanmamızı sağlar
    
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = soyisim+isim+"@gmail.com"
        
        Calisan.counter = Calisan.counter + 1
        
    def giveNameSurname(self):            #eğer buaraya self yazmazsak hata alırız ve contructordaki değerlere erişemeyiz
        return self.isim +" "+ self.soyisim
     
    def zamYap(self):
        self.maas = self.maas + self.maas*self.zamOrani
        
        
# isci1 = Calisan("Tugay", "Alkan",5000)   # Classımızdan obje yarattık 
# print(isci1.giveNameSurname())
# print(isci1.maas)
# print(isci1.email)

#Class Variable

calisan1 = Calisan("Sultan", "Kalkanoğlu",5000)
print("ilk maas: ",calisan1.maas)
calisan1.zamYap()
print("yeni maas: ",calisan1.maas)

calisan2 = Calisan("A","B",2000)

#Calisan.counter dersek eğer clasımızdan kaç tane obje yaratıldığını görebiliriz

calisan3 = Calisan("AAAA","SADAD",1000)
calisan4 = Calisan("C","D",50)
calisan5 = Calisan("E","F",18000)
 
liste = [calisan1,calisan2,calisan3,calisan4,calisan5]
 
maxMaas = -1
index = -1

for each in liste:
    if(each.maas>maxMaas):
        maxMaas=each.maas
        index = each        #en yüksek maaş alanın indeksini tutuyoruz

print(maxMaas)
print(index.giveNameSurname())  # burada da en yüksek maaş alanın adını soyadını yazdırıyoruz
