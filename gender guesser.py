# -*- coding: utf-8 -*-

import gender_guesser.detector as gender
import csv

input_path = r'/Users/brigitanderson/Documents/Thesis/input datasets/ebird argentina.csv'
output_path = r'/Users/brigitanderson/Documents/Thesis/gender guesser/ebird argentina write.csv'

with open(input_path) as input_file, open(output_path, 'w', newline='') as output_file:
    gender_reader = csv.reader(input_file, delimiter = ',')
    writer = csv.writer(output_file)
    for row in gender_reader:
        name = row[2]
        d = gender.Detector(case_sensitive=False)
        new_column_value = d.get_gender(name)
        row.append(new_column_value)
        writer.writerow(row)
     
        
        




