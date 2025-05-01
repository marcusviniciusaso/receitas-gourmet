from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configurações da Aplicação
# class Config:
#     SECRET_KEY = 'sua_chave_secreta'
#     CACHE_TYPE = 'simple'
#     SWAGGER = {
#         'title': 'Catálogo de Receitas Gourmet',
#         'uiversion': 3
#     }

#     SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     JWT_SECRET_KEY = 'sua_chave_jwt_secreta'

app = Flask(__name__)

# app.config.from_object(Config)

app.config.from_object('config')

# print(app.config['SECRET_KEY'])
# print(app.config['SQLALCHEMY_DATABASE_URI'])
# print(app.config['SWAGGER'])
# print(app.config['CACHE_TYPE'])

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    time_minutes = db.Column(db.Integer, nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de dados criado!")