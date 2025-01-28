import client_module.client
import client_module.object
import time
import random
from server_module.utils import separate_address

network = [separate_address(address) for address in ['127.0.0.1:8080', '127.0.0.1:8081', '127.0.0.1:8082', '127.0.0.1:8083', '127.0.0.1:8084']]
client = client_module.client.Client(network)

time.sleep(8)

i = 1
while (True):
    key = str(i) + '_client1_message'
    client.manual_send({key : 'random message'})
    i += 1 
    
    time.sleep(random.randint(1, 3))