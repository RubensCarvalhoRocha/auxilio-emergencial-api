from flask_restx import Namespace, Resource, fields
from services.beneficiario_service import listar_beneficiarios

api = Namespace("beneficiarios", description="Dados dos beneficiários por enquadramento")

beneficiario_model = api.model("Beneficiario", {
    "uf": fields.String(required=True, description="Unidade da Federação"),
    "extra_cadun": fields.Integer(description="Beneficiários extra CadÚnico"),
    "bolsa_familia": fields.Integer(description="Beneficiários do Bolsa Família"),
    "cadun_nao_bolsa": fields.Integer(description="Beneficiários do CadÚnico não Bolsa Família"),
})

@api.route("/")
class BeneficiariosResource(Resource):
    @api.marshal_list_with(beneficiario_model)
    def get(self):
        """Retorna os beneficiários por enquadramento"""
        beneficiarios = listar_beneficiarios()
        return [b.to_dict() for b in beneficiarios]
