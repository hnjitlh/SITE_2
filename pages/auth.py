from flask import Blueprint, g, session, redirect, abort, render_template, escape, flash, request
from backend.objs.User import User
from app import db
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['username']
        pw = request.form['password']
        if check_username(name):
            # we can create a user
            usr = User(name=name, )
        else:
            abort(500)
            # user name already exists, should not happen


@auth.route('/check_username', methods='GET')
def check_username():
    if request.method == 'GET':
        username = request.args['id']
        if User.query.filter_by(name=username) is not None:
            return True
    return False


def check_username(uname):
    return User.query.filter_by(name=uname) is None
