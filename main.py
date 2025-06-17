from fastapi import FastAPI, HTTPException, Depends, status, Response
from sqlalchemy.orm import Session
import models,schemas
from database import SessionLocal, engine, Base
from utils import formatar_status, formatar_destinatario, formatar_endereco

# Cria as tabelas no banco de dados com base nos modelos (caso ainda não existam)
Base.metadata.create_all(bind=engine)

# Instancia o app FastAPI
app = FastAPI(title="MyDeliveryAPI")

# Função utilitária para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db # Entrega a sessão para ser usada em rotas
    finally:
        db.close() # Fecha a sessão após o uso

# Rota para criar uma nova entrega
@app.post("/entregas", response_model=schemas.EntregaOut, status_code=201)
def criar_entrega(entrega: schemas.EntregaCreate, db: Session = Depends(get_db)):
    nova_entrega = models.Entrega(
        destinatario=formatar_destinatario(entrega.destinatario),
        endereco=formatar_endereco(entrega.endereco),
        status=formatar_status("pendente")
    )
    db.add(nova_entrega)
    db.commit()
    db.refresh(nova_entrega)
    return nova_entrega

# Rota para listar todas as entregas
@app.get("/entregas/", response_model=list[schemas.EntregaOut])
def listar_entregas(db: Session = Depends(get_db)):
    return db.query(models.Entrega).all()

# Rota para buscar uma entrega específica pelo ID
@app.get("/entregas/{entrega_id}", response_model=schemas.EntregaOut)
def buscar_entrega(entrega_id: int, db: Session = Depends(get_db)):
    entrega = db.get(models.Entrega, entrega_id)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega não encontrada")
    return entrega

# Rota para atualizar o status de uma entrega
@app.put("/entregas/{entrega_id}", response_model=schemas.EntregaOut)
def atualizar_entrega(entrega_id: int, dados: schemas.EntregaUpdate, db: Session = Depends(get_db)):
    entrega = db.get(models.Entrega, entrega_id)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega não encontrada")

    if dados.status is not None:
        entrega.status = formatar_status(dados.status)

    db.commit()
    db.refresh(entrega)
    return entrega

# Rota para deletar uma entrega
@app.delete("/entregas/{entrega_id}", status_code=204)
def deletar_entrega(entrega_id: int, db: Session = Depends(get_db)):
    entrega = db.get(models.Entrega, entrega_id)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega não encontrada")
    db.delete(entrega)
    db.commit()
    return Response(status_code=204)
