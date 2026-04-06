from flask import Flask,render_template
from flask_login import LoginManager
from models import db, User
from config import Config

from routes.main.main import main_routes
from routes.auth.auth import auth_routes

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
