#!/bin/python3
import os
import sys
from pathlib import Path
ver = "1.0"
vernum = 1.0
# The RUNPY thingy
# Who Will Use This Anyways?
# -- IPYTHON is dead exept for IPYNB (jupyter notebooks with IPYthon)
# -- == PYNB does not exist.
# for more info, use python3 run.py help
# Don't Forget Addons

# Make Addons!
# ---
# To make addons,
#   1. Create a file alongside run.py
#   2. Add "import run" at the top
#   3. change vars (runpyfilename, helpfilename, message (the help message))
#   4. add the code "run.py()" to run or "run.showhelp()" to show help at the end.
# Done!
# To run the addon, run THAT py!

# -----------------------settings---------------------

# Insert File To RUN.PY here; main.ipy is recomended.
runpyfilename = "main.ipy" # Change This With addons! (run.runpyfilename)
path = Path("./" + runpyfilename)
# File Name For Help And Log (Really Does Not Matter, Unless You Use This Filename in your code.)
helpfilename = "runpy.willautoremove.help.txt"
log = open("runpy.log", "a")

def wtl(messagetolog): # WriteToLog
    log.write(messagetolog + "\n")

wtl("Starting Program...")

# ------------------------Code For RUNPY Is Below.----------------
# IF moment...
runpyifmessage = ""
if path.is_file():
    # if the file exists, put the following message in.
    runpyifmessage = f"To Setup RunPY with a dummy file, delete '{runpyfilename}' (without the qoutes).\nfor a diffrent file to be RUN.PY, Open The Code."
    # But
else:
    # put info about the dummy file
    runpyifmessage = f"{runpyfilename} Is not in the current folder.\n{runpyfilename} is going to be a dummy file when run, but if you change the variable 'runpyfilename', that file shall be chosen as eather\n1. the dummy file, or\n2. the selected RunPY file."
# Help Message Below:
message = f"\nRunPY IPython Launcher\nStart IPY files with the PYTHON3 command!\nTo Use, Type 'python3 run.py' (without qoutes)\nOr Incorperate into your main.py by typing in \"import run\" and putting this file in.\n\n{runpyifmessage} "# This prob. will start a long story...

def runit():
    wtl("Running...")
    os.system("ipython3 " + runpyfilename) # Run.PY the program!11!!!1!!1!!1!!!
    print("_______________________\nThis Program Was run by RUN.PY\n_______________________\n") # Show End Of Program
    wtl("Closing Program...")
    log.close()
    exit() # Goodbye!

def showhelp():
    wtl("Showing Help GUI")
    print(message) # Backup! 
    f = open(helpfilename, "w") # Open File and 
    f.write(message) # Write Message!
    f.close() # Close The File
    os.system("less " + helpfilename) # Show File In manpage-style format
    os.system("rm " + helpfilename) # Remove File For Disk Space!
    wtl("Closing Program...")
    log.close()
    exit()


# Show RUNPY splash
print("\n_______________________\nRUN.PY IPython Launcher\n_______________________\n") # wow!
if sys.argv == ['run.py', 'help']: # Sombody Wants Help?
    showhelp()
elif not path.is_file(): # File Needs Setup
    wtl("Setting Up File...")
    print("Setting Up File: The File '" + runpyfilename + "' does not exist.") # Show Message
    f = open(runpyfilename, "w") # Open File and Write Code + Message...
    f.write(f"# This IPYthon Program ({runpyfilename}) Will Be Run By RUN.PY.\n# For More Info, Type 'python3 run.py help' (whithout the qoutes!) for info\n# This is Dummy Code; Replace This Later.\n!ls\n%magic\n?help\nprint(\"hello ipython!\")") # cont.
    f.close() # close File
    print("This File Was Setup!") # More Info
elif sys.argv == ['']: # long story short, we need import run to work
    print("Has Been Imported\nThanks for using RUNPY!\n") # They should use the included functions
elif sys.argv == ['./run.py', 'help']: # Sombody Wants Help? (for work with ./)
    showhelp()
elif sys.argv == ['./run.py']: # long story short, we need ./ to work
    runit()
elif sys.argv == ['run.py']:
    runit()
del runit
del showhelp
def showhelp():
    wtl("Addon: Showing help GUI...")
    print(message) # Backup! 
    f = open(helpfilename, "w") # Open File and 
    f.write(message) # Write Message!
    f.close() # Close The File
    os.system("less " + helpfilename) # Show File In manpage-style format
    os.system("rm " + helpfilename) # Remove File For Disk Space!
def py():
    wtl("Addon: Running...")
    os.system("ipython3 " + runpyfilename) # Run.PY the program!11!!!1!!1!!1!!!
    print("_______________________\nThis Program Was run by RUN.PY\n_______________________\n") # Show End Of Program
def devhelp():
    wtl("Addon: Showing DEVhelp...")
    print("Use showhelp to open normal runpy help\nUse py to run.py\nSet runpyfilename To run a diffrent file\n")
def createfile():
    if not path.is_file(): # File Needs Setup
        wtl("Addon: Setting Up File...")
        print("Setting Up File: The File '" + runpyfilename + "' does not exist.") # Show Message
        f = open(runpyfilename, "w") # Open File and Write Code + Message...
        f.write(f"# This IPYthon Program ({runpyfilename}) Will Be Run By RUN.PY.\n# For More Info, Type 'python3 run.py help' (whithout the qoutes!) for info\n# This is Dummy Code; Replace This Later.\n!ls\n%magic\n?help\nprint(\"hello ipython!\")") # cont.
        f.close() # close File
        print("This File Was Setup!") # More Info(
    else:
        wtl("Addon: No file setup.")
