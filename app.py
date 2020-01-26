from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Faça. Ou não faça. Não existe a tentativa.'
app.config["DEBUG"] = True




@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True, use_reloader=True)
