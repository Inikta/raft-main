from server_module import Server

server = Server('127.0.0.1:8082', ['127.0.0.1:8080', '127.0.0.1:8081'])
server.run()
