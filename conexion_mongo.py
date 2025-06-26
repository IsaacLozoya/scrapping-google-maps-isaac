# conexion_mongo.py

from pymongo import MongoClient

def obtener_conexion():
    cliente = MongoClient("mongodb://localhost:27017/")
    base_de_datos = cliente["TEST"]
    coleccion = base_de_datos["restaurantes"]
    return coleccion
