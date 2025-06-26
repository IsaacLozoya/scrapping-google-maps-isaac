# exportador_datos.py

import json
import csv
from conexion_mongo import obtener_conexion
from collections import Counter

def exportar_a_json(nombre_archivo="restaurantes_exportados.json"):
    coleccion = obtener_conexion()
    datos = list(coleccion.find({}, {"_id": 0}))  # No incluir el _id

    with open(nombre_archivo, "w", encoding="utf-8") as archivo_json:
        json.dump(datos, archivo_json, indent=4, ensure_ascii=False)

    print(f"✅ Datos exportados a JSON: {nombre_archivo}")

def exportar_a_csv(nombre_archivo="restaurantes_exportados.csv"):
    coleccion = obtener_conexion()
    datos = list(coleccion.find({}, {"_id": 0}))

    if not datos:
        print("⚠️ No hay datos para exportar.")
        return

    campos = list(datos[0].keys())

    with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

    print(f"✅ Datos exportados a CSV: {nombre_archivo}")

def generar_estadisticas_basicas():
    coleccion = obtener_conexion()
    datos = list(coleccion.find({}, {"_id": 0}))

    total = len(datos)
    codigos = [dato.get("codigo_postal") for dato in datos if dato.get("codigo_postal")]
    conteo_codigos = Counter(codigos)

    print("\n📊 Estadísticas Básicas:")
    print(f"• Total de restaurantes guardados: {total}")
    print(f"• Código postales encontrados: {len(conteo_codigos)}")
    print("• Distribución por código postal:")
    for cp, cantidad in conteo_codigos.items():
        print(f"  - {cp}: {cantidad} restaurantes")

if __name__ == "__main__":
    exportar_a_json()
    exportar_a_csv()
    generar_estadisticas_basicas()
