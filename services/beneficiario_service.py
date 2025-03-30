from models.beneficiario import BeneficiarioPorEnquadramento

def listar_beneficiarios(limit=200):
    return BeneficiarioPorEnquadramento.query.limit(limit).all()
