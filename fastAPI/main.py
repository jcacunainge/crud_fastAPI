from fastapi import FastAPI
import uvicorn

import v1.model.Model as model
from v1.db.config import engine
from v1.router.router import router as router_crud

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tienda de libros GECELCA",
    description="PRUEBA DE PROCESO CRUD",
    version="1.0.0"
)

app.include_router(router=router_crud, tags=["CRUD DE PRUEBA"], prefix="/books")

if __name__ == "__main__":
    uvicorn.run("entrypoint:app",
                host="localhost",
                reload=True)