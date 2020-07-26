import os , shutil

try:
    path="//Users//isudy//Downloads"
    for (path,dirs,files) in os.walk(path):
        for file in files:
            extension=file.split('.')[1]
            print(extension)
            if os.path.exists(r"//Users//isudy//Downloads" +extension):
                if file.endswith(extension):
                    shutil.move(file,"//Users//isudy//Downloads" +extension)
            else:
                os.system("mkdir extension")
                shutil.move(file,"//Users//isudy//Downloads" +extension)



except:
    print("An error has occured")

