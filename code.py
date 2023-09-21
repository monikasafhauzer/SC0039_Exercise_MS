#importing a csv file brca_cnvc_tvga-1.csv

import csv

#create a function that creates a new csv file with an added column

def add_segment_length(input_file, output_file):
#reads the input file, and opens the output file (write)
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
#reads a csv file
        reader = csv.DictReader(infile)
#fieldname is name of columns and adds the fifth column
        fieldnames = reader.fieldnames + ['segment_length']
#to write out our creation with 5 columns in the out file
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

#data parsing, to convert all data forms into numbers for making the column that needs subtraction
        for row in reader:
            loc_start = int(row['loc.start'])
            loc_end = int(row['loc.end'])
            segment_length = loc_end - loc_start
            row['segment_length'] = segment_length
            writer.writerow(row)
#names of files
if __name__ == "__main__":
    input_file = 'brca_cnvs_tcga-1.csv'  
    output_file = 'output.csv'  
    add_segment_length(input_file, output_file)
