'''txt = 'I like Mutton Briyani.'
file_path = 'output.txt'
try:
    with open(file_path,"x") as file:
        file.write(txt)
        print(f'the file {file_path} is written.')
except FileExistsError:
    print('That file is already exists')'''

import csv
txt = [['name','age','job'],
       ['spiderman',18,'superhero']]
file_path = 'output.csv'
try:
    with open(file_path,'w') as file:
        writer = csv.writer(file)
        for row in txt:
            writer.writerow(row)
        print(f'the file {file_path} is written.')
except FileExistsError:
    print('That file is already exists')

