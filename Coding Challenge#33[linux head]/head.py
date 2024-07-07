import sys

if len(sys.argv) == 2: ## first item is the script name and second item is the file name sent as argument
    file_name = sys.argv[1]

    file_handle = open(file_name, 'r', encoding="utf-8")
    print(file_handle.read())
    file_handle.close()
else:
    ## no file name. Take option from command line and print it. Shold exit ater 10 lines.
    if len(sys.argv) == 1 :
        count = 0
        while(count < 10):
            print(input())
            count+=1

    elif sys.argv[1] == "-n":
        line_to_print = sys.argv[2]
        files = sys.argv[3:]
        if len(files) > 1:
            for fileName in files:
                print(f"==> {fileName} <==")
                filehdl = open(fileName, 'r', encoding="utf-8")
                for i in range(int(line_to_print)):
                    line = filehdl.readline()
                    if line == "": ## end of file has been reached
                        break
                    print(line)
                filehdl.close()
        else:
            file_name_to_work = sys.argv[3]
            file_hdl = open(file_name_to_work, 'r', encoding="utf-8")
            for i in range(int(line_to_print)):
                line = file_hdl.readline()
                if line == "": ## end of file has been reached
                    break
                print(line)

            file_hdl.close()

    elif sys.argv[1] == "-c":
        chars_to_print = sys.argv[2]
        file_name_to_work = sys.argv[3]
        with open(file_name_to_work, 'r', encoding="utf-8") as r:
            print(r.read()[:int(chars_to_print) ])
    



