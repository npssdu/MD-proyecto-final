# Proyecto Final — Minería de Datos en Python

**Curso:** 26160 Minería de Datos (RF 2) 020-81

## Requisitos Generales

El proyecto final debe desarrollarse en **Python utilizando Google Colab**.

El notebook debe contener:

- Código.
- Explicación.
- Interpretación técnica.

> No se aceptan notebooks compuestos únicamente por código.

Cada grupo deberá justificar las decisiones tomadas durante la preparación de datos:

- Variables eliminadas.
- Tratamiento de valores nulos.
- Transformación de variables.
- Escalado.
- División Train/Test.
- Selección de modelos.

El proyecto debe comparar varios modelos vistos durante el curso y seleccionar el mejor con base en:

- Métricas.
- Interpretación.
- Contexto del problema.

---

# Entregables

1. Notebook de Google Colab (`.ipynb`)
2. Informe PDF exportado desde el notebook
3. Presentación
4. Dataset o enlace al dataset

---

# Estructura Obligatoria del Notebook

## 1. Comprensión del problema

Descripción del problema y objetivo del análisis.

---

## 2. Carga del dataset

Importación y visualización inicial de los datos.

---

## 3. Diccionario de variables

Descripción de cada variable presente en el conjunto de datos.

---

## 4. Calidad de datos

Analizar:

- Valores nulos.
- Registros duplicados.
- Outliers.
- Tipos de datos.

---

## 5. Análisis Exploratorio de Datos (EDA)

Incluir:

### Histogramas

Análisis e interpretación de distribuciones.

### Boxplots

Detección e interpretación de valores atípicos.

### Conteos

Frecuencias y distribución de categorías.

### Correlaciones

Relaciones entre variables.

### Análisis multivariado

Exploración de relaciones entre múltiples variables.

> Cada gráfica debe incluir su respectiva interpretación.

---

## 6. Preparación de Datos

### Variables eliminadas

Justificación de la eliminación.

### Imputación

Tratamiento de valores faltantes.

### Encoding

Transformación de variables categóricas.

### Escalado

Normalización o estandarización de variables.

### División Train/Test

Justificación de la estrategia utilizada.

---

## 7. Modelos Supervisados

### Clasificación

Implementar y comparar:

- Regresión Logística
- K-Nearest Neighbors (KNN)
- Árbol de Decisión
- Random Forest
- Support Vector Machine (SVM)
- Naive Bayes

### Regresión

Implementar y comparar:

- Regresión Lineal
- Ridge
- Lasso
- Árbol de Decisión
- Random Forest

---

## 8. Modelos No Supervisados

Implementar y analizar:

- PCA (Análisis de Componentes Principales)
- K-Means
- Clustering Jerárquico
- DBSCAN

---

## 9. Evaluación

### Métricas de Clasificación

- Accuracy
- Precision
- Recall
- F1-Score
- Matriz de Confusión

### Métricas de Regresión

- MAE
- MSE
- RMSE
- R²

### Métricas de Clustering

- Silhouette Score
- Índice de Dunn

---

## 10. Comparación de Modelos

Comparar resultados obtenidos entre los diferentes modelos aplicados.

---

## 11. Mejor Modelo y Justificación

Seleccionar el modelo con mejor desempeño y justificar la elección.

---

## 12. Conclusiones

Presentar las conclusiones finales del proyecto, destacando:

- Hallazgos relevantes.
- Limitaciones.
- Posibles mejoras futuras.

---

# Criterios de Éxito

El proyecto debe demostrar:

- Correcta preparación de datos.
- Análisis exploratorio completo.
- Implementación de múltiples modelos.
- Comparación objetiva mediante métricas.
- Justificación técnica de decisiones.
- Interpretación adecuada de resultados.
- Conclusiones coherentes con el análisis realizado.