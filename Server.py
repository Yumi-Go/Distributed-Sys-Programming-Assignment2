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
            "CR_KSDEV_8",
            "CR_KDNET_8",
            "CR_KCOMP_7"
        ],
        [
            "Project (An example assessment would be to create a simple client server application using sockets)\n"
            "20.0% Week 6",
            "Project (Programming assignment(s) using the technologies covered in the lectures.\n"
            "Example assignment(s) will access if a student can apply design patterns to write distributed code,\n"
            "use technologies such as RMI and secure communication and information in transit.)\n"
            "30.0% Week 12"
        ]
    ],
    "SOFT8009": [
        [
            "Apply programming techniques to facilitate the importation, manipulation and cleaning of  data.",
            "Implement exploratory data analysis techniques and interpret results.",
            "Choose and employ appropriate visualization techniques for depicting data."
            "Select and apply basic classification and clustering techniques to a range of  datasets."
            "Evaluate the accuracy and interpret the results of  classification algorithms."
        ],
        [
            "CA_KCOMP_3",
            "HO_KCWMP_8",
            "IY_JCOMP_7"
        ],
        [
            "Open-book Examination: Perform importation, "
            "cleaning and manipulation of a dataset and perform exploratory data analysis.\n"
            "20.0% Week 6",
            "Project: Complete a comprehensive analysis of a real-world dataset "
            "and produce a report documenting findings and incorporating appropriate visualizations.\n"
            "30.0% Week 8"
            "Project: Select and apply appropriate classification techniques to a dataset from a specific application domain."
            "Findings should be documented and supported with appropriate visualisations.\n"
            "50.0% Sem End"
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
                print("from client... ", module_id)

                if module_id in list(my_dictionary):
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

            while True:
                # 6. receive the answer for root question from the client
                data = self.c_socket.recv(1024)
                if not data:
                    break
                if data.decode() == "exit":
                    break
                # if data.decode() == "lo":
                    # self.c_socket.send(bytes(str(my_dictionary[module_id][0]), 'UTF-8'))
                    # for line in my_dictionary[module_id][0]:
                    #     print(line) # for check
                    #     self.c_socket.send(bytes(line), 'UTF-8')

                elif data.decode() == "lo":
                    while True:
                        # 7. send the Learning Outcomes list to the client
                        lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                        self.c_socket.send(lo_list_to_send)

                        while True:
                            # 10. receive the Learning Outcome's menu (among Add, Edit, Delete, or Return) from the client
                            data = self.c_socket.recv(1024)
                            lo_selected = data.decode()
                            print("check here... if add or not", lo_selected) # for check
                            if not lo_selected:
                                break
                            if lo_selected == 'add':
                                # 12-a. receive the Learning Outcome to add from the client
                                data = self.c_socket.recv(1024)
                                lo_to_add = data.decode()
                                print("from client... ", lo_to_add)
                                # print(my_dictionary[module_id][0]) # for check
                                my_dictionary[module_id][0].append(lo_to_add)
                                # print(my_dictionary[module_id][0]) # for check
                                # 13. send the updated Learning Outcomes list to the client
                                updated_lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                                self.c_socket.send(updated_lo_list_to_send)
                                print(updated_lo_list_to_send)  # for check
                            elif lo_selected == 'edit':
                                # 12-e-(1). receive the number of Learning Outcome to overwrite from the client
                                data = self.c_socket.recv(1024)
                                lo_num_to_delete = data.decode()
                                print("from client... ", lo_num_to_delete)
                                # 12-e-(2). receive the text of Learning Outcome to overwrite existing text from the client
                                data = self.c_socket.recv(1024)
                                lo_txt_to_overwrite = data.decode()
                                print("from client... ", lo_txt_to_overwrite)
                                # print(my_dictionary[module_id][0]) # for check
                                index_to_edit = int(lo_num_to_delete) - 1
                                my_dictionary[module_id][0][int(index_to_edit)] = lo_txt_to_overwrite
                                # 13. send the updated Learning Outcomes list to the client
                                updated_lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                                self.c_socket.send(updated_lo_list_to_send)
                                print(updated_lo_list_to_send)  # for check
                            elif lo_selected == 'delete':
                                # 12-d. receive the number of Learning Outcome to delete from the client
                                data = self.c_socket.recv(1024)
                                lo_num_to_delete = data.decode()
                                print("from client... ", lo_num_to_delete)
                                # print(my_dictionary[module_id][0]) # for check
                                index_to_edit = int(lo_num_to_delete) - 1
                                del my_dictionary[module_id][0][int(index_to_edit)]
                                print("after delete") # for check
                                print(my_dictionary[module_id][0]) # for check

                                # 13. send the updated Learning Outcomes list to the client
                                updated_lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                                self.c_socket.send(updated_lo_list_to_send)
                                print(updated_lo_list_to_send)  # for check
                            elif lo_selected == 'return':
                                break
                            elif lo_selected == 'incorrect':
                                print("from client... got incorrect answer")
                        break
                elif data.decode() == "incorrect answer":
                    print("got incorrect answer")

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
