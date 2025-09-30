{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a3c28f7c-2c9b-42f3-837b-d1fbd075607a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<h1 style='color:darkred;'>🌟 Simulación Interactiva de Caída Libre sin Resistencia del Aire 🌟</h1>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "\n",
       "<p style='font-size:16px; text-align:center; margin-bottom:15px;'>\n",
       "En esta simulación observarás cómo una bola cae bajo la acción de la gravedad, <b style='color:red;'>sin resistencia del aire</b>. \n",
       "Podrás variar la altura inicial y la velocidad inicial de la bola, y ver cómo cambian la altura, la velocidad y el tiempo durante la caída. La simulación muestra que, sin aire, la masa no afecta el tiempo de caída, y todos los objetos caen con la misma aceleración de 9.8 m/s².\n",
       "</p>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "\n",
       "<p style='font-size:15px; color:darkblue; margin-top:15px;'>\n",
       "Elige altura y velocidad inicial. Marca <b>Mostrar fórmulas</b> para ver los cálculos. Pulsa <b>Soltar objeto</b> y luego ▶ Play.\n",
       "</p>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "99971a411b9a45689f7056d35aa9cbda",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(ToggleButtons(description='Altura:', index=2, options=(('1 m', 1.0), ('2 m', 2.0), ('5 m', 5.0)…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0ac95fc6e6e5419ea69d44fa23663ccc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(Button(button_style='info', description='💧 Soltar objeto', style=ButtonStyle()), Button(button_…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<hr>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "\n",
       "<h3 style='color:darkblue;'>📌 Conceptos clave de la caída libre</h3>\n",
       "<p style='font-size:15px;'>\n",
       "✔️ La <b>aceleración gravitacional</b> de 9.8 m/s², se considera positiva al descender el objeto y negativa al ascender el objeto.<br>\n",
       "✔️ La <b>velocidad final</b> aumenta con el tiempo (<b>vf = vi + g·t</b>).<br>\n",
       "✔️ La <b>altura</b> o posición cambia según (<b>y = vi·t + ½·g·t²</b>).<br>\n",
       "✔️ El <b>tiempo</b> se obtiene de (<b>t = (vf - vi)/g</b>).<br>\n",
       "✔️ Otras fórmulas: 2gh = vf² - vi².\n",
       "</p>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1d123114047e45dd8dc2683753265226",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(Play(value=0, description='Play', interval=30, max=199), IntSlider(value=0, description='Frame:…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2b1e05c15e92436588c0836954d34211",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Output()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# ----------------------------- \n",
    "# Simulación completa: Caída libre (corrección para slider y fórmula)\n",
    "# -----------------------------\n",
    "\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.patches as patches\n",
    "from matplotlib.animation import FuncAnimation\n",
    "from IPython.display import display, clear_output, HTML\n",
    "import ipywidgets as widgets\n",
    "import math\n",
    "\n",
    "# Activar modo interactivo para Matplotlib\n",
    "plt.ion()\n",
    "\n",
    "# ------------------------------------------------\n",
    "# Constantes\n",
    "g = 9.8  # m/s^2\n",
    "# ------------------------------------------------\n",
    "\n",
    "# -------------------------\n",
    "# Función para formatear a 2 decimales sin redondear\n",
    "# -------------------------\n",
    "def trunc2(x):\n",
    "    return math.floor(x * 100) / 100\n",
    "\n",
    "# -------------------------\n",
    "# Funciones de escena/actualización\n",
    "# -------------------------\n",
    "def create_scene(h0):\n",
    "    \"\"\"Crea figura con regla vertical y texto de fase dentro del gráfico.\"\"\"\n",
    "    fig, ax = plt.subplots(figsize=(4, 6))\n",
    "    ax.set_xlim(-1.0, 0.6)\n",
    "    ax.set_ylim(0, max(1.0, h0 * 1.2))\n",
    "    ax.axis('off')\n",
    "\n",
    "    # Suelo\n",
    "    ax.hlines(0, -0.5, 0.5, color='saddlebrown', linewidth=6, zorder=1)\n",
    "\n",
    "    # Regla vertical\n",
    "    xruler = -0.85\n",
    "    ax.vlines(xruler, 0, h0 if h0 > 0 else 1.0, color='black', linewidth=2, zorder=2)\n",
    "    tick_len = 0.04\n",
    "    for h in np.arange(0, max(h0, 1) + 1, 1):\n",
    "        ax.hlines(h, xruler, xruler + tick_len, color='black', linewidth=1, zorder=3)\n",
    "        ax.text(xruler - 0.04, h, f\"{int(h)} m\", fontsize=8, va='center', ha='right', color='black')\n",
    "\n",
    "    # Tamaño visual del objeto\n",
    "    radius = max(0.12, min(0.25, h0 * 0.03))\n",
    "\n",
    "    # Objeto (pelota)\n",
    "    circle = patches.Circle((0, h0), radius, color='dodgerblue', ec='navy', zorder=5)\n",
    "    ax.add_patch(circle)\n",
    "\n",
    "    # Flecha de velocidad\n",
    "    arrow = patches.FancyArrowPatch((0, h0 - radius - 0.05), (0, h0 - radius - 0.35),\n",
    "                                    arrowstyle='->', mutation_scale=20, color='orange', linewidth=3, zorder=6)\n",
    "    ax.add_patch(arrow)\n",
    "\n",
    "    # Textos dinámicos\n",
    "    t_text = ax.text(-0.9, max(1.0, h0 * 1.2) * 0.9, \"\", fontsize=11, color='black')\n",
    "    v_text = ax.text(-0.9, max(1.0, h0 * 1.2) * 0.85, \"\", fontsize=11, color='orange')\n",
    "    y_text = ax.text(-0.9, max(1.0, h0 * 1.2) * 0.8, \"\", fontsize=11, color='green')\n",
    "    phase_text = ax.text(0.0, max(1.0, h0 * 1.2) * 0.95, \"\", fontsize=11, ha='center', va='bottom', color='blue')\n",
    "\n",
    "    # Tiempo estimado de caída (usando vi = 0 como referencia, ajustable)\n",
    "    vi = float(masa_btns.value)\n",
    "    t_end = np.sqrt(2 * h0 / g) if vi == 0 else (np.sqrt(vi**2 + 2 * g * h0) - vi) / g\n",
    "\n",
    "    return fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, t_end, vi\n",
    "\n",
    "def update_scene(frame_idx, fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, h0, show_formulas, vi, frames=200):\n",
    "    \"\"\"Actualiza la figura y construye HTML con fórmulas.\"\"\"\n",
    "    t_end = np.sqrt(2 * h0 / g) if vi == 0 else (np.sqrt(vi**2 + 2 * g * h0) - vi) / g\n",
    "    t = (frame_idx / (frames - 1)) * t_end if frames > 1 else 0.0\n",
    "    displacement = vi * t + 0.5 * g * t ** 2  # Desplazamiento positivo downward\n",
    "    y = h0 - displacement  # Posición descendente\n",
    "    v = vi + g * t\n",
    "\n",
    "    circle.center = (0.0, y)\n",
    "    start = (0.0, y - radius - 0.05)\n",
    "    max_visual = max(0.28, h0 * 0.35)\n",
    "    arrow_len = min(max_visual, 0.18 + 0.35 * (v / (np.sqrt(2 * g * h0) + 1e-9))) if h0 > 0 else 0.18\n",
    "    end = (0.0, y - radius - 0.05 - arrow_len)\n",
    "    arrow.set_positions(start, end)\n",
    "\n",
    "    t_text.set_text(f\"t = {trunc2(t)} s\")\n",
    "    v_text.set_text(f\"v = {trunc2(v)} m/s\")\n",
    "    y_text.set_text(f\"y = {trunc2(y)} m\")\n",
    "\n",
    "    if t < 1e-6:\n",
    "        phase_text.set_text(\"La bola está en su posición inicial. Prepárate para observar su caída bajo la gravedad.\")\n",
    "        phase_text.set_color('blue')\n",
    "    elif y > 1e-3:\n",
    "        phase_text.set_text(\"La gravedad acelera el objeto: la velocidad aumenta con el tiempo.\")\n",
    "        phase_text.set_color('green')\n",
    "    else:\n",
    "        phase_text.set_text(\"¡La bola ha llegado al suelo! En ausencia de aire, cae con aceleración constante!\")\n",
    "        phase_text.set_color('red')\n",
    "\n",
    "    fig.canvas.draw()\n",
    "\n",
    "    info_html = \"\"\n",
    "    if show_formulas:\n",
    "        t_current = t\n",
    "        v_current = vi + g * t_current\n",
    "        h_current = vi * t_current + 0.5 * g * t_current ** 2  # Signo positivo como solicitado\n",
    "        info_html = f\"\"\"\n",
    "        <div style=\"font-family: sans-serif; font-size:14px; line-height:1.4\">\n",
    "          <b>Fórmulas:</b><br>\n",
    "          vf = vi + {trunc2(g)}·t<br>\n",
    "          y = vi·t + ½·{trunc2(g)}·t²<br>\n",
    "          t = (vf - vi) / {trunc2(g)}\n",
    "        </div>\n",
    "        \"\"\"\n",
    "    return info_html\n",
    "\n",
    "# -------------------------\n",
    "# Widgets e interfaz\n",
    "# -------------------------\n",
    "altura_btns = widgets.ToggleButtons(\n",
    "    options=[('1 m', 1.0), ('2 m', 2.0), ('5 m', 5.0), ('10 m', 10.0)],\n",
    "    description='Altura:', value=5.0\n",
    ")\n",
    "masa_btns = widgets.ToggleButtons(\n",
    "    options=[('0.0 m/s', 0.0), ('0.5 m/s', 0.5), ('1 m/s', 1.0), ('2 m/s', 2.0), ('5 m/s', 5.0)],\n",
    "    description='Velocidad inicial:', value=0.0\n",
    ")\n",
    "show_formulas_cb = widgets.Checkbox(value=True, description='Mostrar fórmulas')\n",
    "btn_soltar = widgets.Button(description='💧 Soltar objeto', button_style='info')\n",
    "btn_reiniciar = widgets.Button(description='↺ Reiniciar', button_style='warning', disabled=True)\n",
    "\n",
    "frames = 200\n",
    "slider = widgets.IntSlider(value=0, min=0, max=frames-1, step=1, description='Frame:', layout=widgets.Layout(width='60%'))\n",
    "play = widgets.Play(value=0, min=0, max=frames-1, interval=30, description=\"Play\", disabled=False)\n",
    "widgets.jslink((play, 'value'), (slider, 'value'))\n",
    "\n",
    "anim_out = widgets.Output()\n",
    "\n",
    "# Título + introducción\n",
    "title_html = HTML(\"<h1 style='color:darkred;'>🌟 Simulación Interactiva de Caída Libre sin Resistencia del Aire 🌟</h1>\")\n",
    "intro_html = HTML(\"\"\"\n",
    "<p style='font-size:16px; text-align:center; margin-bottom:15px;'>\n",
    "En esta simulación observarás cómo una bola cae bajo la acción de la gravedad, <b style='color:red;'>sin resistencia del aire</b>. \n",
    "Podrás variar la altura inicial y la velocidad inicial de la bola, y ver cómo cambian la altura, la velocidad y el tiempo durante la caída. La simulación muestra que, sin aire, la masa no afecta el tiempo de caída, y todos los objetos caen con la misma aceleración de 9.8 m/s².\n",
    "</p>\n",
    "\"\"\")\n",
    "seleccion_html = HTML(\"\"\"\n",
    "<p style='font-size:15px; color:darkblue; margin-top:15px;'>\n",
    "Elige altura y velocidad inicial. Marca <b>Mostrar fórmulas</b> para ver los cálculos. Pulsa <b>Soltar objeto</b> y luego ▶ Play.\n",
    "</p>\n",
    "\"\"\")\n",
    "importante_html = HTML(\"\"\"\n",
    "<h3 style='color:darkblue;'>📌 Conceptos clave de la caída libre</h3>\n",
    "<p style='font-size:15px;'>\n",
    "✔️ La <b>aceleración gravitacional</b> de 9.8 m/s², se considera positiva al descender el objeto y negativa al ascender el objeto.<br>\n",
    "✔️ La <b>velocidad final</b> aumenta con el tiempo (<b>vf = vi + g·t</b>).<br>\n",
    "✔️ La <b>altura</b> o posición cambia según (<b>y = vi·t + ½·g·t²</b>).<br>\n",
    "✔️ El <b>tiempo</b> se obtiene de (<b>t = (vf - vi)/g</b>).<br>\n",
    "✔️ Otras fórmulas: 2gh = vf² - vi².\n",
    "</p>\n",
    "\"\"\")\n",
    "\n",
    "# Mostrar interfaz inicial\n",
    "display(\n",
    "    title_html,\n",
    "    intro_html,\n",
    "    seleccion_html,\n",
    "    widgets.HBox([altura_btns, masa_btns, show_formulas_cb]),\n",
    "    widgets.HBox([btn_soltar, btn_reiniciar]),\n",
    "    HTML(\"<hr>\"),\n",
    "    importante_html,\n",
    "    widgets.HBox([play, slider]),\n",
    "    anim_out  # Mostrar el área de salida explícitamente\n",
    ")\n",
    "\n",
    "# -------------------------\n",
    "# Lógica de interacción\n",
    "# -------------------------\n",
    "current_scene = {}\n",
    "\n",
    "def on_soltar_clicked(b):\n",
    "    global fig, ani\n",
    "    h0 = float(altura_btns.value)\n",
    "    vi = float(masa_btns.value)\n",
    "    show_form = bool(show_formulas_cb.value)\n",
    "    print(\"Botón 'Soltar objeto' presionado\")  # Depuración\n",
    "\n",
    "    with anim_out:\n",
    "        anim_out.clear_output(wait=True)\n",
    "        fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, t_end, vi = create_scene(h0)\n",
    "        current_scene.update(dict(fig=fig, ax=ax, circle=circle, arrow=arrow, t_text=t_text, v_text=v_text, y_text=y_text, radius=radius, phase_text=phase_text, h0=h0, show_form=show_form, vi=vi))\n",
    "\n",
    "        btn_reiniciar.disabled = False\n",
    "\n",
    "        # Inicia la animación\n",
    "        ani = FuncAnimation(fig, lambda i: update_scene(i, fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, h0, show_form, vi, frames=frames), frames=frames, interval=50, repeat=False, blit=False)\n",
    "        display(fig)  # Intenta mostrar el gráfico directamente\n",
    "        if show_form:\n",
    "            formulas = f\"\"\"\n",
    "            <div style=\"font-family: sans-serif; font-size:14px; line-height:1.4\">\n",
    "              <b>Fórmulas:</b><br>\n",
    "              vf = vi + {trunc2(g)}·t<br>\n",
    "              y = vi·t + ½·{trunc2(g)}·t²<br>\n",
    "              t = (vf - vi) / {trunc2(g)}\n",
    "            </div>\n",
    "            \"\"\"\n",
    "            display(HTML(formulas))\n",
    "\n",
    "            # Cálculos finales con sustitución de valores (mostrado solo al inicio, no en handler)\n",
    "            t_final = t_end\n",
    "            v_final = vi + g * t_final\n",
    "            h_final = vi * t_final + 0.5 * g * t_final ** 2  # Signo positivo como solicitado\n",
    "            sustitucion = f\"\"\"\n",
    "            <div style=\"font-family: sans-serif; font-size:14px; line-height:1.4; margin-top:10px;\">\n",
    "              <b>Sustitución de valores finales:</b><br>\n",
    "              Tiempo: t = (vf - vi) / {trunc2(g)} = ({trunc2(v_final)} - {trunc2(vi)}) / {trunc2(g)} = {trunc2(t_final)} s<br>\n",
    "              Velocidad: vf = vi + {trunc2(g)}·{trunc2(t_final)} = {trunc2(vi)} + {trunc2(g)}·{trunc2(t_final)} = {trunc2(v_final)} m/s<br>\n",
    "              Altura: y = vi·{trunc2(t_final)} + ½·{trunc2(g)}·{trunc2(t_final)}^2 = {trunc2(vi)}·{trunc2(t_final)} + ½·{trunc2(g)}·{trunc2(t_final)}^2 = {trunc2(h_final)} m\n",
    "            </div>\n",
    "            \"\"\"\n",
    "            display(HTML(sustitucion))\n",
    "\n",
    "    # Vincula el slider para actualizaciones manuales\n",
    "    def handler(change):\n",
    "        with anim_out:\n",
    "            clear_output(wait=True)\n",
    "            update_scene(change['new'], fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, h0, show_form, vi, frames=frames)\n",
    "            display(fig)\n",
    "            if show_form:\n",
    "                display(HTML(update_scene(change['new'], fig, ax, circle, arrow, t_text, v_text, y_text, radius, phase_text, h0, show_form, vi, frames=frames)))\n",
    "\n",
    "                # Cálculos dinámicos con sustitución de valores al mover el slider\n",
    "                t_current = (change['new'] / (frames - 1)) * t_end if frames > 1 else 0.0\n",
    "                v_current = vi + g * t_current\n",
    "                h_current = vi * t_current + 0.5 * g * t_current ** 2  # Signo positivo como solicitado\n",
    "                sustitucion_current = f\"\"\"\n",
    "                <div style=\"font-family: sans-serif; font-size:14px; line-height:1.4; margin-top:10px;\">\n",
    "                  <b>Sustitución de valores actuales (t = {trunc2(t_current)} s):</b><br>\n",
    "                  Tiempo: t = (vf - vi) / {trunc2(g)} = ({trunc2(v_current)} - {trunc2(vi)}) / {trunc2(g)} = {trunc2(t_current)} s<br>\n",
    "                  Velocidad: vf = vi + {trunc2(g)}·{trunc2(t_current)} = {trunc2(vi)} + {trunc2(g)}·{trunc2(t_current)} = {trunc2(v_current)} m/s<br>\n",
    "                  Altura: y = vi·{trunc2(t_current)} + ½·{trunc2(g)}·{trunc2(t_current)}^2 = {trunc2(vi)}·{trunc2(t_current)} + ½·{trunc2(g)}·{trunc2(t_current)}^2 = {trunc2(h_current)} m\n",
    "                </div>\n",
    "                \"\"\"\n",
    "                display(HTML(sustitucion_current))\n",
    "\n",
    "    slider.observe(handler, names='value')\n",
    "    # Inicia el slider automáticamente\n",
    "    play.play()\n",
    "\n",
    "btn_soltar.on_click(on_soltar_clicked)\n",
    "\n",
    "def on_reiniciar_clicked(b):\n",
    "    with anim_out:\n",
    "        clear_output(wait=True)\n",
    "    play.value = 0\n",
    "    slider.value = 0\n",
    "    btn_reiniciar.disabled = True\n",
    "    if current_scene.get('fig'):\n",
    "        plt.close(current_scene['fig'])\n",
    "    current_scene.clear()\n",
    "    display(HTML(\"<p style='color:darkblue; background-color:lightyellow; padding:10px;'><b>¡Simulación reiniciada! Selecciona una nueva altura y pulsa 'Soltar objeto'.</b></p>\"))\n",
    "\n",
    "btn_reiniciar.on_click(on_reiniciar_clicked)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c96135f-e459-4dee-9a5d-843ea4198063",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
