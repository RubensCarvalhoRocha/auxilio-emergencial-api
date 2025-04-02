from models.uf_total_beneficiarios import UFTotalBeneficiarios

def listar_totais_por_uf():
    return UFTotalBeneficiarios.query.all()
