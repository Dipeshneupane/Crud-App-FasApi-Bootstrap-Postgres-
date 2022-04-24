from fastapi import Request, Form, APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.model import Web
from app.schemas.schema import WebSchema

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory="templates/")


@router.get("/twoforms", response_class=HTMLResponse)
async def form_get(request: Request, db: Session = Depends(get_db)):
    result = db.query(Web).first()
    print(f'result is {result.name}')
    return templates.TemplateResponse('twoforms.html', context={'request': request, 'result': result})


@router.post("/form1", response_class=HTMLResponse)
def form_post1(request: Request, name: str = Form(...),db: Session = Depends(get_db)):
    _web = Web(name= name)
    db.add(_web)
    db.commit()
    db.refresh(_web)
    return templates.TemplateResponse('twoforms.html',
                                      context={'request': request, 'result': name})


@router.post("/form2", response_class=HTMLResponse)
def form_post2(request: Request, number: int = Form(...)):
    result = number + 100
    return templates.TemplateResponse('twoforms.html',
                                      context={'request': request, 'result': result, 'yournum': number})
