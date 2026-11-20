"""
Módulo Unificado de Inteligencia de Mercado - Sector Automoción (Alicante / Vega Baja)
Incluye:
1. Extracción de censo de concesionarios (Google Places API -> CSV & SQLite)
2. Análisis de reseñas y frecuencia de palabras clave (NLP básico)
3. Generación de mapa interactivo geoespacial (Folium HTML)
"""

import os
import re
import time
import sqlite3
from collections import Counter
import requests
import pandas as pd
import folium

# CONFIGURACIÓN GLOBAL (Reemplazar con tu API Key o usar variable de entorno)
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

STOPWORDS_ES = {
    "el", "la", "los", "las", "un", "una", "unos", "unas", "y", "o", "pero",
    "de", "del", "a", "al", "en", "con", "por", "para", "sin", "sobre",
    "que", "es", "son", "fue", "muy", "mi", "me", "te", "se", "lo", "le",
    "he", "ha", "han", "todo", "toda", "todos", "como", "más", "mas", "ya"
}


def ejecutar_censo_concesionarios():
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    registros = {}
    print("Iniciando rastreo de concesionarios en Alicante y Vega Baja...")

    for marca in MARCAS_OBJETIVO:
        for zona in ZONAS_ALICANTE:
            consulta = f"Concesionario oficial {marca} en {zona}, Alicante"
            res = requests.get(url, params={"query": consulta, "language": "es", "key": API_KEY}).json()
            for lugar in res.get("results", []):
                pid = lugar.get("place_id")
                if pid and pid not in registros:
                    registros[pid] = {
                        "place_id": pid,
                        "marca_buscada": marca,
                        "nombre": lugar.get("name"),
                        "direccion": lugar.get("formatted_address"),
                        "nota_media": lugar.get("rating", 0),
                        "total_resenas": lugar.get("user_ratings_total", 0),
                        "latitud": lugar["geometry"]["location"]["lat"],
                        "longitud": lugar["geometry"]["location"]["lng"],
                        "estado": lugar.get("business_status")
                    }
            time.sleep(0.2)

    df = pd.DataFrame(list(registros.values()))
    df.to_csv("censo_concesionarios_alicante.csv", index=False, encoding="utf-8-sig")

    conn = sqlite3.connect(DB_NAME)
    df.to_sql("concesionarios", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Censo completado: {len(df)} concesionarios guardados en {DB_NAME}.")


def analizar_resenas_talleres(diccionario_place_ids):
    resultados = []
    for nombre, pid in diccionario_place_ids.items():
        url = (
            f"https://maps.googleapis.com/maps/api/place/details/json?"
            f"place_id={pid}&fields=name,rating,user_ratings_total,reviews&language=es&key={API_KEY}"
        )
        respuesta = requests.get(url).json()
        if respuesta.get("status") != "OK":
            continue

        datos = respuesta.get("result", {})
        resenas = datos.get("reviews", [])
        texto = " ".join([r.get("text", "") for r in resenas]).lower()
        palabras = [p for p in re.findall(r'\b[a-záéíóúñ]{4,}\b', texto) if p not in STOPWORDS_ES]
        top_palabras = ", ".join([f"{w} ({c})" for w, c in Counter(palabras).most_common(10)])

        resultados.append({
            "Taller": nombre,
            "Nota Media": datos.get("rating", 0),
            "Total Reseñas": datos.get("user_ratings_total", 0),
            "Palabras Clave Frecuentes": top_palabras
        })

    df = pd.DataFrame(resultados)
    with open("analisis_competencia_talleres.md", "w", encoding="utf-8") as f:
        f.write("# Análisis de Reputación Online - Talleres\n\n")
        f.write(df.to_markdown(index=False))
    print("Análisis de reseñas exportado a analisis_competencia_talleres.md")


def generar_mapa_folium(lat_centro=37.9815, lon_centro=-0.7895, salida_html="mapa_concesionarios_alicante.html"):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM concesionarios WHERE estado = 'OPERATIONAL'", conn)
    conn.close()

    mapa = folium.Map(location=[lat_centro, lon_centro], zoom_start=11, tiles="CartoDB positron")

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
            <b>Nota Google:</b> {fila['nota_media']} ({fila['total_resenas']} reseñas)<br>
            <b>Dirección:</b> {fila['direccion']}
        </div>
        """

        folium.Marker(
            location=[fila["latitud"], fila["longitud"]],
            popup=folium.Popup(html_popup, max_width=250),
            tooltip=f"{fila['nombre']} ({marca})",
            icon=folium.Icon(color=color_pin, icon=icono, prefix="fa")
        ).add_to(mapa)

    mapa.save(salida_html)
    print(f"Mapa interactivo guardado en {salida_html}")


if __name__ == "__main__":
    # Descomenta las funciones que desees ejecutar tras configurar tu API_KEY:
    # ejecutar_censo_concesionarios()
    # generar_mapa_folium()
    pass
