from statistics import median
import numpy as np
import pandas as pd

nortegrande = ['Chacalluta, Arica Ap.','Diego Aracena Iquique Ap.','Desierto de Atacama, Caldera  Ad.',
'Putre','El Loa, Calama Ad.','Copiapó Universidad de Atacama','Visviri Tenencia'] 
nortechico = ['La Florida, La Serena Ad.','Freirina Nicolasa','Vicuña, Parque Los Pimientos',
'Liceo Samuel Román Rojas (Combarbalá)']
centro = ['Quinta Normal, Santiago','Pudahuel Santiago ',"General Bernardo O'Higgins, Chillán Ad.",'La Araucanía Ad.',
'General Freire, Curicó Ad.','Eulogio Sánchez, Tobalaba Ad.','Carriel Sur, Concepción Ap.','Los Libertadores',
'Termas de Chillán','Carriel Sur, Concepción Ap.','El Paico','San Felipe Escuela Agrícola','Lo Prado Cerro San Francisco',
'Lord Cochrane Ad.','Rancagua','Retiro Copihue','Rodelillo, Ad.','San José  Guayacán','Santo Domingo, Ad.']
sur = ['Pichoy, Valdivia Ad.','El Tepual  Puerto Montt Ap.','Quellón Ad.','Maquehue, Temuco Ad.','Quellón Ad.',
'Cañal Bajo,  Osorno Ad.','Futaleufú Ad.']
austral = ['Teniente Gallardo, Puerto Natales Ad.','Puerto Aysén Ad.','Teniente Vidal, Coyhaique Ad.',
'Fuentes Martínez, Porvenir Ad.', 'Guardiamarina Zañartu, Pto Williams Ad.',
'Carlos Ibañez, Punta Arenas Ap.','Balmaceda Ad.']


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

df = df[(df['nombreEstacion'].isin(centro)) | (df['nombreEstacion'].isin(nortegrande)) |
(df['nombreEstacion'].isin(nortechico)) | (df['nombreEstacion'].isin(sur)) | 
(df['nombreEstacion'].isin(austral)) ]

df = df.drop_duplicates(subset=['fecha','nombreEstacion'])

df = df[['fecha','nombreEstacion','mmtotal','hum_min','hum_max','hum_prom','pres_min','pres_max',
'pres_prom','dd_Valor','vel_min','vel_max','vel_prom','temp_rocio_min','temp_rocio_max','temp_rocio_prom',
'temp_min','temp_max','temp_prom']]

df.rename(columns={'mmtotal': 'mmAguaCaidadiaria','hum_min': 'HumedadRelativaMin',
'hum_max': 'HumedadRelativaMax','hum_prom': 'HumedadRelativaProm','pres_min':'PresionAtmosfericaMin',
'pres_max':'PresionAtmosfericaMax','pres_prom':'PresionAtmosfericaProm','dd_Valor':'Direccionviento',
'vel_min':'VelocidadvientoMin','vel_max':'VelocidadvientoMax','vel_prom':'VelocidadvientoProm','temp_rocio_min':
'TemperaturarocioMin','temp_rocio_max':'TemperaturarocioMax','temp_rocio_prom':'TemperaturarocioProm',
'temp_min':'TemperaturaMin','temp_max':'TemperaturaMax','temp_prom':'TemperaturaProm'}, inplace=True)


conditions = [
    (df['nombreEstacion'].isin(nortegrande)),
    (df['nombreEstacion'].isin(nortechico)),
    (df['nombreEstacion'].isin(centro)),
    (df['nombreEstacion'].isin(sur)),
    (df['nombreEstacion'].isin(austral))
    ]

values = ['norte_grande','norte_chico', 'centro', 'sur', 'austral']

df['zona'] = np.select(conditions, values)


fecha = df['fecha'].str.split(expand=True,pat="-")
fecha.columns = ['año','mes','dia']
df = pd.concat([df, fecha], axis=1)

verano = ['12','01','02','03']
otoño = ['04','05','06']
invierno = ['07','08','09']
primavera = ['10','11']

conditions = [
    (df['mes'].isin(verano)),
    (df['mes'].isin(otoño)),
    (df['mes'].isin(invierno)),
    (df['mes'].isin(primavera))
    ]

values = ['verano','otoño', 'invierno', 'primavera']

df['estacion'] = np.select(conditions, values)

df = df.drop(columns=['año','mes','dia'])

df.to_csv('csvlimpios\\lluvia.csv',index=False)
print('termine')