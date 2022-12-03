import pickle
import socket
import threading

my_dictionary = {
    "SOFT8023": [
        [
            "Evaluate and apply design patterns in the design and development of a distributed system.",
            "Assess and apply different architectural patterns in a distributed system.",
            "Critically access and apply threading in a distributed application.",
            "Debug a distributed client/server application, identifying object properties and variables at run-time.",
            "Create a distributed object application using RMI, allowing client/server to communicate securely via interfaces and objects."
        ],
        [
            "prog1",
            "prog2"
        ],
        [
            "assess1",
            "assess2"
        ]
    ],
    "SOFT8009":
        [
            [
                "lo1",
                "lo2",
                "lo3"
            ],
            [
                "prog1",
                "prog2"
            ],
            [
                "assess1",
                "assess2"
            ]
        ]
}

# learning_outcome = "1. Evaluate and apply design patterns in the design and development of a distributed system.\n" \
#                    "2. Assess and apply different architectural patterns in a distributed system.\n" \
#                    "3. Critically access and apply threading in a distributed application.\n" \
#                    "4. Debug a distributed client/server application, identifying object properties and variables at run-time.\n" \
#                    "5. Create a distributed object application using RMI, allowing client/server to communicate securely via interfaces and objects.\n"



class ClientThread(threading.Thread):

    def __init__(self, client_address, client_socket, identity):
        threading.Thread.__init__(self)
        self.c_socket = client_socket
        print("Connection no. " + str(identity))
        print("New connection added: ", client_address)

    def run(self):
        print("Connection from : ", clientAddress)

        while True:
            while True:
                # 2. receive module ID from client
                data = self.c_socket.recv(1024)
                if not data:
                    break
                module_id = data.decode()
                print("from client", module_id)

                if module_id in list(my_dictionary):
                    # print(list(my_dictionary))
                    # 3. send boolean value to client (for existence of module ID in dictionary)
                    self.c_socket.send(bytes('1', 'UTF-8'))
                    break
                # if module_id is not in my_dictionary, loop until it matches
                self.c_socket.send(bytes('0', 'UTF-8'))


            # while True:
            #     if module_id in list(my_dictionary):
            #         # print(list(my_dictionary))
            #         # 3. send boolean value to client (for existence of module ID in dictionary)
            #         self.c_socket.send(bytes('True', 'UTF-8'))
            #         break
            #     else:
            #         self.c_socket.send(bytes('Enter the correct Module ID!', 'UTF-8'))

            # 6. receive the request for Learning Outcomes from the client
            data = self.c_socket.recv(1024)
            if not data:
                break
            # if data.decode() == "request LO":
                # self.c_socket.send(bytes(str(my_dictionary[module_id][0]), 'UTF-8'))
                # for line in my_dictionary[module_id][0]:
                #     print(line) # for check
                #     self.c_socket.send(bytes(line), 'UTF-8')

            # 7. send the Learning Outcomes to the client
            lo_to_send = pickle.dumps(my_dictionary[module_id][0])
            self.c_socket.send(lo_to_send)

            # 10. receive the Learning Outcome to be added
            data = self.c_socket.recv(1024)
            lo_to_add = data.decode()
            added_result = str(my_dictionary[module_id][0].append(lo_to_add))
            self.c_socket.send(bytes(added_result, 'UTF-8'))

        print("Client at ", clientAddress, " disconnected...")


LOCALHOST = "127.0.0.1"
PORT = 64003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

# print("Server started")
# print("Waiting for client request..")
print("Module System 1.0")
# print("What is the module id?")

counter = 0

while True:
    server.listen(1)
    my_socket, clientAddress = server.accept()
    counter = counter + 1
    new_thread = ClientThread(clientAddress, my_socket, counter)
    new_thread.start()
