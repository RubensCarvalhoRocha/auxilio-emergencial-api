class PopulacaoEstados2024(db.Model):
    __tablename__ = 'populacao_estados_2024'

    uf = db.Column(db.String(2), primary_key=True)
    populacao = db.Column(db.BigInteger, nullable=False)

    def to_dict(self):
        return {
            "uf": self.uf,
            "populacao": self.populacao
        }
