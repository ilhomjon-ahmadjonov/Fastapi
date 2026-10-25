from fastapi import FastAPI
from accounts.router import router as acc_router
from products.router import router as pr_router
from movie.router import router as mv_router
from library.router import router as li_router
from restaurant.router import router as res_router

app = FastAPI()

app.include_router(router=acc_router,prefix='/accounts')
app.include_router(router=pr_router,prefix='/products')
app.include_router(router=mv_router,prefix='/movies')
app.include_router(router=li_router,prefix='/librarys')
app.include_router(router=res_router,prefix='/restaurants')

# @app.get('/')
# def ishla():
#     return {'my name is Ilkhom'}