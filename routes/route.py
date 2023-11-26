from fastapi import APIRouter,Request,Response
from fastapi.responses import JSONResponse

tempe_c = []
rotacao = []
pressao = []
vazao = []
forca = []


Router = APIRouter()

@Router.post('/incluir_pacote', status_code=200,tags=['pacote'])
async def pacote(request: Request):
        global tempe_c,rotacao,pressao,vazao,forca
        pacote = await request.json()
        print("pacote",pacote)
        temperatura =pacote['temperatura']
        rotacao_ = pacote['rotacao']
        pressao_ = pacote['pressao']
        vazao_ = pacote['vazao']
        forca_ = pacote['forca']
        tempe_c.append(temperatura)
        rotacao.append(rotacao_)
        pressao.append(pressao_)
        vazao.append(vazao_)
        forca.append(forca_)

        return JSONResponse(content={'success': True}, status_code=200)


    

    
            