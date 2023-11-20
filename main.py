# main.py
import tkinter as tk
from tkinter import ttk
import requests
from src.config import Config
import threading

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter with FastAPI")
        self.root.geometry('350x200')

        self.label = ttk.Label(root, text="API Response:")
        self.label.pack(pady=10)

        self.button = ttk.Button(root, text="Call API", command=self.call_api)
        self.button.pack(pady=10)

    def call_api(self):
        response = requests.get(f'http://{Config.HOST}:{Config.PORT}/api/hello')
        data = response.json()
        self.label.config(text=f"API Response: {data['message']}")

if __name__ == "__main__":
    from fastapi import FastAPI
    from routes.temperatura import Temperatura
    import uvicorn
   
    # Run the API using uvicorn in a separate thread
    api_thread = threading.Thread(target=uvicorn.run, kwargs={'app':Temperatura.app_tempe, 'host': Config.HOST, 'port': Config.PORT})
    api_thread.start()

    # Run the Tkinter app
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
