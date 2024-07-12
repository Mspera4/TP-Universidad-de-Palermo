#ACÁ SE LIMPIAN LA TABLAS DE LOS DATOS CLIMÁTICOS Y SE CREA LA TABLA LIMPIA

import pandas as pd
import numpy as np
import calendar

df_temp_hum = pd.read_csv('Trabajo Practico/Tablas_originales/Temperatura.csv')
df_temp_hum.head()

#-----------------------------------------

#Nos quedamos con la columna de temperatura media y descartamos las otras dos de temperatura
df_limpio = df_temp_hum[[column for column in df_temp_hum if column not in ['Temp. Maxima (°C) ', 'Temp. Minima (°C) ']]]

#Renombramos las columnas para corregir errores
df_limpio = df_limpio.rename(columns={'Temp. Media (°C) ': 'T Media'})
df_limpio = df_limpio.rename(columns={'Hum. Relativa Media (%)': 'H Media (%)'})
df_limpio = df_limpio.rename(columns={'Fecha      ': 'Fecha'})
df_limpio = df_limpio.rename(columns={'Estacion ' : 'Estacion'})

#-----------------------------------------

#Convierto la columna 'Fecha' a tipo datetime
df_limpio['Fecha'] = pd.to_datetime(df_limpio['Fecha'])

#Creo las columnas año y mes
df_limpio['año'] = df_limpio['Fecha'].dt.year
df_limpio['mes'] = df_limpio['Fecha'].dt.month
df_limpio['dia'] = df_limpio['Fecha'].dt.day

#Convertimos los números de los meses a nombre
df_limpio['mes'] = df_limpio['mes'].apply(lambda x: calendar.month_name[x])

#Eliminamos la columna Fecha
df_limpio.drop(['Fecha'], axis=1, inplace=True)
df_limpio

#-----------------------------------------

#Corregimos los valores que están dando error en las filas
df_limpio['T Media'] = df_limpio['T Media'].replace('\\N               ', np.nan)
df_limpio['H Media (%)'] = df_limpio['H Media (%)'].replace('\\N               ', np.nan)
df_limpio['T Media'] = df_limpio['T Media'].replace('\\N', np.nan)
df_limpio['H Media (%)'] = df_limpio['H Media (%)'].replace('\\N', np.nan)

#-----------------------------------------

#Convertimos los datos a numéricos para poder operar con ellos
df_limpio['T Media'] = df_limpio['T Media'].astype(float)
df_limpio['H Media (%)'] = df_limpio['H Media (%)'].astype(float)
df_limpio['año'].astype(int)
df_limpio['Estacion'].astype(int)
df_limpio['mes'].astype(str)
df_limpio['dia'].astype(int)

#-----------------------------------------

#ordenamos los meses cronológicamente
mes_ordenado = list(calendar.month_name)[1:]
df_limpio['mes'] = pd.Categorical(df_limpio['mes'], categories=mes_ordenado, ordered=True)
df_limpio = df_limpio.sort_values(by=['año', 'mes'])

#-----------------------------------------

#Creamos el csv de la tabla limpia y lista para utilziar
df_limpio.to_csv('Trabajo Practico/Tablas_creadas/Temp_humedad.csv', index=False)