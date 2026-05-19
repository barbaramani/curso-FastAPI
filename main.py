#para colocar api no ar, executar no terminal: uvicorn main:app --reload
#ou seja, cria um executor usando uvicorn e roda o aplicativo main

from fastapi import FastAPI
app = FastAPI(title='Criando uma API')

#depois de criar o app, vai importar os arquivos de rotas

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

#criando rotas, que podem ser as requisiçoes:
# GET -> leitura/pegar, 
# POST -> enviar/criar, 
# PUT/PATCH -> edição, 
# DELETE -> deletar

#endpoint:
#dominio.com/pedidos/lista