from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RENOVA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class RespuestasVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p1 = db.Column(db.String(200))
    p2 = db.Column(db.String(200))
    p3 = db.Column(db.String(200))

class RespuestasInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p1 = db.Column(db.String(200))
    p2 = db.Column(db.String(200))
    p3 = db.Column(db.String(200))

# 📌 CREAR BASE DE DATOS Y TABLAS
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video")
def video():
    return render_template("video.html")

@app.route("/preguntasvideo", methods=["GET", "POST"])
def preguntasvideo():
    if request.method == "POST":
        nueva = RespuestasVideo(
            p1=request.form.get("p1"),
            p2=request.form.get("p2"),
            p3=request.form.get("p3")
        )
        db.session.add(nueva)
        db.session.commit()

        return render_template("preguntasvideo.html", respuestas=nueva)

    return render_template("preguntasvideo.html")

@app.route("/informacion")
def informacion():
    return render_template("informacion.html")

@app.route("/preguntasinfo", methods=["GET", "POST"])
def preguntasinfo():
    if request.method == "POST":
        nueva = RespuestasInfo(
            p1=request.form.get("p1"),
            p2=request.form.get("p2"),
            p3=request.form.get("p3")
        )
        db.session.add(nueva)
        db.session.commit()

        return render_template("preguntasinfo.html", respuestas=nueva)

    return render_template("preguntasinfo.html")

@app.route("/agradecimiento")
def agradecimiento():
    return render_template("agradecimiento.html")

if __name__ == "__main__":
    app.run(debug=True)


