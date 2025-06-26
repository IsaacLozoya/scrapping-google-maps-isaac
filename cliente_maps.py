# cliente_maps.py

import googlemaps
import os
from dotenv import load_dotenv
import time
import random


load_dotenv()
CLAVE_API = os.getenv("CLAVE_API_GOOGLE_MAPS")

class ClienteGoogleMaps:
    def __init__(self):
        self.cliente = googlemaps.Client(key=CLAVE_API)

    def buscar_restaurantes_por_codigo_postal(self, codigo_postal: str, reintentos_maximos=5):
        reintento = 0
        while reintento < reintentos_maximos:
            try:
                print(f"🔍 Buscando restaurantes en {codigo_postal} (Intento {reintento + 1})")
                respuesta = self.cliente.places(
                    query=f"restaurantes en {codigo_postal}",
                    type="restaurant"
                )

                estado = respuesta.get("status")

                if estado == "OK":
                    time.sleep(random.uniform(1.5, 3.5))  # Delay entre peticiones
                    return respuesta.get("results", [])

                elif estado == "OVER_QUERY_LIMIT":
                    espera = 2 ** reintento  # Backoff exponencial
                    print(f"⚠️ Límite de consultas alcanzado. Esperando {espera} segundos...")
                    time.sleep(espera)
                    reintento += 1

                else:
                    print(f"❌ Error en respuesta de la API: {estado}")
                    break

            except Exception as error:
                espera = 2 ** reintento
                print(f"⚠️ Error inesperado: {error}. Reintentando en {espera} segundos...")
                time.sleep(espera)
                reintento += 1

        print("🚫 No se pudieron obtener los resultados después de varios intentos.")
        return []
