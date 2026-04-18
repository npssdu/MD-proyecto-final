# Proyecto Final - Dataset de Cancer de Mama

## Descripcion general
Este repositorio trabaja con el dataset **Cancer Data** de Kaggle:
- Fuente: https://www.kaggle.com/datasets/erdemtaha/cancer-data
- Archivo local usado: `Cancer_Data.csv`

El dataset corresponde a una version del **Breast Cancer Wisconsin (Diagnostic) Dataset (WDBC)**, ampliamente usado en tareas de clasificacion binaria para apoyar diagnostico de cancer de mama a partir de caracteristicas extraidas de imagenes.

Cada fila representa una muestra/paciente y contiene:
- Un identificador unico (`id`)
- La etiqueta diagnostica (`diagnosis`)
- Variables numericas derivadas de caracteristicas morfologicas de la masa tumoral

## Estado actual del proyecto
En este workspace ya se encuentran:
- `Cancer_Data.csv` (dataset)
- `MD_Trabajo_Primer_Corte.ipynb` (primer informe/notebook)
- `Informe-Trabajo-Primer-Corte.pdf` (reporte generado)

## Estructura del dataset
A partir del archivo local cargado en este repositorio:
- Filas: **569**
- Columnas: **32**
- Archivo: **CSV**
- Tamano reportado en Kaggle: aprox. **125.2 kB**

### Variable objetivo
`diagnosis`:
- `M`: Maligno
- `B`: Benigno

Distribucion de clases en el CSV local:
- `B` (Benigno): **357** (~62.74%)
- `M` (Maligno): **212** (~37.26%)

## Diccionario de variables

### 1) Identificacion y etiqueta
- `id`: identificador unico de la observacion
- `diagnosis`: clase objetivo (M/B)

### 2) Variables de medias (`*_mean`)
- `radius_mean`
- `texture_mean`
- `perimeter_mean`
- `area_mean`
- `smoothness_mean`
- `compactness_mean`
- `concavity_mean`
- `concave points_mean`
- `symmetry_mean`
- `fractal_dimension_mean`

### 3) Variables de error estandar (`*_se`)
- `radius_se`
- `texture_se`
- `perimeter_se`
- `area_se`
- `smoothness_se`
- `compactness_se`
- `concavity_se`
- `concave points_se`
- `symmetry_se`
- `fractal_dimension_se`

### 4) Variables de peor caso (`*_worst`)
- `radius_worst`
- `texture_worst`
- `perimeter_worst`
- `area_worst`
- `smoothness_worst`
- `compactness_worst`
- `concavity_worst`
- `concave points_worst`
- `symmetry_worst`
- `fractal_dimension_worst`

## Calidad de datos observada en este CSV
Revision rapida del archivo local:
- No se detectaron valores faltantes vacios por columna
- Todas las variables predictoras son numericas continuas
- `diagnosis` es categorica binaria

## Fuente original y trazabilidad
El autor del dataset en Kaggle indica que este conjunto deriva del WDBC, con referencias a:
- UCI Machine Learning Repository (Breast Cancer Wisconsin - Diagnostic)
- Dataset relacionado en Kaggle (`uciml/breast-cancer-wisconsin-data`)

Por trazabilidad academica, en reportes y presentaciones conviene citar:
1. El dataset utilizado en Kaggle (erdemtaha/cancer-data)
2. La fuente base WDBC/UCI

## Licencia y uso
En Kaggle, este dataset aparece con licencia:
- **CC BY-NC-SA 4.0**
- Link: https://creativecommons.org/licenses/by-nc-sa/4.0/

Implicaciones practicas:
- Requiere atribucion
- Uso no comercial
- Compartir bajo la misma licencia cuando aplique

## Recomendaciones para analisis/modelado
Para continuar despues del primer informe, se sugiere:
1. Separar conjunto de entrenamiento/prueba con estratificacion por `diagnosis`.
2. Estandarizar variables numericas antes de modelos sensibles a escala (KNN, SVM, Regresion Logistica).
3. Comparar modelos base: Regresion Logistica, KNN, SVM, Random Forest, XGBoost.
4. Usar validacion cruzada y metricas mas alla de accuracy: precision, recall, F1, ROC-AUC.
5. Priorizar sensibilidad/recall de la clase maligna (`M`) segun el objetivo clinico.
6. Analizar importancia de variables y correlaciones para interpretabilidad.

## Consideraciones tecnicas
- Algunas columnas contienen espacios en su nombre (por ejemplo `concave points_mean`).
  - Si se trabaja con pandas, puede ser util renombrar columnas (ej. reemplazar espacios por `_`) para facilitar consultas y pipelines.

## Referencias
- Dataset Kaggle: https://www.kaggle.com/datasets/erdemtaha/cancer-data
- UCI WDBC: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29
- Licencia CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/
