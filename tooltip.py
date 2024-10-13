import tkinter as tk
class ToolTip:
    def __init__(self, widget,texto ):
        self.widget = widget
        self.texto = texto
        self.tooltip = None
        self.widget.bind("<Enter>", self.mostrar)
        self.widget.bind("<Leave>", self.esconder)

    def mostrar(self, click=None):
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True) 
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.texto, background="white", relief="solid", borderwidth=1)
        label.pack()

    def esconder(self, click=None):
        if self.tooltip:
            self.tooltip.destroy()  
            self.tooltip = None
