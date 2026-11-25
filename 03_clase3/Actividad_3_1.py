# Ejercicio 1.1: Carga del Dataset e Inspección de Filas (head y tail)
import pandas as pd

df_estudiantes = pd.read_csv("00_fapd\\03_clase3\\00_DATA_Clase03_Archivos_Actividades\\DATA_Estudiantes.csv")
print(df_estudiantes.head(5))  # Muestra las primeras 5 filas del DataFrame
print(df_estudiantes.tail(5))  # Muestra las últimas 5 filas del Data



#Ejercicio 1.2: Dimensiones y Radiografía General (shape e info)
print(df_estudiantes.shape)  # Muestra las dimensiones del DataFrame (filas, columnas)
print(df_estudiantes.info())  # Muestra información general sobre el DataFrame, incluyendo tipos de datos y valores nulos






#Ejercicio 2: Clasificación de Tipos de Datos (dtypes y select_dtypes)
print(df_estudiantes.dtypes)  # Muestra los tipos de datos de cada columna
print(df_estudiantes.columns)  # Muestra los nombres de las columnas del DataFrame


print(df_estudiantes.select_dtypes(include="number").columns)
print(df_estudiantes.select_dtypes(include=["object", "bool"]))


print(df_estudiantes.describe())  # Muestra estadísticas descriptivas para las columnas numéricas

print( df_estudiantes[["nota_parcial","nota_final"]].describe().round(2))




#ejercicio 3: Diagnóstico de Valores Faltantes (isnull / isna)
print ("_______________________________________")
print(df_estudiantes.isnull().sum())
print((df_estudiantes.isnull().mean() * 100).round(2))

# Ejercicio 3.2: Detección de Filas Duplicadas (duplicated)
print(df_estudiantes.duplicated().sum())
print(df_estudiantes[df_estudiantes.duplicated(keep=False)])