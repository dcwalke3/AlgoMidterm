import os

def Walker(extension):
    csvFiles = []
    for partition, directory, folder in os.walk('C:\\Users'):
        for file in folder:
            if file.endswith(extension):
                csvFiles.append(file)
            
    print("~~~~Files Available for use~~~~")
    print("-------------------------------")
    for i in range((len(csvFiles))-1):
        print(str(i+1)+".) "+str(csvFiles[i]))

