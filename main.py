print("Random user generator by JieJiaoDeMao_wjz")
print("Loading script...",end="")
import random
import string
import subprocess
import time
import traceback
import os
import sys
print("Done.")
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
num_users = int(input("Enter number of random users>"))
num_string = int(input("Enter length of the name of random users>"))
sure = input("Are you sure to create "+str(num_users)+" random users with length of "+str(num_string)+" ?\nEnter \"Y\" for sure, other things to exit>")
if sure=="Y":
    try:
        print("Successfully configured program.\nBefore running, please make sure that you are running the program in administrator mode.\nIf you aren't, close the console at once.\nYou have 3 seconds to check.")
        time.sleep(3)
        print("Program started.")
        for i in range(num_users):
            random_string = generate_random_string(num_string)
            print("["+str(i+1)+"/"+str(num_users)+"] Creating a user with \""+random_string+"\" as user name...")
            cmd = f"net user {random_string} /add"
            os.system(cmd)
    except:
        print("Oops! An error occurred.\nThe following text shows the error information which may helps.")
        traceback.print_exc()
        os.system("pause")
        sys.exit()
    print("Task finished successfully.")
    os.system("pause")
else:
    print("It seems like that you are going to exit.")
    os.system("pause")
