from models.populacao_estados_2024 import PopulacaoEstados2024

def listar_populacao_estados():
    return PopulacaoEstados2024.query.all()
