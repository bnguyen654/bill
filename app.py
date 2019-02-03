from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit
import secrets
from Games import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.FLASK_SECRET_KEY;
socketio = SocketIO(app)
GAMES = {}


@app.route("/")
def index():
    return render_template('index.html')


@socketio.on("create")
def create_game(data):
    gm = Game(data['name'])
    room = gm.id
    GAMES[room] = gm
    join_room(room)
    emit('join_room', {'room'})



if __name__ == "__main__":
    socketio.run(host='0.0.0.0')
