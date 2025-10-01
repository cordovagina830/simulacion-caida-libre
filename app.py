# ----------------------------- 
# Simulación completa: Caída libre (corrección para slider y fórmula)
# -----------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

# ------------------------------------------------
# Constante
g = 9.8  # m/s^2
# ------------------------------------------------

# -------------------------
# Función para formatear a 2 decimales sin redondear
# -------------------------
def trunc2(x):
    return math.floor(x * 100) / 100

# -------------------------
# Funciones de escena/actualización
# -------------------------
def create_scene(h0):
    """Crea figura con regla vertical y texto de fase dentro del gráfico."""
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.set_xlim(-1.0, 0.6)
    ax.set_ylim(0, max(1.0, h0 * 1.2))
    ax.axis('off')

    # Suelo
    ax.hlines(0, -0.5, 0.5, color='saddlebrown', linewidth=6, zorder=1)

    # Regla vertical
    xruler = -0.85
    ax.vlines(xruler, 0, h0 if h0 > 0 else 1.0, color='black', linewidth=2, zorder=2)
    tick_len = 0.04
    for h in np.arange(0, max(h0, 1) + 1, 1):
        ax.hlines(h, xruler, xruler + tick_len, color='black', linewidth=1, zorder=3)
        ax.text(xruler - 0.04, h, f"{int(h)} m", fontsize=8, va='center', ha='right', color='black')

    # Tamaño visual del objeto
    radius = max(0.12, min(0.25, h0 * 0.03))

    # Objeto (pelota)
    circle = patches.Circle((0, h0), radius, color='dodgerblue', ec='navy', zorder=5)
    ax.add_patch(circle)

    # Flecha de velocidad
    arrow = patches.FancyArrowPatch((0, h0 - radius - 0.05), (0, h0 - radius - 0.35),
                                    arrowstyle='->', mutation_scale=20, color='orange', linewidth=3, zorder=6)
    ax.add_patch(arrow)

    # Textos dinámicos
    t_text = ax.text(-0.9, max(1.0, h0 * 1.2) * 0.9, "", fontsize=11, color='black')
    v_text = ax.text(-0.9, max(1.0, h0 * 1.2) * 0.85, "", fontsize=11, color='orange')
    y_text = ax.text(-0.9, max(1.0, h0 * 1.2) * 0.8, "", fontsize=11, color='green')
    phase_text = ax.text(0.0, max(1.0, h0 * 1.2) * 0.95, "", fontsize=11, ha='center', va='bottom', color='blue')

    # Tiempo estimado de caída
    t_end = np.sqrt(2 * h0 / g) if h0 > 0 else 0.0

    return fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, t_end

def update_scene(frame_idx, fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, h0, show_formulas, frames=200):
    """Actualiza la figura y construye HTML con fórmulas (valores truncados a 2 decimales sin redondeo)."""
    # Convertir frame a tiempo
    t_end = np.sqrt(2 * h0 / g) if h0 > 0 else 0.0
    t = (frame_idx / (frames - 1)) * t_end if frames > 1 else 0.0

    # Valores físicos
    vi = 0.0  # Velocidad inicial asumida
    # Posición vertical (y)
    y = max(h0 - 0.5 * g * t ** 2, 0.0)
    v = vi + g * t

    # Calcular los términos de y = vi*t + 0.5*g*t^2 con precisión completa
    term1 = vi * t
    term2 = 0.5 * g * (t ** 2)
    d = term1 + term2  # Desplazamiento calculado con precisión

    # Mover círculo (asegurando movimiento vertical)
    circle.center = (0.0, y)  # La coordenada x debe permanecer en 0.0 para caída vertical

    # Actualizar flecha
    start = (0.0, y - radius - 0.05)
    max_visual = max(0.28, h0 * 0.35)
    arrow_len = min(max_visual, 0.18 + 0.35 * (v / (np.sqrt(2 * g * h0) + 1e-9))) if h0 > 0 else 0.18
    end = (0.0, y - radius - 0.05 - arrow_len)
    try:
        arrow.set_positions(start, end)
    except Exception:
        try:
            arrow.remove()
        except Exception:
            pass
        arrow = patches.FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=20, color='orange', linewidth=3, zorder=6)
        ax.add_patch(arrow)

    # Textos numéricos (truncados a 2 decimales sin redondeo)
    t_text.set_text(f"t = {trunc2(t)} s")
    v_text.set_text(f"v = {trunc2(v)} m/s")
    y_text.set_text(f"y = {trunc2(y)} m")

    # Mensajes dinámicos
    if t < 1e-6:
        phase_text.set_text("El objeto está suspendido en el aire. Prepárate para soltarlo.")
        phase_text.set_color('blue')
    elif y > 1e-3:
        phase_text.set_text("La gravedad acelera el objeto: la velocidad aumenta con el tiempo.")
        phase_text.set_color('green')
    else:
        phase_text.set_text("¡La bola ha llegado al suelo! En ausencia de aire, cae con aceleración constante.")
        phase_text.set_color('red')

    fig.canvas.draw()

    # Fórmulas con sustitución (valores truncados a 2 decimales sin redondeo)
    info_html = ""
    if show_formulas:
        # Calcular valores para mostrar (truncados)
        vi_s = trunc2(vi)
        g_s = trunc2(g)
        t_s = trunc2(t)
        term1_s = trunc2(term1)
        term2_s = trunc2(term2)
        d_s = trunc2(d)
        v_s = trunc2(v)
        # Mostrar paso a paso
        info_html = f"""
        Fórmulas (sustitución numérica — pasos):
          vf = vi + g t → {vi_s} + {g_s}·({t_s}) = {v_s} m/s
          y = vi·t + ½·g·t² → 
             Sustituyendo: {vi_s}·{t_s} + 0.5·{g_s}·({t_s})²  
             Términos: {term1_s} + {term2_s}  
             Suma: {d_s} m
          t = (vf - vi)/g → ({v_s} - {vi_s})/{g_s} = {trunc2((v - vi) / g)} s
        """
    else:
        info_html = "Fórmulas ocultas."

    return info_html

# -------------------------
# Función principal simplificada
# -------------------------
def main():
    print("🌟 Simulación Interactiva de Caída Libre sin Resistencia del Aire 🌟")
    print("En esta simulación observarás cómo una bola cae bajo la acción de la gravedad, sin resistencia del aire.")
    print("La simulación muestra que, sin aire, la masa no afecta el tiempo de caída.")
    print("\n" + "="*50)
    
    # Parámetros de simulación
    h0 = 5.0  # Altura inicial
    show_formulas = True
    
    print(f"\nSimulando caída desde {h0} metros...")
    print("Presiona Enter para avanzar en el tiempo (q para salir)")
    
    # Crear escena
    fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, t_end = create_scene(h0)
    
    # Simulación paso a paso
    frames = 20  # Menos frames para simulación por consola
    for frame in range(frames):
        input(f"Frame {frame+1}/{frames} (Enter para continuar): ")
        
        info = update_scene(frame, fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, h0, show_formulas, frames)
        
        # Mostrar información en consola
        print(f"\n--- Tiempo: {frame/(frames-1)*t_end:.2f}s ---")
        print(info)
        plt.pause(0.1)  # Pausa para ver la actualización
    
    plt.show()

if __name__ == "__main__":
    main()
