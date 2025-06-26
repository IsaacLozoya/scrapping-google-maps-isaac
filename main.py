# main.py

from cliente_maps import ClienteGoogleMaps
from conexion_mongo import obtener_conexion

def extraer_datos_restaurante(info):
   
    return {
        "nombre": info.get("name"),
        "direccion": info.get("formatted_address"),
        "codigo_postal": extraer_codigo_postal(info),
        "telefono": info.get("formatted_phone_number"),
        "calificacion": info.get("rating"),
        "numero_resenas": info.get("user_ratings_total"),
        "tipo_cocina": info.get("types"),
        "horario": info.get("opening_hours", {}).get("weekday_text") if info.get("opening_hours") else None,
        "sitio_web": info.get("website"),
        "coordenadas": info.get("geometry", {}).get("location")
    }

import re  

def extraer_codigo_postal(info):
    direccion = info.get("formatted_address", "")
    coincidencias = re.findall(r"\b\d{5}\b", direccion)
    return coincidencias[0] if coincidencias else None


def main():
    codigo_postal = input("📍 Ingresa un código postal para buscar restaurantes: ")

    cliente = ClienteGoogleMaps()
    coleccion = obtener_conexion()

    resultados = cliente.buscar_restaurantes_por_codigo_postal(codigo_postal)

    print(f"\n🔎 Se encontraron {len(resultados)} restaurantes. Procesando...\n")

    for lugar in resultados:
        detalles = cliente.cliente.place(lugar["place_id"])
        info_completa = detalles.get("result", {})
        datos_restaurante = extraer_datos_restaurante(info_completa)

        if datos_restaurante["codigo_postal"] != codigo_postal:
            print(f"⚠️ El restaurante {datos_restaurante['nombre']} no coincide con el código postal {codigo_postal}.")
            continue

        print(f"✅ Guardando: {datos_restaurante['nombre']} - {datos_restaurante['direccion']}")
        coleccion.insert_one(datos_restaurante)

    print("\n✅ Todos los datos fueron guardados en MongoDB.")

if __name__ == "__main__":
    main()
