from models.beneficiario import BeneficiarioPorEnquadramento

def listar_beneficiarios():
    return BeneficiarioPorEnquadramento.query.all()
