from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    usuario = "Luiz"
    itens = ["fruta", "verdura", "carne"]
    return render_template('teste.html', titulo="Pagina Inicial", usuario=usuario,itens=itens)

if __name__ == '__main__':
    app.run(debug=True)
