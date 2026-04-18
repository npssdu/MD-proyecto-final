# Temas incluidos para la Primera Entrega del PROYECTO FINAL

## Temas del Análisis Exploratorio de Datos (EDA)

### 1) Contexto y planteamiento
- Introducción:
	- Contexto del trabajo de primer corte en Minería de Datos.
	- Uso del conjunto Cancer_Data.csv como base del análisis.
- Comprensión del problema:
	- Problema abordado: diferenciación entre diagnósticos benignos (B) y malignos (M).
	- Decisiones que se pueden apoyar con el análisis.
	- Usuarios objetivo del análisis (ámbito médico, investigación y gestión).
	- Importancia del problema y riesgos de interpretación.
	- Preguntas guía del bloque.

### 2) Comprensión del dataset
- Fuente del dataset (Kaggle).
- Descripción general del conjunto de datos.
- Diccionario de variables del dataset.
- Tipos de variables (categóricas y numéricas).
- Revisión de faltantes y tamaño del dataset.
- Sesgo/desbalance de clases.
- Preguntas guía del bloque.

### 3) Limpieza y preparación de datos
- Verificación de valores nulos.
- Verificación de duplicados (filas e identificador).
- Eliminación de columna identificadora para análisis/modelado.
- Codificación de la variable objetivo a formato numérico.
- Justificación de las decisiones de limpieza y transformación.
- Impacto potencial de decisiones de preparación en resultados.
- Preguntas guía del bloque.

### 4) Exploración univariada y bivariada
- Descripción del dataset para el EDA.
- Comportamiento de variables por diagnóstico.
- Análisis de área media (area_mean).
- Análisis de concavidad y puntos cóncavos (concavity_mean y concave points_mean).
- Análisis de compacidad media (compactness_mean).
- Análisis de textura media (texture_mean).
- Análisis conjunto de suavidad y simetría.

### 5) Relaciones multivariadas
- Relaciones entre variables.
- Matriz de correlación.
- Dispersión de área frente a variables de forma.
- Visualización global mediante gráfico de pares.

### 6) Interpretación y hallazgos
- Capacidad discriminativa de variables.
- Hallazgos principales del análisis.
- Nota clínica de interpretación.
- Patrones encontrados.
- Variables de mayor influencia.

### 7) Conclusiones y cierre
- Resumen y conclusiones del EDA.
- Conclusiones para apoyo a toma de decisiones.
- Siguientes pasos del proyecto.

### 8) Elementos complementarios
- Glosario.
- Preguntas guía integradas a lo largo del documento.

## 9. Temas a agregar en la primera entrega:
- Significado de entrenar un modelo y objetivo de generalización.
- Diferencia entre overfitting y underfitting.
- División de datos en train, validation y test (con estratificación).
- Riesgo de data leakage y ejemplos comunes (escalado/imputación antes de dividir, variables derivadas del target).
- Construcción de un modelo base (baseline) con Regresión Logística.
- Uso de pipeline de preprocesamiento + modelo (escalado y entrenamiento integrado).
- Predicción sobre test y análisis con matriz de confusión.
- Métricas de clasificación a reportar e interpretar:
	- Accuracy
	- Precision
	- Recall
	- F1-score
- Reporte de clasificación y comparación de desempeño entre conjuntos (train vs test).
- Discusión orientada al problema: selección de métrica según contexto (ej. medicina prioriza recall).
- Ejercicio de sensibilidad experimental (cambiar proporciones de partición y comparar métricas).
- Cierre metodológico y conexión con siguientes modelos (profundización en RL y Árboles de Decisión).
