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
    file_content = open(file_name)
    print(field, field_num, file_name)

    field_num_list = []
    if (len(field_num) >= 2):
        ## This is for supporting the case for cut -f1,2 sample.tsv & cut -d, -f"1 2" fourchords.csv
        field_num_list = field_num.split(field_num[1]) # split on the basis of delemeter 
        for line in  file_content.readlines():
            selected_columns = []
            for columnnum in field_num_list:
                selected_columns.append(line.split("\t")[int(columnnum)-1])
            print("\t".join(selected_columns))
    else:
        ## below section is to print based on the default delemeter tab. E.X: cut -f2 sample.tsv
        for line in  file_content.readlines():
            print(line.split("\t")[int(field_num)-1])


    
    