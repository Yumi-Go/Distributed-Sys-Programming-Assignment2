import json
import pickle
import socket
import threading

import pika

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
            "Choose and employ appropriate visualization techniques for depicting data.",
            "Select and apply basic classification and clustering techniques to a range of  datasets.",
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
            "30.0% Week 8",
            "Project: Select and apply appropriate classification techniques to a dataset from a specific application domain."
            "Findings should be documented and supported with appropriate visualisations.\n"
            "50.0% Sem End"
        ]
    ]
}


class ClientThread(threading.Thread):

    def __init__(self, client_address, client_socket, identity):
        threading.Thread.__init__(self)
        self.c_socket = client_socket
        print("Connection no. " + str(identity))
        print("New connection added: ", client_address)

    def run(self):
        print("Connection from : ", clientAddress)

        while True:
            # 2. receive module ID from client
            data = self.c_socket.recv(1024)
            if not data:
                print("No data recognized")

            module_id = data.decode().upper()
            print("from client... ", module_id)

            if module_id in list(my_dictionary):
                # 3. send boolean value to client (for existence of module ID in dictionary)
                self.c_socket.send(bytes('1', 'UTF-8'))
                break
            # if module_id is not in my_dictionary, loop until it matches
            self.c_socket.send(bytes('0', 'UTF-8'))

        while True:
            while True:
                # 6. receive the answer for root question from the client
                data = self.c_socket.recv(1024)
                root_option_selected = data.decode()
                print("from client... ", root_option_selected)
                if root_option_selected == "exit":
                    break
                if root_option_selected == 'none':
                    print("from client... No data")
                elif root_option_selected == "lo":
                    while True:
                        # 7-l. send the Learning Outcomes list to the client
                        lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                        self.c_socket.send(lo_list_to_send)

                        # 10. receive the Learning Outcome's menu (among Add, Edit, Delete, or Return) from the client
                        data = self.c_socket.recv(1024)
                        sub_option_selected = data.decode()
                        rabbitmq_record(clientAddress, module_id, root_option_selected, sub_option_selected)
                        if not sub_option_selected:
                            print("from client... No data")
                        if sub_option_selected == 'add':
                            # 12-a. receive the Learning Outcome to add from the client
                            data = self.c_socket.recv(1024)
                            lo_to_add = data.decode()
                            print("from client... ", lo_to_add)
                            my_dictionary[module_id][0].append(lo_to_add)
                            # 13-a. send the updated Learning Outcomes list to the client
                            updated_lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                            self.c_socket.send(updated_lo_list_to_send)
                        elif sub_option_selected == 'edit':
                            recent_lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                            # 11-e. send the recent LO list to the client if LO list is not empty
                            self.c_socket.send(recent_lo_list_to_send)
                            if len(my_dictionary[module_id][0]) > 0:

                                if data:
                                    # 14-e. receive the number, text of Learning Outcome to overwrite from the client
                                    data = self.c_socket.recv(1024)
                                    lo_num_text_to_edit = pickle.loads(data)
                                    print("from client... ", lo_num_text_to_edit)

                                    index_to_edit = int(lo_num_text_to_edit[0]) - 1
                                    my_dictionary[module_id][0][int(index_to_edit)] = lo_num_text_to_edit[1]

                                    # 15-e. send the updated Learning Outcomes list to the client
                                    updated_lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                                    self.c_socket.send(updated_lo_list_to_send)
                                else:
                                    print("from client... No data")
                            else:
                                print("Learning Outcomes List is empty")
                                break
                        elif sub_option_selected == 'delete':
                            recent_lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                            # 11-d. send the recent LO list to the client if LO list is not empty
                            self.c_socket.send(recent_lo_list_to_send)
                            if len(my_dictionary[module_id][0]) > 0:
                                # 14-d. receive the number of Learning Outcome to delete from the client
                                data = self.c_socket.recv(1024)

                                if data:
                                    lo_num_to_delete = data.decode()
                                    print("from client... ", lo_num_to_delete)
                                    index_to_delete = int(lo_num_to_delete) - 1
                                    del my_dictionary[module_id][0][int(index_to_delete)]

                                    # 15-d. send the updated Learning Outcomes list to the client
                                    updated_lo_list_to_send = pickle.dumps(my_dictionary[module_id][0])
                                    self.c_socket.send(updated_lo_list_to_send)
                                else:
                                    print("from client... No data")
                            else:
                                print("Learning Outcomes List is empty")
                                break
                        elif sub_option_selected == 'return':
                            break
                        elif sub_option_selected == 'incorrect':
                            print("from client... got incorrect answer")
                elif root_option_selected == "course":
                    rabbitmq_record(clientAddress, module_id, root_option_selected, "N/A")
                    while True:
                        # 7-c. send the Courses list to the client
                        course_list_to_send = pickle.dumps(my_dictionary[module_id][1])
                        self.c_socket.send(course_list_to_send)
                        break
                elif root_option_selected == "assess":
                    rabbitmq_record(clientAddress, module_id, root_option_selected, "N/A")
                    while True:
                        # 7-a. send the Assessments list to the client
                        assess_list_to_send = pickle.dumps(my_dictionary[module_id][2])
                        self.c_socket.send(assess_list_to_send)
                        break
                elif root_option_selected == "incorrect":
                    print("got incorrect answer")
            break
        print("Client at ", clientAddress, " disconnected...")


LOCALHOST = "127.0.0.1"
PORT = 64003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Module System 1.0")

counter = 0

while True:
    # time.sleep(.10)
    server.listen(1)
    my_socket, clientAddress = server.accept()
    counter = counter + 1
    new_thread = ClientThread(clientAddress, my_socket, counter)
    new_thread.start()

    def rabbitmq_record(client_address, module, root_option_selected, sub_option_selected):

        message = [client_address, module, root_option_selected, sub_option_selected]

        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # we could parameterize the host
        channel = connection.channel()
        channel.queue_declare(queue='module-stats')
        channel.basic_publish(exchange='',
                              routing_key='module-stats',
                              body=json.dumps(message))
        connection.close()
