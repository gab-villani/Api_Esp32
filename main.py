from fastapi.middleware.cors import CORSMiddleware
from src.config import Config
import threading
from fastapi import FastAPI
import uvicorn
import tkinter as tk
from app import MyApp
from routes.temperatura import Router_temp

# Criação da instância FastAPI
fastapi_app = FastAPI(
    title="Api Instrumentacao",
    description="Telemetria",
    version="1.0.0",
)

# Configuração do CORS
origins = ["*"]
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adição das rotas
fastapi_app.include_router(Router_temp, prefix='/api/temperatura')

# Função para iniciar o mainloop do Tkinter
def start_tkinter():
    root = tk.Tk()
    my_app_instance = MyApp(root)
    root.mainloop()

# Inicialização da thread para o FastAPI
fastapi_thread = threading.Thread(
    target=uvicorn.run,
    kwargs={'app': fastapi_app, 'host': Config.HOST, 'port': Config.PORT + 1}
)

# Inicialização da thread para a aplicação Tkinter
tkinter_thread = threading.Thread(target=start_tkinter)

# Inicialização simultânea das duas threads
fastapi_thread.start()
tkinter_thread.start()
