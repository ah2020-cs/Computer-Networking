from socket import *
import time
import sys

def ping(host, port):
  resps = []

  for seq in range(1,11):

  # Send ping message to server and wait for response back 
  # On timeouts, you can use the following to add to resps # resps.append((seq, ‘Request timed out’, 0))
  # On successful responses, you should instead record the server response and the RTT (must compute server_reply and rtt properly)
  # resps.append((seq, server_reply, rtt))

  #Fill in start
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    start = time.time()
    message = 'Ping ' + str(seq) + ' ' + str(start)
    #print(message)
    clientSocket.sendto(message.encode(),(host,port))
    clientSocket.settimeout(1)
    
    try:
        server_reply, serverAddress = clientSocket.recvfrom(1024)
        rtt = float(time.time()-start)
    except timeout:
        resps.append((seq, 'Request timed out', 0))
        clientSocket.close()
    else:
        resps.append((seq, server_reply.decode(), rtt))
  #Fill in end

  return resps
if __name__ == '__main__':
  resps = ping('127.0.0.1', 12000)
  print(resps)



