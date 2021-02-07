from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Personne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    travail = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Personne {self.nom}>'
