
"""
Módulo Unificado de Inteligencia de Mercado - Sector Automoción (Alicante / Vega Baja)
Actualizado a Google Places API (New)
"""

import os
import re
import time
import sqlite3
from collections import Counter
import requests
import pandas as pd
import folium

# 1. PEGA AQUÍ TU CLAVE DE API DE GOOGLE CLOUD (entre las comillas)
API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "TU_API_KEY_DE_GOOGLE_CLOUD")
DB_NAME = "mercado_automocion_alicante.db"

MARCAS_OBJETIVO = [
    "Ford",
    "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "SEAT", "Cupra", "Škoda",
    "Renault", "Dacia", "Peugeot", "Citroën", "Opel", "Toyota", "Hyundai", "Kia", "Nissan",
    "MG", "BYD", "Omoda", "Jaecoo", "Ebro", "Leapmotor", "Lynk & Co",
    "Volvo", "Polestar", "Zeekr", "XPeng", "DFSK", "SWM", "EVO", "DR Automobiles"
]

ZONAS_ALICANTE = [
    "Orihuela", "Torrevieja", "San Miguel de Salinas", "Rojales", "Guardamar del Segura",
    "Almoradí", "Callosa de Segura", "Pilar de la Horadada", "Elche", "Alicante", "Crevillente"
]

MARCAS_CHINAS = {
    "MG", "BYD", "Omoda", "Jaecoo", "Chery", "EVO", "DR Automobiles",
    "Ebro", "Leapmotor", "Lynk & Co", "XPeng", "DFSK", "SWM"
}


def ejecutar_censo_concesionarios():
    url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.location,places.businessStatus"
    }
    registros = {}
    print("Iniciando rastreo con Places API (New) en Alicante y Vega Baja...")

    for marca in MARCAS_OBJETIVO:
        for zona in ZONAS_ALICANTE:
            consulta = f"Concesionario oficial {marca} en {zona}, Alicante"
            payload = {"textQuery": consulta, "languageCode": "es"}
            respuesta = requests.post(url, json=payload, headers=headers)
            
            if respuesta.status_code != 200:
                print(f"Aviso en {consulta}: {respuesta.text}")
                continue
                
            datos = respuesta.json()
            for p in datos.get("places", []):
                pid = p.get("id")
                if pid and pid not in registros:
                    registros[pid] = {
                        "place_id": pid,
                        "marca_buscada": marca,
                        "nombre": p.get("displayName", {}).get("text"),
                        "direccion": p.get("formattedAddress"),
                        "nota_media": p.get("rating", 0),
                        "total_resenas": p.get("userRatingCount", 0),
                        "latitud": p.get("location", {}).get("latitude"),
                        "longitud": p.get("location", {}).get("longitude"),
                        "estado": p.get("businessStatus", "OPERATIONAL")
                    }
            time.sleep(0.15)

    df = pd.DataFrame(list(registros.values()))
    df.to_csv("censo_concesionarios_alicante.csv", index=False, encoding="utf-8-sig")

    conn = sqlite3.connect(DB_NAME)
    df.to_sql("concesionarios", conn, if_exists="replace", index=False)
    conn.close()
    print(f"✅ Censo completado: {len(df)} concesionarios guardados en {DB_NAME} y CSV.")




"""
Módulo Unificado de Inteligencia de Mercado - Sector Automoción (Alicante / Vega Baja)
Versión optimizada con MarkerCluster para carga instantánea en navegador
"""

import os
import sqlite3
import pandas as pd
import folium
from folium.plugins import MarkerCluster

API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "TU_API_KEY_DE_GOOGLE_CLOUD")
DB_NAME = "mercado_automocion_alicante.db"

MARCAS_CHINAS = {
    "MG", "BYD", "Omoda", "Jaecoo", "Chery", "EVO", "DR Automobiles",
    "Ebro", "Leapmotor", "Lynk & Co", "XPeng", "DFSK", "SWM"
}


def generar_mapa_folium(lat_centro=37.9815, lon_centro=-0.7895, salida_html="04_Entregables_Visuales/mapa_concesionarios_alicante.html"):
    os.makedirs(os.path.dirname(salida_html), exist_ok=True)
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM concesionarios WHERE estado = 'OPERATIONAL'", conn)
    conn.close()

    mapa = folium.Map(location=[lat_centro, lon_centro], zoom_start=11, tiles=None)
    folium.TileLayer("Esri.WorldStreetMap", name="Mapa de Calles").add_to(mapa)


    folium.Circle(
        location=[lat_centro, lon_centro],
        radius=15000,
        color="#1f77b4",
        fill=True,
        fill_opacity=0.08,
        popup="Radio de influencia directa (15 km)"
    ).add_to(mapa)

    folium.Marker(
        location=[lat_centro, lon_centro],
        popup="<b>Área Central de Estudio</b><br>Comarca de la Vega Baja",
        tooltip="Centro Zona de Estudio",
        icon=folium.Icon(color="black", icon="star")
    ).add_to(mapa)

    cluster = MarkerCluster(name="Concesionarios Alicante").add_to(mapa)

    for _, fila in df.iterrows():
        marca = fila["marca_buscada"]
        if marca == "Ford":
            color_pin, icono, categoria = "blue", "wrench", "Red Oficial Ford"
        elif marca in MARCAS_CHINAS:
            color_pin, icono, categoria = "red", "car", "Marca China / Emergente"
        else:
            color_pin, icono, categoria = "cadetblue", "info-sign", "Marca Tradicional"

        html_popup = f"""
        <div style="font-family: Arial; width: 220px;">
            <h4 style="margin:0;">{fila['nombre']}</h4>
            <span style="color: gray; font-size: 12px;">{categoria} ({marca})</span><br><br>
            <b>Nota Google:</b> {fila['nota_media']} ⭐ ({fila['total_resenas']} reseñas)<br>
            <b>Dirección:</b> {fila['direccion']}
        </div>
        """

        folium.Marker(
            location=[fila["latitud"], fila["longitud"]],
            popup=folium.Popup(html_popup, max_width=250),
            tooltip=f"{fila['nombre']} ({marca})",
            icon=folium.Icon(color=color_pin, icon=icono, prefix="fa")
        ).add_to(cluster)

    mapa.save(salida_html)
    print(f"✅ Mapa ligero guardado en {salida_html}")


if __name__ == "__main__":
    generar_mapa_folium()


    # Ya están activadas ambas funciones para ejecutarse al darle a Play:
    #ejecutar_censo_concesionarios()
    
