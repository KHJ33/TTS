from flask import Blueprint, render_template

bp = Blueprint('about', __name__, url_prefix='/about')

@bp.route('/index/')
def index():

    return render_template("about/about.html")