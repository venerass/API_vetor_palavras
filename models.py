from sqlalchemy import Column, Integer, String
from database import Base


class Textos(Base):
    __tablename__ = "textos"

    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String, unique=True, index=True)

class Vocabularios_t(Base):
    __tablename__ = "vocabularios_t"

    id = Column(Integer, primary_key=True, index=True)
    vocabularios = Column(String, index=True)

class Vetores_t(Base):
    __tablename__ = "vetores_t"

    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String, index=True)
    gram_1 = Column(String, index=True)
    gram_2 = Column(String, index=True)