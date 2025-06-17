from pydantic import BaseModel, ConfigDict
from typing import Optional

# Modelo base para uma entrega, usado como estrutura comum
class EntregaBase(BaseModel):
    destinatario: str
    endereco: str

# Modelo usado para criação de uma nova entrega (reutiliza os campos do modelo base)
class EntregaCreate(EntregaBase):
    pass # Não adiciona campos extras além dos já definidos em EntregaBase

# Modelo usado para atualização de uma entrega (ex: atualização de status)
class EntregaUpdate(BaseModel):
    status: Optional[str] = None

# Modelo de saída (resposta da API) com todos os campos que serão retornados
class EntregaOut(EntregaBase):
    id: int
    status: str
# Configuração do modelo Pydantic para usar atributos como campos
    model_config = ConfigDict(from_attributes=True)