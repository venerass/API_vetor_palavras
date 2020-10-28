import models
from fastapi import FastAPI, Request, Depends
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from models import Textos, Vocabularios_t, Vetores_t
import voc_vec as v

 
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

voc = v.Vocabularios()


@app.get("/adc_texto/{inserir_texto}")
def adicionar_texto(inserir_texto: str):

    voc.atualizar_vocabularios(inserir_texto)

    voc1 = ", ".join(voc.vocabulario_1)
    voc2 = ", ".join(voc.vocabulario_2)



    vetor1 = "[" + ",".join(v.gerador_vetor_freq_1(inserir_texto,voc.vocabulario_1)) + "]"
    vetor2 = "[" + ",".join(v.gerador_vetor_freq_2(inserir_texto,voc.vocabulario_2)) + "]"
    
    return{
        "texto": inserir_texto,
        "voc1": voc1,
        "voc2" : voc2,
        "vetor1": vetor1,
        "vetor2": vetor2
    }
