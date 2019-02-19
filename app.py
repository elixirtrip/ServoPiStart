from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from servotest import MyServo as servo

app = Flask('FlaskServo',
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


socketio = SocketIO(app)

s = servo()


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode,
                           servoPIN=s.servoPIN)


@app.route('/valueofslider')
def slide():
    a = request.args.get('a')
    s.ServoAngle(a)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
