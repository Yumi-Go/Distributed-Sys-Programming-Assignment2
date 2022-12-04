import pickle
import socket

SERVER = "127.0.0.1"
PORT = 64003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

data_to_send_moduleID = ""
# learning_outcome = "1. Evaluate and apply design patterns in the design and development of a distributed system.\n" \
#                    "2. Assess and apply different architectural patterns in a distributed system.\n" \
#                    "3. Critically access and apply threading in a distributed application.\n" \
#                    "4. Debug a distributed client/server application, identifying object properties and variables at run-time.\n" \
#                    "5. Create a distributed object application using RMI, allowing client/server to communicate securely via interfaces and objects.\n"

learning_outcome = []
response = 'Y'
while response == 'Y' or response == 'y':
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
            root_option_selected = ""
            while True:
                root_option_selected = input("(L)earning Outcomes, (C)ourses, (A)ssessments or e(X)it? ")
                if root_option_selected == 'L' or root_option_selected == 'l':

                    # 5-l. send the request for Learning Outcomes to the server
                    sock.sendall(bytes("lo", 'UTF-8'))

                    # 8-l. receive the Learning Outcomes list from the server
                    data = sock.recv(1024)
                    lo_list = pickle.loads(data)
                    # print(type(lo_list)) # for check
                    # print(lo_list) # for check
                    print("\nLO list")
                    for i in range(len(lo_list)):
                        print(f'{i + 1}. {lo_list[i]}')

                    sub_option_selected = ""
                    while True:
                        sub_option_selected = input("(A)dd, (E)dit, (D)elete or (R)eturn? ")
                        if sub_option_selected == 'A' or sub_option_selected == 'a':
                            # 9-l-a. send the add request to the server
                            sock.sendall(bytes("add", 'UTF-8'))
                            print("you choose Add option in Learning Outcomes menu")
                            add_lo = input("Enter new LO description: ")
                            # 11-l-a. send the Learning Outcome to be added
                            sock.sendall(bytes(add_lo, 'UTF-8'))
                            # 14-l-a. receive the updated Learning Outcomes list from the server
                            data = sock.recv(1024)
                            updated_lo_list = pickle.loads(data)
                            print(type(updated_lo_list))  # for check
                            print(updated_lo_list)  # for check
                            print("\nUpdated LO List:")
                            for i in range(len(updated_lo_list)):
                                print(f'{i + 1}. {updated_lo_list[i]}')

                        elif sub_option_selected == 'E' or sub_option_selected == 'e':
                            # 9-l-e. send the edit request to the server
                            sock.sendall(bytes("edit", 'UTF-8'))
                            print("you choose Edit option in Learning Outcomes menu")
                            edit_lo_num = input("Enter LO #: ")
                            # 11-l-e. send the number of LO to be overwritten
                            sock.sendall(bytes(edit_lo_num, 'UTF-8'))
                            edit_lo_txt = input("Enter new text: ")
                            # 11-l-e. send the text of LO to overwrite
                            sock.sendall(bytes(edit_lo_txt, 'UTF-8'))
                            # 14-l-e. receive the updated Learning Outcomes list from the server
                            data = sock.recv(1024)
                            updated_lo_list = pickle.loads(data)
                            print(type(updated_lo_list))  # for check
                            print(updated_lo_list)  # for check
                            print("\nUpdated LO List:")
                            for i in range(len(updated_lo_list)):
                                print(f'{i + 1}. {updated_lo_list[i]}')
                        elif sub_option_selected == 'D' or sub_option_selected == 'd':
                            # 9-l-d. send the edit request to the server
                            sock.sendall(bytes("delete", 'UTF-8'))
                            print("you choose Delete option in Learning Outcomes menu")
                            edit_lo_num = input("Enter LO #: ")
                            # 11-l-d. send the number of LO to be deleted
                            sock.sendall(bytes(edit_lo_num, 'UTF-8'))
                            # 14-l-d. receive the updated Learning Outcomes list from the server
                            data = sock.recv(1024)
                            updated_lo_list = pickle.loads(data)
                            print(type(updated_lo_list))  # for check
                            print(updated_lo_list)  # for check
                            print("\nUpdated LO List:")
                            for i in range(len(updated_lo_list)):
                                print(f'{i + 1}. {updated_lo_list[i]}')
                        elif sub_option_selected == 'R' or sub_option_selected == 'r':
                            # 9-l-r. send the return request to the server
                            sock.sendall(bytes("return", 'UTF-8'))
                            print("you choose Return option in Learning Outcomes menu")
                            break
                        else:
                            # 9-l-i. send the Incorrect input message to the server
                            sock.sendall(bytes('incorrect', 'UTF-8'))
                            print("Enter the correct answer")

                if root_option_selected == 'C' or root_option_selected == 'c':

                    # 5-c. send the request for Courses to the server
                    sock.sendall(bytes("course", 'UTF-8'))

                    # 8-c. receive the Courses list from the server
                    data = sock.recv(1024)
                    course_list = pickle.loads(data)
                    # print(type(lo_list)) # for check
                    # print(lo_list) # for check
                    print("\nCourses list")
                    for i in range(len(course_list)):
                        print(f'{i + 1}. {course_list[i]}')

                    # 메일 답장오면 이 부분 살려서 수정할지 결정
                    # sub_option_selected = ""
                    # while True:
                    #     sub_option_selected = input("(A)dd, (E)dit, (D)elete or (R)eturn? ")
                    #     if sub_option_selected == 'A' or sub_option_selected == 'a':
                    #         # 9-a. send the add request to the server
                    #         sock.sendall(bytes("add", 'UTF-8'))
                    #         print("you choose Add option in Learning Outcomes menu")
                    #         add_lo = input("Enter new LO description: ")
                    #         # 11-a. send the Learning Outcome to be added
                    #         sock.sendall(bytes(add_lo, 'UTF-8'))
                    #         # 14-a. receive the updated Learning Outcomes list from the server
                    #         data = sock.recv(1024)
                    #         updated_lo_list = pickle.loads(data)
                    #         print(type(updated_lo_list))  # for check
                    #         print(updated_lo_list)  # for check
                    #         print("\nUpdated LO List:")
                    #         for i in range(len(updated_lo_list)):
                    #             print(f'{i + 1}. {updated_lo_list[i]}')
                    #
                    #     elif sub_option_selected == 'E' or sub_option_selected == 'e':
                    #         # 9-e. send the edit request to the server
                    #         sock.sendall(bytes("edit", 'UTF-8'))
                    #         print("you choose Edit option in Learning Outcomes menu")
                    #         edit_lo_num = input("Enter LO #: ")
                    #         # 11-e-(1). send the number of LO to be overwritten
                    #         sock.sendall(bytes(edit_lo_num, 'UTF-8'))
                    #         edit_lo_txt = input("Enter new text: ")
                    #         # 11-e-(2). send the text of LO to overwrite
                    #         sock.sendall(bytes(edit_lo_txt, 'UTF-8'))
                    #         # 14-e. receive the updated Learning Outcomes list from the server
                    #         data = sock.recv(1024)
                    #         updated_lo_list = pickle.loads(data)
                    #         print(type(updated_lo_list))  # for check
                    #         print(updated_lo_list)  # for check
                    #         print("\nUpdated LO List:")
                    #         for i in range(len(updated_lo_list)):
                    #             print(f'{i + 1}. {updated_lo_list[i]}')
                    #     elif sub_option_selected == 'D' or sub_option_selected == 'd':
                    #         # 9-d. send the edit request to the server
                    #         sock.sendall(bytes("delete", 'UTF-8'))
                    #         print("you choose Delete option in Learning Outcomes menu")
                    #         edit_lo_num = input("Enter LO #: ")
                    #         # 11-d. send the number of LO to be deleted
                    #         sock.sendall(bytes(edit_lo_num, 'UTF-8'))
                    #         # 14-d. receive the updated Learning Outcomes list from the server
                    #         data = sock.recv(1024)
                    #         updated_lo_list = pickle.loads(data)
                    #         print(type(updated_lo_list))  # for check
                    #         print(updated_lo_list)  # for check
                    #         print("\nUpdated LO List:")
                    #         for i in range(len(updated_lo_list)):
                    #             print(f'{i + 1}. {updated_lo_list[i]}')
                    #     elif sub_option_selected == 'R' or sub_option_selected == 'r':
                    #         # 9-r. send the return request to the server
                    #         sock.sendall(bytes("return", 'UTF-8'))
                    #         print("you choose Return option in Learning Outcomes menu")
                    #         break
                    #     else:
                    #         # 9-i. send the incorrect input message to the server
                    #         sock.sendall(bytes('incorrect', 'UTF-8'))
                    #         print("Enter the correct answer")

                if root_option_selected == 'A' or root_option_selected == 'a':

                    # 5-a. send the request for Assessments to the server
                    sock.sendall(bytes("assess", 'UTF-8'))

                    # 8-a. receive the Courses list from the server
                    data = sock.recv(1024)
                    course_list = pickle.loads(data)
                    # print(type(lo_list)) # for check
                    # print(lo_list) # for check
                    print("\nAssessments list")
                    for i in range(len(course_list)):
                        print(f'{i + 1}. {course_list[i]}')

                    # 메일 답장오면 이 부분 살려서 수정할지 결정
                    # sub_option_selected = ""
                    # while True:
                    #     sub_option_selected = input("(A)dd, (E)dit, (D)elete or (R)eturn? ")
                    #     if sub_option_selected == 'A' or sub_option_selected == 'a':
                    #         # 9-a. send the add request to the server
                    #         sock.sendall(bytes("add", 'UTF-8'))
                    #         print("you choose Add option in Learning Outcomes menu")
                    #         add_lo = input("Enter new LO description: ")
                    #         # 11-a. send the Learning Outcome to be added
                    #         sock.sendall(bytes(add_lo, 'UTF-8'))
                    #         # 14-a. receive the updated Learning Outcomes list from the server
                    #         data = sock.recv(1024)
                    #         updated_lo_list = pickle.loads(data)
                    #         print(type(updated_lo_list))  # for check
                    #         print(updated_lo_list)  # for check
                    #         print("\nUpdated LO List:")
                    #         for i in range(len(updated_lo_list)):
                    #             print(f'{i + 1}. {updated_lo_list[i]}')
                    #
                    #     elif sub_option_selected == 'E' or sub_option_selected == 'e':
                    #         # 9-e. send the edit request to the server
                    #         sock.sendall(bytes("edit", 'UTF-8'))
                    #         print("you choose Edit option in Learning Outcomes menu")
                    #         edit_lo_num = input("Enter LO #: ")
                    #         # 11-e-(1). send the number of LO to be overwritten
                    #         sock.sendall(bytes(edit_lo_num, 'UTF-8'))
                    #         edit_lo_txt = input("Enter new text: ")
                    #         # 11-e-(2). send the text of LO to overwrite
                    #         sock.sendall(bytes(edit_lo_txt, 'UTF-8'))
                    #         # 14-e. receive the updated Learning Outcomes list from the server
                    #         data = sock.recv(1024)
                    #         updated_lo_list = pickle.loads(data)
                    #         print(type(updated_lo_list))  # for check
                    #         print(updated_lo_list)  # for check
                    #         print("\nUpdated LO List:")
                    #         for i in range(len(updated_lo_list)):
                    #             print(f'{i + 1}. {updated_lo_list[i]}')
                    #     elif sub_option_selected == 'D' or sub_option_selected == 'd':
                    #         # 9-d. send the edit request to the server
                    #         sock.sendall(bytes("delete", 'UTF-8'))
                    #         print("you choose Delete option in Learning Outcomes menu")
                    #         edit_lo_num = input("Enter LO #: ")
                    #         # 11-d. send the number of LO to be deleted
                    #         sock.sendall(bytes(edit_lo_num, 'UTF-8'))
                    #         # 14-d. receive the updated Learning Outcomes list from the server
                    #         data = sock.recv(1024)
                    #         updated_lo_list = pickle.loads(data)
                    #         print(type(updated_lo_list))  # for check
                    #         print(updated_lo_list)  # for check
                    #         print("\nUpdated LO List:")
                    #         for i in range(len(updated_lo_list)):
                    #             print(f'{i + 1}. {updated_lo_list[i]}')
                    #     elif sub_option_selected == 'R' or sub_option_selected == 'r':
                    #         # 9-r. send the return request to the server
                    #         sock.sendall(bytes("return", 'UTF-8'))
                    #         print("you choose Return option in Learning Outcomes menu")
                    #         break
                    #     else:
                    #         # 9-i. send the incorrect input message to the server
                    #         sock.sendall(bytes('incorrect', 'UTF-8'))
                    #         print("Enter the correct answer")

                elif root_option_selected == 'X' or root_option_selected == 'x':
                    # 5-x. send the request for Exit to the server
                    sock.sendall(bytes("exit", 'UTF-8'))
                    break
                else:
                    # 5-i. send the incorrect input message to the server
                    sock.sendall(bytes('incorrect', 'UTF-8'))
                    print("Enter the correct answer")

            print("Goodbye")
            break
        else:
            print("Enter the correct Module ID!")

    response = input("Do you want to continue? (Y/N) ")
    if response == 'N' or response == 'n':
        # 15-q. send the request to quit
        sock.sendall(bytes('quit', 'UTF-8'))
        break
    elif response != 'Y' and response != 'y':
        # 15-c. send the request to continue
        sock.sendall(bytes('continue', 'UTF-8'))
    else:
        print("Enter the correct answer Y or N")
        # 15-i. send the Incorrect input message
        sock.sendall(bytes('incorrect', 'UTF-8'))


sock.close()
