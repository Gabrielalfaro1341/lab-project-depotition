import pandas as pd
from matplotlib import pyplot as plt
from eliminar_datos_erroneos import eliminar_datos
from sumar import suma
import statsmodels.api as sm
from calculo_pendiente import calculo_pendiente


directorio=input()
nombre = directorio.split('/')
path=[n+'/' for n in nombre[:-1]]
direccion=''

for i in path:
    direccion+=i
df=pd.read_csv(directorio,delimiter=',')
fig, (ax,ax2)=plt.subplots(2,1)
df=eliminar_datos(df)
df=suma(df)
ax.plot(df['Time(s)'],df['DeltaP(Deg)'],alpha=1)
ax.set_ylabel('Delta P°')
ax2.set_xlabel('Tiempo (s)')
ax.set_title('Crecimiento de pelicula para '+nombre[-1].replace('.txt',''))
calculo_pendiente(df,ax)
ax2.plot(df['Time(s)'],df['StraylightVoltage(V)']*1000,alpha=0.5)
fig.subplots_adjust(hspace=0)
ax2.set_ylabel('StraylightVoltage(mV)')
ax2.xaxis.grid()
ax.xaxis.grid()

# suavizado straylight
lowes1 = sm.nonparametric.lowess(df.loc[:, 'StraylightVoltage(V)']*1000,
                                     df.loc[:, 'Time(s)'], frac=0.1)

ax2.plot(lowes1[:, 0], lowes1[:, 1], color='blue')




plt.savefig(direccion+nombre[-1].replace('.txt', '.png'),dpi=300)
plt.show()
