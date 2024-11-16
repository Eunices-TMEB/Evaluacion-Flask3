from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario1Notas', methods=['GET', 'POST'])
def formulario1Notas():
    try:
        if request.method == 'POST':
            if not all(key in request.form for key in ['nota1', 'nota2', 'nota3', 'asistencia']):
                abort(400, description="Faltan campos requeridos")

            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            for nota in [nota1, nota2, nota3]:
                if not (10 <= nota <= 70):
                    abort(400, description="Las notas deben estar entre 10 y 70")

            if not (0 <= asistencia <= 100):
                abort(400, description="La asistencia debe estar entre 0 y 100")

            promedio = (nota1 + nota2 + nota3) / 3
            estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

            return render_template('formulario1Notas.html',
                                promedio=round(promedio, 1),
                                estado=estado,
                                mostrar_resultado=True)

    except ValueError:
        abort(400, description="Los valores ingresados deben ser números")

    return render_template('formulario1Notas.html', mostrar_resultado=False)

@app.route('/formulario2Nombres', methods=['GET', 'POST'])
def formulario2Nombres():
    try:
        if request.method == 'POST':
            if not all(key in request.form for key in ['nombre1', 'nombre2', 'nombre3']):
                abort(400, description="Faltan campos requeridos")

            nombre1 = request.form['nombre1'].strip()
            nombre2 = request.form['nombre2'].strip()
            nombre3 = request.form['nombre3'].strip()

            if not all([nombre1, nombre2, nombre3]):
                abort(400, description="Los nombres no pueden estar vacíos")

            if len(set([nombre1, nombre2, nombre3])) != 3:
                abort(400, description="Los nombres deben ser diferentes")

            nombres = [nombre1, nombre2, nombre3]
            nombre_mas_largo = max(nombres, key=len)
            longitud = len(nombre_mas_largo)

            return render_template('formulario2Nombres.html',
                                nombre_largo=nombre_mas_largo,
                                longitud=longitud,
                                mostrar_resultado=True)

    except Exception as e:
        abort(400, description=str(e))

    return render_template('formulario2Nombres.html', mostrar_resultado=False)


if __name__ == '__main__':
    app.run(debug=True)