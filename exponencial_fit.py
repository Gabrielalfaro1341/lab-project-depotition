import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import math
def func(x,a,b):
    return (math.e/2.6)**(a*(x-b))


def fiteo(df,ax,func):
    popt, pcov = curve_fit(func,df['Time(s)'],df['DeltaP(Deg)'],maxfev=10000)
    print(popt)
    yy = func(df['Time(s)'], *popt)
    residuals = df['DeltaP(Deg)']-func(df['Time(s)'], popt[0],popt[1])
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((df['DeltaP(Deg)'] - np.mean(df['DeltaP(Deg)'])) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    print(r_squared)
    ax.plot(df['Time(s)'],yy,color='red',label='fit exponencial: , a=%5.3f, b=%5.3f' % tuple(popt),linestyle='--')
    ax.legend()


