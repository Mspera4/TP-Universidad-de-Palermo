#EN ESTA SECCIÓN SE LIMPIAN LOS CSV EXTRAÍDOS DE LA BASE DE DATOS PÚBLICA
#SE CREA NUESTRA TABLA GENERAL CON TODOS LOS DATOS POR DEPARTAMENTO, PROVINCIA, RANGO ETÁREO Y CANTIDAD DE CASOS DEL PAÍS EN EL PERÍODO 2018-2024

import pandas as pd
import numpy as np
import re
import calendar
'''import seaborn as sns
import matplotlib.pyplot as plt
import pycaret as pc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
sns.set_theme()'''

#Cargamos los csv de la base de datos pública
df2018_2 = pd.read_csv('Trabajo Practico/Tablas_originales/Dengue, Zika 2018 - 2.csv')
df2018 = pd.read_csv('Trabajo Practico/Tablas_originales/Dengue, Zika 2018.csv')
df2019 = pd.read_csv('Trabajo Practico/Tablas_originales/Dengue, Zika 2019.csv')
df2020 = pd.read_csv('Trabajo Practico/Tablas_originales/Dengue, Zika 2020.csv')
df2021 = pd.read_csv('Trabajo Practico/Tablas_originales/Dengue, Zika 2021.csv')
df2022 = pd.read_csv('Trabajo Practico/Tablas_originales/Dengue, Zika 2022.csv')
df2023 = pd.read_csv('Trabajo Practico/Tablas_originales/Dengue, Zika 2023.csv')
df2024 = pd.read_csv('Trabajo Practico/Tablas_originales/Dengue, Zika 2024.csv')

#-----------------------------------------

#Estandarizamos el formato de prov_id y de id_depto dependiendo de si están fusionados o no en su csv.

#Hago String a todos los id_depto y prov_id de 2018
df2018['id_depto'] = df2018['id_depto'].values.astype(str)
df2018["prov_id"] = df2018["prov_id"].map(str)

#Aplico el zfill
df2018['id_depto'] = df2018['id_depto'].str.zfill(5)
df2018["prov_id"] = df2018 ["prov_id"].str.zfill(2)

#Hago String a todos los id_depto y prov_id de 2018_2
df2018_2["id_depto"] = df2018_2["id_depto"].astype(str)
df2018_2["prov_id"] = df2018_2["prov_id"].astype(str)

#Aplico el zfill
df2018_2['id_depto'] = df2018_2['id_depto'].str.zfill(3)
df2018_2['prov_id'] = df2018_2['prov_id'].str.zfill(2)

# Hago String a todos los id_depto y prov_id de 2019
df2019["id_depto"] = df2019["id_depto"].astype(str)
df2019["prov_id"] = df2019["prov_id"].astype(str)

#Aplico el zfill
df2019['id_depto'] = df2019['id_depto'].str.zfill(5)
df2019["prov_id"] = df2019 ["prov_id"].str.zfill(2)

# Hago String a todos los id_depto y prov_id de 2020
df2020["id_depto"] = df2020["id_depto"].astype(str)
df2020["prov_id"] = df2020["prov_id"].astype(str)

# Aplico el zfill
df2020["id_depto"] = df2020 ["id_depto"].str.zfill(5)
df2020["prov_id"] = df2020 ["prov_id"].str.zfill(2)

# Hago String a todos los id_depto y prov_id de 2021
df2021["id_depto"] = df2021["id_depto"].astype(str)
df2021["prov_id"] = df2021["prov_id"].astype(str)

# Aplico el zfill
df2021["id_depto"] = df2021 ["id_depto"].str.zfill(5)
df2021["prov_id"] = df2021 ["prov_id"].str.zfill(2)

# Hago String a todos los id_depto y prov_id de 2022
df2022["id_depto"] = df2022["id_depto"].astype(str)
df2022["prov_id"] = df2022["prov_id"].astype(str)

#Aplico el zfill
df2022["id_depto"] = df2022 ["id_depto"].str.zfill(3)
df2022["prov_id"] = df2022 ["prov_id"].str.zfill(2)

#Hago String a todos los id_depto y prov_id de 2023
df2023["id_depto"] = df2023["id_depto"].astype(str)
df2023["prov_id"] = df2023["prov_id"].astype(str)

# Aplico el zfill
df2023["id_depto"] = df2023 ["id_depto"].str.zfill(5)
df2023["prov_id"] = df2023 ["prov_id"].str.zfill(2)

# Hago String a todos los id_depto y prov_id de 2024
df2024["id_depto"] = df2024["id_depto"].astype(str)
df2024["prov_id"] = df2024["prov_id"].astype(str)

# Aplico el zfill
df2024["id_depto"] = df2024 ["id_depto"].str.zfill(3)
df2024["prov_id"] = df2024 ["prov_id"].str.zfill(2)

#-----------------------------------------

#Concatenamos los df de cada año para crear una TablaCompleta
TablaCompleta = pd.concat([df2018_2, df2018, df2019, df2020, df2021, df2022, df2023, df2024])
TablaCompleta.sample(10)
TablaCompleta.info()

#-----------------------------------------

#Estandarizamos el formato de id_depto agregandole prov_id a todos los id_depto donde originalmente no estaba

#Encuentro dónde tiene una longitud de 3 caracteres
id_corto = TablaCompleta['id_depto'].str.len() == 3

#Junto los prov_id con el id_depto en las id_depto donde tiene una longitud de 3 caracteres
TablaCompleta.loc[id_corto, 'id_depto'] =  TablaCompleta.loc[id_corto, 'prov_id'] + TablaCompleta.loc[id_corto, 'id_depto']

#Corroboramos lo hecho hasta ahora
TablaCompleta.sample(10)

#-----------------------------------------

#Estandarizamos las mayúsculas y corregimos errores en la TablaCompleta['prov']
TablaCompleta['prov'] = TablaCompleta['prov'].str.replace(r'([a-z])([A-Z])', r'\1 \2', regex=True).str.title()
TablaCompleta['prov'] = TablaCompleta['prov'].replace('(En Blanco)', 'Desconocida')
TablaCompleta['prov'] = TablaCompleta['prov'].replace('Desconocido', 'Desconocida')
TablaCompleta['prov'] = TablaCompleta['prov'].replace('Desconocidoo', 'Desconocida')
TablaCompleta['prov'] = TablaCompleta['prov'].replace('Desconocida', pd.NA)
TablaCompleta['prov'] = TablaCompleta['prov'].replace('Caba', 'CABA')
TablaCompleta['prov'] = TablaCompleta['prov'].replace('C�Rdoba', 'Córdoba')

#Estandarizamos las mayúsculas y corregimos errores en la TablaCompleta['depto']
TablaCompleta['depto'] = TablaCompleta['depto'].str.replace(r'([a-z])([A-Z])', r'\1 \2', regex=True).str.title()
TablaCompleta['depto'] = TablaCompleta['depto'].replace('(En Blanco)', 'Desconocida')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Desconocido', 'Desconocida')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Desconocidoo', 'Desconocida')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Desconocida', pd.NA)
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Jun�N', 'Junín')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Santa Mar�A', 'Santa María')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Ituzaing�', 'Ituzaingo')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Lan�S', 'Lanús')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Mor�N', 'Morón')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Col�N', 'Colón')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Or�N', 'Orán')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Guaran�', 'Guaraní')
TablaCompleta['depto'] = TablaCompleta['depto'].replace('Constituci�N', 'Constitución')

#-----------------------------------------

#CORREGIMOS LOS CASOS EN QUE LOS DATOS DE LAS COLUMNAS 'SEMANA' Y 'EVENTO' ESTÁN INTERCAMBIADOS

#Agarramos las filas de la columna evento donde hay números en lugar de lo que corresponde ('Dengue' o 'Zika')
filas_malas = TablaCompleta['evento'].str.isnumeric()

#Hacemos un df_temporal con las filas que tienen mal la información
temp_df = TablaCompleta.loc[filas_malas, ['evento', 'semanas']]

#Intercambio los nombres de las columnas del df temporal para que coincidan
temp_df = temp_df.rename(columns={'evento': 'semanas', 'semanas': 'evento'})

#Reinserto el df_temporal en la TablaCompleta
TablaCompleta.loc[filas_malas, ['evento', 'semanas']] = temp_df

#-----------------------------------------

#CORREGIMOS EL MISMO TIPO DE ERROR PERO EN LAS COLUMNAS 'EDADES' Y 'EDAD_ID'

#Agarro las filas donde edad_desc está compuesto por nros
filas_m = TablaCompleta['edad_desc'].str.isnumeric()

#Hago un df temporal con las filas que tienen mal la información
df_temp = TablaCompleta.loc[filas_m, ['edad_desc', 'edad_id']]

#Switcheo los nombres de las columnas del df temporal para que quede bien
df_temp = df_temp.rename(columns={'edad_desc': 'edad_id', 'edad_id': 'edad_desc'})

#Reinserto el df temporal en el df original
TablaCompleta.loc[filas_m, ['edad_desc', 'edad_id']] = df_temp

#Filleo los valores nulos de la columna 'edad_id' con 0
TablaCompleta['edad_id'] = TablaCompleta['edad_id'].fillna(0)

#Filleo los valores nulos de la columna 'edad_desc' con 'Desconocido/Sin Especificar'
TablaCompleta['edad_desc'] = TablaCompleta['edad_desc'].fillna('Desconocido/Sin Especificar')

#-----------------------------------------

#ESTANDARIZAMOS LOS DETALLES DE LA COLUMNA DE EDADES

#Corregimos errores con la ñ
TablaCompleta['edad_desc'] = TablaCompleta['edad_desc'].str.replace('anos', 'años', regex=True, flags=re.IGNORECASE)
TablaCompleta['edad_desc'] = TablaCompleta['edad_desc'].str.replace('ano', 'año', regex=True, flags=re.IGNORECASE)

# Estandarizo las mayúsculas de edad_desc

TablaCompleta['edad_desc'] = TablaCompleta['edad_desc'].str.title()

'''  Ahora me aseguro que el mismo nro. de edad_id se corresponda con la misma descripción; dónde: 
0- Desconocido/Sin Especificar
1- Menor a 1 año
2- 1 a 2 años
3- 2 a 4 años
4- 5 a 9 años
5- 10 a 14 años
6- 15 a 24 años
7- 25 a 34 años
8- 35 a 44 años
9- 45 a 64 años
10- Mayor o igual a 65
'''

condition = TablaCompleta['edad_desc'].str.contains('1 a 2 años', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 2, TablaCompleta['edad_id'])

condition = TablaCompleta['edad_desc'].str.contains('2 a 4 años', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 3, TablaCompleta['edad_id'])

condition = TablaCompleta['edad_desc'].str.contains('13 a 24', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 3, TablaCompleta['edad_id'])
TablaCompleta['edad_desc'] = np.where(condition, '1 a 2 años', TablaCompleta['edad_desc'])

condition = TablaCompleta['edad_desc'].str.contains('5 a 9 años', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 4, TablaCompleta['edad_id'])

condition = TablaCompleta['edad_desc'].str.contains('10 a 14 años', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 5, TablaCompleta['edad_id'])

condition = (TablaCompleta['edad_desc'].str.contains('15 a', case=False, regex=False) | 
             TablaCompleta['edad_desc'].str.contains('24', case=False, regex=False))
TablaCompleta['edad_id'] = np.where(condition, 6, TablaCompleta['edad_id'])
TablaCompleta['edad_desc'] = np.where(condition, 'De 15 a 24 años', TablaCompleta['edad_desc'])

condition = TablaCompleta['edad_desc'].str.contains('25 a 34 años', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 7, TablaCompleta['edad_id'])

condition = TablaCompleta['edad_desc'].str.contains('35 a 44 años', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 8, TablaCompleta['edad_id'])

condition = TablaCompleta['edad_desc'].str.contains('45 a 64 años', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 9, TablaCompleta['edad_id'])

condition = TablaCompleta['edad_desc'].str.contains('65', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 10, TablaCompleta['edad_id'])
TablaCompleta['edad_desc'] = np.where(condition, 'Mayor a 65 años', TablaCompleta['edad_desc'])

condition = TablaCompleta['edad_desc'].str.contains('nato', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 1, TablaCompleta['edad_id'])
TablaCompleta['edad_desc'] = np.where(condition, 'Menor a 1 año', TablaCompleta['edad_desc'])

condition = TablaCompleta['edad_desc'].str.contains('menor', case=False, regex=False)
TablaCompleta['edad_desc'] = np.where(condition, 'Menor a 1 año', TablaCompleta['edad_desc'])

condition = TablaCompleta['edad_desc'].str.contains('-', case=False, regex=False)
TablaCompleta['edad_desc'] = np.where(condition, 'Desconocido/Sin Especificar', TablaCompleta['edad_desc'])


condition = TablaCompleta['edad_desc'].str.contains('Sin', case=False, regex=False)
TablaCompleta['edad_id'] = np.where(condition, 0, TablaCompleta['edad_id'])
TablaCompleta['edad_desc'] = np.where(condition, 'Desconocido/Sin Especificar', TablaCompleta['edad_desc'])
#-----------------------------------------

#Limpiamos la columna eventos

condition = TablaCompleta['evento'].str.contains('Zi', case=False, regex=False)
TablaCompleta['evento'] = np.where(condition, 'Zika', TablaCompleta['evento'])


condition = TablaCompleta['evento'].str.contains('Den', case=False, regex=False)
TablaCompleta['evento'] = np.where(condition, 'Dengue', TablaCompleta['evento'])

#-----------------------------------------

#LIMPIAMOS LA COLUMNA DEPTO

#Eliminamos los valores en los que la ubicación es desconocida puesto que no son un porcentaje representativo
TablaCompleta = TablaCompleta.dropna()

#Convertimos la columna 'id_depto' a string
TablaCompleta['id_depto'] = TablaCompleta['id_depto'].astype(str)

#Nos fijamos cuantas veces no figura la provincia
id_00 = TablaCompleta['id_depto'].str.startswith('00').sum()

# Notamos que en la tabla hay instancias en deptos donde falta que el id_depto identifique la provincia
condition = TablaCompleta['depto'].str.contains('matanza', case=False, regex=False)
TablaCompleta['depto'] = np.where(condition, 'La Matanza', TablaCompleta['depto'])
TablaCompleta['id_depto'] = np.where(condition, '06427', TablaCompleta['id_depto'])

condition = (TablaCompleta['depto'] == ('Comuna 1'))
TablaCompleta['id_depto'] = np.where(condition, '02001', TablaCompleta['id_depto'])

print(f"Hay {id_00} columnas que arrancan con '00'.")

#Acomodamos las comunas (en cada año varía la forma de registro)

# Arranco convirtiendolo en un string para poder aplicarle startswith
TablaCompleta['id_depto'] = TablaCompleta['id_depto'].astype(str)

# Creo la mascara
mask = TablaCompleta['id_depto'].str.startswith('020') & TablaCompleta['id_depto'].str[3:].apply(lambda x: x.isdigit() and 1 <= int(x) <= 15)

# Actualizo la columna deptos
TablaCompleta.loc[mask, 'depto'] = 'Comuna ' + TablaCompleta.loc[mask, 'id_depto'].str[3:]

# Como solo hay 35 instancias en las que id_depto arranca con 00, los nulifico y elimino a todos
id00 = TablaCompleta['id_depto'].str.startswith('00').sum()
TablaCompleta['id_depto'] = np.where(condition, pd.NA, TablaCompleta['id_depto'])
TablaCompleta = TablaCompleta.dropna()

#-----------------------------------------

#Limpiamos las provincias

condition = TablaCompleta['prov'].str.contains('Entre', case=False, regex=False)
TablaCompleta['prov_id'] = np.where(condition, '30', TablaCompleta['prov_id'])

#-----------------------------------------

#Reducimos la granularidad, pasamos de semanas a meses con sus nombres

#Convierto las semanas a meses
TablaCompleta['mes'] = TablaCompleta['semanas'].astype(int).apply(lambda x: calendar.month_name[((x - 1) // 4 + 1) % 12 or 12])

#Elimino la columna semanas (Ya qué se volvió irrelevante)
TablaCompleta = TablaCompleta.drop('semanas', axis=1)

TablaCompleta.info()
TablaCompleta.describe()

TablaCompleta.to_csv('Trabajo Practico/Tablas_creadas/TablaCompleta.csv', index=False)
