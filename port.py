import socket

def scan_port(ip,port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5)
  try:
     connect = sock.connect((ip,port))
     print('Port :',port,' is open.')
     connect.close()
  except:
     pass

ip = '192.168.0.1'
for i in range(1000):
  scan_port(ip,i)
