from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['auth'])
#todos os caminhos que criar nesta rota, o domínio do site será:
#dominio/auth/
#todas as rotas entram na documentaçao /docs
#pode colocar mais de uma tag

@auth_router.get('/')
async def autenticar():
    """
    Essa é a rota padrão de autenticação.
    """
    return {'message': 'Você acessou a rota padrão de autenticação', 'autenticado': False}

