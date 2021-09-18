import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

def calculo_pendiente(df,ax):
    regresion_lineal1=LinearRegression()
    regresion_lineal1.fit(df.loc[700:2400,'Time(s)'].array.reshape(-1,1),df.loc[700:2400,'DeltaP(Deg)'])
    print(' DAtos : n = ' + str(regresion_lineal1.coef_) + ', m = ' + str(regresion_lineal1.intercept_))
    ax.plot(df.loc[700:2400,'Time(s)'],df.loc[700:2400,'DeltaP(Deg)'],color='green',label='Taza de evaporacion : '+str(round(regresion_lineal1.coef_[0],6)) + ' Deg/s')
    ax.legend()


