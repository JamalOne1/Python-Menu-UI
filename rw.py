# read and write to file
# by jamalmarlone@gmail.com 2023-10-07
# https://pyautogui.readthedocs.io/en/latest/quickstart.html
import pyautogui

   
  
# Imports PIL module 
from PIL import Image

fname = "demofile2" #default filename

def w_function(newtxt):
    f = open(fname +".txt", "w")
    f.write(newtxt)
    f.close()

#open and read the file after the appending:
def r_function():
    f = open(fname +".txt", "r")
    return f.read()

while True:  
    print("\n*** MENU ***")  
    print(" 1.  Read file")  
    print(" 2.  Write to file")  
    print(" 3.  Set filename")  
    print(" 4.  Screendump to scrdmp.png")  
    print(" 5.  Exit")  

    print("\n Current filename: " + fname + ".txt\n")
    users_choice = int(input("\n Enter your Choice: "))  

    # based on the users choice the relevant method is called
    if users_choice == 1:  
        print( "\nRead file\n---\n")  
        print(r_function())
        print("\n---\n\n")
    elif users_choice == 2:  
        print( "\nWrite to file\n---\n")  
        oldtxt = r_function()  
        # newtxt = input(oldtxt)  
        pyautogui.typewrite(oldtxt)
        newtxt = input()
        w_function(newtxt)  
        #print(r_function())
        print("\n---\n\n")
    elif users_choice == 3:  
        print( "\nSet filename\n---\n")  
        print(" Old filename: " + fname)
        fname = input(" New filename: ")
        f = open(fname +".txt", "a")
        f.close()
        print("\n New filename: " + fname)
    elif users_choice ==4:
        print("\nScreen dumping\n---\n")
        pyautogui.screenshot('scrdmp.png')
        im =Image.open(r"scrdmp.png")
        im.show()
        print("\n---\n")
 # exit the while loop
    elif users_choice == 5:  
        break  
      
    else:  
        print( " Please enter a valid Input from the list")          
