from fastapi import FastAPI,Request


tempe_c = None
viscosidade = None
massa_espe = None


class Temperatura:
    app_tempe = FastAPI()

    @app_tempe.post('/api/temperatura', status_code=200)
    async def temperatura(request: Request):
        global tempe_c
        tempe_c = await request.json()
        print("temperatura", tempe_c)
        return tempe_c
            