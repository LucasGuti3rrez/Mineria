import numpy as np
import pandas as pd


df_agua_caida_diaria = pd.read_csv('csvlimpios\\agua_caida_diaria.csv')
df_humedad = pd.read_csv('csvlimpios\\humedad.csv')
df_presion = pd.read_csv('csvlimpios\\presion.csv')
df_viento = pd.read_csv('csvlimpios\\viento.csv')
df_rocio = pd.read_csv('csvlimpios\\rocio.csv')
df_temp = pd.read_csv('csvlimpios\\temp.csv')

df = pd.merge(df_agua_caida_diaria,df_humedad,left_on=['fecha','nombreEstacion'],right_on = ['fecha','nombreEstacion'])
df = pd.merge(df,df_presion,left_on=['fecha','nombreEstacion'],right_on = ['fecha','nombreEstacion'])
df = pd.merge(df,df_viento,left_on=['fecha','nombreEstacion'],right_on = ['fecha','nombreEstacion'])
df = pd.merge(df,df_rocio,left_on=['fecha','nombreEstacion'],right_on = ['fecha','nombreEstacion'])
df = pd.merge(df,df_temp,left_on=['fecha','nombreEstacion'],right_on = ['fecha','nombreEstacion'])

df = df['nombreEstacion'].unique()
print(df)

#output
""" ['Visviri Tenencia' 'Chacalluta, Arica Ap.' 'Putre'
 'Diego Aracena Iquique Ap.' 'El Loa, Calama Ad.'
 'Mataveri  Isla de Pascua Ap.' 'Desierto de Atacama, Caldera  Ad.'
 'Copiapó Universidad de Atacama' 'Freirina Nicolasa'
 'La Florida, La Serena Ad.' 'Vicuña, Parque Los Pimientos'
 'Liceo Samuel Román Rojas (Combarbalá)' 'San Felipe Escuela Agrícola'
 'Los Libertadores' 'Rodelillo, Ad.' 'Eulogio Sánchez, Tobalaba Ad.'
 'Quinta Normal, Santiago' 'Pudahuel Santiago ' 'Santo Domingo, Ad.'
 'Juan Fernández, Estación Meteorológica.' 'El Colorado'
 'Lo Prado Cerro San Francisco' 'San José  Guayacán' 'El Paico'
 'General Freire, Curicó Ad.' 'Rancagua'
 "General Bernardo O'Higgins, Chillán Ad." 'Carriel Sur, Concepción Ap.'
 'Termas de Chillán' 'Retiro Copihue' 'Maquehue, Temuco Ad.'
 'La Araucanía Ad.' 'Victoria (Reg.)' 'Pichoy, Valdivia Ad.'
 'Cañal Bajo,  Osorno Ad.' 'El Tepual  Puerto Montt Ap.' 'Quellón Ad.'
 'Futaleufú Ad.' 'Puerto Aysén Ad.' 'Teniente Vidal, Coyhaique Ad.'
 'Balmaceda Ad.' 'Lord Cochrane Ad.'
 'Teniente Gallardo, Puerto Natales Ad.' 'Carlos Ibañez, Punta Arenas Ap.'
 'Fuentes Martínez, Porvenir Ad.'
 'Guardiamarina Zañartu, Pto Williams Ad.'
 'C.M.A. Eduardo Frei Montalva, Antártica '] """