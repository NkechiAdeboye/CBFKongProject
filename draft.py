
import csv

with open('C:/Users/nky98/Documents/Python Project/gender_development_index.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader :
        print(row)
    
    