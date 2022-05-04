from flask import Flask,render_template
from flask_socketio import SocketIO,emit
import socketio

app=Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio=SocketIO(app,cors_allowed_origins="*")
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('my response',{'data':'connected'})

@socketio.on('my event')
def test_message(message):
    emit('my response',{'data':message['data']})

@socketio.on('my_event')
def test_event(message):
    emit('my response',{'data':message['data']},broadcast=False)

@socketio.on('my broadcast event')
def test_response(message):
    emit('my response',{'data':message['data']},broadcast=True)


if __name__ == "__main__":
    socketio.run(app,debug=True)