import socketserver
import socket
import time
import sys
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    input=int(input("Enter 1 for forever server and 2 for a server of 30 seconds: "))
    if input==1:
    # Create the server, binding to localhost on port 9999
        with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            server.serve_forever()
    elif input==2:
        time_len=30
        print('TIMED SERVER STARTS WITH {0} seconds'.format(time_len))
        server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
        for i in range(time_len):
            time.sleep(1)
            print('server has remaining time: ',time_len-i)
        server.server_close()
        print('server closed')



