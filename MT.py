import tkinter as tk
from tkinter import messagebox, font
import re

# Funciones de traducción
def translate_to_python(code):
    code = re.sub(r'if\s*\((.*?)\)\s*\{', r'if \1:', code)
    code = re.sub(r'\}\s*else\s*\{', r'else:', code)
    code = re.sub(r'\}', '', code)
    code = re.sub(r'for\s*\(\s*int\s+(\w+)\s*=\s*(\d+)\s*;\s*\1\s*<\s*(\d+)\s*;\s*\1\+\+\s*\)\s*\{', r'for \1 in range(\2, \3):', code)
    code = re.sub(r'printf\("%d\\n",\s*(.*?)\);', r'print(\1)', code)
    return code

def translate_to_go(code):
    code = re.sub(r'if\s*\((.*?)\)\s*\{', r'if \1 {', code)
    code = re.sub(r'for\s*\(\s*int\s+(\w+)\s*=\s*(\d+)\s*;\s*\1\s*<\s*(\d+)\s*;\s*\1\+\+\s*\)\s*\{', r'for \1 := \2; \1 < \3; \1++ {', code)
    code = re.sub(r'printf\("%d\\n",\s*(.*?)\);', r'fmt.Println(\1)', code)
    return code

def translate_to_javascript(code):
    code = re.sub(r'if\s*\((.*?)\)\s*\{', r'if (\1) {', code)
    code = re.sub(r'for\s*\(\s*int\s+(\w+)\s*=\s*(\d+)\s*;\s*\1\s*<\s*(\d+)\s*;\s*\1\+\+\s*\)\s*\{', r'for (let \1 = \2; \1 < \3; \1++) {', code)
    code = re.sub(r'printf\("%d\\n",\s*(.*?)\);', r'console.log(\1);', code)
    return code

def process_code():
    c_code = input_text.get("1.0", "end-1c")
    try:
        python_code = translate_to_python(c_code)
        go_code = translate_to_go(c_code)
        javascript_code = translate_to_javascript(c_code)
        
        python_output.config(state='normal')
        python_output.delete("1.0", "end")
        python_output.insert("1.0", python_code)
        python_output.config(state='disabled')
        
        go_output.config(state='normal')
        go_output.delete("1.0", "end")
        go_output.insert("1.0", go_code)
        go_output.config(state='disabled')
        
        javascript_output.config(state='normal')
        javascript_output.delete("1.0", "end")
        javascript_output.insert("1.0", javascript_code)
        javascript_output.config(state='disabled')
        
    except Exception as e:
        messagebox.showerror("Error", "Error en la sintaxis del código en C. No se aceptó la cadena.")
        print(f"Error: {e}")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Traductor de Código de Control de Estructuras")
root.geometry("800x500")
root.configure(bg="#f0f0f0")

# Estilos
label_font = font.Font(family="Arial", size=10, weight="bold")
output_font = ("Courier", 10)

# Marco para organizar la interfaz en dos columnas
frame_left = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame_left.pack(side="left", fill="both", expand=True)

frame_right = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame_right.pack(side="right", fill="both", expand=True)

# Input de código en C en la columna izquierda
tk.Label(frame_left, text="Código en C:", font=label_font, bg="#f0f0f0").pack(anchor="nw", pady=5)
input_text = tk.Text(frame_left, height=20, width=40, font=output_font)
input_text.pack(anchor="nw", fill="both", expand=True)

# Botón de traducción en la columna izquierda
translate_button = tk.Button(frame_left, text="Traducir", command=process_code, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
translate_button.pack(pady=10)

# Cuadro de texto para Python en la columna derecha
tk.Label(frame_right, text="Python:", font=label_font, bg="#f0f0f0").pack(anchor="nw", pady=5)
python_output = tk.Text(frame_right, height=5, width=40, font=output_font, state='disabled', bg="#e0e0e0")
python_output.pack(anchor="nw", fill="x", expand=True, pady=5)

# Cuadro de texto para Go en la columna derecha
tk.Label(frame_right, text="Go:", font=label_font, bg="#f0f0f0").pack(anchor="nw", pady=5)
go_output = tk.Text(frame_right, height=5, width=40, font=output_font, state='disabled', bg="#e0e0e0")
go_output.pack(anchor="nw", fill="x", expand=True, pady=5)

# Cuadro de texto para JavaScript en la columna derecha
tk.Label(frame_right, text="JavaScript:", font=label_font, bg="#f0f0f0").pack(anchor="nw", pady=5)
javascript_output = tk.Text(frame_right, height=5, width=40, font=output_font, state='disabled', bg="#e0e0e0")
javascript_output.pack(anchor="nw", fill="x", expand=True, pady=5)

# Ejecutar la aplicación
root.mainloop()
