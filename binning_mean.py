import pandas as pd
import numpy as np
import openpyxl

d=pd.read_excel(r'C:\Users\STUDENT\Downloads\iris.xls')
print(d)
c=d['sepal length']
value=np.zeros(len(c))

for i in range(len(c)):
    value[i]=c[i]
value=np.sort(value)
print(value)
bin_size=int(input("Enter the bin size:"))
    

for j in range(int(len(c)/bin_size)):
    sum=0
    for k in range(j*bin_size,j*bin_size+bin_size):
        sum=sum+value[k]
    sum=sum/bin_size
    for k in range(j*bin_size,j*bin_size+bin_size):
        value[k]=sum
print(value)
dataset = pd.DataFrame({'Sepal length':value[:]})
print(dataset)
book = openpyxl.load_workbook(r'C:\Users\STUDENT\Desktop\iris.xlsx')
sheet = book.get_sheet_by_name('Iris')

for i in range(2,len(c)+2):    
    sheet.cell(row=i,column=1).value =value[i-2]
book.save(r'C:\Users\STUDENT\Desktop\iris.xlsx')
