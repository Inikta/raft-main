from server_module import Server
import time

server = Server('127.0.0.1:8082', ['127.0.0.1:8080', '127.0.0.1:8081'])

time.sleep(5)

print("Server 3")
server.run()