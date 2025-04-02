from flask_restx import Namespace, Resource, fields
from services.uf_total_beneficiarios_service import listar_totais_por_uf

api = Namespace("totais_uf", description="Total de beneficiários por UF")

uf_total_model = api.model("Total de Beneficiários por UF", {
    "uf": fields.String(required=True, description="Unidade da Federação"),
    "total_beneficiarios": fields.Integer(required=True, description="Total de beneficiários"),
})

@api.route("/")
class UFTotalBeneficiariosResource(Resource):
    @api.marshal_list_with(uf_total_model)
    def get(self):
        """Retorna o total de beneficiários por UF"""
        totais = listar_totais_por_uf()
        return [t.to_dict() for t in totais]
