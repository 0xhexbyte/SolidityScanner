#importing regex and sys module
import re

print ("""\
   _____       _ _     _ _ _          _____                                 
  / ____|     | (_)   | (_) |        / ____|                                
 | (___   ___ | |_  __| |_| |_ _   _| (___   ___ __ _ _ __  _ __   ___ _ __ 
  \___ \ / _ \| | |/ _` | | __| | | |\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  ____) | (_) | | | (_| | | |_| |_| |____) | (_| (_| | | | | | | |  __/ |   
 |_____/ \___/|_|_|\__,_|_|\__|\__, |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                __/ |                                       
                               |___/                                        """)

#creating list holder for public functions
publicFunctions = []

#open the solidity contr
#act file
f = open("contract.sol", "r")
file_contents = f.read()

#Calculate lines of code
def calc_loc():
    line = 1
    for each in file_contents:
        if each == '\n':
            line+=1
    print("Number of lines in code: ", line)

#Test Case 1 - Reporting publicly declared functions
#checking for functions with "public" keyword and adding them to alerts
def anyPublicFunc():

    broken_lines = file_contents.splitlines()

    for e in broken_lines:
        if 'function' in e:
            if 'public' in e:
                #appending all the lines containing "public" keyword to the empty list
                publicFunctions.append(e.strip())
                #print(publicFunctions)         // remove this comment to print the functions                                                   

    for element in publicFunctions:
        tmp = str(element)
        x = re.findall("^function", tmp)
        if x:
            print("Publicly declared function detected")

calc_loc()
anyPublicFunc()

#close the file
f.close()