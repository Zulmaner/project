import socket

import os

ClientSocket = socket.socket()

host = '192.168.73.130'

port = 8888



os.system('clear')

print('Waiting for connection')

try:

    ClientSocket.connect((host, port))

except socket.error as e:

    print(str(e))



Response = ClientSocket.recv(1024)

print(Response)

Response = ClientSocket.recv(1024)

print(Response)

Continue = True

while True: 

   # while Continue:

        Input = int(input('1 : Scissors \n2: Rock \n3: Paper \n\n enter number for selection: '))
        if  Input < 4 and Input > 0 :

            ClientSocket.send(str.encode(str(Input)))

            Response = ClientSocket.recv(1024)

            print(Response.decode('utf-8'))

            Input = input('\nContinue Y/N :' )

            Input = Input.upper()

            if Input == 'Y' or Input == 'N' :

            	ClientSocket.send(str.encode(Input))

            	os.system('clear')

            	Response = ClientSocket.recv(1024)
            	print(Response)
            	sgnl = ClientSocket.recv(1024)
            	
            	if sgnl.decode('utf-8') == 'd' :
            	   break
ClientSocket.close()
