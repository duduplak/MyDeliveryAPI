# Remove espaços extras e capitaliza
def formatar_status(status: str) -> str:
    return status.strip().title()

def formatar_destinatario(nome: str) -> str:
    return nome.strip().title()

def formatar_endereco(endereco: str) -> str:
    return endereco.strip().title()