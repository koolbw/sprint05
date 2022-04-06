import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ints = socket(domain, type, protocol)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234
s.bind((host, port))

# client01 = ''
# client02 = ''

# Going to start listening for any clients trying to connect to the server
print("LISTENING...")
s.listen(5)
running = True

while True:
   c1, addr1 = s.accept()
   client01 = addr1
   print(f'Got connection from {client01}(CLIENT01)!')
   c1.send(bytes('Thank you for connecting!', 'utf-8'))
   c1.send(bytes('1', 'utf-8'))

   c2, addr2 = s.accept()
   client02 = addr2
   print(f'Got connection from {client02}(CLIENT02)!')
   c2.send(bytes('Thank you for connecting!', 'utf-8'))
   c2.send(bytes('2', 'utf-8'))



   while running:
      msgReceived1 = c1.recv(1024).decode('utf-8')
      # msgDecoded1 = msgReceived1.decode('utf-8')
      c2.send(bytes(msgReceived1, 'utf-8'))
      # msgSend = input("\n-->")
      # c1.send(bytes(msgSend, 'utf-8'))

      msgReceived2 = c2.recv(1024).decode('utf-8')
      # msgDecoded2 = msgReceived2.decode('utf-8')
      c1.send(bytes(msgReceived2, 'utf-8'))

      # if msgSend == 'end':
      #    running = False
      #    print("\nGoodbye!")
      #    break
      if msgReceived1 == 'end' or msgReceived2 == 'end':
         running = False
         print("\nGoodbye!")
         break

   break
   # c.close()
