import os 
import shutil 

from_dir = "C:/Users/Vanshika/Downloads"
to_dir = "V:/BYJU's Coding/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    root, ext = os.path.splitext(file_name)

    if ext == "":
        continue
    if ext in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + '/' + file_name                        
        path2 = to_dir                  
        path3 = to_dir + '/' + file_name   
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)