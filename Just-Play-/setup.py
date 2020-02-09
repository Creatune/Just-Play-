import time
import os
os.system('sudo apt-get install python3-tk')
import tkinter as tk
from tkinter import messagebox

def message_box(subject, content):                                                                            
    root = tk.Tk()                                                                                           
    root.attributes("-topmost", True)                                                                        
    root.withdraw()                                                                                          
    messagebox.showinfo(subject, content)                                                                    
    try:                                                                                                     
        root.destroy()                                                                                       
    except:                                                                                                  
        pass                                                                                                              
message_box('Disclaimer!', 'This program WILL install a third party software... Terminate it if you do not want to install it')                                                                                                               
message_box('','The download will start in exactly  4.5 SECONDS')                                                                                                                                                           
time.sleep(4.5)
os.system('sudo apt-get update --fix-missing')
os.system('sudo apt-get install python3-pip')
os.system('pip install --upgrade pip')
os.system('pip3 install pygame')
message_box('Done!','The installation process has completed. You can now run the game.py file and play the full game.')
