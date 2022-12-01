import socket

SERVER = "127.0.0.1"
PORT = 64003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

response = ""
data_to_send_moduleID = ""
learning_outcome = "1. Evaluate and apply design patterns in the design and development of a distributed system.\n" \
                   "2. Assess and apply different architectural patterns in a distributed system.\n" \
                   "3. Critically access and apply threading in a distributed application.\n" \
                   "4. Debug a distributed client/server application, identifying object properties and variables at run-time.\n" \
                   "5. Create a distributed object application using RMI, allowing client/server to communicate securely via interfaces and objects.\n"

while response != 'X' or response != 'x':

    # module ID
    data_to_send_moduleID = input("What is the module id? ")
    sock.sendall(bytes(data_to_send_moduleID, 'UTF-8'))

    # learning outcomes
    data = sock.recv(1024)
    if data == "True":
        response = input("(L)earning Outcomes, (C)ourses, (A)ssessments or e(X)it? ")
        if response == 'L' or response == 'l':
            sock.sendall(bytes(data_to_send_moduleID, 'UTF-8'))
            print(learning_outcome)
            lo_answer = ''
            while lo_answer != 'R' or lo_answer != 'r':
                lo_answer = input("(A)dd, (E)dit, (D)elete or (R)eturn? ")
                if lo_answer == 'A' or lo_answer == 'a':
                    print("you choose Add option in Learning Outcomes menu")
                    add_lo = input("Enter new LO description: ")
                    sock.sendall(bytes(add_lo, 'UTF-8'))
                    data = sock.recv(1024)
                    print("Updated LO List: \n")
                elif lo_answer == 'E' or lo_answer == 'e':
                    print("you choose Edit option in Learning Outcomes menu")
                elif lo_answer == 'D' or lo_answer == 'd':
                    print("you choose Delete option in Learning Outcomes menu")
                else:
                    print("Enter the correct answer")
    else:
        print("error")

    data = sock.recv(1024)
    print('Received', repr(data))

    data = sock.recv(1024)
    print(repr(data))
    if response == 'L' or response == 'l':
        lo_answer = input(learning_outcome)

sock.close()
