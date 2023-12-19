#!/usr/bin/env python3
# '''
# ZMQ server
# '''
# # Server binds to a port
# import zmq
# import time

# context = zmq.Context()
# socket = context.socket(zmq.PUB)
# socket.bind("tcp://*:42069")


# # List of static messages to be published
# static_messages = [
#     "Hello, World!",
#     "This is a static message.",
#     "Another static message.",
# ]

# while True:
#     for message in static_messages:
#         socket.send_string(message)
#         time.sleep(1)  

'''
ZMQ server and a basic Hello World web page
'''

import zmq
import time
from flask import Flask

app = Flask(__name__)

# ZMQ server setup
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:42069")

# List of static messages to be published
static_messages = [
    "Hello, World!",
    "This is a static message.",
    "Another static message.",
]

# Flask route to display "Hello, World!" on port 5000
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Start Flask web server
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

    # Start ZMQ server
    while True:
        for message in static_messages:
            socket.send_string(message)
            time.sleep(1)