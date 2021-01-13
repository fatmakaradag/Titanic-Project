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

#Sütunları kontrol ediyoruz.
print(train_dataset.columns )

#---------------------------------------------------------------------------------------

#İki veri setindeki toplam yolcu sayısı
print(train_dataset.shape[0] + test_dataset.shape[0])

#---------------------------------------------------------------------------------------

#Hayatta kalma oranı
train_dataset['Survived'].mean()

#---------------------------------------------------------------------------------------





