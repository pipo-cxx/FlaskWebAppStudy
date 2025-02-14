from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

## blueprints for convenience
## pages is the name of bp, __name__ is for importing to __init__

@bp.route('/')
def home():
    return render_template("pages/home.html")

@bp.route('/about')
def about():
    return render_template("pages/about.html")