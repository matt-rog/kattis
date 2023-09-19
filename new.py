import sys, getopt
import os
import shutil

name = ""
force = False
opts, args = getopt.getopt(sys.argv[1:],"n:f",["name=","force="])
for opt, arg in opts:
    if opt in ("-n", "--name"):
        name = arg
    elif opt in ("-f", "--force"):
        force = (arg != None) or (arg.lower() == "y")
    else:
        print("Invalid command.")
        exit()

new_dir = os.path.join(os.getcwd(), name)

if os.path.exists(new_dir):
    if not force:
        ow = str(input(("FAIL: Directory already exists")))
        exit()
    else:
        shutil.rmtree(new_dir)
        
os.makedirs(new_dir)

# Make input.txt
input_f = open(os.path.join(new_dir, "input.txt"), "w")
input_f.write("")
input_f.close()

# Make soln.py
soln_f = open(os.path.join(new_dir, "soln.py"), "w")
soln_f.write(f"#https://open.kattis.com/problems/{name}")
soln_f.close()

exit()