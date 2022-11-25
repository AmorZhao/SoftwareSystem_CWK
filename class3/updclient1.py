import socket
import time
#the server name and port client wishes to access
server_name = 'localhost'
server_port = 12000
client_port1 = 11000
#create a UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind (('', client_port1))

print("UDP client running...");
print("Connecting to server at IP: ", server_name, " PORT: ", server_port)

for i in range (1, 101):
    msg = str(i)
    time.sleep(1)
    
    #send the message to the udp server
    client_socket.sendto(msg.encode(),(server_name, server_port))

#client_socket.close()
