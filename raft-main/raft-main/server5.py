from server_module.server import Server
import time

server_name = "Server #5"
server = Server('127.0.0.1:8084', ['127.0.0.1:8080', '127.0.0.1:8081', '127.0.0.1:8082', '127.0.0.1:8083'], server_name)

time.sleep(0)

print("Server 5")
server.run()