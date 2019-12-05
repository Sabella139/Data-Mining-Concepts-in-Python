import pandas as pd
import numpy as np
import statistics as st


d=pd.read_excel(r'Iris.xls')
print(d)
c=d['sepal length']
value=np.zeros(len(c))
value_mean=np.zeros(len(c))
value_bdd=np.zeros(len(c))
value_med=np.zeros(len(c))

for i in range(len(c)):
    value[i]=c[i]

value=np.sort(value)
value_bdd=value.copy()
value_med=value.copy()
print(value)
bin_size=int(input("Enter the bin size:"))
value_m=np.zeros(bin_size)
index=0   
print("Smoothing by Mean:")

for j in range(int(len(c)/bin_size)):
    sum=0
    for k in range(j*bin_size,j*bin_size+bin_size):
        sum=sum+value[k]
    sum=sum/bin_size
    for k in range(j*bin_size,j*bin_size+bin_size):
        value_mean[k]=sum
print(value_mean)
n=0

print("Smoothing by Median:")
for j in range(int(len(c)/bin_size)):
    n=0    
    for k in range(j*bin_size,j*bin_size+bin_size):
        value_m[n]=value[k]
        n=n+1
    index=st.median(value_m)    
    for k in range(j*bin_size,j*bin_size+bin_size):
        value_med[k]=index
    
  
    
print(value_med)

print("Smoothing by Boundary:")
for j in range(int(len(c)/bin_size)):
    for k in range(j*bin_size,j*bin_size+bin_size):
        if(np.abs(value_bdd[k]-value_bdd[j*bin_size])<np.abs(value_bdd[k]-value_bdd[j*bin_size+bin_size-1])):
            value_bdd[k]=value_bdd[j*bin_size]
        else:
            value_bdd[k]=value_bdd[j*bin_size+bin_size-1]
    
    
print(value_bdd)

