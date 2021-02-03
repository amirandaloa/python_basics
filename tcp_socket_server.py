import socketserver
import sys
import time
import threading

class TCPSocketServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = ''
        while data != 'salir':
            try:
                data = self.request.recv(2048)
                print(data.decode('utf-8'))
                time.sleep(1)
            except KeyboardInterrupt:
                print('C/S')
                data = 'salir'

class ThreadTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def main():
    tcp_ip = '127.0.0.1'
    tcp_port = 55000
    sever = ThreadTCPServer((tcp_ip, tcp_port), TCPSocketServer)
    thread = threading.Thread(target=sever.serve_forever)
    thread.start()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()