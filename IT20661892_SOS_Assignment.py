#IT20661892

#Importing built-in python libraries
import platform
import os
import datetime

#Define Function for windows platform to print output to Log File
def print_windows(printfile):
    output_path = "C:\\Users\\rithm\\OneDrive\\Desktop\\entries_Win10.log" 
    fileprint = open(output_path, 'a')
    fileprint.write(f"{printfile}")
    fileprint.close()

#Define Function for windows platform to print output to Log File
def print_linux(printfile):
    output_path = "/home/rithma/Desktop/entries_Lin.log" 
    fileprint = open(output_path, "a")
    fileprint.write(f"{printfile}")
    fileprint.close()

#Checking Condition to identify the os version is "Windows"
#'nt' means that Computer running windows
if os.name == "nt": 
    
    #retrieve information about the platform on which the program is being currently executed
    system_info = platform.platform()
    print ('Platform:',(system_info))
    print_windows((system_info)) 

  
    #Getting current System Date & Time
    from datetime import datetime, timezone   
    datetime = datetime.now(timezone.utc).astimezone()
    print(datetime.strftime("%d/%b/%y\n%H:%M %p"'\n'))
    print_windows(datetime.strftime("%d/%b/%y\n%H:%M %p"'\n'))

    print()
    print_windows("")
   
    #Generate a list of all the ‘.exe’ files available in ‘C:\Windows\system32’ directory
    os.system('DIR C:\Windows\System32\*.exe')
    os.system('DIR C:\Windows\System32\*.exe >> "C:\\Users\\rithm\\OneDrive\\Desktop\\entries_Win10.log"')
   
    pass

#Checking Condition to identify the os version is "Linux"
#'posix'= Linux
elif os.name == "posix":

    #retrieve information about the platform on which the program is being currently executed
    system_info = platform.platform()
    print ('Platform:',(system_info))
    print_linux("Platform:")
    print_linux(system_info)
    print_linux("\n")

    #Getting current System Date & Time
    from datetime import datetime, timezone   
    SDT = datetime.now(timezone.utc).astimezone()
    print(SDT.strftime("%a %b %d %H:%M:%S %z %Y"'\n'))
    print_linux("\n")
    print_linux(SDT.strftime("%a %b %d %H:%M:%S %z %Y"'\n'))
    
    #Generate a list of all the ‘.bin’ files in directories and subdirectories inside the ‘lib’ folder
    for root, dirs, files in os.walk('/lib/'):
	    for file in files:
		    if file.endswith('.bin'):
			    print(os.path.join(root, file))
			    print_linux("\n")
			    print_linux(os.path.join(root, file))
    pass	

#If either "Windows" or "Linux" not detected, programe will redirrect to else part execute
else:
    print("No match")
    
