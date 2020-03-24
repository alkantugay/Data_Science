# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:23:00 2020

@author: alkan
"""

# matplotlib kutuphanesi
#Görselleştirme kütüphanesi
#lineplot, scatter plot, bar plot, sub plots, hhistogram

import pandas as pd

## CSV dosyamız ile py dosyamız aynı klasörde olmalı. Eğer değilse, dosyanın pathini yazmamız gerek ;
## mesela masaüstündeyse "C:\Users\alkan\Desktop\iris.csv" şeklinde. Önerim aynı klasörde saklamanız.

df = pd.read_csv("iris.csv")
#iris dataset bir çiçek türü. o türe ait veri setini barındırıyor iris.csv

print(df.columns)

print(df.Species.unique())    #türlerin içinde kaç tane tür varsa onu yazdırır. (yani kaç farklı tür varsa)  (aynı türü iki kez yazmaz)

print(df.info())

print(df.describe)

setosa = df[df.Species == "Iris-setosa"]   # eğer setosa = df.Species=="Iris-setosa"  dersek bize sadece true-false lardan oluşan tabloyu gösteriyor
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())      #2 türü kıyaslayabiliriz bu şekilde
print(versicolor.describe())

#%%  Line Plot

import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis=1)

# df1.plot()  veriyi çizdirmek için kullanırız
# plt.show()

setosa = df[df.Species == "Iris-setosa"]   # eğer setosa = df.Species=="Iris-setosa"  dersek bize sadece true-false lardan oluşan tabloyu gösteriyor
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")  # çizdirme işleminde kullandığımız değişkenler
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = "virginica")


plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()  #default değeri en uygun yere yerleştir. Yani neyi çizdirdiğimizi söyler bize
plt.show()

df1.plot(grid = True)  # grafiği gridlere böler
#plt.show()

df1.plot(grid = True, linestyle = ':')  # lineları noktalar haline dönüştürür
#plt.show()

df1.plot(grid=True, alpha=0.1)   #lineları saydamlaştırır
#plt.show()

#%% Scatter Plot

setosa = df[df.Species == "Iris-setosa"]   # eğer setosa = df.Species=="Iris-setosa"  dersek bize sadece true-false lardan oluşan tabloyu gösteriyor
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color ="red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color ="blue", label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color ="green", label = "virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

#%% Histogram

plt.hist(setosa.PetalLengthCm, bins = 10)   # bin barların sayısını ifade eder
plt.xlabel("PetalLEngthCm Values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

#%% Bar Plot

import numpy as np

# x = np.array([1,2,3,4,5,6,7])

# y  = x*2 + 5

# plt.bar(x,y)
# plt.title("Bar plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

x = np.array([1,2,3,4,5,6,7])
a = ["turkey", "usa", "a", "b", "c", "d","w"]

y  = x*2 + 5  # burayı gelir dağılımı gibi düşünelim

plt.bar(a,y)
plt.title("Bar plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#%% Subplots

df1.plot(grid=True, alpha=0.9, subplots = True) 
plt.show()

setosa = df[df.Species == "Iris-setosa"]   # eğer setosa = df.Species=="Iris-setosa"  dersek bize sadece true-false lardan oluşan tabloyu gösteriyor
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)   # 2 grafikten oluşur ve 1. column 1. satırı ifade eder
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")  # çizdirme işleminde kullandığımız değişkenler
plt.ylabel("setosa.PetalLengthCm")

plt.subplot(2,1,2)   #2 grafikten oluşur ve 1. column 2. satırı ifade eder
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.ylabel("versicolor.PetalLengthCm")

plt.show()

#%% QUIZ NOTLAR

import numpy as np

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[-1,:])   #

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(array.reshape(3,3)) 

a = np.array([1,2,3])

print(a.sum()) 

print(a.max()) 

print(a.min()) 

print(np.linspace(10,15,5)) 

import pandas as pd


dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

ortalama_maas = dataFrame1.MAAS.mean()

s = np.sum([True if ortalama_maas > each else False for each in dataFrame1.MAAS])

print(s)
print(dataFrame1.describe())
c = dataFrame1.iloc[:,2]
