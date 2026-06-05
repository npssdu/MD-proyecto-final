import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Cargar dataset y limpiar espacios/comillas en columnas
df = pd.read_csv('Cancer_Data.csv')
df.columns = df.columns.str.strip().str.replace('"', '').str.replace("'", "")

# Limpieza de datos exactamente como en el notebook
if 'Unnamed: 32' in df.columns:
    df.drop('Unnamed: 32', axis=1, inplace=True)
if 'id' in df.columns:
    df.drop('id', axis=1, inplace=True)

# Mapear diagnóstico: M=1, B=0, asegurando quitar espacios y comillas
df['diagnosis'] = df['diagnosis'].astype(str).str.replace('"', '').str.replace("'", "").str.strip().map({'M': 1, 'B': 0})

# Variables dependientes e independientes
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

# Separar en conjunto de entrenamiento y prueba (no estrictamente necesario para guardar el modelo final,
# pero es buena práctica para asegurar consistencia; aquí entrenamos el modelo final con todo el dataset o X_train)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalado
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test) # Opcional si solo queremos guardar

# Crear directorio de modelos si no existe
os.makedirs('modelos', exist_ok=True)

# Guardar el scaler
with open('modelos/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Diccionario de modelos
modelos = {
    'lr_model.pkl': LogisticRegression(random_state=42, max_iter=1000),
    'knn_model.pkl': KNeighborsClassifier(n_neighbors=5),
    'dt_model.pkl': DecisionTreeClassifier(random_state=42),
    'rf_model.pkl': RandomForestClassifier(random_state=42, n_estimators=100),
    'svm_model.pkl': SVC(random_state=42, probability=True),
    'nb_model.pkl': GaussianNB()
}

# Entrenar y guardar cada modelo
for nombre_archivo, modelo in modelos.items():
    modelo.fit(X_train_scaled, y_train)
    ruta_guardado = os.path.join('modelos', nombre_archivo)
    with open(ruta_guardado, 'wb') as f:
        pickle.dump(modelo, f)
    print(f'Guardado exitosamente: {ruta_guardado}')

print('Proceso de entrenamiento y guardado finalizado.')
