from sqlalchemy import Column, Integer, String
from database import Base

# Modelo de tabela: Entrega
class Entrega(Base):
    __tablename__ = "entregas" # Nome da tabela no banco

    # Cada coluna da tabela com seus tipos e propriedades
    id = Column(Integer, primary_key=True, index=True) 
    destinatario = Column(String, index=True)
    endereco = Column(String)
    status = Column(String, default="Pendente")   