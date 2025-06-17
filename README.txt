#MyDeliveryAPI

Uma API RESTful simples para gerenciamento de entregas, desenvolvida com Python, FastAPI e SQLite. Projeto criado como parte do meu processo de estudo.


#Funcionalidades:

- Cadastrar entrega (`POST /entregas`)
- Listar todas as entregas (`GET /entregas`)
- Buscar entrega por ID (`GET /entregas/{id}`)
- Atualizar status da entrega (`PUT /entregas/{id}`)
- Deletar entrega (`DELETE /entregas/{id}`)


#Tecnologias utilizadas:

- Python 3.10+
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn


#Como executar:

1 - Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

2 - Instale as dependências:
pip install -r requirements.txt

3 - Rode o servidor:
uvicorn main:app --reload

4 - Acesse a documentação interativa:
http://127.0.0.1:8000/docs


# Rodando testes automatizados

1 - Se não estiver com o (venv) ativado, execute:
.\venv\Scripts\activate

2 - Instale o pytest dentro do ambiente virtual
pip install pytest
pip install httpx

3 - Execute o pytest
pytest