from flask import Flask, jsonify, request, render_template

#Flask: la clase principal para crear la aplicación
#jsonify: convierte datos de Python (listas, diccionarios) a formato JSON para enviárselos al frontend
#request: permite recibir y leer los datos que el frontend le manda al servidor
#render_template: permite servir archivos HTML desde la carpeta templates ya que asi se hace normalmente

app = Flask(__name__)  #simplemente se crea la aplicacion __name__

tareas = ["Teoria de Probabilidades", "Software I"]  #lista en memoria que funciona como base de datos temporal

@app.route('/')  #esta ruta es la principal, cuando se entra  a localhost:5000 sirve el HTML
def inicio():
    return render_template('fronted.html')  #busca el archivo dentro de la carpeta templates y lo manda al navegador

@app.route('/tareas', methods=['GET']) #lo que hace esto es que crea una ruta 
def obtener_tareas():
    return jsonify(tareas) # lo convierte a json y lo manda a fronted

@app.route('/tareas', methods=['POST']) #tambien hace lo mismo pero para cuando alguien quiera crear una nueva tarea
def agregar_tarea():
    nueva = request.json.get('tarea')
    tareas.append(nueva)# aqui se agrega la tarea en este caso ya que es POST
    return jsonify({"mensaje": "Tarea agregada"}), 201 #simplemente muestra que se agrego y el estado 

if __name__ == '__main__':
    app.run(debug=True)