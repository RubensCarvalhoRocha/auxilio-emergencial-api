from flask_restx import Namespace, Resource, fields
from services.valor_total_beneficio_service import listar_valores_totais

api = Namespace("valores_totais", description="Valores totais dos benefícios por UF")

valor_total_model = api.model("Valor Total do Benefício", {
    "uf": fields.String(required=True, description="Unidade da Federação"),
    "valor_total": fields.Float(required=True, description="Valor total do benefício"),
})

@api.route("/")
class ValorTotalBeneficioResource(Resource):
    @api.marshal_list_with(valor_total_model)
    def get(self):
        """Retorna os valores totais dos benefícios por UF"""
        valores = listar_valores_totais()
        return [v.to_dict() for v in valores]
