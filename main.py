import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

socketio = SocketIO(app)

users = {}
chats = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', users=users, chats=chats)

# TRŪKSTA:
# TO DO: Live typing indication - 50 % (left to make indication for users typo too)
# TO DO: Sent/Delivered/Seen statuses
# TO DO: Per session chat history (save as output?)
# TO DO: Load chat history for user too (after refresh keep in same old room?)
# TO DO: Alert new user, new messages for admin (+autoadd new user to chat menu)
# TO DO: Break words if they are tooooooo long to fit chatbox window
# TO DO: Doesn't work input required
# TO DO: If user message room != current admin room change chat menu button color
# TO DO: Add log out/disconnected

# Get username
@socketio.on('username', namespace='/message')
def receive_username(username):
    room = request.sid
    users[room] = username
    chats[room] = ''
    send(username + ' has entered the room.')
    emit('creat_room', room)

# Send user messages
@socketio.on('user_message', namespace='/message')
def user_message(data):
    username = data['username']
    message = data['message']
    room = data['room']
    msg = username + ': ' + message
    chats[room] = chats[room] + msg + '<br>'
    emit('print_message', msg, room=room)    # broadcast=True

# Send admin messages
@socketio.on('admin_message', namespace='/message')
def admin_message(data):
    room = data['room']
    message = data['message']
    msg = 'Agent: ' + message
    chats[room] = chats[room] + msg + '<br>'
    emit('print_message', msg, room=room)

# Open one of chat in admin dashboard
@socketio.on('chat_menu', namespace='/message')
def chat_chat(data):
    join_room(data['room'])
    past_messages = chats[data['room']]
    emit('show_past_messages', past_messages)

# Live typing indicator
@socketio.on('typing', namespace='/message')
def live_typing(data):
    room = data['room']
    emit('display', data, room=room)


@socketio.on_error(namespace='/message')
def chat_error_handler(e):
    print('An error has occurred: ' + str(e))



# @socketio.on('leave')
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', room=room)
#
# @socketio.on('connect')
# def test_connect():
#     emit('my response', {'data': 'Connected'})
#
# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
