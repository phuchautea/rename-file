import os

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        
def main():
    
    dirName = './';
    
    listOfFiles = getListOfFiles(dirName)
    
    for elem in listOfFiles:
        print(elem)
    print ("****************")
    
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
        
    for elem in listOfFiles:
        print(elem)    
        
        
        
        
if __name__ == '__main__':
    main()