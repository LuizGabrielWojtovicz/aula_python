from formulario import db, app, User

with app.app_context():
    db.create_all()