import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_entrega():
    response = client.post("/entregas", json={
        "destinatario": "João Pedro",
        "endereco": "Rua das Laranjeiras, 456"
    })
    if response.status_code != 201:
        print(response.json())
    assert response.status_code == 201
    data = response.json()
    assert data["destinatario"] == "João Pedro"
    assert data["endereco"] == "Rua Das Laranjeiras, 456"
    assert data["status"] == "Pendente"

def test_criar_entrega_dados_invalidos():
    # Destinatário ausente
    response = client.post("/entregas", json={
        "endereco": "Rua dos Testes, 321"
    })
    assert response.status_code == 422  # Unprocessable Entity


def test_atualizar_entrega():
    # Primeiro cria uma entrega
    response = client.post("/entregas", json={
        "destinatario": "Carlos",
        "endereco": "Rua Nova, 789"
    })
    entrega = response.json()
    entrega_id = entrega["id"]

    # Atualiza o status da entrega
    response = client.put(f"/entregas/{entrega_id}", json={"status": "Em rota"})
    assert response.status_code == 200
    updated = response.json()
    assert updated["status"] == "Em Rota"

    
def test_atualizar_entrega_inexistente():
    # Tenta atualizar uma entrega que não existe
    response = client.put("/entregas/999999", json={"status": "Entregue"})
    assert response.status_code == 404

def test_deletar_entrega():
    # Cria uma entrega para deletar
    response = client.post("/entregas", json={
        "destinatario": "Teste Delete",
        "endereco": "Rua Fantasma, 000"
    })
    entrega_id = response.json()["id"]

    # Deleta a entrega
    response = client.delete(f"/entregas/{entrega_id}")
    assert response.status_code == 204

    # Confirma que não existe mais
    response = client.put(f"/entregas/{entrega_id}", json={"status": "Entregue"})
    assert response.status_code == 404

def test_listar_entregas():
    response = client.get("/entregas/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_obter_entrega_por_id():
    response = client.post("/entregas", json={
        "destinatario": "Joana",
        "endereco": "Rua Joana, 123"
    })
    entrega_id = response.json()["id"]

    response = client.get(f"/entregas/{entrega_id}")
    assert response.status_code == 200
    assert response.json()["destinatario"] == "Joana"

def test_get_entrega_inexistente():
    response = client.get("/entregas/999999")
    assert response.status_code == 404