import pandas as pd
import openpyxl
import warnings
import matplotlib.pyplot as plt
import numpy as np

# Para que no salga advertencia
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

df = pd.read_excel("excel/Medals.xlsx", engine="openpyxl")

df.rename(columns={"Team/NOC": "Country"}, inplace=True)
df.set_index("Country", inplace=True)

# Los mejores 10 paises
df_best = df.nsmallest(10, "Rank")
print(df_best)

# Creacion del grafico
fig, ax = plt.subplots(figsize=(8, 5), dpi=100)  # 800 x 500 px
bar_width = 0.30
x = np.arange(df_best.index.size)

golden_medals = ax.bar(
    x - bar_width, df_best["Gold"], bar_width, label="Gold", color="#ffd700"
)

silver_medals = ax.bar(x, df_best["Silver"], bar_width, label="Silver", color="#aaa9ad")
bronze_medals = ax.bar(
    x + bar_width, df_best["Bronze"], bar_width, label="Bronze", color="#cd7f32"
)

ax.set_xticks(x)
ax.set_xticklabels(df_best.index, rotation=90)
ax.legend()

# Etiquetas en barra
ax.bar_label(golden_medals, padding=3)
ax.bar_label(silver_medals, padding=3)
ax.bar_label(bronze_medals, padding=3)

ax.spines["right"].set_visible(False)  # Ocultar borde derecho
ax.spines["top"].set_visible(False)  # Ocultar borde superior

fig.tight_layout()  # Ajustar elementos al tamaño de la figura
print(fig)
