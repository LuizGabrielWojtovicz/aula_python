from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'  # Use o URI do banco de dados desejado
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    message = db.Column(db.Text, nullable=True)

class ExampleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    message = TextAreaField('Message', validators=[Length(max=200)])
    submit = SubmitField('Submit')

@app.route("/", methods=["GET", "POST"])
def index():
    form = ExampleForm()
    if form.validate_on_submit():

        user = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
            message=form.message.data
        )

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success')) 
    return render_template('teste_2.html', form=form)

@app.route("/success")
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)