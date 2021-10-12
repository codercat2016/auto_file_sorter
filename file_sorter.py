import os
import shutil
import json
current_dir = os.getcwd()

savefile = os.path.join(current_dir,"file_info.dat")
config = open('config.json',"r+")
config_object  = json.load(config)

file_object = open(savefile,"r+")
# file_object.close()
folders = []
initial_run = False
new_temp_folders = []
lines =file_object.read().splitlines()

#Getting already stored folders
if not lines: 
  initial_run = True
else:    
    for line in lines:
        folders.append(line)
    
#getting new folder names 

for f in os.listdir(current_dir):
    filename , file_ext = os.path.splitext(f)
    try:
        if not file_ext:
            if filename not in folders :
                new_temp_folders.append(filename)
                folders.append(filename)   
            else:
                pass
        else:
            pass
    except(FileNotFoundError,PermissionError):
        pass
print(folders)    
if not new_temp_folders:
    pass
else:
    for folder_name in new_temp_folders:

       file_object.write(folder_name+"\n")    
           
for current_folder_name in folders :
    current_folder_name_str = str(current_folder_name) 
    
    for f in os.listdir(current_dir):
        filename , file_ext = os.path.splitext(f)
        temp_file_ext = file_ext.replace(".","")
        if filename+file_ext == str(os.path.basename(__file__)):
            pass
        else: 
            try:
                if not file_ext:
                    
                    pass
                elif temp_file_ext == current_folder_name :
                    if(temp_file_ext.casefold() == current_folder_name_str.casefold() ):
                        
                        shutil.move(
                            os.path.join(current_dir,f'{filename}{file_ext}'),
                            os.path.join(current_dir,current_folder_name_str,f'{filename}{file_ext}')
                    )


            except(FileNotFoundError,PermissionError):
                pass