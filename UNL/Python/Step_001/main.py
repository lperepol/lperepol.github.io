import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_csv_file(fn):
    df = pd.read_csv(fn)
    return df

def merge_csv_file(df1, df2):
    df1["Genus"] = ''
    df1["ImageName"] = ''
    for index1, row1 in df1.iterrows():
        Fname = str(row1['Fname']).strip()
        Genus = ''
        SaveimageName = ''
        for index, row in df2.iterrows():
            Fname2 = str(row['Fname']).strip()
            Fname2 = Fname2.split('/')
            strln = len(Fname2)-1
            imageName = Fname2[strln]
            if ".jpg" in imageName:
                if imageName in Fname:
                    if len(Fname2) > 3:
                        Genus = Fname2[3]
                        SaveimageName = imageName
                        print(Genus)
                        print(SaveimageName)
                        print ('************************')
                        break
        df1.loc[index1, 'Genus'] = Genus
        df1.loc[index1, 'ImageName'] = SaveimageName

    fn = "../Metadata/KeepMetadata.csv"  # 11,913
    df1.to_csv(fn)

def main():
    fn = "../Metadata/all_ImageFiles.csv" # 11,913
    df1 = read_csv_file(fn)
    fn = "../Metadata/Genus.csv"          # 11,005
    df2 = read_csv_file(fn)
    merge_csv_file(df1,df2)




if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

