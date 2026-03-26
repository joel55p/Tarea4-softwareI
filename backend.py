from flask import Flask, jsonify, request, render_template

#Flask: clase principal de la aplicación
#jsonify: convierte datos Python a JSON
#request: lee datos que manda el frontend
#render_template: sirve archivos HTML desde templates

# PATRÓN FACTORY: función que construye y configura la app
def create_app():
    app = Flask(__name__)

    # PATRÓN MVC - MODEL: datos de la aplicación
    tareas = ["Teoria de Probabilidades", "Software I"]

    # PATRÓN MVC - VIEW: sirve el HTML al usuario
    @app.route('/')
    def inicio():
        return render_template('fronted.html')

    # PATRÓN DECORATOR: registra cada funcion a una URL específica
    # PATRON MVC - CONTROLLER: recibe peticiones y devuelve respuestas

    @app.route('/tareas', methods=['GET'])
    def obtener_tareas():
        return jsonify(tareas) # convierte a JSON y manda al frontend

    @app.route('/tareas', methods=['POST'])
    def agregar_tarea():
        nueva = request.json.get('tarea')
        tareas.append(nueva) # agrega la tarea nueva al model
        return jsonify({"mensaje": "Tarea agregada"}), 201

    return app # PATRÓN FACTORY: retorna la app lista para usar

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)