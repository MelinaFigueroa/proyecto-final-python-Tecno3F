import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import csv
import os

class SistemaTickets:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Tickets")
        self.root.geometry("400x300")
        
        self.tickets = self.cargar_tickets()
        
        self.crear_interfaz()
    
    def cargar_tickets(self):
        """Carga los tickets desde un archivo CSV"""
        if not os.path.exists('tickets.csv'):
            return []
        try:
            with open('tickets.csv', 'r', newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                return list(lector)
            
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al cargar los tickets: {str(e)}")
        return []
    
    def guardar_ticket(self, ticket):
        """Guarda un ticket en el archivo CSV"""
        try:
            archivo_existe = os.path.exists('tickets.csv')
        
            with open('tickets.csv', 'a', newline='', encoding='utf-8') as archivo:
                campos = ['numero', 'nombre', 'sector', 'asunto', 'problema']
                escritor = csv.DictWriter(archivo, fieldnames=campos)
            
                if not archivo_existe:
                    escritor.writeheader()
            
                escritor.writerow(ticket)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el ticket: {str(e)}")
            
    
    def crear_interfaz(self):
        """Crea la interfaz gráfica principal"""
        # Botón de Alta de Ticket
        btn_alta = tk.Button(self.root, text="Generar un nuevo ticket", command=self.mostrar_alta_ticket)
        btn_alta.pack(pady=20, padx=50, fill=tk.X)
        
        # Botón de Leer Ticket
        btn_leer = tk.Button(self.root, text="Leer Ticket", command=self.mostrar_leer_ticket)
        btn_leer.pack(pady=20, padx=50, fill=tk.X)
        
        # Botón de Salir
        btn_salir = tk.Button(self.root, text="Salir", command=self.root.quit)
        btn_salir.pack(pady=20, padx=50, fill=tk.X)
    
    def mostrar_alta_ticket(self):
        """Muestra la ventana para dar de alta un ticket"""
        ventana_alta = tk.Toplevel(self.root)
        ventana_alta.title("Alta de Ticket")
        ventana_alta.geometry("300x400")
        
        # Campos de entrada
        tk.Label(ventana_alta, text="Nombre:").pack()
        nombre_entry = tk.Entry(ventana_alta)
        nombre_entry.pack()
        
        tk.Label(ventana_alta, text="Sector:").pack()
        sector_entry = tk.Entry(ventana_alta)
        sector_entry.pack()
        
        tk.Label(ventana_alta, text="Asunto:").pack()
        asunto_entry = tk.Entry(ventana_alta)
        asunto_entry.pack()
        
        tk.Label(ventana_alta, text="Problema:").pack()
        problema_text = tk.Text(ventana_alta, height=4)
        problema_text.pack()
        
        def guardar():
            # Validar que todos los campos estén llenos
            if not (nombre_entry.get() and sector_entry.get() and 
                    asunto_entry.get() and problema_text.get("1.0", tk.END).strip()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            # Generar número de ticket
            numero_ticket = random.randint(1000, 9999)
            
            # Crear diccionario de ticket
            ticket = {
                'numero': str(numero_ticket),
                'nombre': nombre_entry.get(),
                'sector': sector_entry.get(),
                'asunto': asunto_entry.get(),
                'problema': problema_text.get("1.0", tk.END).strip()
            }
            
            # Guardar ticket
            self.tickets.append(ticket)
            self.guardar_ticket(ticket)
            
            # Mostrar número de ticket
            messagebox.showinfo("Ticket Generado", 
                f"Ticket generado con número: {numero_ticket}\n\n"
                f"Nombre: {ticket['nombre']}\n"
                f"Sector: {ticket['sector']}\n"
                f"Asunto: {ticket['asunto']}")
            
            # Preguntar si desea crear otro ticket
            respuesta = messagebox.askyesno("Continuar", "¿Desea crear otro ticket?")
            if not respuesta:
                ventana_alta.destroy()
        
        # Botón de guardar
        btn_guardar = tk.Button(ventana_alta, text="Guardar Ticket", command=guardar)
        btn_guardar.pack(pady=10)
    
    def mostrar_leer_ticket(self):
        """Muestra la ventana para leer un ticket"""
        if not self.tickets:
            messagebox.showinfo("Información", "No hay tickets almacenados")
            return
        
        # Pedir número de ticket
        numero_buscar = simpledialog.askinteger("Leer Ticket", 
            "Ingrese el número de ticket a buscar:")
        
        if numero_buscar:
            # Buscar ticket
            ticket_encontrado = None
            for ticket in self.tickets:
                if int(ticket['numero']) == numero_buscar:
                    ticket_encontrado = ticket
                    break
            
            if ticket_encontrado:
                # Mostrar detalles del ticket
                mensaje = (f"Número de Ticket: {ticket_encontrado['numero']}\n"
                           f"Nombre: {ticket_encontrado['nombre']}\n"
                           f"Sector: {ticket_encontrado['sector']}\n"
                           f"Asunto: {ticket_encontrado['asunto']}\n"
                           f"Problema: {ticket_encontrado['problema']}")
                
                messagebox.showinfo("Ticket Encontrado", mensaje)
                
                # Preguntar si desea leer otro ticket
                respuesta = messagebox.askyesno("Continuar", "¿Desea leer otro ticket?")
                if respuesta:
                    self.mostrar_leer_ticket()
            else:
                messagebox.showerror("Error", "Ticket no encontrado")

def main():
    root = tk.Tk()
    app = SistemaTickets(root)
    root.mainloop()

if __name__ == "__main__":
    main()