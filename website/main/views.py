from flask import render_template, Blueprint, request, session, current_app

home = Blueprint('home',__name__,url_prefix="/")

@home.route('/', methods=('GET', 'POST'))
def homepage():
    return render_template("main/main.html")