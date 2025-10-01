# app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

# -------------------------
# Constante
g = 9.8  # m/s^2
# -------------------------

# -------------------------
# Función truncar a 2 decimales sin redondear
# -------------------------
def trunc2(x):
    return math.floor(x * 100) / 100

# -------------------------
# Configuración de la página
# -------------------------
st.set_page_config(page_title="Caída Libre", layout="wide")
st.title("🌟 Simulación Interactiva de Caída Libre 🌟")

st.markdown("""
En esta simulación observarás cómo una bola cae bajo la acción de la gravedad, **sin resistencia del aire**.  
Podrás variar la altura inicial y ver cómo cambian la altura, la velocidad y el tiempo durante la caída.
""")

# -------------------------
# Controles de usuario
# -------------------------
h0 = st.radio("Altura inicial:", [1, 2, 5, 10], index=2)
show_formulas = st.checkbox("Mostrar fórmulas", value=True)

# Tiempo de caída
t_end = np.sqrt(2 * h0 / g) if h0 > 0 else 0.0
t = st.slider("Tiempo (s)", 0.0, float(t_end), 0.0, 0.01)

# -------------------------
# Cálculos físicos
# -------------------------
vi = 0.0
y = max(h0 - 0.5 * g * t ** 2, 0.0)
v = vi + g * t

# -------------------------
# Gráfico con pelota
# -------------------------
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(0, max(1, h0 * 1.2))
ax.axis('off')

# suelo
ax.hlines(0, -0.5, 0.5, color='saddlebrown', linewidth=6)

# regla
xruler = -0.8
ax.vlines(xruler, 0, h0, color='black', linewidth=2)
for h in np.arange(0, h0 + 1, 1):
    ax.hlines(h, xruler, xruler+0.05, color='black')
    ax.text(xruler-0.05, h, f"{int(h)} m", fontsize=8, va='center', ha='right')

# pelota
circle = patches.Circle((0, y), 0.2, color='dodgerblue', ec='navy')
ax.add_patch(circle)

# flecha velocidad
arrow = patches.FancyArrowPatch((0, y-0.25), (0, y-0.5), 
                                arrowstyle='->', mutation_scale=20, 
                                color='orange', linewidth=2)
ax.add_patch(arrow)

st.pyplot(fig)

# -------------------------
# Resultados numéricos
# -------------------------
st.subheader("📊 Resultados")
st.write(f"Tiempo: {trunc2(t)} s")
st.write(f"Altura: {trunc2(y)} m")
st.write(f"Velocidad: {trunc2(v)} m/s")

# -------------------------
# Fórmulas
# -------------------------
if show_formulas:
    st.markdown("### 📐 Fórmulas con valores")
    st.latex(r"v_f = v_i + g t")
    st.write(f"{vi} + {g}·({trunc2(t)}) = **{trunc2(v)} m/s**")

    st.latex(r"y = v_i t + \tfrac{1}{2} g t^2")
    st.write(f"{vi}·{trunc2(t)} + 0.5·{g}·({trunc2(t)})² = **{trunc2(y)} m**")
