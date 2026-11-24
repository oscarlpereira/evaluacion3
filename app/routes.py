from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = ""
    estado = ""
    if request.method == "POST":
        try:
            nota1 = float(request.form.get("nota1",""))
            nota2 = float(request.form.get("nota2",""))
            nota3 = float(request.form.get("nota3",""))
            asistencia = float(request.form.get("porcentajeasistencia", ""))
        except ValueError:
            estado = "Ingresa solo números válidos"
            return render_template("ejercicio1.html", promedio=promedio, estado=estado)
        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 4 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"


    return render_template("ejercicio1.html", promedio=promedio, estado=estado)

@main.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mas_largo = ""
    cantidad = ""

    if request.method == "POST":
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        mas_largo = nombre1
        if len(nombre2) > len(mas_largo):
            mas_largo = nombre2
        if len(nombre3) > len(mas_largo):
            mas_largo = nombre3

        cantidad = len(mas_largo)

    return render_template("ejercicio2.html", mas_largo=mas_largo, cantidad=cantidad)