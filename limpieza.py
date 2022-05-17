import numpy as np
import pandas as pd


#Base de datos agua caida diaria (de 00:00 a 00:00)

df = pd.read_csv('csv\\agua6_dmc.csv')

fecha = df['time'].str.split(expand=True)
fecha.columns = ['fecha', 'hora']
df = pd.concat([df, fecha], axis=1)

df = df.drop(columns=['time','latitud','longitud','Traza_Valor','CodigoNacional'])

df = df[df['fecha'] > '2009-12-31']

df['mmtotal']= df.groupby(['nombreEstacion','fecha'])['RRR6_Valor'].transform("sum")

df = df.drop(columns=['RRR6_Valor','hora'])
df = df.drop_duplicates()
df = df.dropna()
df.to_csv('csvlimpios\\agua_caida_diaria.csv',index=False)

#Base de datos rocio

df = pd.read_csv('csv\\rocio_dmc.csv')

fecha = df['time'].str.split(expand=True)
fecha.columns = ['fecha', 'hora']
df = pd.concat([df, fecha], axis=1)

df = df.drop(columns=['time','latitud','longitud','CodigoNacional'])

df = df[df['fecha'] > '2009-12-31']

df['temp_rocio_min'] = df.groupby(['nombreEstacion','fecha'])['Td_Valor'].transform("min")
df['temp_rocio_max'] = df.groupby(['nombreEstacion','fecha'])['Td_Valor'].transform("max")
df['temp_rocio_prom'] = df.groupby(['nombreEstacion','fecha'])['Td_Valor'].transform("mean")

df = df.drop(columns=['Td_Valor','hora'])
df = df.drop_duplicates()
df = df.dropna()
df.to_csv('csvlimpios\\rocio.csv',index=False)

#Base de datos viento

df = pd.read_csv('csv\\viento_dmc.csv')

fecha = df['time'].str.split(expand=True)
fecha.columns = ['fecha', 'hora']
df = pd.concat([df, fecha], axis=1)

df = df.drop(columns=['time','latitud','longitud','CodigoNacional','VRB_Valor'])

df = df[df['fecha'] > '2009-12-31']

df['vel_min'] = df.groupby(['nombreEstacion','fecha'])['ff_Valor'].transform("min")
df['vel_max'] = df.groupby(['nombreEstacion','fecha'])['ff_Valor'].transform("max")
df['vel_prom'] = df.groupby(['nombreEstacion','fecha'])['ff_Valor'].transform("mean")

df = df.drop(columns=['ff_Valor','hora'])
df = df.drop_duplicates()
df = df.dropna()
df.to_csv('csvlimpios\\viento.csv',index=False)

#Base de datos humedad

df = pd.read_csv('csv\\humedad_dmc.csv')

fecha = df['time'].str.split(expand=True)
fecha.columns = ['fecha', 'hora']
df = pd.concat([df, fecha], axis=1)

df = df.drop(columns=['time','latitud','longitud','CodigoNacional'])

df = df[(df['fecha'] > '2009-12-31') & (df['fecha'] < '2020-01-01')]

df['hum_min'] = df.groupby(['nombreEstacion','fecha'])['HR_Valor'].transform("min")
df['hum_max'] = df.groupby(['nombreEstacion','fecha'])['HR_Valor'].transform("max")
df['hum_prom'] = df.groupby(['nombreEstacion','fecha'])['HR_Valor'].transform("mean")

df = df.drop(columns=['HR_Valor','hora'])
df = df.drop_duplicates()
df = df.dropna()
df.to_csv('csvlimpios\\humedad.csv',index=False)

#Base de datos presion atmosferica

df = pd.read_csv('csv\\presionqff_dmc.csv')

fecha = df['time'].str.split(expand=True)
fecha.columns = ['fecha', 'hora']
df = pd.concat([df, fecha], axis=1)

df = df.drop(columns=['time','latitud','longitud','CodigoNacional'])

df = df[(df['fecha'] > '2009-12-31') & (df['fecha'] < '2020-01-01')]

df['pres_min'] = df.groupby(['nombreEstacion','fecha'])['QFF_Valor'].transform("min")
df['pres_max'] = df.groupby(['nombreEstacion','fecha'])['QFF_Valor'].transform("max")
df['pres_prom'] = df.groupby(['nombreEstacion','fecha'])['QFF_Valor'].transform("mean")

df = df.drop(columns=['QFF_Valor','hora'])
df = df.drop_duplicates()
df = df.dropna()
df.to_csv('csvlimpios\\presion.csv',index=False)

#Base de datos temperatura 

df = pd.read_csv('csv\\temperatura_dmc.csv')

fecha = df['time'].str.split(expand=True)
fecha.columns = ['fecha', 'hora']
df = pd.concat([df, fecha], axis=1)

df = df.drop(columns=['latitud','longitud','CodigoNacional','time'])

df = df[(df['fecha'] > '2009-12-31') & (df['fecha'] < '2020-01-01')]

df['temp_min'] = df.groupby(['nombreEstacion','fecha'])['Ts_Valor'].transform("min")
df['temp_max'] = df.groupby(['nombreEstacion','fecha'])['Ts_Valor'].transform("max")
df['temp_prom'] = df.groupby(['nombreEstacion','fecha'])['Ts_Valor'].transform("mean")

df = df.drop(columns=['Ts_Valor','hora'])
df = df.drop_duplicates()
df = df.dropna()
df.to_csv('csvlimpios\\temp.csv',index=False)

##############################################
print('termine')