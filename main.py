# main.py
import tkinter as tk
from tkinter import ttk
from fastapi.middleware.cors import CORSMiddleware
import requests
from src.config import Config
import threading

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter with FastAPI")
        self.root.geometry('550x400')

        self.label = ttk.Label(root, text="API Response:")
        self.label.pack(pady=10)

        self.tempe_label = ttk.Label(root, text="Temperatura:")
        self.tempe_label.pack(pady=10)

        self.button = ttk.Button(root, text="Call API", command=self.call_api)
        self.button.pack(pady=10)

        # Atualiza a temperatura a cada 1000 milissegundos (1 segundo)
        self.root.after(1000, self.update_tempe_label)

    def call_api(self):
        response = requests.post(f'http://{Config.HOST}:{Config.PORT+1}/api/temperatura', json={"tempe_c": 25.5})
        data = response.json()
        self.label.config(text=f"API Response: {data}")

    def update_tempe_label(self):
        from routes.temperatura import tempe_c
        if tempe_c is not None:
            self.tempe_label.config(text=f"Temperatura: {tempe_c}")
            self.root.after(1000, self.update_tempe_label)

if __name__ == "__main__":
    from fastapi import FastAPI
    from routes.temperatura import Temperatura
    import uvicorn
    import threading
    app_tempe = Temperatura.app_tempe
    # Run the API using uvicorn in a separate thread
    api_thread_tempe = threading.Thread(target=uvicorn.run, kwargs={'app': app_tempe, 'host': Config.HOST, 'port': Config.PORT+1})
    api_thread_tempe.start()

    # Run the Tkinter app
    root = tk.Tk()
    app = MyApp(root)

    # Configuração do CORS para permitir solicitações de qualquer origem
    origins = ["*"]
    app_tempe.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    root.mainloop()
