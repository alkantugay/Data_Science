# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:05:28 2020

@author: alkanT
"""

#%%  variable (degisken)

var1 = 10   #integer
var2 = 20 

gun = "cumartesi"   #string

var3 = 10.0  #float  (double)
var4 = 10

#%%  string

s = "bugün günlerden cumartesi"

variable_type = type(s)  #str = string

print(s)

var5 = "Ankara"
var6 = "İst"
var7 = var5+var6

uzunluk = len(var5)  # var5 in uznluğunu söyler

#%%  numbers

#int 
integer_deneme = -50

#double = float ondalikli sayi
float_deneme = -8.8

#%% built in function

str1 = "deneme"
float1 = 10.6
##Console Ekranında deneyebileceğin fonksiyonlar
# float(10)  -> 10 u floata çevirir = 10.0
# int(float1)-> 10.6 yı int e çevirir = 10
#round(float1) -> sayıyı yuvarlar  10.6 = 11 olur

str2 = "1995"
#console ekranında int(str2) dersek eğer "1995" olan stringi 1995 int e çevirir

#%% User Defined Functions

var8 = 10
var9 = 100

output = (((var8+var9)*50)/100)*var8/var9


# fonksiyon tanımlama  // Fonk parametresi = input
def my_first_function(x,y):
    """
    Bu benım ilk fonksiyonum.  (Burayı fonksiyonun ne yaptığını başka bir insana açıklamak için kullanırız)
    
    parametre:
    
    return:
    """
    output = (((x+y)*50)/100)*x/y
    
    return output

sonuc = my_first_function(var8,var9)

def deneme1():
    print("ikinci deneme")

# %% Default and Flexible Functions

#default f: cemberin cevre uzunlugu = 2*pi*r

def cember_cevre_hesapla(r,pi = 3.14):   #Default olarak pi tanımladığım için fonksiyon içine artık pi=3.14 yazmama gerek yok
    """
    Cember Cevresi Hesaplama 
    input(Parametre): r    
    return = cemberin cevresi
    """
    output = 2*pi*r
    return output

result = cember_cevre_hesapla(var2)

#flexible

#Topluca commente almak için Ctrl+

#Benim boy ve kilo parametrelerim kesin olacak fakat, args olarak eklediğim parametre 
#değeri olabilir fakat olmayadabilir. hesapla(1,2) de yazarsak fonk çalışır, hesapla(1,2,8) yazarsam da çalışır
def hesapla(boy,kilo,*args):     
    print(args)
    output = (boy + kilo)*args[0]
    return output

#%%  QUIZ 1
    
# int variable yas
# string name isim
# fonksiyon olacak
# fonksiyon print(type(),len,floot)
# fonksiyonumuz fazladan parametre alabilsin (*args kullanımı yani) args soyisim gibi
# default parametre ayakkabi numarasi

yas = 25
name = "Tugay"
surname = "Alkan"

def func_quiz(yas,name,*args,ayakkabi_numarasi=45):   # default parametler en sona yazılır
    
    print("Cocugun ismi: ", name, " Yasi:",yas,"Ayak Numarasi: ", ayakkabi_numarasi)
    print(type(name))  #name in türünü yazdırdık
    print(float(yas))  #yas değerini floata cevirdik
    
    output = args[0]*yas   #args ın ilk elemanını yas ile carptık
    
    return output

sonuc = func_quiz(yas,name,surname) # fonksiyon inputuna args koyduğumuz için surname i ekleyebildik, ve default olduğu için de ayakkabi numarasını tekrar yazmadık.
print("args[0]*yas: ",sonuc)

#%%

#lambda Function ın amacı daha hızlı bir şekilde fonksiyon yazmaktır

def hesapla(x):
    return x*x

sonuc = hesapla(3)

sonuc2 = lambda x: x*x   # x yukarıda ki parametremize esdege
print(sonuc2(3))

#%% List

liste = [1,2,3,4,5,6]
type(liste)

liste_str = ["ptesi","sali","cars",""] 
type(liste_str)

value = liste[1]
print(value)

list_value = liste[-1]      #listedeki son elemanı alır

liste_divide = liste[0:3]   # 0 dan 3 e kadar elemanları al. = 0 dahil 3 dahil degil

"""
Console ekranında;

dir(liste)  # liste ile kullanabileceğimiz metodları verir

help(list.append) diyerek nasıl kullanıldığını görebiliriz

"""

liste.append(7)
liste.remove(7)
liste.reverse()
liste.insert(2,89)

liste2 = [1,5,4,3,6,7,2]
liste2.sort()

string_int_liste = [1,2,3,"aa","bb"]
string_int_liste.reverse()

#%%  Tuple

t = (1,2,3,3,4,5,6)
t.count(3)
t.index(5)

#%% Dictionary

#kendimize küçük bir database oluşturacaksak dictionary kullanabiliriz

dictionary = {"Ali":32, "Veli":45, "Ayse":13}
#type(dictionary["Ali"])   Alinin yasinin veri tipini söyler 

#Ali, Veli, Ayse = keys
#32, 45, 13 = values

def deneme():
    dictionary2 = {"Ali":32, "Veli":45, "Ayse":13}
    return dictionary2

dic = deneme()

#dic["Veli"] komutu ile Velinin yaşını öğrenebilirz.

#%% If Else Conditions

var10 = 10
var11 = 20

if(var10>var11):
    print("var10 buyuktur var11")
elif(var10 == var11):
    print("var10 esittie var11")
else:
    print("var10 kucuktur var 11")
    

liste = [1,2,3,4,5]

if 6 in liste:                                #6 degeri listenin icinde ise
    print("Evet 6 degeri listenin icinde")
else:
    print("Hayır icinde degil")
    

val = 3

if val in liste:
    print("Evet {} degeri listenin icinde".format(val))  # Tanimladigim val degerini cekmek icin bu sekilde kullanilir
else:
    print("hayir")
    
keys = dictionary.keys()

if "Can" in keys:
    print("Evet")
else:
    print("Hayir")
    
    
#%%  QUIZ2
    
#100. yıl kaçıncı yüzyıldır vs gibi yıllar girildikçe hangi yüzyılda olduğunu bize söyleyecek
    #1640.yıl == 17. yy
    #109. yıl == 2. yy

#metod yazın.
    #input integer yıllar
    #output integer yüzyıl(yy)
    
#input = year >>>     1 <= year <= 2005
    

def year2century(year):
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"):     #100,200,300...
            return int(str_year[0])
        else:                             #190,250,340...
            return int(str_year[0])+1
    else:                                 #1750, 1800, 1905
        if(str_year[2:4]=="00"):          #1500, 1800, 1700...
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1
        
year2century(1550)

#%%   LOOPS
#    for loops

for each in range(1,11):   #1 den 11 e kadar olan tüm sayıları print et. 1 dahil 11 değil
    print(each)

for each in "Ankara İst":
    print(each)
    
for each in "Ankara ist".split():   # Kelimeleri boşluklara göre ayır
    print(each)


liste_2 = [1,2,6,8,9,10]
summation = sum(liste_2)

count = 0

for each in liste_2:
    count = count + each
    print(count)
    

#   while loops
    
i = 0

while(i < 4):
    print(i)
    i = i+1
    
sinir = len(liste_2)
each = 0
count = 0

while(each < sinir):
    count = count + liste_2[each]   # listenin her bir elemanını seç
    each = each + 1

#%%  QUIZ 3
    
# verilen listenin içindeki en küçük sayıyı bul
    
liste_3 = [1,5,6,8,9,2,3,59,89,-50]

minValue = 100000
for each in liste_3:
    if(each < minValue ):
        minValue = each
    else:
        continue
    
print("Listedeki en küçük sayı = {}".format(minValue))