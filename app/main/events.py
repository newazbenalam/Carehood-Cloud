from flask import request, session
from flask_socketio import disconnect, emit, join_room, leave_room
from app import db

from app.main.model import MessageHistory
from .. import socketio

# Dictionary to store message history for each room
message_history = {}

@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    
    # Retrieve message history for this room from the database
    history = MessageHistory.query.filter_by(room=room).all()
    for msg in history:
        emit('message', {'msg': msg.message}, room=request.sid)  # Send history to specific user
    
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    
    # Save the message in the database
    new_message = MessageHistory(room=room, message=session.get('name') + ':' + message['msg'])
    db.session.add(new_message)
    db.session.commit()
    
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)


@socketio.on('connect')
def handle_connect():
    user_id = 'system_link'
    print(f'User {user_id} connected.')
    # socketio.run(app)

@socketio.on('disconnect')
def handle_disconnect():
    user_id = 'system_link'
    if session.get('user_id') != user_id:
        disconnect()
        return
    print(f'User {user_id} disconnected.')

@socketio.on('send_message')
def handle_send_message(data):
    message = data['message']
    print(message)
    emit('receive_message', {'message': message, 'user': 'system_link'}, broadcast=True)