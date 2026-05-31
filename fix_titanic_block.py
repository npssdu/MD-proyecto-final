import json
from pathlib import Path


path = Path(r"C:\Users\andru\Documents\2026-I (S10)\Mineria de Datos\Proyecto Final\entrega-final\MD_Proyecto_Final_Completo.ipynb")

with path.open("r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb["cells"]


def set_cell(i, text):
    cells[i]["source"] = text.strip() + "\n"
    if cells[i]["cell_type"] == "code":
        cells[i]["execution_count"] = None
        cells[i]["outputs"] = []


set_cell(78, r"""
# Mineria de Datos - Random Forest con Comparacion de Modelos

Este bloque compara **Random Forest** contra modelos supervisados trabajados previamente:

1. Regresion logistica.
2. KNN.
3. Arbol de decision.
4. Random Forest.

Usaremos el dataset **Cancer_Data.csv** para mantener continuidad.

## Objetivo general

Comprender cuando Random Forest puede ser mas conveniente que un arbol individual, KNN o regresion logistica.

## Pregunta central

> ¿Que modelo clasifica mejor el diagnostico en Cancer_Data.csv y cual conviene usar segun desempeno, interpretabilidad y robustez?
""")

set_cell(82, r"""
# 3. Carga del dataset Cancer_Data.csv

La variable objetivo es `diagnosis`:

- `B`: tumor benigno.
- `M`: tumor maligno.
""")

set_cell(83, r"""
from pathlib import Path

data_path = Path("Cancer_Data.csv")
if not data_path.exists():
    data_path = Path("../Cancer_Data.csv")

df = pd.read_csv(data_path)
df.columns = df.columns.str.replace('"', '', regex=False).str.strip()
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
df = df.dropna(axis=1, how="all")

print("Archivo usado:", data_path)
print("Dimensiones:", df.shape)
df.head()
""")

set_cell(87, r"""
# 5. Variable objetivo

Revisamos cuantos registros son benignos y cuantos son malignos. Esto es importante porque un desbalance fuerte puede hacer que el accuracy sea enganoso.
""")

set_cell(88, r"""
conteo = df["diagnosis"].value_counts().reindex(["B", "M"])
porcentaje = df["diagnosis"].value_counts(normalize=True).reindex(["B", "M"]) * 100

resumen_target = pd.DataFrame({
    "diagnosis": conteo.index,
    "descripcion": ["Benigno", "Maligno"],
    "conteo": conteo.values,
    "porcentaje": porcentaje.round(2).values
})

resumen_target
""")

set_cell(89, r"""
plt.figure(figsize=(6,4))
plt.bar(resumen_target["descripcion"], resumen_target["conteo"])
plt.title("Distribucion del diagnostico")
plt.xlabel("Diagnostico")
plt.ylabel("Numero de registros")
plt.show()
""")

set_cell(90, r"""
# 6. Exploracion: diagnostico y variables clinicas

Estas variables permiten revisar si algunas mediciones del tumor cambian claramente entre casos benignos y malignos.
""")

set_cell(91, r"""
variables_explorar = ["radius_mean", "area_mean", "concavity_mean", "concave points_mean"]
resumen_por_diagnostico = df.groupby("diagnosis")[variables_explorar].mean().round(3)
resumen_por_diagnostico
""")

set_cell(92, r"""
resumen_por_diagnostico.T.plot(kind="bar", figsize=(9,4))
plt.title("Promedio de variables clinicas por diagnostico")
plt.xlabel("Variable")
plt.ylabel("Promedio")
plt.xticks(rotation=25)
plt.show()
""")

set_cell(93, r"""
df_bins = df.copy()
df_bins["area_mean_grupo"] = pd.qcut(df_bins["area_mean"], q=3, labels=["Baja", "Media", "Alta"])
tabla_area = pd.crosstab(df_bins["area_mean_grupo"], df_bins["diagnosis"], normalize="index") * 100
tabla_area.columns = ["Benigno (%)", "Maligno (%)"]
tabla_area.round(2)
""")

set_cell(94, r"""
tabla_area.plot(kind="bar", figsize=(7,4))
plt.title("Diagnostico segun grupo de area_mean")
plt.xlabel("Grupo de area_mean")
plt.ylabel("Porcentaje")
plt.xticks(rotation=0)
plt.show()
""")

set_cell(95, r"""
# 7. Preparacion de datos

Variables usadas:

- Todas las mediciones numericas del tumor.
- Se elimina `id` porque es un identificador y no una caracteristica clinica.
- Se elimina cualquier columna completamente vacia.

Tratamiento:

- `diagnosis` se codifica como 0 = benigno y 1 = maligno.
- Las variables predictoras son numericas.
- El escalado se aplica dentro de los modelos que lo requieren, usando `Pipeline` para evitar data leakage.
""")

set_cell(96, r"""
df_model = df.copy()

if "id" in df_model.columns:
    df_model = df_model.drop(columns=["id"])

df_model = df_model.dropna(axis=1, how="all")
df_model["diagnosis"] = df_model["diagnosis"].map({"B": 0, "M": 1})

for col in df_model.columns:
    if col != "diagnosis":
        df_model[col] = pd.to_numeric(df_model[col], errors="coerce")

df_model = df_model.fillna(df_model.median(numeric_only=True))

print("Dimensiones:", df_model.shape)
df_model.head()
""")

set_cell(99, r"""
X = df_model.drop(columns=["diagnosis"])
y = df_model["diagnosis"]

print("X:", X.shape)
print("y:", y.shape)
print("Variables:", list(X.columns))
""")

set_cell(105, r"""
modelo_logistica = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000, random_state=42))
])

modelo_logistica.fit(X_train, y_train)
pred_logistica = modelo_logistica.predict(X_test)

print(classification_report(y_test, pred_logistica, target_names=["Benigno", "Maligno"]))
""")

set_cell(107, r"""
modelo_knn = Pipeline([
    ("scaler", StandardScaler()),
    ("model", KNeighborsClassifier(n_neighbors=5))
])

modelo_knn.fit(X_train, y_train)
pred_knn = modelo_knn.predict(X_test)

print(classification_report(y_test, pred_knn, target_names=["Benigno", "Maligno"]))
""")

set_cell(109, r"""
modelo_arbol = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

modelo_arbol.fit(X_train, y_train)
pred_arbol = modelo_arbol.predict(X_test)

print(classification_report(y_test, pred_arbol, target_names=["Benigno", "Maligno"]))
""")

set_cell(111, r"""
plt.figure(figsize=(22, 10))
plot_tree(
    modelo_arbol,
    feature_names=X.columns,
    class_names=["Benigno", "Maligno"],
    filled=True,
    rounded=True,
    fontsize=9
)
plt.title("Arbol de decision - Cancer_Data.csv")
plt.show()
""")

set_cell(113, r"""
modelo_rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42
)

modelo_rf.fit(X_train, y_train)
pred_rf = modelo_rf.predict(X_test)

print(classification_report(y_test, pred_rf, target_names=["Benigno", "Maligno"]))
""")

with path.open("w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Converted inherited Titanic block to Cancer_Data.csv")
