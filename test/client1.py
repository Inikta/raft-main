import client_module.object

repl_dict = client_module.object.ReplicatedDict(['127.0.0.1:8080', '127.0.0.1:8081', '127.0.0.1:8082'])

repl_dict['hello'] = 'world!'
repl_dict['omg'] = 1
repl_dict['replicated'] = 'Hello other client!'