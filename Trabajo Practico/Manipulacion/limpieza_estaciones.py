#ACÁ SE LIMPIAN LA TABLAS DE LAS ESTACIONES POR DEPTO Y PROVINCIA Y SE CREA LA TABLA LIMPIA

import pandas as pd
import numpy as np

df_estaciones_depto = pd.read_csv('Trabajo Practico/Tablas_originales/estaciones smn PAIS.csv')
df_estaciones_depto

#limpiamos los nombres de las columnas para que coincidan con las otras tablas
df_estaciones_depto = df_estaciones_depto.rename(columns={'PROVINCIA': 'prov'})
df_estaciones_depto = df_estaciones_depto.rename(columns={'NOMBRE': 'depto'})

#limpiamos estandarizamos los nombres de las provincias y departamentos
df_estaciones_depto = df_estaciones_depto.map(lambda x: x.title() if isinstance(x, str) else x)
df_estaciones_depto['depto'] = df_estaciones_depto['depto'].str.replace('Aero', '')

#cambio de nombre la columna NRO por Estación

df_estaciones_depto = df_estaciones_depto.rename(columns={'NRO': 'Estacion'})

#creamos la nueva tabla con las columnas Estación, depto y provincia
df_estaciones = df_estaciones_depto[['Estacion', 'depto', 'prov']]

#corrijo problema con las ñ
df_estaciones = df_estaciones.map(lambda x: x.replace('ﾑ', 'ñ') and x.title() if isinstance(x, str) else x)

#Corrijo los errores de tipeo
df_estaciones['prov'] = df_estaciones['prov'].replace('Cordoba', 'Córdoba')
df_estaciones['prov'] = df_estaciones['prov'].replace('Rio Negro', 'Río Negro')
df_estaciones['prov'] = df_estaciones['prov'].replace('Neuquen', 'Neuquén')
df_estaciones['prov'] = df_estaciones['prov'].replace('Tucuman', 'Tucumán')

#Elimino los espacios vacíos de la columna depto y prov
df_estaciones['depto'] = df_estaciones['depto'].str.strip()
df_estaciones['prov'] = df_estaciones['prov'].str.strip()

#-----------------------------------------

#HACEMOS EL MERGE PARA QUE LA TABLA ESTACIONES COMPARTA EL ID_PROV CON EL RESTO DE LAS TABLAS

#Cargo la tabla Provincias
Provincias = pd.read_csv('Trabajo Practico/Tablas_creadas/Provincias.csv')

df_estacion = pd.merge(df_estaciones, Provincias, on='prov', how='left')
df_estacion['prov_id'].dropna()

#Eliminamos las filas con prov_id NaN
df_estacion.dropna(subset=['prov_id'], inplace=True)
df_estacion.info()

#Convertimos los prov_id que están como float a int
df_estacion['prov_id'] = df_estacion['prov_id'].astype(int)

#Reseteamos el indice
df_estacion = df_estacion.reset_index()
df_estacion
#-----------------------------------------

#Creamos el csv de la tabla limpia y lista para utilziar
df_estacion.to_csv('Trabajo Practico/Tablas_creadas/Estaciones.csv', index=False)
