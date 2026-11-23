import pandas as pd


df = pd.read_csv("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\01_ventas_estandar.csv", index_col="id_venta")
print(df)

df2 = pd.read_csv("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\02_clientes_punto_coma_latin1.csv", sep=";", encoding="latin-1")
print(df2)

df3 = pd.read_csv("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\03_sensores_tabulado.txt", sep="\t")
print(df3)

df4 = pd.read_csv("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\04_inventario_barras.txt", sep="|", index_col="sku")
print(df4)

df5 = pd.read_csv("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\05_accesos_espacios.txt", sep=r"\s+")
print(df5)

df6 = pd.read_csv("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\06_mediciones_sin_cabecera.csv", header=None)
print(df6)

df7 = pd.read_csv("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\07_reporte_sucursal_metadatos.csv", skiprows=3, header=0, index_col=0)
print(df7)

df8 = pd.read_excel("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\08_finanzas_multihoja.xlsx", sheet_name="Ventas_2025", skiprows=3, header=0)
print(df8)

df9 = pd.read_json("C:\\Users\\adria\\Desktop\\00_fapd_total\\00_fapd\\01_DATA_Clase03_Archivos_practica\\09_paises_del_mundo.json")
print(df9)
