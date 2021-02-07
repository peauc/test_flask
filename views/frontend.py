from flask import Blueprint, render_template, request, current_app
from models import Personne, db
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def index():
    return render_template('frontend/index.html')


@api.route('/person', methods=('POST', 'GET'))
def add_person():
    if request.method == 'POST':
        age = request.form['age']
        nom = request.form['nom']
        travail = request.form['travail']
        if not age or not nom or not travail:
            return 'age nom and travail required in form'
        person = Personne(age=age, nom=nom, travail=travail)
        with current_app.app_context():
            db.session.add(person)
            db.session.commit()
            return 'ok'
        return 'nok'
    else:
        personnes = Personne.query.all()
        print(len(personnes))
        return render_template('frontend/personnes.html', personnes=personnes)
