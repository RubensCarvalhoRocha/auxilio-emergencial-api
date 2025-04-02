from flask_restx import Namespace, Resource, fields
from services.populacao_estados_service import listar_populacao_estados

api = Namespace("populacao-estados", description="População dos Estados em 2024")

populacao_model = api.model("População por Estado", {
    "uf": fields.String(required=True, description="Unidade da Federação"),
    "populacao": fields.Integer(description="População estimada para 2024"),
})

@api.route("/")
class PopulacaoEstadosResource(Resource):
    @api.marshal_list_with(populacao_model)
    def get(self):
        """Retorna a população estimada dos estados em 2024"""
        populacoes = listar_populacao_estados()
        return [p.to_dict() for p in populacoes]
