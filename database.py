from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
DATABASE_URL = "sqlite:///./entregas.db"

# Cria o engine de conexão com o banco
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma fábrica de sessões de banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base usada pelos modelos
Base =  declarative_base()

