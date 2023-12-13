#!/usr/bin/env python3

# Server binds to a port
import zmq

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_string()
    print(f"Received request: {message}")
    reply = "World"
    socket.send_string(reply)
