from fastapi import APIRouter,Request

tempe_c = None
viscosidade = None
massa_espe = None


Router_temp = APIRouter()

@Router_temp.post('/incluir_temperatura', status_code=200,tags=['temperatura'])
async def temperatura(request: Request):
        global tempe_c
        tempe_c = await request.json()
        print("temperatura", tempe_c)

        return tempe_c
            