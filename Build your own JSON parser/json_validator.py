import subprocess
import os

def json_validator(folder_name, test_folders): 
    new_folder = test_folders+"/"+folder_name
    print(f"===================== checking the valid and invalid json files under the folder {new_folder} =====================")
    for file in (os.listdir(new_folder)):
        print("\nChecking file: ", new_folder+"/"+file)
        if os.stat(new_folder+"/"+file).st_size == 0:
            print(f"{new_folder+"/"+file} is an INVALID JSON file")
        else:
            with open(new_folder+"/"+file, "r") as fp:
                content = fp.read()
            #fp.close()
            if file_scrape(content):
                print(f"{new_folder+"/"+file} is a VALID JSON file")
            else:
                print(f"{new_folder+"/"+file} is an INVALID JSON file")

            print("====================")


def file_scrape(content):
    content = content.strip()
    if not (content.startswith("{") and content.endswith("}")) : ## if json file does not start with { and end with }, it's invalid JSON file
        print("content does not start with { and end with }")
        return False
    else:
        if content[1:-1] == "": ##strip out first and last characters: { & }. if it is empty then it's valied 
            print("content empty between {}, hence valid")
            return True
        else:
            pairs = content.split(",")
            print(pairs)
            for pair in pairs:
                print("pair:", pair)
                if ":" not in pair:
                    print("pair:", pair, "does not contain :. Returning false")
                    return False

                key, value = pair.split(":")
                if key.strip().startswith('"') and key.endswith('"') and value.startswith('"') and value.endswith('"'):
                    print(key, value)
                    print("true")
                    return True
                else:
                    print(key, value)
                    print("false")
                    return False

# def keyValuePaircheck(jsoncontent):
#     pairs = jsoncontent.split(",")
#     print(pairs)
#     for pair in pairs:
#         if ":" not in pair:
#             return False
#         else:
#             return True
                

## Loop over the test folder and pass the folder needed to the function arguments
test_folders=("tests")
for folder in (os.listdir(test_folders)):
    json_validator(folder, test_folders)

