import os
import shutil
path="/Users/akbalsinghbhullar/Desktop/"
Folder_Name=["Images","TextFiles","Applications","Videos","Music","Blender","Archive","Minecraft"]
names=os.listdir(path)
for x in range(len(Folder_Name)):
    if not os.path.exists(path+Folder_Name[x]):
        os.makedirs(path+Folder_Name[x])
for files in names:
    #Groups Supported so far are: ".jpg",".jpeg",".png",".app",".rtf",".blend",".mp4",".mp3",".m4a",".txt",".mkv"
    if ".gif"  in files and not os.path.exists(path+"Images/"+files):
        shutil.move(path+files,path+"Images/"+files)
    elif ".pdf"in files and not os.path.exists(path+"TextFiles/"+files):
        shutil.move(path+files,path+"TextFiles/"+files)
    elif ".docx"in files and not os.path.exists(path+"TextFiles/"+files):
        shutil.move(path+files,path+"TextFiles/"+files)
    elif ".app" in files and not os.path.exists(path+"Applications/"+files):
        shutil.move(path+files,path+"Applications/"+files)
    elif ".jpg" in files and not os.path.exists(path+"Videos/"+files):
        shutil.move(path+files,path+"Images/"+files)
    elif ".mp3"in files and not os.path.exists(path+"Music/"+files):
        shutil.move(path+files,path+"Music/"+files)
    elif ".blend"in files and not os.path.exists(path+"Blender/"+files):
        shutil.move(path+files,path+"Blender/"+files)
    elif ".m4a"in files and not os.path.exists(path+"Music/"+files):
        shutil.move(path+files,path+"Music/"+files)
    elif ".png"in files and not os.path.exists(path+"Images/"+files):
        shutil.move(path+files,path+"Images/"+files)
    elif ".jpeg"  in files and not os.path.exists(path+"Images/"+files):
        shutil.move(path+files,path+"Images/"+files)
    elif ".docx"in files and not os.path.exists(path+"TextFiles/"+files):
        shutil.move(path+files,path+"TextFiles/"+files)
    elif ".mkv" in files and not os.path.exists(path+"Videos/"+files):
        shutil.move(path+files,path+"Videos/"+files)
    elif ".mov" in files and not os.path.exists(path+"Videos/"+files):
        shutil.move(path+files,path+"Videos/"+files)
    elif ".docx" in files and not os.path.exists(path+"Archive/"+files):
        shutil.move(path+files,path+"TextFiles/"+files)
    elif ".jar" in files and not os.path.exists(path+"Minecraft/"+files):
        shutil.move(path+files,path+"Minecraft/"+files)
    elif ".png"  in files and not os.path.exists(path+"Images/"+files):
        shutil.move(path+files,path+"Images/"+files)