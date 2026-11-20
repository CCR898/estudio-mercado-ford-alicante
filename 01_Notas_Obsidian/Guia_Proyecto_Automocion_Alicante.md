# Guía Completa y Recursos Técnicos: Estudio de Mercado Automoción (Alicante / Vega Baja)

Este documento recopila toda la guía estratégica, plantillas de prompts, scripts en Python, consultas SQL, estructura de repositorio GitHub/Obsidian y documentación comercial generada para tu investigación de mercado sobre el sector automoción en la provincia de Alicante.

---

## 1. Gestión de Cuotas y Optimización de Prompts en IA

### Estrategias para evitar límites de tokens en cuentas gratuitas
* **Usa NotebookLM para análisis extensos:** Permite subir PDFs, estudios de mercado y documentos largos para cruzar información y redactar esquemas sin agotar los límites del chat estándar.
* **Divide el flujo de trabajo por herramientas:**
  * **Perplexity:** Investigación de mercado en tiempo real con enlaces directos a fuentes (ANFAC, FACONAUTO, prensa económica).
  * **Claude:** Redacción ejecutiva y tono de consultoría.
  * **Google AI Studio:** Procesamiento de textos muy largos gracias a su amplia ventana de contexto gratuita.
* **Buenas prácticas de ahorro:** Abre un chat nuevo por cada bloque temático, pide primero el índice antes que el texto completo y edita tus mensajes anteriores en lugar de corregir en mensajes nuevos.

---

## 2. Plantillas de Prompts Optimizadas

### A. Prompt: Análisis de Competencia en el Sector Automoción
```text
Actúa como un analista de inteligencia de mercado especializado en el sector de la automoción y posventa en España. 

Tu objetivo es recopilar datos objetivos, recientes (2025-2026) y verificables sobre el siguiente competidor o grupo: [NOMBRE DE LA MARCA O CONCESIONARIO, ej: Grupo Marcos Automoción / Stellantis España / Renault].

Extrae la información siguiendo estrictamente esta estructura y reglas:

1. Cuota y Ventas: Datos de matriculaciones recientes en España, variación porcentual interanual y modelos líderes en ventas.
2. Estrategia de Producto y Precios: Cambios recientes en su catálogo (retirada de modelos, apuesta por híbridos/eléctricos, descuentos agresivos o campañas de financiación).
3. Red de Concesionarios y Posventa: Número aproximado de puntos de venta, expansión o cierre de instalaciones, y servicios clave de taller oficial o multimarca.
4. Posicionamiento Digital y Marketing: Canales principales de captación, enfoque de sus campañas actuales y reputación online (valoración media y quejas frecuentes en talleres/ventas).

Reglas de formato para optimizar la respuesta:
- Sé directo, telegráfico y usa viñetas con datos numéricos concretos.
- No incluyas introducciones, saludos ni conclusiones genéricas.
- Cita la fuente exacta (ANFAC, GANVAM, prensa económica, web corporativa) junto a cada dato relevante.
- Si un dato concreto no está disponible públicamente, indica "Dato no disponible" en lugar de especular.
```

### B. Prompt: Diagnóstico de Caída de Ventas (Concesionario Local - Caso Privado)
```text
Actúa como un consultor estratégico senior especializado en redes de concesionarios oficiales, posventa automotriz y marketing local en España.

Analiza las posibles causas de caída de ventas y los riesgos de negocio para el siguiente concesionario oficial:
- Empresa: Talleres José Martínez S.L. (Concesionario y taller oficial Ford desde 1981).
- Ubicación: Ronda Norte, 17, San Miguel de Salinas, Alicante (comarca de la Vega Baja).
- Cartera: Venta de turismos Ford (híbridos, eléctricos), comerciales, vehículos de ocasión (VO), compra de coches y taller de mantenimiento/mecánica rápida.
- Fortaleza actual: Alta reputación histórica (desde 1974) y excelentes reseñas de clientes locales.

Desarrolla un informe diagnóstico estructurado exactamente en estos 4 puntos:

1. Impacto directo de la crisis de catálogo de Ford España en este perfil de negocio:
   - Cómo afecta la eliminación de modelos económicos de alto volumen (Fiesta, Focus) y el giro hacia SUV/eléctricos más caros a un concesionario de tamaño medio en una comarca de renta media-baja como la Vega Baja.
   - Riesgos en la rotación de stock y pérdida de cuota frente a marcas asiáticas o generalistas con precios más bajos en la zona (Orihuela, Torrevieja).

2. Efecto dominó en el área de Taller y Posventa (el verdadero motor de rentabilidad):
   - Si caen las matriculaciones de coches nuevos Ford en la zona, ¿cómo y en qué plazo cae la entrada de vehículos al taller oficial para revisiones en garantía?
   - Estrategias de defensa del taller: captación de vehículos de más de 5 años, potenciación del Vehículo de Ocasión (VO) y servicios multimarca.

3. Análisis del entorno competitivo local (Vega Baja / Alicante Sur):
   - Presión de macro-grupos de concesionarios cercanos (como Grupo Marcos Automoción o grandes exposiciones en Torrevieja/Orihuela/Elche) con mayor músculo financiero y de marketing digital.
   - Oportunidad demográfica específica: cómo captar al cliente residente extranjero (británicos, nórdicos, centroeuropeos) de San Miguel de Salinas, Orihuela Costa y Villamartín.

4. Auditoría de Marketing Digital y Captación Local (Acciones rápidas):
   - Qué revisar en su web actual (talleresmartinez.es), SEO Local (Google Business Profile en varios idiomas) y embudos de venta de Vehículo de Ocasión para compensar la caída de ventas de coche nuevo.

Reglas de respuesta:
- Sé analítico, directo y orientado a negocio (sin texto de relleno ni introducciones).
- Usa viñetas cortas y lenguaje técnico del sector automoción (VO, VN, paso por taller, ticket medio, margen comercial).
- Devuelve el resultado en formato Markdown limpio para integrarlo en un informe de investigación.
```

---

## 3. Ecosistema Competitivo en Alicante y España

### Principales Grupos de Concesionarios en Alicante y Vega Baja
* **Grupo Marcos Automoción:** Gigante nacido en Orihuela con dominio multimarca en toda la provincia.
* **Mundicar:** Operador relevante en distribución oficial y posventa en la zona.
* **Grupo Borjamotor:** Fuerte presencia en Alicante/Elche; distribuye MG, Omoda, Jaecoo y marcas Stellantis (Opel, Citroën, Peugeot).
* **Grupo Serrano Automoción:** Eje Elche – Vega Baja (Torrevieja, Orihuela); controla el Grupo Volkswagen (VW, Audi, SEAT, Cupra, Škoda).
* **Grupo Sala Rodríguez:** Referente premium en Alicante, Elche y Torrevieja (Mercedes-Benz, Smart, Jaguar, Land Rover).
* **Movilbegar / Hispamóvil:** Operadores históricos en Elche y Alicante (BMW, MINI y generalistas).
* **Grupo MS Dealer:** Opera en Alicante y Elche (Mitsubishi, Suzuki, Subaru, Honda, DFSK).
* **Grupo Unione:** Distribuye Mercedes-Benz, BYD, Omoda, Jaecoo y Foton en Alicante.
* **Grupo Montalt / Vedat Mediterráneo:** Gran distribuidor de Ford en la Comunidad Valenciana.

### Principales Marcas Chinas en España
* **SAIC Motor:** MG (Morris Garage) – Amenaza directa nº 1 por volumen y precio (MG ZS, MG3, MG4).
* **BYD Auto:** BYD – Líder en eléctricos e híbridos enchufables.
* **Chery Automobile:** Omoda, Jaecoo, Lepas y Ebro.
* **Grupo Geely:** Volvo, Polestar, Lynk & Co, Zeekr, Geely, Livan.
* **Stellantis (Alianza China):** Leapmotor (integrada en concesionarios Stellantis).
* **Otros grupos:** XPeng, GWM (Ora/Wey), DFSK, SWM, EVO, DR Automobiles, Dongfeng (Voyah), Changan, GAC, BAIC.

---

## 4. Scripts en Python

### Script 1: Censo Automatizado de Concesionarios (`censo_concesionarios.py`)
```python
import requests
import pandas as pd
import sqlite3
import time

API_KEY = "TU_API_KEY_DE_GOOGLE_CLOUD"

MARCAS = [
    "Ford",
    "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "SEAT", "Cupra", "Škoda",
    "Renault", "Dacia", "Peugeot", "Citroën", "Opel", "Toyota", "Hyundai", "Kia", "Nissan",
    "MG", "BYD", "Omoda", "Jaecoo", "Ebro", "Leapmotor", "Lynk & Co", 
    "Volvo", "Polestar", "Zeekr", "XPeng", "DFSK", "SWM", "EVO", "DR Automobiles"
]

ZONAS = [
    "Orihuela", "Torrevieja", "San Miguel de Salinas", "Rojales", "Guardamar del Segura",
    "Almoradí", "Callosa de Segura", "Pilar de la Horadada", "Elche", "Alicante", "Crevillente"
]

def buscar_concesionarios(query):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "language": "es",
        "key": API_KEY
    }
    res = requests.get(url, params=params).json()
    return res.get("results", [])

registros = {}

print("Iniciando rastreo de concesionarios en Alicante y Vega Baja...")

for marca in MARCAS:
    for zona in ZONAS:
        consulta = f"Concesionario oficial {marca} en {zona}, Alicante"
        resultados = buscar_concesionarios(consulta)
        
        for lugar in resultados:
            pid = lugar.get("place_id")
            if pid not in registros:
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

conn = sqlite3.connect("mercado_automocion_alicante.db")
df.to_sql("concesionarios", conn, if_exists="replace", index=False)
conn.close()

print(f"Proceso terminado. Se han encontrado {len(df)} concesionarios únicos.")
```

### Script 2: Análisis de Reseñas y Palabras Clave (`analizar_resenas.py`)
```python
import requests
import re
from collections import Counter
import pandas as pd

API_KEY = "TU_API_KEY_DE_GOOGLE_CLOUD"

TALLERES = {
    "Concesionario Caso Estudio (Vega Baja)": "ChIJ...", 
    "Marcos Motor (Alicante/Orihuela)": "ChIJ...",
    "Mundicar": "ChIJ..."
}

STOPWORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas", "y", "o", "pero",
    "de", "del", "a", "al", "en", "con", "por", "para", "sin", "sobre",
    "que", "es", "son", "fue", "muy", "mi", "me", "te", "se", "lo", "le",
    "he", "ha", "han", "todo", "toda", "todos", "como", "más", "mas", "ya"
}

def obtener_resenas(place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,user_ratings_total,reviews&language=es&key={API_KEY}"
    respuesta = requests.get(url).json()
    if respuesta.get("status") != "OK":
        return None
    return respuesta.get("result", {})

def analizar_texto(lista_resenas):
    texto_completo = " ".join([r.get("text", "") for r in lista_resenas]).lower()
    palabras = re.findall(r'\b[a-záéíóúñ]{4,}\b', texto_completo)
    palabras_filtradas = [p for p in palabras if p not in STOPWORDS]
    return Counter(palabras_filtradas).most_common(10)

resultados = []

for nombre, pid in TALLERES.items():
    datos = obtener_resenas(pid)
    if datos:
        nota = datos.get("rating", 0)
        total = datos.get("user_ratings_total", 0)
        resenas = datos.get("reviews", [])
        top_palabras = analizar_texto(resenas)
        palabras_str = ", ".join([f"{palabra} ({cuenta})" for palabra, cuenta in top_palabras])
        
        resultados.append({
            "Taller": nombre,
            "Nota Media": nota,
            "Total Reseñas": total,
            "Palabras Clave Frecuentes": palabras_str
        })

df = pd.DataFrame(resultados)
tabla_md = df.to_markdown(index=False)

with open("analisis_competencia_talleres.md", "w", encoding="utf-8") as f:
    f.write("# Análisis de Reputación Online - Talleres Ford\n\n")
    f.write(tabla_md)
```

### Script 3: Mapa Interactivo con Folium (`mapa_competencia.py`)
```python
import sqlite3
import pandas as pd
import folium

conn = sqlite3.connect("mercado_automocion_alicante.db")
df = pd.read_sql_query("SELECT * FROM concesionarios WHERE estado = 'OPERATIONAL'", conn)
conn.close()

# Centro geográfico de estudio (San Miguel de Salinas / Vega Baja)
LAT_BASE = 37.9815
LON_BASE = -0.7895

mapa = folium.Map(location=[LAT_BASE, LON_BASE], zoom_start=11, tiles="CartoDB positron")

folium.Circle(
    location=[LAT_BASE, LON_BASE],
    radius=15000,
    color="#1f77b4",
    fill=True,
    fill_opacity=0.08,
    popup="Radio de influencia directa (15 km)"
).add_to(mapa)

folium.Marker(
    location=[LAT_BASE, LON_BASE],
    popup="<b>Área Central de Estudio</b><br>Comarca de la Vega Baja",
    tooltip="Centro Zona de Estudio",
    icon=folium.Icon(color="black", icon="star")
).add_to(mapa)

MARCAS_CHINAS = {"MG", "BYD", "Omoda", "Jaecoo", "Chery", "EVO", "DR Automobiles", "Ebro", "Leapmotor", "Lynk & Co", "XPeng", "DFSK", "SWM"}

for _, fila in df.iterrows():
    marca = fila["marca_buscada"]
    
    if marca == "Ford":
        color_pin = "blue"
        icono = "wrench"
        categoria = "Red Oficial Ford"
    elif marca in MARCAS_CHINAS:
        color_pin = "red"
        icono = "car"
        categoria = "Marca China / Emergente"
    else:
        color_pin = "cadetblue"
        icono = "info-sign"
        categoria = "Marca Tradicional"

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

mapa.save("mapa_concesionarios_alicante.html")
print("Mapa generado con éxito.")
```

---

## 5. Consultas SQL de Inteligencia de Mercado (`consultas_mercado.sql`)

```sql
-- 1. Cuota de presencia: Marcas Chinas vs. Ford vs. Tradicionales
SELECT 
    CASE 
        WHEN marca_buscada IN ('MG', 'BYD', 'Omoda', 'Jaecoo', 'Chery', 'EVO', 'DR Automobiles', 'Ebro', 'Leapmotor', 'Lynk & Co', 'XPeng', 'DFSK', 'SWM') THEN 'Marcas Chinas / Emergentes'
        WHEN marca_buscada = 'Ford' THEN 'Ford'
        ELSE 'Tradicionales Europeas/Asiáticas'
    END AS segmento,
    COUNT(DISTINCT place_id) AS total_concesionarios,
    ROUND(AVG(nota_media), 2) AS satisfaccion_media,
    SUM(total_resenas) AS volumen_resenas
FROM concesionarios
WHERE estado = 'OPERATIONAL'
GROUP BY segmento
ORDER BY total_concesionarios DESC;

-- 2. Concentración de mercado por Grupo Empresarial en Alicante
WITH ClasificacionGrupos AS (
    SELECT 
        place_id,
        nombre,
        marca_buscada,
        nota_media,
        total_resenas,
        CASE 
            WHEN LOWER(nombre) LIKE '%marcos%' THEN 'Grupo Marcos Automoción'
            WHEN LOWER(nombre) LIKE '%mundicar%' THEN 'Mundicar'
            WHEN LOWER(nombre) LIKE '%borja%' THEN 'Grupo Borjamotor'
            WHEN LOWER(nombre) LIKE '%serrano%' THEN 'Grupo Serrano Automoción'
            WHEN LOWER(nombre) LIKE '%sala%' THEN 'Grupo Sala Rodríguez'
            WHEN LOWER(nombre) LIKE '%unione%' THEN 'Grupo Unione'
            WHEN LOWER(nombre) LIKE '%ms dealer%' OR LOWER(nombre) LIKE '%autos ms%' THEN 'Grupo MS Dealer'
            WHEN LOWER(nombre) LIKE '%movilbegar%' OR LOWER(nombre) LIKE '%hispamovil%' OR LOWER(nombre) LIKE '%hispamóvil%' THEN 'Movilbegar / Hispamóvil'
            WHEN LOWER(nombre) LIKE '%vedat%' OR LOWER(nombre) LIKE '%montalt%' THEN 'Grupo Montalt / Vedat'
            ELSE 'Concesionarios Independientes / Otros'
        END AS grupo_empresarial
    FROM concesionarios
    WHERE estado = 'OPERATIONAL'
)
SELECT 
    grupo_empresarial AS "Grupo Empresarial",
    COUNT(DISTINCT place_id) AS "Puntos de Venta",
    ROUND(
        COUNT(DISTINCT place_id) * 100.0 / (SELECT COUNT(DISTINCT place_id) FROM ClasificacionGrupos), 
        2
    ) AS "Cuota Física (%)",
    ROUND(AVG(nota_media), 2) AS "Valoración Media",
    SUM(total_resenas) AS "Volumen Reseñas",
    GROUP_CONCAT(DISTINCT marca_buscada) AS "Marcas Operadas"
FROM ClasificacionGrupos
GROUP BY grupo_empresarial
ORDER BY "Puntos de Venta" DESC;
```

---

## 6. Estructura del Informe Ejecutivo (PDF) y Repositorio GitHub

### Índice Ejecutivo del Informe (PDF)
* **0. Resumen Ejecutivo:** Hallazgo principal, KPIs clave y hoja de ruta recomendada.
* **1. Metodología y Arquitectura de Datos:** Fuentes sectoriales (ANFAC, FACONAUTO) + pipeline técnico (Python, SQL, Folium).
* **2. Diagnóstico Macro (Ford España):** Retirada de modelos de volumen, brecha precio-renta e irrupción asiática.
* **3. Radiografía Competitiva (Alicante y Vega Baja):** Concentración por grupos, análisis geoespacial y benchmarking de reseñas.
* **4. Análisis de Impacto en el Concesionario Local:** Efecto dominó (VN -> Posventa) y análisis DAFO cruzado.
* **5. Plan de Acción y Estrategia Digital:** Vehículo de Ocasión (VO), fidelización >5 años, SEO Local multilingüe para residentes internacionales y optimización web.
* **6. Anexos Técnicos:** Tablas SQL y enlace al mapa interactivo.

### Archivo `.gitignore` para proteger confidencialidad
```text
*Privado*
*Talleres_Martinez*
*Jose_Martinez*
*.db
*.sqlite
*.sqlite3
resenas_brutas.csv
.env
config_local.py
*secret*
*api_key*
__pycache__/
*.py[cod]
venv/
.venv/
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.DS_Store
Thumbs.db
```

---

## 7. Plantilla de Correo Electrónico para Gerencia

**Asunto:** Estudio de mercado y propuestas estratégicas para Talleres José Martínez S.L. (Sector Automoción – Vega Baja)

**Cuerpo:**
Estimado equipo de gerencia de Talleres José Martínez S.L.:

Me pongo en contacto con ustedes tras realizar un estudio de inteligencia de mercado y análisis competitivo centrado en la evolución actual de Ford España, la presión de los grandes grupos de concesionarios en Alicante y el impacto de las nuevas marcas asiáticas en la comarca de la Vega Baja.

Como residente en la zona y especialista en Marketing Digital y Análisis de Datos, tomé la trayectoria histórica de su concesionario en San Miguel de Salinas como caso de estudio aplicado. Mi objetivo era analizar cómo un taller oficial con una reputación tan sólida puede proteger su rentabilidad y captar nuevas oportunidades ante los cambios actuales del catálogo de la marca.

Adjunto a este correo les hago llegar de forma totalmente gratuita y confidencial el **Informe Ejecutivo** resultante, donde encontrarán:
* **Diagnóstico competitivo en la Vega Baja:** Mapa de presión comercial en un radio de 20 km (macro-grupos y marcas emergentes) y comparativa de reputación online.
* **Análisis de impacto en posventa:** Cómo anticipar el efecto de la caída de matriculaciones en el paso por taller a medio plazo.
* **Plan de acción digital y local:** Propuestas concretas para potenciar el Vehículo de Ocasión (VO), fidelizar clientes fuera de garantía y captar al cliente residente internacional de San Miguel de Salinas y Orihuela Costa.

*(Nota: Por estricto respeto a su privacidad comercial, este documento es de uso exclusivo para ustedes y sus datos identificativos no han sido publicados en ningún medio).*

Quedo a su entera disposición por si desean comentar cualquiera de las conclusiones o explorar cómo implementar alguna de estas mejoras en su estrategia digital.

Un cordial saludo,

**[Tu Nombre y Apellidos]**  
Especialista en Marketing Digital & Gestión de Sistemas de Información  
Teléfono: [Tu Teléfono] | LinkedIn: [Enlace] | GitHub: [Enlace]
