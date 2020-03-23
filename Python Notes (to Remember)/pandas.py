# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:10:01 2020

@author: alkan
"""

"""
1 - Pandas hızlı ve etkili (dataframe için)  Dataframe nedir ? örnek:
    isim  yas   medeniHal
    Tugay 25     Bekar          Bu yapılara dataframe nedir. Datayı içinde depoladığımız excel dosyaları gibi yapılar.
    
2- CSV ve text dosyalarını açıp inceleyip sonuçlarımızı da bu dosya tiplerine rahat bir şekilde kaydedebiliriz

3- Dosyamızda bazı değerler boş olabilir. NaN value, yani missing data dediğimiz şey. fakat bizim buna rağmen bu dosyaları handle etmemiz gerek
Pandas burada işimizi kolaylaştırıyor (Missing data için)

4- reshape yapıp datayı daha etkili bir şekilde kullanabiliriz.

5- slicing ve indexing daha kolay

6- time series data analizinde çok yardımcı olur (zamanla gelen data analizi)

7 - herşeyden önemlisi hız açısından optimize edilmiş hızlı bir kütüphanedir
"""
import pandas as pd

dictionary = {"NAME":["Ali","Veli","Kenan","Hilal","Ayse","Evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS":[100,150,240,350,500,800]}

dataFrame1 = pd.DataFrame(dictionary)  #dataframe oluşturma

head = dataFrame1.head()   # data frame içindeki baştan 5 satırı bize ver demek   eğerhead(x) içine bir xsayı değeri girersek x kadar satırı bize gösterir
tail = dataFrame1.tail()  #dataframe içindeki sonran 5 i gösterir

#%% Pandas Basic Methods

print(dataFrame1.columns)   # Bize sütunları gösterir
 
print(dataFrame1.info())   #dataframe ile ilgili tüm bilgileri yazar

print(dataFrame1.dtypes)   #Sütunlardaki verilerin hangi tür olduğunu yazar

print(dataFrame1.describe())   # describe sadece nümerik(sayısal) değerleri alır.  numeric feature = columns(age,maas)
                               #nümerik değerlere sahip olan sütunların ortalama, min max, standart sapma vb gibi değerleri bize gösterir.

#%%  Indexing and Slicing

print(dataFrame1["AGE"])   # iki şekilde de kullanılabiliyor
print(dataFrame1.AGE)

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]
print(dataFrame1.yeni_feature)


print(dataFrame1.loc[:,"AGE"])    #tüm satırları ve istediğim sütunu aldım
print(dataFrame1.loc[:3,"AGE"])  #3. index dahiil olmak üzere baştan 3. satıra kadar yazdırır.


print(dataFrame1.loc[:3,"NAME":"AGE"])

print(dataFrame1.loc[::-1,:"MAAS"])     #1. : nokta tüm satırlar,  2. : Name e akdar olan sütunları yazdır

print(dataFrame1.iloc[:,1])   #iloc olursa isim yerine indeksini yazmam gerekir

#%%  Filtering

filtre1 = dataFrame1.MAAS>200                # Maaşı 200 liranın üzerinde olan insanları bul. Burada bize true ve false olarak bir seri döndürür
filtrelenmis_data = dataFrame1[filtre1]       # filtrelenmiş veriyi dataframe in içine koyarak maası 200 ün üzerinde olan kişilerin tüm bilgilerini getirir

filtre2 = dataFrame1.AGE<20 

dataFrame1[filtre1 & filtre2]   #yaşı 20den küçük olup maaşı 200den fazla olanları listeler

print(dataFrame1[dataFrame1.AGE>60])


#%% List Comprehension

import numpy as np

ortalama_maas = dataFrame1.MAAS.mean()      #pandankütüphanesi ile kullanımı

# ortalama_maas_np = np.mean(dataFrame1.MAAS) #numpy kutuphanesi ile kullanımı

dataFrame1["maas_seviyesi"] = ["Yuksek" if ortalama_maas < each else "Dusuk" for each in dataFrame1.MAAS]  # data frame içine maas_seviyesi diye bir sütun açtık ve
                                                                                                           #her bir maaşla ortalamayı kıyaslayarak yuksek ya da dusuk yazdırdık
# for each in dataFrame1.MAAS:
#     if(ortalama_maas>each):
#         print("Yuksek")
#     else:
#         print("Dusuk")

dataFrame1.columns = [each.lower() for each in dataFrame1.columns]   ##columnları sıra sıra dolaş, ve harfleri küçült


##Arasında boşluk olan sütun adı varsa eğer aradaki boşluğu silip araya "_" ekler
dataFrame1.columns = [each.split()[0]+ "_"+ each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]

#%% drop and concatenating

dataFrame1.drop(["yeni_feature"],axis = 1)  ## sütun drop etmek için axis=1 (yukarıdan aşağıya drop et),  axis=0 dersek sütun drop et(soldan sağa drop et)

# dataFrame1.drop(["yeni_feature"],axis = 1, inplace=True) # Yukarı satırdaki kod drop eder fakat dataframe1 i güncellemez, bu şekilde dataframeimizi de güncelleriz


data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical birleştirme
data_concat = pd.concat([data1,data2],axis=0)

#horizontal birleştirme

maas = dataFrame1.maas 
age = dataFrame1.age

data_h_concat = pd.concat([maas,age],axis=1)

#%% transforming data

dataFrame1["list_comp"] = [each*2 for each in dataFrame1.age]   # list_comp sütunu oluşturduk ve yaşları 2 ile çarpıp bu sütuna ekledik


#apply func

def multiply(age):
    return age*2

dataFrame1["applyMetodu"] = dataFrame1.age.apply(multiply)   # yukarıda yaptığımız işlemin aynısını apply fonksiyonu ile yaptık