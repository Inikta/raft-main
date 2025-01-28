from server_module.server import Server
import time

server_name = "Server #1"
server = Server('127.0.0.1:8080', ['127.0.0.1:8081', '127.0.0.1:8082', '127.0.0.1:8083', '127.0.0.1:8084'], server_name)

time.sleep(5)

print("Server 1")
server.run()