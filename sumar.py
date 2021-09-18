import pandas as pd
from matplotlib import pyplot as plt

def suma(df):
    lista_suma = list()
    indice = list()
    diferencia = 0
    for i in range(len(df) - 1):
        pendiente = (df['DeltaP(Deg)'][i + 1] - df['DeltaP(Deg)'][i]) / (df['Time(s)'][i + 1] - df['Time(s)'][i])
        if pendiente < -0.01:
            indice.append(i + 1)
            diferencia = -(df['DeltaP(Deg)'][i + 1] - df['DeltaP(Deg)'][i])
            lista_suma.append(diferencia)
    print(lista_suma)
    for i in range(len(lista_suma)):
        df.loc[indice[i]:,'DeltaP(Deg)'] = df[indice[i]:]['DeltaP(Deg)'] + lista_suma[i]
        df.loc[indice[i]:,'Time(s)']=df[indice[i]:]['Time(s)']-(df['Time(s)'][indice[i]]-df['Time(s)'][indice[i]-1])
        print(df.iloc[indice[i]]['Time(s)'],df.iloc[indice[i]-1]['Time(s)'])
    return df