from flask import Flask, render_template
import core
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Faça. Ou não faça. Não existe a tentativa.'
app.config["DEBUG"] = True


@app.route("/")
def home():
    position = core.get_value_positions()
    return render_template("index.html", position=position)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
