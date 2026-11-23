# 🚗 Inteligencia de Mercado y Análisis Geoespacial: Sector Automoción en Alicante

**Estudio estratégico sobre el impacto de la reestructuración de Ford España, la concentración de macro-grupos y el auge de marcas asiáticas en la red oficial y posventa de la provincia de Alicante (Comarca de la Vega Baja).**

> 🔒 *Nota de confidencialidad: Los datos identificativos del concesionario oficial analizado como caso de estudio aplicado han sido anonimizados para proteger su privacidad comercial. Todos los datos de mercado, red de competencia y reputación pública proceden de fuentes abiertas y APIs oficiales.*

---

## 🎯 Objetivo del Proyecto
Analizar las causas estructurales de la caída de matriculaciones de **Ford España** y modelar su efecto dominó sobre la rentabilidad de los concesionarios independientes y talleres oficiales en el sur de la provincia de Alicante, proponiendo una hoja de ruta de **Marketing Digital y Posventa** basada en datos.

### Preguntas clave resueltas:
1. ¿Cómo afecta la retirada de modelos de volumen (Fiesta, Focus) y el giro hacia SUV/eléctricos a la demanda real en comarcas de renta media como la Vega Baja?
2. ¿Cuál es el grado de concentración territorial de los grandes grupos (*Grupo Marcos Automoción*, *Mundicar*) y qué cuota física han ganado las marcas chinas (*MG, BYD, Omoda/Jaecoo*)?
3. ¿Cómo blindar la rentabilidad del área de taller (posventa) mediante estrategias de SEO Local, vehículo de ocasión (VO) y captación del residente internacional?

---

## 🛠️ Stack Tecnológico y Metodología
Este proyecto combina investigación de mercado tradicional (informes **ANFAC**, **FACONAUTO** y datos demográficos) con herramientas propias de extracción y análisis de datos:

* **Extracción de Datos (Python + Google Places API):** Automatización del censo de concesionarios oficiales en Alicante y la Vega Baja (`pipeline_mercado_automocion.py`).
* **Modelado y Análisis (SQL / SQLite):** Consultas relacionales para calcular cuotas de presencia por marca, concentración por grupo empresarial y radios de competencia (`consultas_mercado.sql`).
* **Procesamiento de Lenguaje Natural básico (Python):** Análisis de frecuencia de palabras clave y sentimiento en reseñas públicas de clientes.
* **Visualización Geoespacial (Folium):** Mapa interactivo en HTML para visualizar la densidad de puntos de venta y áreas de influencia.
* **Gestión del Conocimiento (Obsidian + Markdown):** Documentación estructurada mediante enlaces bidireccionales y exportación ejecutiva a PDF.

---

## 🗺️ Entregable Interactivo
👉 **[[Explorar Mapa Interactivo de Concesionarios en Vivo (GitHub Pages)](https://ccr898.github.io/estudio-mercado-ford-alicante/04_Entregables_Visuales/mapa_concesionarios_alicante.html)](https://ccr898.github.io/estudio-mercado-ford-alicante/04_Entregables_Visuales/mapa_concesionarios_alicante.html)**  
*(Sustituye `CCR898` por tu nombre de usuario de GitHub tras activar GitHub Pages).*

---

## 📊 Principales Hallazgos (Resumen Ejecutivo)
* **Efecto Dominó (VN ➔ Posventa):** La caída en la venta de vehículo nuevo (VN) reduce a 24 meses vista el parque móvil en garantía oficial, obligando a los talleres independientes a pivotar hacia el mantenimiento de vehículos de más de 5 años y el servicio multimarca.
* **Presión Competitiva en Polígonos Costeros:** El análisis geoespacial demuestra una fuerte concentración de puntos de venta de marcas emergentes asiáticas y macro-grupos en los ejes de **Torrevieja, Orihuela y Elche**, generando fuga de clientes desde los municipios de interior.
* **Oportunidad Demográfica (Nicho Internacional):** La alta densidad de residentes europeos en la Vega Baja representa un segmento de alto valor poco explotado digitalmente por los talleres tradicionales (oportunidad en SEO Local multilingüe y campañas hiperlocalizadas).

---

## 📂 Estructura del Repositorio

```text
📁 estudio-mercado-ford-alicante/
├── 📄 README.md                        # Documentación principal del proyecto
├── 📄 Informe_Ejecutivo_Publico.pdf    # Versión anonimizada del informe de consultoría
├── 📁 01_Notas_Obsidian/               # Síntesis de investigación en formato Markdown
├── 📁 02_Scripts_Python/               # Scripts de extracción, NLP y generación de mapas
├── 📁 03_Datos_y_SQL/                  # Consultas SQL y dataset público anonimizado
└── 📁 04_Entregables_Visuales/         # Mapa interactivo (Folium HTML) y gráficos
```

---

## 🚀 Cómo reproducir este proyecto en local

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/CCR898/estudio-mercado-ford-alicante.git
   cd estudio-mercado-ford-alicante
   ```
