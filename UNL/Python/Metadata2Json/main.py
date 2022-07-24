import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn)
    return df


def fixup(df):
    df = df.fillna(0)
    for index, row in df.iterrows():
        Magnification = str(row['Magnification']).strip()
        if Magnification.isdigit():
            Magnification = int(Magnification)
            Magnification = "{:03d}X".format(Magnification)
        df.loc[index, 'Magnification'] = Magnification
    return df

def get_order(adic, df):
    for index, row in df.iterrows():
        View = str(row['View']).strip()
        if View == '0':
            continue

        Order = str(row['Order']).strip()
        adic[Order] = SortedDict()
    return adic

def get_family(adic, df):
    for index, row in df.iterrows():
        View = str(row['View']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        adic[Order][Family] = SortedDict()
    return adic

def get_genus(adic, df):
    for index, row in df.iterrows():
        View = str(row['View']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        adic[Order][Family][Genus] = SortedDict()
    return adic

def get_gender(adic, df):
    for index, row in df.iterrows():
        View = str(row['View']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        adic[Order][Family][Genus][Gender] = SortedDict()
    return adic

def get_magnification(adic, df):
    for index, row in df.iterrows():
        View = str(row['View']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        Magnification = str(row['Magnification']).strip()
        adic[Order][Family][Genus][Gender][Magnification] = SortedDict()
    return adic

def get_view(adic, df):
    for index, row in df.iterrows():
        View = str(row['View']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        Magnification = str(row['Magnification']).strip()
        View = str(row['View']).strip()
        adic[Order][Family][Genus][Gender][Magnification][View]  = list()
    return adic

def get_image_file_name(adic, df):
    orderSet = set()
    FamilySet = set()
    GenusSet = set()
    ImageSet = set()
    for index, row in df.iterrows():
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        Magnification = str(row['Magnification']).strip()
        View = str(row['View']).strip()
        orderSet.add(Order)
        FamilySet.add(Family)
        GenusSet.add(Genus)

        if View == '0':
            continue

        ImageName = str(row['ImageName']).strip()
        ImageSet.add(ImageName)

        if ImageName not in adic[Order][Family][Genus][Gender][Magnification][View]:
            adic[Order][Family][Genus][Gender][Magnification][View].append(ImageName)

    print ("Order:" + str(len(orderSet)) + ", Family:" + str(len(FamilySet)) + ", Genus:" + str(len(GenusSet)) + ", Completed:" + str(len(ImageSet)) )
    # Order:12, Family:67, Genus:248
    return adic

def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/unl/KeepMetadata2Json_7.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_metadata()
    df = fixup(df)
    nematode_dict = SortedDict()
    nematode_dict = get_order(nematode_dict, df)
    nematode_dict = get_family(nematode_dict, df)
    nematode_dict = get_genus(nematode_dict, df)
    nematode_dict = get_gender(nematode_dict, df)
    nematode_dict = get_magnification(nematode_dict, df)
    nematode_dict = get_view(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

