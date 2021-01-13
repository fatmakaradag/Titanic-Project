#imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------------------------------------

#load data

#Test verisetini pandas kütüphanesi ile tanımlıyoruz.
train_dataset = pd.read_csv(r'C:\Users\pesen\Desktop\new\train.csv')     #(r'C:\Users\Fatma\Downloads\titanic_data.csv')

#Eğitim verisetini pandas kütüphanesi ile tanımlıyoruz.
test_dataset = pd.read_csv(r'C:\Users\pesen\Desktop\new\test.csv')

#---------------------------------------------------------------------------------------
train_dataset.info()
test_dataset.info()

#----------------------------------------------------------------------------------------
#ilk olarak train_dataset içinden çıkarttık
cikarilacaklar = ['Name','Ticket','Cabin'] #datamızı incelediğimizde bazı sütünlerin bizim verimiz için gerekli olmadığını fark edip çıkartık.
train_dataset = train_dataset.drop(cikarilacaklar,axis=1)


#ikinci olarak test_dataset içinden çıkarttık.
cikarilacaklar = ['Name','Ticket','Cabin']
test_dataset = test_dataset.drop(cikarilacaklar,axis=1)

#------------------------------------------------------------------------------------------
