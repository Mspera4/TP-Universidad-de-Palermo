#EN ESTE ARCHIVO NORMALIZAMOS Y CREAMOS LAS TALBAS QUE SE RELACIONAN CON LA TABLA COMPLETA

import pandas as pd
import numpy as np
import re
import calendar

#Cargamos la TablaCompleta
TablaCompleta = pd.read_csv('Trabajo Practico/Tablas_creadas/TablaCompleta.csv')


#Definimos las nuevas tablas
Provincias = TablaCompleta[['prov_id', 'prov']].drop_duplicates().reset_index(drop = True).sort_values(by='prov_id')
Departamentos = TablaCompleta[['id_depto', 'depto']].drop_duplicates().reset_index(drop = True).sort_values(by='id_depto')
Edades = TablaCompleta[['edad_id', 'edad_desc']].drop_duplicates().reset_index(drop=True).sort_values(by='edad_id')
Eventos = TablaCompleta[['evento']].drop_duplicates().reset_index(drop = True)
Reportes = TablaCompleta[['prov_id','id_depto', 'año', 'mes', 'evento', 'edad_id', 'cantidad']]
Reportes['id_reporte'] = range(1, len(Reportes) + 1)

#Creamos las nuevas tablas
Provincias.to_csv('Trabajo Practico/Tablas_creadas/Provincias.csv', index=False)
Departamentos.to_csv('Trabajo Practico/Tablas_creadas/Departamentos.csv', index=False)
Edades.to_csv('Trabajo Practico/Tablas_creadas/Edades.csv', index=False)
Eventos.to_csv('Trabajo Practico/Tablas_creadas/Eventos.csv', index=False)
Reportes.to_csv('Trabajo Practico/Tablas_creadas/Reportes.csv', index=False)