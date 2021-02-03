import socket
import logging
import sys


tcp_ip = '127.0.0.1'
tcp_port = 55000
buffer_size = 2048


try:
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect((tcp_ip, tcp_port))
except socket.error as e:
    logging.error(e.strerror)

output_message = ''

while output_message != 'salir':
    output_message = input('Ingrese un mensaje: ')
    try: 
        tcp_client.sendall(output_message.encode('utf-8'))
    except:
        output_message == 'salir'

tcp_client.close()
  




