#!/usr/bin/env python3
'''
ZMQ Client
'''

import zmq
import time
import os
server=os.environ.get("server")
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://{server}:42069")
print(f"Publisher: {server}")

# Subscribe to all messages (empty string matches all topics)
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    message = socket.recv_string()
    print(f"Received message: {message}")