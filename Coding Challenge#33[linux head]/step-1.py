import sys

if len(sys.argv) == 2: ## first item is the script name and second item is the file name sent as argument
    ## take the file name from the command line and print the contents of it
    file_name = sys.argv[1]
    print(f"file name is: {file_name}")

    file_handle = open(file_name, 'r', encoding="utf-8")
    print(file_handle.read())
    file_handle.close()
    ######################
else:
    ## no file name. Take option from command line and print it. Shold exit ater 10 lines.
    count = 0
    while(count <= 10):
        print(input())
        count+=1
    


