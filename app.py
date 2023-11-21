from tkinter import ttk
import requests
from src.config import Config

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter with FastAPI")
        self.root.geometry('550x400')

        self.label = ttk.Label(root, text="API Response:")
        self.label.pack(pady=10)

        self.tempe_label = ttk.Label(root, text="Temperatura:")
        self.tempe_label.pack(pady=10)

        # Atualiza a temperatura a cada 1000 milissegundos (1 segundo)
        self.root.after(1000, self.update_tempe_label)

    def update_tempe_label(self):
        try:
            # Make a GET request to your FastAPI endpoint
            response = requests.get(f'http://{ Config.HOST}:{Config.PORT+1}/api/temperatura/incluir_temperatura')
            response.raise_for_status()  # Raise an exception for bad responses

            # Extract temperature from the response JSON
            tempe_c = response.json().get("temperature")

            # Update the Tkinter label with the obtained temperature
            if tempe_c is not None:
                self.tempe_label.config(text=f"Temperatura: {tempe_c}")

        except Exception as e:
            # Handle exceptions, e.g., network errors or invalid responses
            print(f"Error: {e}")

        finally:
            # Schedule the next update
            self.root.after(1000, self.update_tempe_label)

