import tkinter as tk
from tkinter import ttk
from routes.route import tempe_c, vazao, rotacao, forca, pressao
from src.config import Config

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter with FastAPI")
        self.root.geometry('550x400')

        self.label = ttk.Label(root, text="API Response:")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry widgets for displaying values
        ttk.Label(root, text="Pressure:").grid(row=1, column=0)
        self.pressure_entry = ttk.Entry(root, width=20)
        self.pressure_entry.grid(row=1, column=1, pady=5)

        ttk.Label(root, text="Force:").grid(row=2, column=0)
        self.force_entry = ttk.Entry(root, width=20)
        self.force_entry.grid(row=2, column=1, pady=5)

        ttk.Label(root, text="Temperature:").grid(row=3, column=0)
        self.tempe_entry = ttk.Entry(root, width=20)
        self.tempe_entry.grid(row=3, column=1, pady=5)

        ttk.Label(root, text="Rotation:").grid(row=4, column=0)
        self.rotation_entry = ttk.Entry(root, width=20)
        self.rotation_entry.grid(row=4, column=1, pady=5)

        ttk.Label(root, text="Flow:").grid(row=5, column=0)
        self.flow_entry = ttk.Entry(root, width=20)
        self.flow_entry.grid(row=5, column=1, pady=5)

        # Atualiza os valores a cada 1000 milissegundos (1 segundo)
        self.root.after(1000, self.update_values)

    def update_values(self):
        try:
            # Get the last values from the lists, defaulting to 0 if the list is empty
            temperature = tempe_c[-1] if tempe_c else 0
            rotation = rotacao[-1] if rotacao else 0
            pressure = pressao[-1] if pressao else 0
            flow = vazao[-1] if vazao else 0
            force = forca[-1] if forca else 0

            # Display the values in the entry widgets
            self.tempe_entry.delete(0, tk.END)
            self.tempe_entry.insert(0, temperature)

            self.rotation_entry.delete(0, tk.END)
            self.rotation_entry.insert(0, rotation)

            self.pressure_entry.delete(0, tk.END)
            self.pressure_entry.insert(0, pressure)

            self.flow_entry.delete(0, tk.END)
            self.flow_entry.insert(0, flow)

            self.force_entry.delete(0, tk.END)
            self.force_entry.insert(0, force)

        except Exception as e:
            # Handle exceptions, e.g., invalid input
            print(f"Error: {e}")

        finally:
            # Schedule the next update
            self.root.after(1000, self.update_values)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
