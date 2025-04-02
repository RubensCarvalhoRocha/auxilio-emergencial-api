from models.beneficiario_por_enquadramento import BeneficiarioPorEnquadramento

def listar_beneficiarios():
    return BeneficiarioPorEnquadramento.query.all()
