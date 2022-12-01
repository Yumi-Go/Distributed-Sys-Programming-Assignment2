import socket
import threading

my_dictionary = {
    "SOFT8023": [["lo1", "lo2", "lo3"], ["prog1", "prog2"], ["assess1", "assess2"]],
    "SOFT8009": [["lo1", "lo2", "lo3"], ["prog1", "prog2"], ["assess1", "assess2"]]
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
                break
            module_id = data.decode()
            print("from client", module_id)
            if module_id in list(my_dictionary):
                # print(list(my_dictionary))
                # 3. send boolean value to client (for existence of module ID in dictionary)
                self.c_socket.send(bytes('True', 'UTF-8'))

            # Add learning outcome
            data = self.c_socket.recv(1024)
            if not data:
                break
            add_lo = data.decode()
            added_result = str(my_dictionary[module_id][0].append(add_lo))
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
