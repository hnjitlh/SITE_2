from flask import Blueprint, g, session, redirect, render_template, escape, flash, request
from backend.objs.User import User
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['username']
        pw = request.form['password']
        error = None


@auth.route('/check_username', methods='GET')
def check_username():
    if request.method == 'GET':
        username = request.data['id']
        return True
    return False
