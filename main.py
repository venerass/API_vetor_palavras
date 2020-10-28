import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Textos, Vocabularios_t, Vetores_t
import voc_vec as v


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


class Inserir(BaseModel):
    texto: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
@app.get("/")
def root(request: Request, db: Session= Depends(get_db)):
    """
    Recebe os textos, vocabulários e vetores em forma de JSON
    """
    textos = db.query(Textos).all()
    vocabularios = db.query(Vocabularios_t).all()
    vetores = db.query(Vetores_t).all()

    return {
        "Textos": textos,
        "Vocabularios": vocabularios,
        "Vetores": vetores
    }

@app.get("/home")
def home(request: Request, db: Session= Depends(get_db)):
    """
    UI interativa onde pode adicionar e receber os textos, vocabulários e vetores
    """
    textos = db.query(Textos).all()
    vocabularios = db.query(Vocabularios_t).all()
    vetores = db.query(Vetores_t).all()


    return templates.TemplateResponse("home.html", {
        "request": request,
        "Textos": textos,
        "Vocabularios": vocabularios,
        "Vetores": vetores
    })

@app.post("/adc_texto")
def adicionar_texto(inserir_texto: Inserir, db: Session= Depends(get_db)):
    """
    Adc textos ao banco de dados
    """

    #textos

    texto = Textos()
    
    texto.texto = inserir_texto.texto

    db.add(texto)

    db.commit()
    
    #Vocabularios

    

    if(len(db.query(Vocabularios_t).all()) > 0):

        old_voc_1 = db.query(Vocabularios_t).filter_by(id=1).all()[0].vocabularios.split(", ")
        old_voc_2 = db.query(Vocabularios_t).filter_by(id=2).all()[0].vocabularios.split(", ")

        voc1 = ", ".join(v.gerador_voc_1(inserir_texto.texto,old_voc_1))
        voc2 = ", ".join(v.gerador_voc_2(inserir_texto.texto,old_voc_2))

        novo_voc_1 = db.query(Vocabularios_t).filter_by(id=1).first()
        novo_voc_2 = db.query(Vocabularios_t).filter_by(id=2).first()

        novo_voc_1.vocabularios = voc1
        novo_voc_2.vocabularios = voc2

    else:

        voc1 = ", ".join(v.gerador_voc_1(inserir_texto.texto))
        voc2 = ", ".join(v.gerador_voc_2(inserir_texto.texto))

        novo_voc_1 = Vocabularios_t(id=1, vocabularios= voc1)
        novo_voc_2 = Vocabularios_t(id=2, vocabularios= voc2)


    db.add(novo_voc_1)
    db.add(novo_voc_2)


    db.commit()
    
    #vetores

    vetor = Vetores_t()

    # voc_1_list = novo_voc_1.vocabularios.split(", ")
    # voc_2_list = novo_voc_2.vocabularios.split(", ")

    for t in db.query(Vetores_t).all():

        t.gram_1 = "[" + ",".join(v.gerador_vetor_freq_1(t.texto,novo_voc_1.vocabularios.split(", "))) + "]"
        t.gram_2 = "[" + ",".join(v.gerador_vetor_freq_2(t.texto,novo_voc_2.vocabularios.split(", "))) + "]"

        db.add(t)

    
    vetor.texto = inserir_texto.texto
    vetor.gram_1 = "[" + ",".join(v.gerador_vetor_freq_1(inserir_texto.texto,novo_voc_1.vocabularios.split(", "))) + "]"
    vetor.gram_2 = "[" + ",".join(v.gerador_vetor_freq_2(inserir_texto.texto,novo_voc_2.vocabularios.split(", "))) + "]"
    
    db.add(vetor)
    
    db.commit()


    return{
        "code": "sucesso",
        "message" : "texto adicionado"
    }

@app.post("/reset")
def resetar_tabela(db: Session= Depends(get_db)):
    """
    resetar db
    """

    for d in db.query(Textos).all():
        db.delete(d)
        db.commit()

    for d in db.query(Vocabularios_t).all():
        db.delete(d)
        db.commit()
    
    for d in db.query(Vetores_t).all():
        db.delete(d)
        db.commit()

    return {
        "code": "sucesso",
        "message": "db resetada"
    }