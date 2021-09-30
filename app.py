from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/prueba2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lqditflmvevwsw:6a39b9f645f4b512e12e7e42221186c2eedd3b255ce4d6482cfd7c8ed9a27320@ec2-54-83-137-206.compute-1.amazonaws.com:5432/d1890fir2j27oe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

# Importar los modelos
from models import Song, User, Room

# Crear el esquema de la DB
db.create_all()
db.session.commit()

# Rutas de paginas
@app.route('/')
def get_home():
    return 'Este es el home'

@app.route('/signup')
def sign_up():
    return 'Esta es la pagina de registro'


@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    fecha = request.form["birthdate"]

    genre = ""
    if(request.form["genre"] == 'masculino'):
        genre = "Masculino"

    elif(request.form["genre"] == 'femenino'):
        genre = "Femenino"

    elif(request.form["genre"] == 'otro'):
        genre = "Femenino"
        genre = "Otro"
     

    user = User(email, password, fecha, genre)

    db.session.add(user)
    db.session.commit()
    return "Ok"


@app.route('/room')
def enter_room():
    return render_template("room.html")

@app.route('/create_room',methods=['POST'])
def create_room():
    room_code = request.form["room_code"]
    print("El codigo de sale es: ",room_code)
    return "Ok"


# Rutas de otras acciones
@app.route('/song', methods=['GET','POST'])
def crud_song():
    if request.method == 'GET':
        # Hago algo
        print("Llegó un GET")

        # insertar canción
        name = "Perfect"
        artist = "Ed Sheeran"
        genre = "Rock"
        album = "Romanticonas"
        year = 2017
        link = "https://youtu.be/2Vv-BfVoq4g"

        entry = Song(name,artist,genre,album,year,link)
        db.session.add(entry)
        db.session.commit()

        return 'Esto fue un GET'

    elif request.method == 'POST':
        # Registrar una cancion
        request_data = request.form
        name = request_data['name']
        artist = request_data['artist']
        genre = request_data['genre']

        print("Nombre:" + name)
        print("Artista:" + artist)
        print("Genero:" + genre)

        # Insertar en la base de datos la canción

        return 'Se registro la canción exitosamente'


@app.route('/updatesong')
def update_song():
    old_name = "Imagine"
    new_name = "Despacito"
    old_song = Song.query.filter_by(name=old_name).first()
    old_song.name = new_name
    db.session.commit()
    return "Actualizacion exitoso"

@app.route('/getsongs')
def get_songs():
    songs = Song.query.all()
    print(songs[0].artist)
    #for song in songs: ...crear registro HTML
    return "Se trajo la lista de canciones"

@app.route('/deletesong')
def delete_song():
    song_name = "Despacito"
    song = Song.query.filter_by(name=song_name).first() 
    db.session.delete(song)
    db.session.commit()
    return "Se borro la cancion"



if __name__ == "__main__":
    app.run()
