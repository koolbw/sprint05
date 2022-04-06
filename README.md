# Overview

For this project I wanted to learn about networking so I made a program that will allow two clients/computers to send messages back and forth.

To acomplish this I created a program that works with the Client/Server method. That means that to use the program you have to run the server.py file then the client.py file on each of the computers that you would like to connect. 

For now the server only handles two clients but at a later time can be improved to handle multiple clients/computers to connect.

# Network Communication

I used a client to server conncection so that in the future the server can help multiple computers connect and not just two. 

I just used the default port that is used with the socket library (1234).

Whenever you are sending messages between the clients through the server each string is encoded using 'utf-8' encoding and is decoded before being used/displayed.

# Development Environment

While working on this project I used the following:

* VS Code
* Python 3.10
* Socket Library

# Useful Websites

* [Python Sockets Documentation](https://docs.python.org/3.6/library/socket.html)
* [Tutorials Point](https://www.tutorialspoint.com/python/python_networking.htm)
* [Alto Palo](https://alto-palo.com/blogs/connect-two-computers-using-secure-socket-programming-in-python/)

# Future Work

Some things I would do in the future if I had time to expand on this code:
* First off I would probably make it so more than two computers can connect at the same time.
* I would probably also add the option so that you can choose which commputer you wanted to send a message to.
* I would make it look a little better aesthetic wise.