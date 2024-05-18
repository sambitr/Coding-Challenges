import subprocess
import os

def file_scraper(folder_name, test_folders): 
    new_folder = test_folders+"/"+folder_name
    print(f"===================== checking the valid and invalid json files under the folder {new_folder} =====================")
    for file in (os.listdir(new_folder)):
        print("\nChecking file: ", new_folder+"/"+file)
        if os.stat(new_folder+"/"+file).st_size == 0:
            print(f"{new_folder+"/"+file} is an INVALID JSON file")
        else:
            json_validate(new_folder+"/"+file)

def json_validate(file):
    with open(file, "rb") as fp:
        first = fp.read(1).decode('utf-8')
        fp.seek(-1,2) ## move to the end of the file
        last = fp.read(1).decode('utf-8')
    fp.close()
    if first == "{" and last == "}":
        print(f"{file} is a VALID JSON file")
        os._exit(0)        
    print("====================")
    



## Loop over the test folder and pass the folder needed to the function arguments
test_folders=("tests")
for folder in (os.listdir(test_folders)):
    file_scraper(folder, test_folders)


