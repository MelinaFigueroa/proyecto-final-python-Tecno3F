import tkinter as tk
from tkinter import messagebox

class ConversorTemperaturas:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Temperaturas")
        self.root.geometry("400x300")
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Título
        tk.Label(self.root, text="Conversor de Temperaturas", 
                 font=("Arial", 16)).pack(pady=20)
        
        # Frame principal
        frame_principal = tk.Frame(self.root)
        frame_principal.pack(pady=10)
        
        # Entrada de temperatura
        tk.Label(frame_principal, text="Temperatura:", 
                 font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.entrada_temp = tk.Entry(frame_principal, width=10, font=("Arial", 12))
        self.entrada_temp.grid(row=0, column=1, padx=5)
        
        # Selector de escala de entrada
        self.escala_entrada = tk.StringVar(value="Seleccionar")
        escalas_entrada = ["Celsius", "Fahrenheit"]
        menu_entrada = tk.OptionMenu(frame_principal, self.escala_entrada, *escalas_entrada)
        menu_entrada.grid(row=0, column=2, padx=5)
        
        # Botón de conversión
        tk.Button(frame_principal, text="Convertir", 
                  command=self.convertir_temperatura).grid(row=1, column=1, pady=10)
        
        # Resultado
        self.resultado = tk.StringVar()
        tk.Label(self.root, textvariable=self.resultado, 
                 font=("Arial", 14, "bold")).pack(pady=10)
    
    def convertir_temperatura(self):
        try:
            # Obtener valor de entrada
            temperatura = float(self.entrada_temp.get())
            escala = self.escala_entrada.get()
            
            # Convertir según la escala
            if escala == "Celsius":
                # Convertir de Celsius a Fahrenheit
                fahrenheit = (temperatura * 9/5) + 32
                self.resultado.set(f"{temperatura}°C = {fahrenheit:.2f}°F")
            else:
                # Convertir de Fahrenheit a Celsius
                celsius = (temperatura - 32) * 5/9
                self.resultado.set(f"{temperatura}°F = {celsius:.2f}°C")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido")

def main():
    root = tk.Tk()
    app = ConversorTemperaturas(root)
    root.mainloop()

if __name__ == "__main__":
    main()