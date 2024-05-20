from flask import Flask, render_template, request, redirect
import os
import database as db #importamos las datos de las conexiones a la base de datos


# Obtener la ruta del proyecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Unir la ruta del proyecto con las carpetas src y templates
template_dir = os.path.join(template_dir, 'src', 'templates')  

# Configurar Flask con la ruta de las templates para lanzar el aplicativo en puerto libre
app = Flask(__name__, template_folder=template_dir, static_folder='static') #Le inidicamos a flask el directorio donde esta almacenado nuestro template

#Rutas de la aplicación
##Ruta principal de la aplicación
@app.route('/') # @app es la variable inicializada de Flask. El / permite con el nombre de la aplicacion accedemos el index html

##Vinculamos a esta ruta una funcion que llamameremos home para poder acceder al index
def home():
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM usuarios')
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columNames = [column[0] for column in cursor.description] #Nombres de campos
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close    
    return render_template('index.html', data=insertObject)

# @app es la ruta para guardar usauarios en la bd
@app.route('/user', methods=['POST'] ) 
def addUser():
    first_name = request.form('first_name')
    last_name = request.form('last_name')
    username = request.form('username')
    city = request.form('city')
    zip = request.form('zip')
    terms_accepted = request.form()
    

#Creamos una condicion que si se lanza como programa principal el main se ejecute
if __name__ == '__main__':
    app.run(debug=True, port=4000)
