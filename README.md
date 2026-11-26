Repositorio de prácticas del curso de Fundamentos de Análisis y Procesamiento de Datos. Contiene ejercicios organizados por clases, ejercicios de carga y limpieza de datos, notebooks de práctica y un proyecto independiente para demostrar el uso de módulos y paquetes en Python.

Contenido por clases

Clase 1: Primer contacto con Python mediante un ejercicio de salida por consola con print() y caracteres especiales.

hola_Mundo.py

Clase 2: Fundamentos del lenguaje y estructura de datos.

Variables y tipos de datos.
Conversión o coerción de tipos.
Operadores matemáticos y funciones básicas.
Listas, tuplas, conjuntos y cadenas.
Diccionarios y DataFrames con Pandas.
Condicionales, bucles y funciones con *args y **kwargs.
mi_practica_clase02_fapd.ipynb

Clase 3: Carga, inspección y limpieza de datos.

Lectura de archivos CSV, TXT, Excel y JSON.
Separadores, codificaciones, filas iniciales e índices personalizados.
Diagnóstico de tipos de datos, duplicados y valores nulos.
Eliminación e imputación de datos faltantes.
Detección de valores atípicos mediante boxplots, IQR y Z-score.
Eliminación, transformación y winsorización de outliers.


load_files.py
Actividad_3_1.py
Práctica de valores nulos
Práctica de valores atípicos

Clase 4: Preparación y transformación de un dataset de vuelos.

Exploración con head, info, dtypes y valores nulos.
Ordenación, filtrado, renombrado y creación de variables.
Agrupación y estadísticas con groupby.
Codificación de variables categóricas.
Estandarización y normalización.
Conversión de tipos y fechas.
Optimización de memoria.
Exportación a CSV, Excel y Parquet.
mi_practica_clase04.ipynb
Proyecto independiente
La carpeta 01_fapd_proyecto contiene un ejercicio práctico sobre organización de código mediante módulos y paquetes:

main.py utiliza funciones importadas desde el paquete utilidades.
finanzas.py contiene funciones para calcular descuentos e IVA.
texto.py forma parte del paquete de utilidades.
Tecnologías utilizadas
Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn, SciPy, scikit-learn, OpenPyXL y PyArrow/Parquet.
