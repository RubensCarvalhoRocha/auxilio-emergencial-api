from extensions import db

class AuxilioEmergencial(db.Model):
    __tablename__ = 'auxilio_emergencial'

    id = db.Column(db.BigInteger, primary_key=True)
    ano_mes = db.Column(db.Integer)
    uf = db.Column(db.String(2))
    codigo_ibge_municipio = db.Column(db.Integer)
    municipio = db.Column(db.String(100))
    nis_beneficiario = db.Column(db.String(100))
    cpf_beneficiario = db.Column(db.String(11))
    beneficiario = db.Column(db.String(255))
    nis_responsavel = db.Column(db.String(100))
    cpf_responsavel = db.Column(db.String(11))
    responsavel = db.Column(db.String(255))
    enquadramento = db.Column(db.String(63))
    parcela = db.Column(db.Integer)
    observacao = db.Column(db.String(255))
    valor = db.Column(db.Numeric(10, 2))

    def to_dict(self):
        return {
            "id": self.id,
            "ano_mes": self.ano_mes,
            "uf": self.uf,
            "codigo_ibge_municipio": self.codigo_ibge_municipio,
            "municipio": self.municipio,
            "nis_beneficiario": self.nis_beneficiario,
            "cpf_beneficiario": self.cpf_beneficiario,
            "beneficiario": self.beneficiario,
            "nis_responsavel": self.nis_responsavel,
            "cpf_responsavel": self.cpf_responsavel,
            "responsavel": self.responsavel,
            "enquadramento": self.enquadramento,
            "parcela": self.parcela,
            "observacao": self.observacao,
            "valor": float(self.valor) if self.valor is not None else None
        }
