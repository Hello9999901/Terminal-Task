import tkinter as tk
import os

action = tk.Tk()

action.title("Terminal Task V0.2")

cask = False

numtask = tk.IntVar()
numtask.set(1)

appnameentry = tk.Entry(action)
diskname = tk.Entry(action)
diskform = tk.Entry(action)
diskID = tk.Entry(action)
pip3inst = tk.Entry(action)
brewapp = tk.Entry(action)

tasks = [
    ("Open Application"),
    ("Erase Disk ** CAN ERASE ALL DISKS - USE W/ CAUTION **"),
    ("pip3 install (Requires Python3)"),
    ("Homebrew install (Requires Homebrew)"),
    ("Sleep"),
    ("Quit Program")
]

def OSrun():
    if numtask.get() == 0:
        print (appnameentry.get())
        os.system('open -a ' + "'" + appnameentry.get().strip() + "'" + ".app")
    elif numtask.get() == 1:
        print ('Disk ID: ' + diskID.get().strip())
        print ('Disk Format: ' + diskform.get().strip())
        print ('Disk Name: ' + diskname.get().strip())
        os.system ('diskutil eraseDisk '+ diskform.get().strip() + ' ' + diskname.get().strip() + ' ' + """/dev/""" + diskID.get().strip())
    elif numtask.get() == 2:
        print ('pip3 package: ' + pip3inst.get().strip())
        os.system ('pip3 install '+ pip3inst.get().strip())
    elif numtask.get() == 3:
        if cask == False:
            print ('#no cask# homebrew package: ' + brewapp.get().strip())
            os.system ('brew install ' + brewapp.get().strip())

def ShowChoice():
    print(numtask.get())
    if numtask.get() == 6:
        exit()
    
    elif numtask.get() == 0:
        tk.Label(action, text="""Application Opener:""",
         justify = tk.LEFT,
         pady = 20).pack(anchor=tk.N)
        tk.Label(action, text="App Name:").pack(padx=0, pady=5, side=tk.LEFT)
        appnameentry.pack               (padx=5, pady=20, side=tk.LEFT)
        tk.Button(action, text='Run', command=OSrun).pack (padx=10, pady=30, side=tk.LEFT)
    
    elif numtask.get() == 1:
        x = os.popen('diskutil list').read()

        tk.Label(action, text="""Disk Erase""",
         justify = tk.LEFT,
         pady = 20).pack(anchor=tk.N)
        
        tk.Label(action, text="Disk Name").pack  (padx=0, pady=5, side=tk.LEFT)
        diskname.pack                            (padx=5, pady=20, side=tk.LEFT)

        tk.Label(action, text="Disk Format").pack(padx=10, pady=5, side=tk.LEFT)
        diskform.pack                            (padx=15, pady=20, side=tk.LEFT)

        tk.Label(action, text="Disk ID").pack    (padx=20, pady=5, side=tk.LEFT)
        diskID.pack                              (padx=25, pady=20, side=tk.LEFT)

        tk.Button(action, text='Run', command=OSrun).pack (padx=10, pady=30, side=tk.LEFT)

        diskutillist = x
        msg = tk.Message(action, text = diskutillist)
        msg.config(justify = tk.RIGHT, font=('San Serif', 15))
        msg.pack()

    elif numtask.get() == 2:
        tk.Label(action, text="""pip3 Installer:""",
         justify = tk.LEFT,
         pady = 20).pack(anchor=tk.N)
        tk.Label(action, text="pip3 package name:").pack(padx=0, pady=5, side=tk.LEFT)
        pip3inst.pack               (padx=5, pady=20, side=tk.LEFT)
        tk.Button(action, text='Run', command=OSrun).pack (padx=10, pady=30, side=tk.LEFT)
    
    elif numtask.get() == 3:
        tk.Label(action, text="""Homebrew Package Installer:""",
         justify = tk.LEFT,
         pady = 20).pack(anchor=tk.N)
        tk.Label(action, text="Homebrew Package Name:").pack(padx=0, pady=5, side=tk.LEFT)
        brewapp.pack               (padx=5, pady=20, side=tk.LEFT)
        tk.Button(action, text='Run', command=OSrun).pack (padx=10, pady=30, side=tk.LEFT)
    
    elif numtask.get() == 4:
        os.system('pmset sleepnow')

    


tk.Label(action, text="""Welcome to Terminal Tasks V0.2 - First GUI program by Hello9999901""",
         justify = tk.LEFT,
         pady = 5).pack()


tk.Label(action, text="""There may be bugs. Please use responsibly. Thank you and Enjoy!""",
         justify = tk.LEFT,
         pady = 5).pack()


tk.Label(action, text="""Choose Terminal Task:""",
         justify = tk.LEFT,
         pady = 5).pack()

for val, language in enumerate(tasks): #id framework
    tk.Radiobutton(action, 
                  text=language,
                  indicatoron = 0,
                  width = 50,
                  pady = 20, 
                  variable=numtask, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


action.mainloop() #main loop