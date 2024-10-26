from http import HTTPStatus
from fastapi import FastAPI
from fast_zero.routers import auth, users, todos
from fast_zero.schemas import Message

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

# @app.get('/users/{user_id}', response_model=UserPublic)
# def read_user_by_id(user_id: int, session: Session = Depends(get_session)):
#     db_user = session.scalar(select(User).where(User.id == user_id))
#     if not db_user:
#         raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')
#     return db_user
