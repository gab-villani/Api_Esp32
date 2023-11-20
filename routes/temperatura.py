from fastapi import FastAPI,Request


tempe_c = None
viscosidade = None
massa_espe = None


class Temperatura:
    app_tempe = FastAPI()

    @app_tempe.post('/api/temperatura')
    def temperatura(request:Request):
        global tempe_c
        tempe_c = request.json()
        print("temperatura",tempe_c)
        
        return tempe_c
        