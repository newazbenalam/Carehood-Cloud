#!/bin/env python
import os
from app import create_app, socketio
from dotenv import load_dotenv
load_dotenv()

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app, port=os.getenv('PORT'),  host=os.getenv('HOST'))
