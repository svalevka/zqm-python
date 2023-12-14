#!/usr/bin/env python3
'''
ZMQ server
'''
# Server binds to a port
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")


# List of static messages to be published
static_messages = [
    "Hello, World!",
    "This is a static message.",
    "Another static message.",
]

while True:
    for message in static_messages:
        socket.send_string(message)
        time.sleep(1)  