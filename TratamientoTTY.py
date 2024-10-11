import tkinter as tk
from tkinter import messagebox, font
import pyperclip

commands = [
    "script /dev/null -c bash",
    "stty raw -echo; fg",
    "reset xterm",
    "export TERM=xterm",
    "export SHELL=bash"
]

def copy_to_clipboard(text):
    pyperclip.copy(text)
    messagebox.showinfo("Copiado", f"'{text}' ha sido copiado al portapapeles.")

root = tk.Tk()
root.title("Copiador de Comandos TTY")
root.geometry("400x450")
root.configure(bg="#2C3E50")

title_font = font.Font(family="Helvetica", size=16, weight="bold")
button_font = font.Font(family="Helvetica", size=10)
description_font = font.Font(family="Helvetica", size=10, slant="italic")

title_label = tk.Label(root, text="Copiador de Comandos TTY", font=title_font, bg="#2C3E50", fg="white")
title_label.pack(pady=20)

description = "Haga clic en un botón para copiar el comando correspondiente."
description_label = tk.Label(root, text=description, font=description_font, bg="#2C3E50", fg="#BDC3C7", wraplength=350)
description_label.pack(pady=10)

frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=20)


button_text_color = "red"  

for command in commands:
    button = tk.Button(frame, text=command, command=lambda cmd=command: copy_to_clipboard(cmd),
                    bg="#3498DB", fg=button_text_color, activebackground="#2980B9", activeforeground=button_text_color,
                    relief=tk.FLAT, padx=10, pady=5, font=button_font)
    button.pack(fill=tk.X, padx=20, pady=5)
    

    button.bind("<Enter>", lambda e, btn=button: btn.config(bg="#2980B9"))
    button.bind("<Leave>", lambda e, btn=button: btn.config(bg="#3498DB"))

root.mainloop()


