from extensions import db

class BeneficiarioPorEnquadramento(db.Model):
    __tablename__ = 'beneficiarios_por_enquadramento'

    uf = db.Column(db.String(2), primary_key=True)
    extra_cadun = db.Column(db.BigInteger, default=0)
    bolsa_familia = db.Column(db.BigInteger, default=0)
    cadun_nao_bolsa = db.Column(db.BigInteger, default=0)

    def to_dict(self):
        return {
            "uf": self.uf,
            "extra_cadun": self.extra_cadun,
            "bolsa_familia": self.bolsa_familia,
            "cadun_nao_bolsa": self.cadun_nao_bolsa
        }
