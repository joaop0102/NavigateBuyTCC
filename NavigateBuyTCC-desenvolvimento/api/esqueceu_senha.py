from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

# Configurações do Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bdnavigate'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'NavigateBuy')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Função para enviar o email
def enviar_email(destinatario, assunto, corpo):
    remetente = "navigatebuy@gmail.com"
    senha = "b q x w a x w u b z k h s t s d" 

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Adiciona suporte para requisições OPTIONS
@app.route('/api/request-password-reset', methods=['OPTIONS', 'POST'])
def request_password_reset():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({"error": "Dados de entrada inválidos."}), 400

    email = data['email']
    user = User.query.filter_by(email=email).first()

    if user:
        link_redefinicao = f"http://localhost:3000/redefinir_senha?email={email}"
        corpo_email = f"""
        <h3>Redefinição de Senha</h3>
        <p>Clique no botão abaixo para redefinir sua senha:</p>
        <a href="{link_redefinicao}" style="padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;">Redefinir Senha</a>
        <p>Se você não solicitou a redefinição de senha, por favor, ignore este email.</p>
        """

        enviar_email(email, "Redefinição de Senha - Navigate Buy", corpo_email)
        return jsonify({"message": "Email de redefinição de senha enviado."}), 200
    else:
        return jsonify({"error": "Email não encontrado."}), 404
    
# Endpoint para redefinir a senha
@app.route('/api/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('password')

    if not email or not new_password:
        return jsonify({"error": "Dados insuficientes."}), 400

    user = User.query.filter_by(email=email).first()

    if user:
        user.password = new_password
        db.session.commit()
        return jsonify({"message": "Senha redefinida com sucesso."}), 200
    else:
        return jsonify({"error": "Usuário não encontrado."}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
