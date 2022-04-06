import socket

# Creating a socket and getting the host name and port number for later
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
# print(host)
port = 1234

s.connect((host, port))
running = True
msgReceived = s.recv(1024)
print(f"Message from host: {msgReceived.decode('utf-8')}")
clientNumber = s.recv(1024).decode('utf-8')
print(f"You are client {clientNumber}!")


while running:
   if clientNumber == '1':
      msgSend = input("\n-->")
      s.send(bytes(msgSend, 'utf-8'))

      if msgSend == 'end':
         running = False
         print("\nGoodbye!")
         break
      else:
         msgReceived = s.recv(1024).decode('utf-8')
         if msgReceived == 'end':
            running = False
            print("\nOther client has disconnected. Goodbye!")
            break
         else:
            print(f"Message from other client: {msgReceived}")

   elif clientNumber == '2':
      msgReceived = s.recv(1024).decode('utf-8')

      if msgReceived == 'end':
         running = False
         print("\nOther client has disconnected. Goodbye!")
         break
      else:
         print(f"Message from other client: {msgReceived}")
         msgSend = input("\n-->")
         s.send(bytes(msgSend, 'utf-8'))
         if msgSend == 'end':
            running = False
            print("\nGoodbye!")
            break

   # if msgSend == 'end':
   #    running = False
   #    print("\nGoodbye!")
   #    break
   # elif msgReceived == 'end':
   #    running = False
   #    print("\nOther client has disconnected. Goodbye!")
   #    break
   




# s.close()