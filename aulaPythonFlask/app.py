from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_users():
    conn = sqlite3.connect('project.db')  # Substitua pelo caminho do seu banco de dados
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')  # Substitua 'users' pelo nome da sua tabela
    users = cursor.fetchall()
    conn.close()
    return users

@app.route('/users')
def index():
    users = get_users()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)