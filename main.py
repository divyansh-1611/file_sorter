import os
import shutil

path = "C:/Users/Dell/Downloads/"

#file_names = os.listdir(path)

folder_names=["image files","text files","archives","setups","word files","pdf files","other documents","miscellaneous"]

file_names = set(os.listdir(path)) - set(folder_names)

for i in range(len(folder_names)):
    if not os.path.exists(path+folder_names[i]):
        if file in folder_names:
            continue
        os.mkdir(path+folder_names[i])
    else:
        break

for file in file_names:
    if ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".exe" in file and not os.path.exists(path + "setups/" + file):
        shutil.move(path + file, path + "setups/" + file)
    elif any(ext in file for ext in [".zip", ".rar"]) and not os.path.exists(path + "archives/" + file):
        shutil.move(path + file, path + "archives/" + file)
    elif any(ext in file for ext in [".docx", ".doc"]) and not os.path.exists(path + "word files/" + file):
        shutil.move(path + file, path + "word files/" + file)
    elif any(ext in file for ext in [".jpg",".gif", ".jpeg", ".png"]) and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif any(ext in file for ext in [".pptx", ".xlsx", ".csv"]) and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "other documents/" + file)
    else:
        shutil.move(path + file, path + "miscellaneous/" + file)