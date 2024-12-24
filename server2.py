from server_module import Server
import time

server = Server('127.0.0.1:8081', ['127.0.0.1:8080', '127.0.0.1:8082'])

time.sleep(5)

print("Server 2")
server.run()
