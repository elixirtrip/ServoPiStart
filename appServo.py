from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap
from servotest import MyServo as servo

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

s = servo()


@app.route('/')
def index():
    return render_template('indexServo.html', async_mode=socketio.async_mode,
                           servoPIN=s.servoPIN)


@app.route('/meow')
def meow():
    return 'MEOW.'


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
