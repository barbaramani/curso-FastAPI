from fastapi import APIRouter

order_router = APIRouter(prefix='/pedidos', tags=['pedidos'])

#criando rota
#sempre começa com /
@order_router.get('/')
async def pedidos():#async que diz que é uma função assincrona
    """
    Essa é a rota padrão de pedidos. Todos os pedidos precisam de autenticação.
    """
    return {'message': 'Você acessou a rota de pedidos'}