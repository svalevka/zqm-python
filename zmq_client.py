#!/usr/bin/env python3
'''
ZMQ Client
'''

import zmq
import time
import os
server=os.environ.get("server")

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect(f"tcp://{server}:5555")

request_number = 0
while True:  # Infinite loop to keep the client running
    print(f"Sending request {request_number} ...")
    socket.send_string(f"Hello {request_number}")

    message = socket.recv_string()
    print(f"Received reply {request_number} [{message}]")

    time.sleep(1)  # Wait for 3 seconds before sending the next message
    request_number += 1
