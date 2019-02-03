from flask import Flask, render_template
from flask_socketio import SocketIO
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.FLASK_SECRET_KEY;
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    socketio.run(host='0.0.0.0')
