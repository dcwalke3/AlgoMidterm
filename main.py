import csvReader
import csv, os, random
from ConsoleClear import ConsoleClear
from tkinter import *

class Table:
    def __init__(self, root):
        
        for i in range(total_rows):
            for j in range(total_columns):
                
                self.e = Entry(root, width = 40, fg='black', font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, data[i][j])

data=[[]]

total_rows = []
total_columns = []

def main():
    print("i")