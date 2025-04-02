from extensions import db

class UFTotalBeneficiarios(db.Model):
    __tablename__ = 'uf_total_beneficiarios'

    uf = db.Column(db.String(2), primary_key=True)
    total_beneficiarios = db.Column(db.BigInteger, nullable=False)

    def to_dict(self):
        return {
            "uf": self.uf,
            "total_beneficiarios": self.total_beneficiarios
        }
