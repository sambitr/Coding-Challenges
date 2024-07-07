import sys

#print(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
if len(sys.argv) == 2: ## first item is the script name and second item is the file name sent as argument
    ## take the file name from the command line and print the contents of it
    file_name = sys.argv[1]
    #print(f"file name is: {file_name}")

    file_handle = open(file_name, 'r', encoding="utf-8")
    print(file_handle.read())
    file_handle.close()
    ######################
else:
    ## no file name. Take option from command line and print it. Shold exit ater 10 lines.
    if len(sys.argv) == 1 :
        count = 0
        while(count < 10):
            print(input())
            count+=1

    elif sys.argv[1] == "-n":
        line_to_print = sys.argv[2]
        file_name_to_work = sys.argv[3]
        #file_operation(file_name_to_work, sys.argv[1], line_to_print)
        #print(f"line to print {line_to_print}, file to work {file_name_to_work}")
        file_hdl = open(file_name_to_work, 'r', encoding="utf-8")
        for i in range(int(line_to_print)):
            print(file_hdl.readline())
        file_hdl.close()

    elif sys.argv[1] == "-c":
        chars_to_print = sys.argv[2]
        file_name_to_work = sys.argv[3]
        with open(file_name_to_work, 'r', encoding="utf-8") as r:
            print(r.read()[:int(chars_to_print) ])
    



