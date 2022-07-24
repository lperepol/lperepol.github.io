import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_csv_file(fn):
    df = pd.read_csv(fn,encoding='cp1252')
    return df

def merge_csv_file(df1, df2):
    df1["ScientificName_accepted"] = ''
    df1["ScientificName"] = ''
    df1["Class"] = ''
    df1["Order"] = ''
    df1["Family"] = ''
    for index1, row1 in df1.iterrows():
        Genus = str(row1['Genus']).strip()
        ScientificName_accepted = ''
        ScientificName = ''
        Class = ''
        Order = ''
        Family = ''
        for index, row in df2.iterrows():
            Genus2 = str(row['Genus']).strip()
            if Genus == Genus2:
                ScientificName_accepted = str(row['ScientificName_accepted']).strip()
                ScientificName = str(row['ScientificName']).strip()
                Class = str(row['Class']).strip()
                Order = str(row['Order']).strip()
                Family = str(row['Family']).strip()
                break

        df1.loc[index1, 'ScientificName_accepted'] = ScientificName_accepted
        df1.loc[index1, 'ScientificName'] = ScientificName
        df1.loc[index1, 'Class'] = Class
        df1.loc[index1, 'Order'] = Order
        df1.loc[index1, 'Family'] = Family

    fn = "../Metadata/KeepMetadata_002.csv"  # 11,913
    df1.to_csv(fn)

def main():
    fn = "../Metadata/KeepMetadata.csv"
    df1 = read_csv_file(fn)
    fn = "../Metadata/matchthesegenera_matched.csv"
    df2 = read_csv_file(fn)
    merge_csv_file(df1,df2)


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

