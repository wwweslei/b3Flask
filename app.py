from flask import Flask, render_template
from model.db import Db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Faça. Ou não faça. Não existe a tentativa.'
app.config["DEBUG"] = True




@app.route("/")
def home():
    d = [356.56, 569.58, 365.56]
    position = Db()
    return render_template("index.html", position = position.position(), d = d )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":

    app.run(debug=True, use_reloader=True)
