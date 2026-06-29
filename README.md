# 🧬 Proyecto Final: Minería de Datos - Predicción de Cáncer de Mama
*Universidad - Curso de Minería de Datos*

[🇬🇧 English version below](#-final-project-data-mining---breast-cancer-prediction)

## 📌 Descripción General (Español)
Este repositorio contiene el proyecto final para el curso de Minería de Datos. El objetivo principal de este proyecto es aplicar el ciclo completo de minería de datos (desde el análisis exploratorio hasta el despliegue del modelo) para predecir si una masa tumoral mamaria es **Benigna** o **Maligna**. 

Para ello, utilizamos el [Breast Cancer Wisconsin (Diagnostic) Dataset](https://www.kaggle.com/datasets/erdemtaha/cancer-data) obtenido de Kaggle.

## 🚀 ¿Qué problema soluciona?
El diagnóstico temprano y preciso del cáncer de mama salva vidas. Este proyecto soluciona el problema de clasificar características morfológicas de núcleos celulares obtenidos por biopsia, brindando una herramienta de software de apoyo clínico automatizada basada en Inteligencia Artificial. Esto ayuda a los profesionales médicos a obtener una segunda opinión probabilística rápida y confiable.

## 🛠️ ¿Qué se hizo en este proyecto?
El proyecto cumple con estrictos lineamientos académicos e incluye las siguientes etapas:

1. **Análisis Exploratorio de Datos (EDA) y Calidad de Datos:** Identificación de nulos, outliers, distribuciones (histogramas, boxplots) y análisis multivariado/correlaciones.
2. **Preparación de Datos:** Imputación, transformación, codificación de variables y escalado. División del dataset en conjuntos de entrenamiento (Train) y prueba (Test).
3. **Modelos Supervisados (Clasificación):** Entrenamiento y afinamiento de múltiples algoritmos:
   - Regresión Logística
   - K-Nearest Neighbors (KNN)
   - Árbol de Decisión
   - Random Forest
   - Support Vector Machine (SVM)
   - Naive Bayes
4. **Modelos No Supervisados:** Aplicación de técnicas de agrupamiento y reducción de dimensionalidad: PCA, K-Means, Clustering Jerárquico y DBSCAN.
5. **Evaluación y Selección de Modelos:** Comparación rigurosa utilizando Accuracy, Precision, Recall, F1-Score y Matrices de Confusión, priorizando el Recall para la clase maligna debido al contexto médico.
6. **Despliegue (App Interactiva):** Construcción de un **Sistema de Diagnóstico Oncológico Asistido** usando Streamlit (`app.py`), empaquetado en Docker, que permite realizar inferencias en tiempo real utilizando los modelos entrenados.

## 📁 Estructura Principal del Repositorio
- `Cancer_Data.csv`: Dataset original.
- `entrega-final/Notebook_Final/`: Contiene el notebook de Jupyter/Colab con el proceso de minería de datos documentado y el análisis técnico completo.
- `entrega-final/Programa_Final/`: Contiene el sistema en producción.
  - `app.py`: Interfaz de usuario interactiva (Streamlit).
  - `train_save_model.py`: Script para entrenar y guardar los modelos (`.pkl`).
  - `Dockerfile` & `requirements.txt`: Archivos para fácil contenedorización y despliegue.

## 💻 ¿Cómo ejecutar la aplicación localmente?
1. Instala las dependencias: `pip install -r entrega-final/Programa_Final/requirements.txt`
2. Navega a la carpeta del programa: `cd entrega-final/Programa_Final`
3. Ejecuta Streamlit: `streamlit run app.py`

---

<br>

# 🧬 Final Project: Data Mining - Breast Cancer Prediction
*University - Data Mining Course*

## 📌 General Description (English)
This repository contains the final project for the Data Mining course. The main objective of this project is to apply the full data mining lifecycle (from exploratory analysis to model deployment) to predict whether a breast tumor mass is **Benign** or **Malignant**.

For this, we utilized the [Breast Cancer Wisconsin (Diagnostic) Dataset](https://www.kaggle.com/datasets/erdemtaha/cancer-data) sourced from Kaggle.

## 🚀 What problem does it solve?
Early and accurate diagnosis of breast cancer saves lives. This project solves the problem of classifying morphological features of cell nuclei obtained from biopsies, providing an automated AI-based clinical support software tool. This assists medical professionals in getting a fast and reliable probabilistic second opinion.

## 🛠️ What was done in this project?
The project adheres to strict academic guidelines and includes the following stages:

1. **Exploratory Data Analysis (EDA) and Data Quality:** Identification of missing values, outliers, distributions (histograms, boxplots), and multivariate/correlation analysis.
2. **Data Preparation:** Imputation, transformation, feature encoding, and scaling. Splitting the dataset into Training and Testing sets.
3. **Supervised Learning Models (Classification):** Training and tuning of multiple algorithms:
   - Logistic Regression
   - K-Nearest Neighbors (KNN)
   - Decision Tree
   - Random Forest
   - Support Vector Machine (SVM)
   - Naive Bayes
4. **Unsupervised Learning Models:** Application of clustering and dimensionality reduction techniques: PCA, K-Means, Hierarchical Clustering, and DBSCAN.
5. **Model Evaluation & Selection:** Rigorous comparison using Accuracy, Precision, Recall, F1-Score, and Confusion Matrices, prioritizing Recall for the malignant class given the medical context.
6. **Deployment (Interactive App):** Construction of an **Assisted Oncology Diagnostic System** using Streamlit (`app.py`), containerized with Docker, which allows real-time inferences using the trained models.

## 📁 Main Repository Structure
- `Cancer_Data.csv`: Original dataset.
- `entrega-final/Notebook_Final/`: Contains the Jupyter/Colab notebook with the fully documented data mining process and technical analysis.
- `entrega-final/Programa_Final/`: Contains the production system.
  - `app.py`: Interactive user interface (Streamlit).
  - `train_save_model.py`: Script to train and save the models (`.pkl`).
  - `Dockerfile` & `requirements.txt`: Files for easy containerization and deployment.

## 💻 How to run the application locally?
1. Install dependencies: `pip install -r entrega-final/Programa_Final/requirements.txt`
2. Navigate to the program folder: `cd entrega-final/Programa_Final`
3. Run Streamlit: `streamlit run app.py`
