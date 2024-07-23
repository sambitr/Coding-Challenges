import sys

## Default delemeter is tab (\t)

field = sys.argv[1][1:2] #-f
field_num = sys.argv[1][2:]


if sys.argv[2][1:2].lower() == "d":
    if sys.argv[2][2:] == "":
        delemeter = "\t"
    else:
        delemeter = sys.argv[2][2:]
    #print(delemeter)
    file_name = sys.argv[3]
    file_content = open(file_name)
    for line in file_content.readlines():
        print(line.split(delemeter)[int(field_num)-1])
else:
    file_name = sys.argv[2]
    #print(field, field_num, file_name)

    file_content = open(file_name)
    for line in  file_content.readlines():
        print(line.split("\t")[int(field_num)-1])