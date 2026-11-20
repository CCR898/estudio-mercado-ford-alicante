-- ============================================================================
-- PROYECTO: Inteligencia de Mercado y Análisis Geoespacial (Automoción Alicante)
-- ARCHIVO: consultas_mercado.sql
-- DESCRIPCIÓN: Consultas analíticas sobre la base de datos SQLite generada por
--              pipeline_mercado_automocion.py (mercado_automocion_alicante.db)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. CUOTA DE PRESENCIA: MARCAS CHINAS VS. TRADICIONALES VS. FORD
-- Objetivo: Cuantificar la irrupción de fabricantes asiáticos emergentes frente
--           a la red oficial de Ford y las marcas tradicionales en Alicante.
-- ----------------------------------------------------------------------------
SELECT 
    CASE 
        WHEN marca_buscada IN (
            'MG', 'BYD', 'Omoda', 'Jaecoo', 'Ebro', 'Leapmotor', 'Lynk & Co', 
            'Volvo', 'Polestar', 'Zeekr', 'XPeng', 'DFSK', 'SWM', 'EVO', 
            'DR Automobiles', 'Chery', 'GWM', 'Dongfeng', 'BAIC'
        ) THEN 'Marcas Chinas / Alianzas Asiáticas'
        WHEN marca_buscada = 'Ford' THEN 'Ford (Marca Objeto de Estudio)'
        ELSE 'Tradicionales Europeas / Japonesas / Coreanas'
    END AS segmento_mercado,
    COUNT(DISTINCT place_id) AS total_puntos_venta,
    ROUND(
        COUNT(DISTINCT place_id) * 100.0 / 
        (SELECT COUNT(DISTINCT place_id) FROM concesionarios WHERE estado = 'OPERATIONAL'), 
        2
    ) AS cuota_fisica_porcentaje,
    ROUND(AVG(nota_media), 2) AS valoracion_media,
    SUM(total_resenas) AS volumen_total_resenas
FROM concesionarios
WHERE estado = 'OPERATIONAL'
GROUP BY segmento_mercado
ORDER BY total_puntos_venta DESC;


-- ----------------------------------------------------------------------------
-- 2. CONCENTRACIÓN DE MERCADO POR GRUPO EMPRESARIAL (ALICANTE Y VEGA BAJA)
-- Objetivo: Medir el dominio de los macro-grupos frente a los concesionarios
--           y talleres independientes utilizando una CTE (Common Table Expression).
-- ----------------------------------------------------------------------------
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


-- ----------------------------------------------------------------------------
-- 3. BENCHMARKING DE REPUTACIÓN ONLINE POR MARCA
-- Objetivo: Detectar qué fabricantes presentan peor valoración media en posventa
--           y ventas en la provincia (oportunidad de captación por calidad).
-- ----------------------------------------------------------------------------
SELECT 
    marca_buscada AS "Marca",
    COUNT(DISTINCT place_id) AS "Concesionarios",
    ROUND(AVG(nota_media), 2) AS "Nota Media",
    SUM(total_resenas) AS "Total Reseñas",
    ROUND(SUM(total_resenas) * 1.0 / COUNT(DISTINCT place_id), 0) AS "Media Reseñas/Centro"
FROM concesionarios
WHERE estado = 'OPERATIONAL' AND nota_media > 0
GROUP BY marca_buscada
HAVING COUNT(DISTINCT place_id) >= 1
ORDER BY "Nota Media" DESC, "Total Reseñas" DESC;


-- ----------------------------------------------------------------------------
-- 4. ANÁLISIS DE PROXIMIDAD GEOGRÁFICA (RADIO DE INFLUENCIA VEGA BAJA)
-- Objetivo: Filtrar competidores directos alrededor del centro geográfico de
--           estudio (San Miguel de Salinas / Orihuela Costa: 37.9815, -0.7895)
--           usando aproximación euclidiana ajustada por latitud (válida en SQLite
--           estándar sin extensiones matemáticas).
-- ----------------------------------------------------------------------------
SELECT 
    nombre AS "Concesionario",
    marca_buscada AS "Marca",
    direccion AS "Dirección",
    nota_media AS "Nota",
    total_resenas AS "Reseñas",
    ROUND(
        SQRT(
            POWER((latitud - 37.9815) * 111.32, 2) + 
            POWER((longitud - (-0.7895)) * 111.32 * COS(RADIANS(37.9815)), 2)
        ), 
        1
    ) AS distancia_aprox_km
FROM concesionarios
WHERE estado = 'OPERATIONAL'
  AND SQRT(
        POWER((latitud - 37.9815) * 111.32, 2) + 
        POWER((longitud - (-0.7895)) * 111.32 * COS(RADIANS(37.9815)), 2)
      ) <= 25.0
ORDER BY distancia_aprox_km ASC;
