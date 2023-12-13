#!/usr/bin/env python3
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5555")

request_number = 0
while True:  # Infinite loop to keep the client running
    print(f"Sending request {request_number} ...")
    socket.send_string(f"Hello {request_number}")

    message = socket.recv_string()
    print(f"Received reply {request_number} [{message}]")

    time.sleep(3)  # Wait for 3 seconds before sending the next message
    request_number += 1
