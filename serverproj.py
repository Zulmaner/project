import socket

import sys

import time

import errno

from multiprocessing import Process



ok_message = 'HTTP/1.0 200 OK\n\n'

nok_message = 'HTTP/1.0 404 NotFound\n\n'





if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(("",8888))

    print("listening...")

    s.listen(2)

    try:

        while True:

            try:

                A = 0
                B = 0

                s1_sock, s1_addr = s.accept()

                s1_sock.send(str.encode('you are player 1! \nWaiting for other connection'))

                s2_sock, s2_addr = s.accept()

                s2_sock.send(str.encode('you are player 2! '))

                s1_sock.send(str.encode('Match Found!'))

                s2_sock.send(str.encode('Match Found!'))

                while True: 

                    c1 = int(s1_sock.recv(1024))

                    c2 = int(s2_sock.recv(1024))

                    if c1 == c2:

                        s1_sock.send(str.encode('Draw!'))

                        s2_sock.send(str.encode('Draw!'))

                    elif c1 == 1 :

                        if c2 == 2 :

                            B = B + 1

                            s1_sock.send(str.encode('Lose!\nScore : You '+str(A)+':'+str(B)+ ' Opponent' ))

                            s2_sock.send(str.encode('Win!\nScore : Opponent '+str(A)+':'+str(B)+ ' You'))

                        elif c2 ==3 :

                            A = A + 1 

                            s1_sock.send(str.encode('Win!\nScore : You '+str(A)+':'+str(B)+ ' Opponent' ))

                            s2_sock.send(str.encode('Lose!\nScore : Opponent '+str(A)+':'+str(B)+ ' You'))

                    elif c1 == 2 :

                        if c2 == 3 :

                            B = B + 1

                            s1_sock.send(str.encode('Lose!\nScore : You '+str(A)+':'+str(B)+ ' Opponent' ))

                            s2_sock.send(str.encode('Win!\nScore Opponent : '+str(A)+':'+str(B)+ ' You'))

                        elif c2 == 1 :

                            A = A + 1 

                            s1_sock.send(str.encode('Lose!\nScore : You '+str(A)+':'+str(B)+ ' Opponent' ))

                            s2_sock.send(str.encode('Win!\nScore Opponent : '+str(A)+':'+str(B)+ ' You'))

                        else :

                            A = A + 1 

                            s1_sock.send(str.encode('Win!\nScore : You  '+str(A)+':'+str(B)+ ' Opponent' ))

                            s2_sock.send(str.encode('Lose!\nScore : Opponent '+str(A)+':'+str(B)+ ' You'))

                    elif c1 == 3 :

                        if c2 == 1 :

                            B = B + 1

                            s1_sock.send(str.encode('Lose!\nScore : You '+str(A)+':'+str(B)+ ' Opponent' ))

                            s2_sock.send(str.encode('Win!\nScore : Opponent '+str(A)+':'+str(B)+ ' You'))

                        elif c2 == 2 :

                            A = A + 1 

                            s1_sock.send(str.encode('Win!\nScore : You '+str(A)+':'+str(B)+ ' Opponent' ))

                            s2_sock.send(str.encode('Lose!\nScore : Opponent '+str(A)+':'+str(B)+ ' You'))

                    c1 = s1_sock.recv(1024)

                    c2 = s2_sock.recv(1024)

                    if c1.decode('utf-8') == 'Y' :
                        if c2.decode('utf-8') =='Y' :

                           s1_sock.send(str.encode('Match accepted!\nScore : You '+str(A)+':'+str(B)+ ' Opponent'))

                           s2_sock.send(str.encode('Match accepted!\nScore : Opponent '+str(A)+':'+str(B)+ ' You'))
                           print('new game')
                           time.sleep(1)
                           s1_sock.send(str.encode('c'))
                           s2_sock.send(str.encode('c'))

                    elif c1.decode('utf-8') == 'N' :

                        s1_sock.send(str.encode('Disconnected!\nScore : You '+str(A)+':'+str(B)+ ' Opponent'))

                        s2_sock.send(str.encode('Disconnected!\nScore : Opponent '+str(A)+':'+str(B)+ ' You'))
                        time.sleep(1)
                        s1_sock.send(str.encode('d'))

                        s2_sock.send(str.encode('d'))
                        break
                    else :

                        s1_sock.send(str.encode('Disconnected!\nScore : You '+str(A)+':'+str(B)+ ' Opponent'))

                        s2_sock.send(str.encode('Disconnected!\nScore : Opponent '+str(A)+':'+str(B)+ ' You'))
                        time.sleep(1)
                        s1_sock.send(str.encode('d'))

                        s2_sock.send(str.encode('d'))
                        break
                s2_sock.close()

                s1_sock.close()

                

            except socket.error:



                print('got a socket error')



    except Exception as e:        

                print('an exception occurred!')
                print(e)
                sys.exit(1)

    finally:

     	   s.close()
