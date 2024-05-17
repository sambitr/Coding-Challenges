import sys
import subprocess

def file_operate(first_arg, file_name):
    
    if file_name:
        print(f"File to operate on {file_name}")
        if (first_arg == ""):
            subprocess.call(["wc", file_name])
        else:
            subprocess.call(["wc", first_arg, file_name])
    else:
        print("Reading from stdin...")
        content = sys.stdin.read()
        if first_arg == "":
            subprocess.run(["wc"], input=content, text=True, encoding='utf-8', errors='ignore')
        else:
            subprocess.run(["wc", first_arg], input=content, text=True, encoding='utf-8', errors='ignore')




if ( len(sys.argv) == 1 ):
    print("=== needs file name and/or option of operation to be passed to script ===")
    print("Example: ccwc -c test.txt OR ccwc test.txt")
elif ( len(sys.argv) == 2 ):
    first_arg = sys.argv[1]
    if ( first_arg == "-c" or first_arg == "-l" or first_arg == "-w" or first_arg == "-m" ):
        if sys.stdin.isatty():
            print("=== needs file name to be passed to script too ===")
            print("Example: ccwc -c test.txt")
        else:
            file_operate(first_arg, "")
    else:
        file_operate("", sys.argv[1])
else:
    first_arg = sys.argv[1]
    file_operate(first_arg, sys.argv[2])

