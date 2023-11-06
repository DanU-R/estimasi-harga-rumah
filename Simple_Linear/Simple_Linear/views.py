from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def home(request):
    return render(request, 'home.html')

def predik(request):
    return render(request, 'prediksi.html')

def hasil(request):
    df = pd.read_csv("DATA RUMAH.csv")
    df = df.dropna()
    df = df.dropna(axis=1)
    df = df.drop(columns=['LT'])
    df = df.drop(columns=['NO'])
    df = df.drop(columns=['NAMA RUMAH'])
    # x = df.drop('Price', axis=1)
    # y = df['Price']
    x = df.drop('HARGA', axis=1)
    y = df['HARGA']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)
    
    reg = LinearRegression()
    reg.fit(x_train, y_train)

    var1 = float(request.GET['LB'])
    # var2 = float(request.GET['LT'])
    var3 = float(request.GET['KT'])
    var4 = float(request.GET['KM'])
    var5 = float(request.GET['GRS'])
    
    pred = reg.predict(np.array([var1, var3, var4, var5]).reshape(1,-1))

    pred = round(pred[0])

    harga = "Hasil Estimasi dalam IDR Rp"+'{:,.0f}'.format(pred)

    return render(request, 'prediksi.html', {'harga2':harga})