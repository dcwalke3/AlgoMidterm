import csv, os
from ConsoleClear import ConsoleClear
import fileWalker

def Reader(csvFile):
    csvPath = ""
    print("Started")
    try:
        csvPath = fileWalker.Walker(csvFile)
        print(csvPath)
    
    except:
        print("The CSV file can not be found on the local machine.")
        print("\nWould you like for ")
        while(True):
            ConsoleClear()
            csvFile = input("Please Enter the name of the file.")
            try:
                csvPath = fileWalker.Walker(csvFile)
                break
            except:
                continue
            
    print(csvPath)
    csvName = os.path.basename(csvPath)
    data = {}
    fields = []
    with open(csvName, 'r') as File:
        print("sucsess!")
        csvReader = csv.reader(File)

        fields = next(csvReader)

        counter = 0
        for row in csvReader:
            data[counter] = row
            counter+=1
    
    File.close()
    return data

        
