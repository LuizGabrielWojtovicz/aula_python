from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from config import app, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
from forms import RegisterForm, LoginForm

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    from forms import RegisterForm

    formulario = RegisterForm()

    if formulario.validate_on_submit():
        usu = formulario.username.data
        sen = formulario.password.data
        print(f'-- {usu} -- {sen}')

        usu_ex = User.query.filter_by(username=usu).first()

        if usu_ex:
            print('Usuario ja existe')
        else:
            novo_usuario = User(username=usu, password=sen)
            db.session.add(novo_usuario)
            db.session.commit()
            print('Usuario Criado')


    return render_template('register.html', form=formulario)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print("A")
        return redirect(url_for('dashboard'))  # Redirect to dashboard if already logged in

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print("B")
        print(password)
        user = User.query.filter_by(username=username).first()
        print(user)
        print(user.username)
        print(type(user.password))
        print(type(password))
        print(check_password_hash(user.password, password))
        if user.password == password:
            login_user(user)
            print("C")
            return redirect(url_for('dashboard'))  # Redirect to dashboard after login
        
        flash('Login Unsuccessful. Please check username and password', 'danger')
    else:
        print("D")
        print("Form Errors:", form.errors)  # Print form errors to debug validation issues

    print("Form Data:", form.data)  # Print form data for debugging
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    return render_template('create_event.html')


@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    return render_template('edit_event.html')


@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
