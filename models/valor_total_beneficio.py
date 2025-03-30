class ValorTotalBeneficio(db.Model):
    __tablename__ = 'valor_total_beneficio'

    uf = db.Column(db.String(2), primary_key=True)
    valor_total = db.Column(db.Numeric(15, 2), nullable=False)

    def to_dict(self):
        return {
            "uf": self.uf,
            "valor_total": float(self.valor_total)
        }
