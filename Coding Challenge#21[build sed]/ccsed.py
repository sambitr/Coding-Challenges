import re
import sys

def substitution(file_name, option, what_to_sub, what_to_sub_with, operate_on = "g"):
    print(f"file_name={file_name}, option={option}, what_to_sub={what_to_sub}, what_to_sub_with={what_to_sub_with}, operate_on={operate_on}")
    with open(file_name, "r+") as f:
        file = f.read()

        file_modified = re.sub(what_to_sub, what_to_sub_with, file)
        f.seek(0, 0)
        f.write(file_modified)
        f.truncate()

def sedprint(option, start_from, end_to, file_name):
    print(f"option={option}, start_from={start_from}, end_to={end_to}, file_name={file_name}")
    file = open(file_name, "r")
    file_content = file.readlines()
    for i in range(int(start_from)-1, int(end_to)):
        print(file_content[i].strip())
    
    file.close()

def sedpatternprint(option, string_to_search, what_to_do, file_name):
    print(f"option={option}, string_to_search={string_to_search}, what_to_do={what_to_do}, file_name={file_name}")
    file = open(file_name, "r")
    file_content = file.readlines()
    for line in file_content:
        #print(line)
        if string_to_search in line:
            print(line)
    file.close()

def seddoublespace(option, file_name):
    file = open(file_name)
    file_content = file.readlines()
    file.close()
    with open(file_name, "w") as f:
        for line in file_content:
            f.write(line+"\n\n")

def seddel(option, filename):
    print("hello")
    option_list = option.split("/")
    with open(filename, "r") as f_read:
        data = f_read.read().rstrip("\n")
    with open(filename, "w") as f_write:
        f_write.write(data[:-1])

################################ Script starts from here ################################
## It uses alias ccsed="python ccsed.py"
## take this into consideration when accepting command line arguments

if sys.argv[1] == "-n": 
    options = sys.argv[2]
    #print(sys.argv[1], sys.argv[2])
    try: #ccsed -n '2,4p' file_name
        options_list = options.split(",")
        sedprint(sys.argv[1], options_list[0],options_list[1][0], sys.argv[3])
    except: #ccsed -n /roads/p unquoted.txt
        options_list = options.split("/")
        print(options_list)
        sedpatternprint(sys.argv[1], options_list[1],options_list[2], sys.argv[3])
elif sys.argv[1].upper() == "G":
    file_name = sys.argv[2]
    seddoublespace(sys.argv[1], file_name)
    
elif sys.argv[1].split("/")[1] == "^$":
    seddel(sys.argv[1], sys.argv[2])

else: #ccsed s/this/that/g file_name
    options = sys.argv[1]
    file_name = sys.argv[2]
    options_list = options.split("/")
    if options_list[0].lower() == "s":
        try:
            if options_list[3].lower() != " ":
                substitution(file_name, "s", options_list[1], options_list[2], options_list[3].lower())
        except IndexError:
            substitution(file_name, "s", options_list[1], options_list[2])
