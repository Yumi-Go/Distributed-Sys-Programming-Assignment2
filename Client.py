import pickle
import socket

SERVER = "127.0.0.1"
PORT = 64003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

response = ""
data_to_send_moduleID = ""
# learning_outcome = "1. Evaluate and apply design patterns in the design and development of a distributed system.\n" \
#                    "2. Assess and apply different architectural patterns in a distributed system.\n" \
#                    "3. Critically access and apply threading in a distributed application.\n" \
#                    "4. Debug a distributed client/server application, identifying object properties and variables at run-time.\n" \
#                    "5. Create a distributed object application using RMI, allowing client/server to communicate securely via interfaces and objects.\n"

learning_outcome = []

while response != 'X' or response != 'x':

    while True:
        # 1. send module ID
        data_to_send_moduleID = input("What is the module id? ")
        sock.sendall(bytes(data_to_send_moduleID, 'UTF-8'))
        # 4. receive true or false for existence of module ID in data dictionary from the server
        data = sock.recv(1024)
        # print(data) # for check
        # print(repr(data))
        bool_data = bool(int(data))
        print(bool_data)  # for check
        if bool_data:
            response = input("(L)earning Outcomes, (C)ourses, (A)ssessments or e(X)it? ")
            if response == 'L' or response == 'l':
                # 5. send the request for Learning Outcomes to the server
                sock.sendall(bytes("request LO", 'UTF-8'))

                # 8. receive the Learning Outcomes from the server
                data = sock.recv(1024)
                lo_list = pickle.loads(data)
                # print(type(lo_list)) # for check
                # print(lo_list) # for check
                print("\nLO list")
                for i in range(len(lo_list)):
                    print(f'{i+1}. {lo_list[i]}')

                lo_answer = ''
                while lo_answer != 'R' or lo_answer != 'r':
                    lo_answer = input("(A)dd, (E)dit, (D)elete or (R)eturn? ")
                    # lo_valid_answer_list = ['A', 'a', 'E', 'e', 'D', 'd']
                    # if lo_answer in lo_valid_answer_list:
                    #     # 9. send the
                    # sock.sendall(bytes('1', 'UTF-8'))
                    if lo_answer == 'A' or lo_answer == 'a':
                        # 9-a. send the add request to the server
                        sock.sendall(bytes("add", 'UTF-8'))
                        print("you choose Add option in Learning Outcomes menu")
                        add_lo = input("Enter new LO description: ")
                        # 11-a. send the Learning Outcome to be added
                        sock.sendall(bytes(add_lo, 'UTF-8'))
                        # 14. receive the updated Learning Outcomes list from the server
                        data = sock.recv(1024)
                        updated_lo_list = pickle.loads(data)
                        print(type(updated_lo_list))  # for check
                        print(updated_lo_list)  # for check
                        print("\nUpdated LO List:")
                        for i in range(len(updated_lo_list)):
                            print(f'{i + 1}. {updated_lo_list[i]}')

                    elif lo_answer == 'E' or lo_answer == 'e':
                        # 9-e. send the edit request to the server
                        sock.sendall(bytes("edit", 'UTF-8'))
                        print("you choose Edit option in Learning Outcomes menu")
                        edit_lo_num = input("Enter LO #: ")
                        # 11-e-(1). send the number of LO to be overwritten
                        sock.sendall(bytes(edit_lo_num, 'UTF-8'))
                        edit_lo_txt = input("Enter new text: ")
                        # 11-e-(2). send the text of LO to overwrite
                        sock.sendall(bytes(edit_lo_txt, 'UTF-8'))
                        # 14. receive the updated Learning Outcomes list from the server
                        data = sock.recv(1024)
                        updated_lo_list = pickle.loads(data)
                        print(type(updated_lo_list))  # for check
                        print(updated_lo_list)  # for check
                        print("\nUpdated LO List:")
                        for i in range(len(updated_lo_list)):
                            print(f'{i + 1}. {updated_lo_list[i]}')
                    elif lo_answer == 'D' or lo_answer == 'd':
                        print("you choose Delete option in Learning Outcomes menu")
                    else:
                        sock.sendall(bytes('error', 'UTF-8'))
                        print("Enter the correct answer")
                    # # 14. receive the updated Learning Outcomes list from the server
                    # data = sock.recv(1024)
                    # updated_lo_list = pickle.loads(data)
                    # print(type(updated_lo_list))  # for check
                    # print(updated_lo_list)  # for check
                    # print("\nUpdated LO List:")
                    # for i in range(len(updated_lo_list)):
                    #     print(f'{i + 1}. {updated_lo_list[i]}')
            break
        else:
            print("Enter the correct Module ID!")

    data = sock.recv(1024)
    print('Received', repr(data))

    data = sock.recv(1024)
    print(repr(data))
    if response == 'L' or response == 'l':
        lo_answer = input(learning_outcome)

sock.close()
