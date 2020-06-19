# Write your code here :-)
import sys
import socket
import thread

if __name__=="__main__":
    HOST = '192.168.0.12'
    PORT = 33333

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = ''

    def pr_msg():
        while 1:
            data = s.recv(1024)
            if data:
                print data.upper()
    thread.start_new_thread(pr_msg, ())

    while 1:
        send_data = raw_input()
        if send_data in ['quit', 'Quit', 'QUIT']:
            s.send('Client Quit')
            thread.exit()
            s.close()
        s.send('Client : ' + send_data)