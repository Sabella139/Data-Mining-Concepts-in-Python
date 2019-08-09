# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
d=pd.read_excel(r'C:\Users\STUDENT\Downloads\iris.xls')
print(d)
c=d['sepal length']
value=np.zeros(len(c))

for i in range(len(c)):
    value[i]=c[i]
value=np.sort(value)
print(value)
v=np.zeros(150)
minimum=min(value)
maximum=max(value)
new_max=int(input("Enter the new max"))
new_min=int(input("Enter the new min"))
for i in range(150):
    v[i]=(value[i]-minimum)/(maximum-minimum)*(new_max-new_min)+new_min
print(v)
    
mean_value=np.mean(value)
stddev=np.std(value)

for i in range(150):
    v[i]=(value[i]-mean_value)/stddev
print(v)
import matplotlib.pyplot as p

p.hist(v,150)
p.show()



    
    
            


       
        
    


