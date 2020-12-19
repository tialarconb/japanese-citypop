from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/comingsoon')
def comingsoon():
    return render_template('comingsoon.html')

@bp.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('app.home'))