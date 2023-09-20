# Overview
Using Python Sockets, I created an application that allows a remote client to send commands to a server component to get employee details.
## Client:
A menu-driven console-based program (using Sockets) that allows the user to get information about the modules offered at MTU. Of the query data listed, only the learning outcomes can be edited by the user.
## Server:
Using Socket programming, accept a connection from a client and handle the options
# Extra features
I modified the sockets server program to handle multiple simultaneous client connections.
I modified the server so that each time a request is received for a module, a message is sent to a message queue with the module id, the command and options sent from the client, as well as IP address details. Then I wrote a simple script to print out the activity log details using RabbitMQ.
