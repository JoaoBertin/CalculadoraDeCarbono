#xxxxx
#------------------------------------------- Bibliotecas ------------------------------------------------------

from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "senha123"

@app.route("/")
def index():
    return render_template("index.html")

# xxxxx
if __name__ == "__main__":
    app.run( debug=True )

