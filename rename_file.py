import os

def rename_files(path):    
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        name, extension = os.path.splitext(filename)

        name_new = name.lstrip("b'")
        extension_new = extension.rstrip("'")
        
        os.rename(file_path,path + name_new + extension_new)
        #print(name_new + extension_new)
def listAll(root):
    for path, subdirs, files in os.walk(root):
        for name in files:

            pathFull = path + "/" + name;
            pathFull = pathFull.replace("\\", "/")
            pathFull = pathFull.replace("//", "/")
            #Đây là pathFull: bao gồm cả path và filename
            tachFileName = pathFull.split("/")
            fileName = tachFileName[len(tachFileName) - 1]
            #Tách file name ra: từ dấu / lấy phần tử cuối của mảng
            tachPath = pathFull.split(fileName)
            path = tachPath[0]
            #Tách path thì lấy cái fileName vừa tách để làm mốc, sau đó lấy phần trước
            name, extension = os.path.splitext(fileName)
            name_new = name.lstrip("b'")
            extension_new = extension.rstrip("'")
            #Bắt đầu replace b'*'
            os.rename(pathFull,path + name_new + extension_new)
            print(pathFull)
            #rename_files(pathFull)
            #if(len(path) > 2):
            ##    path = path.replace("\\", "/")
            ##    path = path.replace("//", "/")
            ##print(path + "/" + name)
            #print(os.path.join(path, name))
            #subfile = subfile.replace("\\", "/")
            #rename_files(subfile)

if __name__ == "__main__":
    #rename_files(r"./")
    listAll(r"./")
    