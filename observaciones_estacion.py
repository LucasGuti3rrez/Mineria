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
df = df.drop_duplicates(subset=['fecha','nombreEstacion'])
print(df.groupby('nombreEstacion').count())
print('termine')

#output
"""                                            
                                          fecha  
nombreEstacion                                                          
Balmaceda Ad.                              3648            
C.M.A. Eduardo Frei Montalva, Antártica    3640           
Carlos Ibañez, Punta Arenas Ap.            3652           
Carriel Sur, Concepción Ap.                3651            
Cañal Bajo,  Osorno Ad.                    3643          
Chacalluta, Arica Ap.                      3651          
Copiapó Universidad de Atacama             1095          
Desierto de Atacama, Caldera  Ad.          3529         
Diego Aracena Iquique Ap.                  3652         
El Colorado                                1199        
El Loa, Calama Ad.                          193        
El Paico                                   2408        
El Tepual  Puerto Montt Ap.                3650         
Eulogio Sánchez, Tobalaba Ad.               489          
Freirina Nicolasa                          1091     
Fuentes Martínez, Porvenir Ad.             2941        
Futaleufú Ad.                              2311    
General Bernardo O'Higgins, Chillán Ad.    3545        
General Freire, Curicó Ad.                 3650       
Guardiamarina Zañartu, Pto Williams Ad.    3051      
Juan Fernández, Estación Meteorológica.    3626      
La Araucanía Ad.                           1982      
La Florida, La Serena Ad.                  3652      
Liceo Samuel Román Rojas (Combarbalá)       255      
Lo Prado Cerro San Francisco               2447       
Lord Cochrane Ad.                          2488        
Los Libertadores                           2559     
Maquehue, Temuco Ad.                       3508     
Mataveri  Isla de Pascua Ap.               3652     
Pichoy, Valdivia Ad.                       3309       
Pudahuel Santiago                          3652         
Puerto Aysén Ad.                           2305       
Putre                                      1090         
Quellón Ad.                                2244        
Quinta Normal, Santiago                    3651   
Rancagua                                   1293        
Retiro Copihue                              820       
Rodelillo, Ad.                             3558          
San Felipe Escuela Agrícola                 167           
San José  Guayacán                         2517       
Santo Domingo, Ad.                         3652     
Teniente Gallardo, Puerto Natales Ad.      2483        
Teniente Vidal, Coyhaique Ad.              3651      
Termas de Chillán                          2116           
Victoria (Reg.)                             182         
Vicuña, Parque Los Pimientos                811         
Visviri Tenencia                           2314        """
