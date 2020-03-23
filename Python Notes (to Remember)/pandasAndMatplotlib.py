# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:23:00 2020

@author: alkan
"""

# matplotlin kutuphanesi
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