from flask import Flask
from config import Config
from extensions import db
from flask_restx import Api

from controllers.beneficiario_por_enquadramento_controller import api as beneficiario_ns
from controllers.populacao_estados_controller import api as populacao_estados_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    api = Api(app, version="1.0", title="API Auxilio Emergencial",
              description="API REST para onter os dados do auxilio emergencial", doc="/docs")

    api.add_namespace(beneficiario_ns, path="/beneficiarios")
    api.add_namespace(populacao_estados_ns, path="/populacao-estados")

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
