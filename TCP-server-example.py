import socket

# Creating the socket object
socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

# Binding the socket
socketserver.bind((host, port))

# Starting TCP listener
socketserver.listen(3)

while True:
    # Starting the connection
    clientsocket, address = socketserver.accept()

    print('recieved connetion from ' % str(address))
    message = 'Hello! Thank you for connecting to the server' + '\r\n'

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
