from client_module import ReplicatedDict
import time
import random

repl_dict = ReplicatedDict(['127.0.0.1:8080', '127.0.0.1:8081', '127.0.0.1:8082'])

time.sleep(8)

time.sleep(8)

i = 1
while (True):
    key = str(i) + '_serv2_message'
    repl_dict[key] = 'random message_' + str(i)
    i += 1 
    
    time.sleep(random.randint(1, 3))
