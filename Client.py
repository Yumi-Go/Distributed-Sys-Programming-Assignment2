import pickle
import socket

SERVER = "127.0.0.1"
PORT = 64003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

while True:
    # 1. send module ID
    data_to_send_moduleID = input("What is the module id? ")
    if not data_to_send_moduleID:
        print("Enter the answer")
    else:
        sock.sendall(bytes(data_to_send_moduleID, 'UTF-8'))
        # 4. receive true or false for existence of module ID in data dictionary from the server
        data = sock.recv(1024)
        bool_data = bool(int(data))
        if bool_data:
            # root_option_selected = ""
            while True:
                while True:
                    root_option_selected = input("(L)earning Outcomes, (C)ourses, (A)ssessments or e(X)it? ")
                    if root_option_selected == 'X' or root_option_selected == 'x':
                        # 5-x. send the request for Exit to the server
                        sock.sendall(bytes("exit", 'UTF-8'))
                        break
                    if not root_option_selected:
                        sock.sendall(bytes("none", 'UTF-8'))
                        print("Enter the answer")
                    elif root_option_selected == 'L' or root_option_selected == 'l':

                        # 5-l. send the request for Learning Outcomes to the server
                        sock.sendall(bytes("lo", 'UTF-8'))

                        # sub_option_selected = ""
                        while True:
                            # 8-l. receive the Learning Outcomes list from the server
                            data = sock.recv(1024)
                            lo_list = pickle.loads(data)

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
                                print("\nUpdated LO List:")
                                for i in range(len(updated_lo_list)):
                                    print(f'{i + 1}. {updated_lo_list[i]}')

                            elif sub_option_selected == 'E' or sub_option_selected == 'e':
                                # 9-l-e. send the edit request to the server
                                sock.sendall(bytes("edit", 'UTF-8'))
                                # 12-l-d. receive the recent lo list from the server
                                data = sock.recv(1024)
                                recent_lo_list = pickle.loads(data)
                                # print(recent_lo_list)  # for check
                                if len(recent_lo_list) == 0:
                                    print("Learning Outcomes List is empty!")
                                    break
                                else:
                                    print("you choose Edit option in Learning Outcomes menu")
                                    while True:
                                        edit_lo_num = input("Enter LO #: ")
                                        if not edit_lo_num:
                                            print("Enter the answer")
                                        else:
                                            if not edit_lo_num.isdigit():
                                                print("Enter the Integer number")
                                            else:
                                                if 0 < int(edit_lo_num) <= len(recent_lo_list):
                                                    lo_num_text = ["", ""]
                                                    # # 13-l-d. send the number of LO to be edited
                                                    # sock.sendall(bytes(edit_lo_num, 'UTF-8'))
                                                    edit_lo_txt = input("Enter new text: ")
                                                    # # 13-l-d. send the text of LO to be edited
                                                    # sock.sendall(bytes(edit_lo_txt, 'UTF-8'))

                                                    # 13-l-d. send the num, text of LO to be edited
                                                    lo_num_text[0] = edit_lo_num
                                                    lo_num_text[1] = edit_lo_txt

                                                    lo_num_text_to_send = pickle.dumps(lo_num_text)
                                                    sock.sendall(lo_num_text_to_send)


                                                    # 16-l-d. receive the updated Learning Outcomes list from the server
                                                    data = sock.recv(1024)
                                                    updated_lo_list = pickle.loads(data)
                                                    print("\nUpdated LO List:")
                                                    for i in range(len(updated_lo_list)):
                                                        print(f'{i + 1}. {updated_lo_list[i]}')
                                                    break
                                                else:
                                                    print("Enter the correct number of LO")

                            elif sub_option_selected == 'D' or sub_option_selected == 'd':
                                # 9-l-d. send the edit request to the server
                                sock.sendall(bytes("delete", 'UTF-8'))
                                # 12-l-d. receive the recent lo list from the server
                                data = sock.recv(1024)
                                recent_lo_list = pickle.loads(data)
                                # print(recent_lo_list)  # for check
                                if len(recent_lo_list) == 0:
                                    print("Learning Outcomes List is empty!")
                                    break
                                else:
                                    print("you choose Delete option in Learning Outcomes menu")
                                    while True:
                                        delete_lo_num = input("Enter LO #: ")
                                        if not delete_lo_num:
                                            print("Enter the answer")
                                        else:
                                            if not delete_lo_num.isdigit():
                                                print("Enter the Integer number")
                                            else:
                                                if 0 < int(delete_lo_num) <= len(recent_lo_list):
                                                    # 13-l-d. send the number of LO to be deleted
                                                    sock.sendall(bytes(delete_lo_num, 'UTF-8'))

                                                    # 16-l-d. receive the updated Learning Outcomes list from the server
                                                    data = sock.recv(1024)
                                                    updated_lo_list = pickle.loads(data)
                                                    print("\nUpdated LO List:")
                                                    for i in range(len(updated_lo_list)):
                                                        print(f'{i + 1}. {updated_lo_list[i]}')
                                                    break
                                                else:
                                                    print("Enter the correct number of LO")

                            elif sub_option_selected == 'R' or sub_option_selected == 'r':
                                # 9-l-r. send the return request to the server
                                sock.sendall(bytes("return", 'UTF-8'))
                                print("you choose Return option in Learning Outcomes menu")
                                break
                            else:
                                # 9-l-i. send the Incorrect input message to the server
                                sock.sendall(bytes('incorrect', 'UTF-8'))
                                if sub_option_selected != "":
                                    print("Enter the correct answer (sub question)")
                                else:
                                    print("Enter the answer (sub question)")

                    elif root_option_selected == 'C' or root_option_selected == 'c':

                        # 5-c. send the request for Courses to the server
                        sock.sendall(bytes("course", 'UTF-8'))

                        # 8-c. receive the Courses list from the server
                        data = sock.recv(1024)
                        course_list = pickle.loads(data)
                        print("\nCourses list")
                        for i in range(len(course_list)):
                            print(f'{i + 1}. {course_list[i]}')

                    elif root_option_selected == 'A' or root_option_selected == 'a':

                        # 5-a. send the request for Assessments to the server
                        sock.sendall(bytes("assess", 'UTF-8'))

                        # 8-a. receive the Assessments list from the server
                        data = sock.recv(1024)
                        assess_list = pickle.loads(data)
                        print("\nAssessments list")
                        for i in range(len(assess_list)):
                            print(f'{i + 1}. {assess_list[i]}')
                    else:
                        # 5-i. send the incorrect input message to the server
                        sock.sendall(bytes('incorrect', 'UTF-8'))
                        print("Enter the correct answer (root question)")
                break
            print("Goodbye")
            break
        else:
            print("Enter the correct Module ID!")

sock.close()
