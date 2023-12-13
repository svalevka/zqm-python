Create zqm client and server in python using PAIR socket.
Client sends messages to server every 3 seconds.

Start containers
```
docker-compuse up --build
```
You can see messages exchange in docker compose outputs
BUT it only works if I set  'network_mode = host'