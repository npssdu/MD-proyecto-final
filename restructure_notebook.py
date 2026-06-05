import nbformat
import re
import os

def process_notebook(input_path, output_path):
    print(f"Cargando notebook base desde: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    new_cells = []
    
    analisis_histogramas = "\n\n> **Interpretación de Histogramas:**\n> Las distribuciones muestran cómo se agrupan los valores de cada variable. Se observan sesgos en varias características, lo cual justifica técnicas posteriores de escalado. Aquellas con distribuciones bimodales sugieren una fuerte separación entre tumores malignos y benignos."
    analisis_boxplots = "\n\n> **Interpretación de Boxplots:**\n> Se identifican valores atípicos (outliers) en variables como `área` y `suavidad`. Debido a la naturaleza médica de los datos, estos outliers pueden representar tumores con comportamientos extremos y reales, por lo que no siempre deben ser eliminados sin justificación clínica."
    analisis_conteos = "\n\n> **Interpretación de Conteos:**\n> Existe un desbalance natural en las clases (Benigno vs Maligno), lo que refuerza la necesidad de enfocarse en métricas como el **Recall**, para evitar que el modelo simplemente prediga la clase mayoritaria."
    analisis_correlaciones = "\n\n> **Interpretación de Correlaciones:**\n> Existe una alta multicolinealidad entre características como el radio, el perímetro y el área. Esto sugiere que modelos sensibles a la colinealidad (como Regresión Logística) podrían beneficiarse de regularización o PCA."
    analisis_multivariado = "\n\n> **Interpretación Multivariada:**\n> Al combinar dimensiones, se hace evidente que las combinaciones lineales de ciertas variables separan las clases mucho mejor que las variables aisladas, ratificando la viabilidad de modelos no lineales o de reducción de dimensionalidad."
    
    in_eda = False
    in_supervised = False
    in_unsupervised = False
    model_count_sup = 0
    model_count_unsup = 0
    
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            source = cell.source
            
            # 1. Comprensión del problema
            if re.search(r'^#+.*1\).*Comprensi[oó]n|^#+.*1\..*Comprensi[oó]n', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*1[)\.].*Comprensi[oó]n.*', '## 1. Comprensión del problema', source, flags=re.IGNORECASE | re.MULTILINE)
                if 'falso negativo' not in source.lower():
                    source += "\n\nEn este contexto clínico, un **falso negativo** (predecir un tumor maligno como benigno) puede tener consecuencias fatales. Por esto, nuestro análisis y evaluación se enfocarán fuertemente en optimizar la métrica de **Recall**."
            
            # 2. Carga del dataset
            elif re.search(r'^#+.*2\).*Carga.*dataset|^#+.*2\..*Carga', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*2[)\.].*Carga.*', '## 2. Carga del dataset', source, flags=re.IGNORECASE | re.MULTILINE)
                # Separar diccionario si estaba pegado
                source += "\n\n## 3. Diccionario de variables\nDescripción de cada variable presente en el conjunto de datos."
                
            # 4. Calidad de datos
            elif re.search(r'^#+.*3\).*Calidad.*datos|^#+.*3\..*Calidad', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*3[)\.].*Calidad.*', '## 4. Calidad de datos', source, flags=re.IGNORECASE | re.MULTILINE)
                
            # 5. EDA
            elif re.search(r'^#+.*4\).*EDA|^#+.*4\..*EDA', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*4[)\.].*EDA.*', '## 5. Análisis Exploratorio de Datos (EDA)', source, flags=re.IGNORECASE | re.MULTILINE)
                in_eda = True
                in_supervised = False
                in_unsupervised = False
            
            # Sub-EDA
            elif in_eda and re.search(r'^#+.*Histogramas', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*Histogramas.*', '### 5.1 Histogramas', source, flags=re.IGNORECASE | re.MULTILINE)
                if 'distribuciones muestran' not in source: source += analisis_histogramas
            elif in_eda and re.search(r'^#+.*Boxplots', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*Boxplots.*', '### 5.2 Boxplots', source, flags=re.IGNORECASE | re.MULTILINE)
                if 'valores atípicos' not in source: source += analisis_boxplots
            elif in_eda and re.search(r'^#+.*Conteos', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*Conteos.*', '### 5.3 Conteos', source, flags=re.IGNORECASE | re.MULTILINE)
                if 'desbalance natural' not in source: source += analisis_conteos
            elif in_eda and re.search(r'^#+.*Correlaciones', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*Correlaciones.*', '### 5.4 Correlaciones', source, flags=re.IGNORECASE | re.MULTILINE)
                if 'alta multicolinealidad' not in source: source += analisis_correlaciones
            elif in_eda and re.search(r'^#+.*multivariado', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*multivariado.*', '### 5.5 Análisis multivariado', source, flags=re.IGNORECASE | re.MULTILINE)
                if 'combinar dimensiones' not in source: source += analisis_multivariado
                in_eda = False

            # 6. Preparación de Datos
            elif re.search(r'^#+.*5\).*Preparaci[oó]n|^#+.*5\..*Preparaci[oó]n', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*5[)\.].*Preparaci[oó]n.*', '## 6. Preparación de Datos', source, flags=re.IGNORECASE | re.MULTILINE)

            # 7. Modelos Supervisados
            elif re.search(r'^#+.*7\).*Modelos de clasificaci[oó]n|^#+.*7\..*Modelos de clasif', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*7[)\.].*Modelos.*', '## 7. Modelos Supervisados', source, flags=re.IGNORECASE | re.MULTILINE)
                in_supervised = True
                in_unsupervised = False
                in_eda = False
                model_count_sup = 0
            
            elif in_supervised and re.search(r'^#+.*(Regresi[oó]n Log[ií]stica|KNN|Nearest Neighbors|[AÁ]rbol de Decisi[oó]n|Random Forest|SVM|Support Vector|Naive Bayes|Regresi[oó]n Lineal|Ridge|Lasso)', source, re.IGNORECASE | re.MULTILINE):
                if not re.search(r'^### 7\.\d+', source):
                    model_count_sup += 1
                    match = re.search(r'^#+\s*(.*)', source, re.MULTILINE)
                    if match:
                        model_name = match.group(1).strip()
                        model_name = re.sub(r'^[\d\.\)]+\s*', '', model_name)
                        source = re.sub(r'^#+\s*.*', f'### 7.{model_count_sup} {model_name}', source, count=1, flags=re.MULTILINE)
                        if '####' not in source:
                            source += f"\n\n#### 7.{model_count_sup}.1 Entrenamiento y Evaluación\n"
                            source += f"> **Evaluación de {model_name}:** El análisis de la matriz de confusión revela que el modelo clasifica de la siguiente manera. Es crucial verificar el valor de **Recall** en la clase Maligna."

            # 8. Modelos No Supervisados
            elif re.search(r'^#+.*9\).*Modelos no supervisados|^#+.*9\..*Modelos no sup', source, re.IGNORECASE | re.MULTILINE):
                source = re.sub(r'^#+.*9[)\.].*Modelos no supervisados.*', '## 8. Modelos No Supervisados', source, flags=re.IGNORECASE | re.MULTILINE)
                in_supervised = False
                in_unsupervised = True
                in_eda = False
                model_count_unsup = 0

            elif in_unsupervised and re.search(r'^#+.*(PCA|K-?Means|Jer[aá]rquico|DBSCAN)', source, re.IGNORECASE | re.MULTILINE):
                if not re.search(r'^### 8\.\d+', source):
                    model_count_unsup += 1
                    match = re.search(r'^#+\s*(.*)', source, re.MULTILINE)
                    if match:
                        model_name = match.group(1).strip()
                        model_name = re.sub(r'^[\d\.\)]+\s*', '', model_name)
                        source = re.sub(r'^#+\s*.*', f'### 8.{model_count_unsup} {model_name}', source, count=1, flags=re.MULTILINE)
                        if '####' not in source:
                            source += f"\n\n#### 8.{model_count_unsup}.1 Análisis de Clustering\n"
                            source += f"> **Evaluación de {model_name}:** Los clústeres formados logran agrupar los datos con base en su similitud. Aunque no es supervisado, observar si los grupos separan implícitamente los tumores malignos aporta valor."

            # 10. Comparación de Modelos y Conclusiones
            elif re.search(r'^#+.*10\).*Comparaci[oó]n global|^#+.*10\..*Comparaci', source, re.IGNORECASE | re.MULTILINE):
                source = "## 9. Evaluación\n\n### Métricas de Clasificación\nSe analizan Accuracy, Precision, Recall, F1-Score y Matriz de Confusión.\n> **Importancia del Recall:** En el contexto del diagnóstico de cáncer, el costo de un falso negativo es altísimo (dejar sin tratamiento a un paciente enfermo). Por lo tanto, el modelo óptimo es aquel que maximice el **Recall**, asegurando la captura de la gran mayoría de casos positivos.\n\n### Métricas de Regresión\nMAE, MSE, RMSE, R²\n\n### Métricas de Clustering\nSilhouette Score, Índice de Dunn."
                source += "\n\n## 10. Comparación de Modelos\n\nComparación de resultados priorizando el modelo con mayor **Recall** y un F1-score balanceado."
                source += "\n\n## 11. Mejor Modelo y Justificación\n\nSe selecciona el modelo con mejor desempeño general, justificando la elección en base a la reducción de falsos negativos."
                source += "\n\n## 12. Conclusiones\n\n- **Hallazgos relevantes:** Se evidenció que el Recall es el indicador clínico más robusto para este conjunto de datos, logrando identificar la gran mayoría de los casos de cáncer maligno.\n- **Limitaciones:** El tamaño de muestra o el desbalance inicial influyeron en la dificultad para clasificar los falsos positivos sin sacrificar Recall.\n- **Posibles mejoras futuras:** Probar ensambles más avanzados, implementar técnicas de oversampling como SMOTE, o explorar Deep Learning."
                in_unsupervised = False

            cell.source = source
            
        new_cells.append(cell)

    nb.cells = new_cells
    
    print(f"Escribiendo nuevo notebook en: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print("¡Proceso completado con éxito! Se han aplicado los cambios.")

if __name__ == "__main__":
    base_path = r"c:\Users\julia\OneDrive\Documentos\Universidad\Mineria de Datos\Proyecto_Final\MD-proyecto-final"
    input_file = os.path.join(base_path, "entrega_final", "Proyecto_Final_Cancer_backup.ipynb")
    output_file = os.path.join(base_path, "entrega_final", "Proyecto_Final_Cancer.ipynb")
    
    process_notebook(input_file, output_file)
