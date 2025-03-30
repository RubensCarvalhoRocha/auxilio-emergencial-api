# 📦 API Auxílio Emergencial - Dados Públicos

API REST construída com **Flask** + **PostgreSQL**, que expõe dados abertos do Governo Brasileiro sobre o **Auxílio Emergencial**, organizados por **enquadramento de beneficiários por UF**.

Inclui documentação Swagger interativa.

---

## 🛠️ Tecnologias

- Python 3.10+
- Flask
- Flask-RESTX (Swagger)
- SQLAlchemy
- PostgreSQL (Railway)
- dotenv (`.env`)

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/RubensCarvalhoRocha/auxilio-emergencial-api.git
```
### 2. Instale as dependências
```bash
pip install -r requirements.txt
```
### 3. Configure as variáveis de ambiente no arquivo .env

### 4. Rode a aplicação
```bash
python app.py
```
📚 Acessando a documentação Swagger
Após iniciar a API, acesse: http://localhost:5000

Você verá todos os endpoints documentados com exemplos e descrições interativas.

### Boas práticas aplicadas
✅ Uso de Blueprints via namespaces do Flask-RESTX

✅ Organização em camadas (model, service, controller)

✅ Documentação automática via Swagger

✅ Uso de .env para proteger credenciais

✅ SQLAlchemy ORM para manipulação de dados (ou consultas diretas, se preferir)
