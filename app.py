
from flask import Flask, render_template, request
#from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap

@app.route('/')
def index():
    my_list = ['apples', 'oranges', 'grapes', 'pineapples']
    return render_template('index.html', async_mode=socketio.async_mode, my_list = my_list)

@app.route('/meow')
def meow():
    return 'MEOW.'

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)