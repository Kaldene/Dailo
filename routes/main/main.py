from flask import blueprints,render_template

main_routes = blueprints.Blueprint('main', __name__)

@main_routes.route('/home')
@main_routes.route('/')
def home():
    return render_template('index.html')