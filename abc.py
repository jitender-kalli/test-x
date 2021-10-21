import numpy as np
import pandas as pd
import os

def split(filehandler, delimiter=',', row_limit=499,
          output_name_template='output_%s.csv', output_path='.', keep_headers=True):
    import csv
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers =next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)
#dependency -split()
def filtergenes(tissuelist):

    df =pd.read_csv('normal_tissue.tsv',sep='\t' ,engine='python')
    df=df[["Gene","Tissue"]]
    #for i in tissuelist:    
        #print (i,i in df['Tissue'].values)
    
    df=df[df['Tissue'].isin(tissuelist)]
    df= df['Gene']
    df.drop_duplicates(keep='first',inplace=True) 
    df.to_csv('filtered_normal_tissue.csv', sep="\n" ,header=False, index=False) ;
    split(open('filtered_normal_tissue.csv', 'r'));
 
    return("new files and filtered_normal_tissue.tsv created ")

#dependency - split()
def filtergenescancer(tissuelist):

    df =pd.read_csv('pathology.tsv',sep='\t' ,engine='python')
    df =df[["Gene","Cancer"]]
    #for i in tissuelist:    
    #    print (i,i in df['Cancer'].values)
    #print(df)
    df=df[df['Cancer'].isin(tissuelist)]
    df= df['Gene']
    df.drop_duplicates(keep='first',inplace=True) 
    df.to_csv('filtered_cancer_tissue.csv', sep="\n" ,header=False, index=False) ;
    split(open('filtered_cancer_tissue.csv', 'r'));
    return("new files and filtered_cancer_tissue.tsv created ")
    
# main code
# this generates files of 500 length and filters tissues based on the below list

# this generates files of 500 length and filters based on cancer type given in below list.
list=["lung cancer"]
print(filtergenescancer(list))





