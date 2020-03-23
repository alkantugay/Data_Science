# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:52:23 2020

@author: alkan
"""

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  #♥ 1*15 vector oluşturduk

print(array.shape)  # kaça kaçlık bir matrisimiz olduğunu söyler

a = array.reshape(3,5)
print("shape: ",a.shape)
print("dimension: ",a.ndim)
print("data type: ",a.dtype.name)

print("size: ",a.size)

print("type: ",type(a))

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

zeros = np.zeros((3,4))  # bu boyutlarda 0 matrisi oluştururuz. Ki sonrasında güncelleme için kullanırız

zeros[0,0] = 5
print(zeros)

np.ones((3,4))  # aynı zeros gibi 1 lerden oluşan matris oluşturur

np.empty((3,4))

b = np.arange(10,50,5)   # 10dan 50 ye kadar 5 er artarak dizi oluşturur
print(b)

c = np.linspace(10,50,20)   # 10dan 50 ye kadar(bu kez 50 dahil) araya 20 tane sayı ekler
print(c)

#%% Numpy Basics Operations

x = np.array([1,2,3])
y = np.array([4,5,6])


print(x+y)
print(x-y)
print(x**2)

print(np.sin(x))

print(x<2)

z = np.array([[1,2,3],[4,5,6]])
t = np.array([[1,2,3],[4,5,6]])

print("Z: ",z.shape)
print("T: ",t.shape)
print(z*t)   # element wise product

#matrix product

print(z.T)  # Znin transpozu
print(z.dot(t.T))

print(np.exp(z))

v = np.random.random((5,5))  ## 5e 5 lik random matris oluşturur


print(z.sum())
print(z.max())
print(z.min())

print(z.sum(axis=0))
print(z.sum(axis=1)) 

print(np.sqrt(z))

#%%  indexing and slicing

import numpy as np

array = np.array([1,2,3,4,5,6,7])

print(array[0:4])  #0 dan 4. indekse kadar yazdırır 4 dahil değil

reverse_array = array[::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,1])

print(array1[:,1])  # Satırlardan hepsini al, sütunlardan sadece 1. sütunu al

print(array1[1,1:4])  # sadece 1. satırı al, 1. 2. ve 3. sutunu al

print(array1[-1,:])  #en son satırı al ve tüm sutunları al

#%%  Shape Manipulation

import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

#flatten

a = array.ravel()  ## Arrayi düz hale yani vektör haline getirir

array2 = a.reshape(3,3)

arrayT = array2.T  # array2 nin transpozunu aldık

print(arrayT.shape)

array5 = np.array([[1,2],[3,4],[4,5]])

#%%  Stacking arrays

import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[-1,-2],[-3,-4]])


# vertical
# array([[1, 2],
#        [3, 4]])
# array([[-1, -2],
#        [-3, -4]])

arr3 = np.vstack((arr1,arr2))

# horizontal
# array([[1, 2],[-1, -2],
#        [3, 4][-3, -4]])

arr4 = np.hstack((arr1,arr2))

print(arr3)
print(arr4)

#%% convert and copy

import numpy as np

liste = [1,2,3,4]   # list

array = np.array(liste)   # np.array


liste2 = list(array)

a = np.array([5,6,7])

b = a
b[0] = 10  # b[0] = 10 dersek sadece b nin değil a array inin de değişmiş olduğunu görürüz
c = a

"""  numpy array memeory de bir değer olarak değil alan olarak depolanıyor.
bu yüzden a b ya da c yi değiştirdiğimiz de hepsi değişiyor. Çözümü tabiki de var : """

d = a.copy()

f = d.copy()

