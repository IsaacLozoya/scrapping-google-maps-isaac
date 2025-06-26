# Evaluación Técnica - Desarrollador Python Scraping 


## ✅ Funcionalidades
- Consulta restaurantes por código postal.
- Extracción de datos clave (nombre, dirección, teléfono, rating, coordenadas, etc.).
- Almacenamiento en base de datos MongoDB.
- Exportación a JSON y CSV.
- Estadísticas básicas.
- Manejo de límites de la API (delays, retry con backoff).

---

## 📦 Requisitos

- Python 3.9+
- pip
- MongoDB instalado localmente
- Clave de API de [Google Maps](https://console.cloud.google.com/)

---

## ⚙️ Instalación

```bash
Para instalar:

pip install -r requerimientos.txt

Para Ejecutar:

python main.py

Para generar los csv y json 

python exportador_datos.py

