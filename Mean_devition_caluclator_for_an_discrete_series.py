#program to find mean devation of discrete data series
import numpy as np
# x input
a = []
n = int(input("enter total number of observation in the given data:"))
for i in range(0,n):
    ele = int(input())
    a.append(ele)
print(f"you have enter the the x as {a}")
#frequency input
b = []
n = int(input("enter total number of observation of frequency in the given data:"))
for i in range(0,n):
    ele = int(input())
    b.append(ele)
print(f"you have enter the frequency fi as {b}")
c = []
for n1,n2 in zip(a,b):
    c.append(n1*n2)
fx = c
X = sum(fx)/sum(b)  #X
array1 = np.array(a)
array2 = np.array(X)
D = np.subtract(array1,array2)  # |X-xi|
e = abs(D) #Dx
d = []
for n3,n4 in zip(b,e):
    d.append(n3*n4)
dfx = d
MD = sum(dfx)/sum(b) #mean divation
print(f"the Σfi {sum(b)}")
print(f"the fixi is {fx}")
print(f"the Σxifi is {sum(fx)}")
print(f"the x' is {X}")
print(f"the |xi-x| is {e}")
print(f"the dxfi is {dfx}")
print(f"the Σdfx is {sum(dfx)}")
print(f"the mean devation of the array is,{MD}") 



