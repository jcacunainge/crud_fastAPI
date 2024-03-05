# app/routes.py
from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from v1.db.config import SessionLocal, get_db
from sqlalchemy.orm import Session
from v1.schema.schema import BookSchema, Response, BookSchema
from fastapi.encoders import jsonable_encoder

from v1.utils import crud

# Creamos un router, que es un conjunto de rutas agrupadas
router = APIRouter()

# Creamos la ruta con la que crearemos 
@router.post("/create")
async def create_book_service(request: BookSchema, db: Session = Depends(get_db)):
    crud.create_book(db, book=request)
    print(request)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully",result=request).dict(exclude_none=True)
    # retornamos la respuesta con el schema de response


@router.get("/")
async def get_books( db: Session = Depends(get_db)):
    _books = crud.get_book(db)
    result_books = jsonable_encoder(_books)
    return Response(status="Ok", code="200", message="Success fetch all data", result=result_books)


@router.patch("/update")
async def update_book(request: BookSchema, db: Session = Depends(get_db)):
    try:
        _book = crud.update_book(db, book_id=request.id,
                                title=request.title, description=request.description)
        return Response(status="Ok", code="200", message="Success update data", result=_book)
    except Exception as e:
        return Response(
            status="bad",
            code="304",
            message="the updated gone wrong"
        )

@router.delete("/delete")
async def delete_book(request: BookSchema,  db: Session = Depends(get_db)):
    try:
        crud.remove_book(db, book_id=request.id)
        return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
    except Exception as e:
        return Response(
            status="bad",
            code="",
            message="the deleted gone wrong"
        )
    # colocamos una excepción por si ocurre un error en la escritura en la db