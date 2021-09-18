import pandas as pd
from matplotlib import pyplot as plt

def eliminar_datos(df):
    lista = []
    for i in range(len(df) - 1):
        pendiente = (df['DeltaP(Deg)'][i + 1] - df['DeltaP(Deg)'][i]) / (df['Time(s)'][i + 1] - df['Time(s)'][i])
        if pendiente < -0.01:
            lista.append(i + 1)

    for i in lista:
        df.drop(i, inplace=True)

    df.reset_index(inplace=True)
    return df
