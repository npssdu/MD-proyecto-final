import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Configuración de página para interfaz investigativa médica
st.set_page_config(page_title="Sistema de Diagnóstico Oncológico Asistido", page_icon="🧬", layout="wide")

# Estilos CSS personalizados para apariencia médica
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #0056b3;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #004494;
        color: white;
    }
    .stAlert {
        border-radius: 8px;
    }
    .sidebar-content {
        font-family: 'Arial', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Título Principal
st.title("🔬 Sistema de Análisis Celular y Diagnóstico Oncológico")
st.markdown("---")

st.markdown("""
Esta herramienta de apoyo a la investigación médica utiliza modelos de Machine Learning entrenados sobre mediciones de imágenes digitalizadas de masas mamarias. 
El sistema clasifica el núcleo celular para determinar si la muestra presenta características **Benignas** o **Malignas**.
""")

# Diccionario de modelos
MODELOS_DISPONIBLES = {
    'Regresión Logística': 'modelos/lr_model.pkl',
    'K-Nearest Neighbors (KNN)': 'modelos/knn_model.pkl',
    'Árbol de Decisión': 'modelos/dt_model.pkl',
    'Random Forest': 'modelos/rf_model.pkl',
    'Support Vector Machine (SVM)': 'modelos/svm_model.pkl',
    'Naive Bayes': 'modelos/nb_model.pkl'
}

# Configuración de la barra lateral
st.sidebar.header("⚙️ Configuración del Análisis")
modelo_seleccionado = st.sidebar.selectbox("Seleccione el Modelo Predictivo:", list(MODELOS_DISPONIBLES.keys()))

st.sidebar.markdown("---")
st.sidebar.subheader("Información del Sistema")
st.sidebar.info(
    "Este sistema requiere los archivos `.pkl` generados previamente. "
    "Por favor, asegúrese de haber ejecutado el script de entrenamiento."
)

# Cargar características del dataset para inputs
# En un escenario real leeríamos las columnas guardadas en entrenamiento
# Aquí usamos la lista conocida del dataset de cáncer de mama (30 features)
features_names = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

# Inicializar inputs en session state
if 'paciente_data' not in st.session_state:
    st.session_state.paciente_data = {feat: 0.0 for feat in features_names}

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📋 Datos Clínicos (Biopsia)")
    st.markdown("Ingrese los valores morfológicos o genere un paciente de prueba.")
    
    # Botones para datos aleatorios
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🧪 Generar Muestra Tipo Benigna"):
            # Valores aproximados para tumor benigno (basados en medias de dataset)
            st.session_state.paciente_data = {feat: np.random.uniform(10, 14) if 'radius' in feat or 'perimeter' in feat else np.random.uniform(0.01, 0.1) for feat in features_names}
    with c2:
        if st.button("🦠 Generar Muestra Tipo Maligna"):
            # Valores aproximados para tumor maligno
            st.session_state.paciente_data = {feat: np.random.uniform(18, 25) if 'radius' in feat or 'perimeter' in feat else np.random.uniform(0.1, 0.3) for feat in features_names}

    st.markdown("### Valores manuales")
    # Mostrar solo 5 campos representativos para no saturar la UI, el resto se mantiene oculto pero en data
    principales = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean']
    for feat in principales:
        st.session_state.paciente_data[feat] = st.number_input(f"{feat.replace('_', ' ').title()}", value=float(st.session_state.paciente_data[feat]), format="%.4f")
    
    with st.expander("Ver todas las características..."):
        for feat in features_names:
            if feat not in principales:
                st.session_state.paciente_data[feat] = st.number_input(f"{feat}", value=float(st.session_state.paciente_data[feat]), format="%.4f")

with col2:
    st.subheader("📊 Resultados de Inferencia")
    
    archivo_modelo = MODELOS_DISPONIBLES[modelo_seleccionado]
    
    if st.button("🔬 Realizar Diagnóstico Predictivo", use_container_width=True):
        if not os.path.exists('modelos/scaler.pkl') or not os.path.exists(archivo_modelo):
            st.error("❌ Archivos de modelo o escalador no encontrados. Por favor, asegúrese de haber generado los `.pkl` en la carpeta `modelos/`.")
        else:
            try:
                # Cargar modelo y scaler
                with open('modelos/scaler.pkl', 'rb') as f:
                    scaler = pickle.load(f)
                with open(archivo_modelo, 'rb') as f:
                    modelo = pickle.load(f)
                
                # Preparar datos de entrada
                entrada = np.array([list(st.session_state.paciente_data.values())])
                entrada_scaled = scaler.transform(entrada)
                
                # Predecir
                prediccion = modelo.predict(entrada_scaled)[0]
                
                # Intento de probabilidad (no todos los modelos la soportan, ej SVM sin probability=True, aunque en train_save_model lo forzamos a True)
                try:
                    probabilidades = modelo.predict_proba(entrada_scaled)[0]
                    prob_maligno = probabilidades[1] * 100
                    prob_benigno = probabilidades[0] * 100
                except:
                    prob_maligno = None
                
                st.markdown("### Reporte Médico Automatizado")
                if prediccion == 1:
                    st.error("## ⚠️ DIAGNÓSTICO: MALIGNO (M)")
                    st.markdown("Las características de la muestra indican una alta probabilidad de malignidad celular. Se recomienda evaluación oncológica inmediata y biopsia confirmatoria.")
                else:
                    st.success("## ✅ DIAGNÓSTICO: BENIGNO (B)")
                    st.markdown("Las características de la muestra no sugieren alteraciones malignas. Se recomienda seguimiento clínico rutinario.")
                
                if prob_maligno is not None:
                    st.markdown("#### Confianza del Modelo:")
                    st.progress(int(prob_maligno))
                    st.write(f"- Probabilidad de Malignidad: **{prob_maligno:.2f}%**")
                    st.write(f"- Probabilidad de Benignidad: **{prob_benigno:.2f}%**")
                
                st.info(f"**Modelo utilizado:** {modelo_seleccionado}")
                
            except Exception as e:
                st.error(f"Ocurrió un error al procesar el diagnóstico: {e}")
