from models.valor_total_beneficio import ValorTotalBeneficio

def listar_valores_totais():
    return ValorTotalBeneficio.query.all()