import pandas as pd
#import xlrd
import openpyxl
import os
import json
from sortedcontainers import SortedList, SortedSet, SortedDict
from PIL import Image
from pytesseract import pytesseract

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn)
    df = df.fillna('')
    return df

def GetGender(text):
    List = [
        r"juvenile",
        r"female",
        r"male",
        r"cyst",
        r"female "
    ]
    for i in List:
        if i in text:
            return i
    return ""

def GetMag(text):
    List = [
        r"1000X",
        r"400X",
        r"200X",
        r"100X",
        r"40X",
        r"50X"
    ]
    for i in List:
        if i in text:
            return i
    return ""

def GetLocation(text):
    List = [
        r"9 Mie Prairie",
        r"9 Mile Prairie",
        r"Avoca Prairie",
        r"Bangtail Ridge",
        r"Bearberry",
        r"Brookings",
        r"Clarks",
        r"Colorado",
        r"Costa Rica",
        r"Dalhart",
        r"Delaware",
        r"Douglas County",
        r"Durango",
        r"Falls City",
        r"Florida",
        r"George Washington Memorial",
        r"Governor Dodge",
        r"Great Smoky Mountains National Park",
        r"Great Smoky Mountains",
        r"Great Smoky Moutians",
        r"Grundy county",
        r"Half Moon Bay",
        r"Hamey Peak",
        r"Haughton Crater In oasis",
        r"Haughton Crater",
        r"Haughton Crator",
        r"Homestead Nat'l Monument",
        r"Homestead Restored Prarie",
        r"Jasper county",
        r"Jumbo Valley",
        r"Kalsow Prairie",
        r"Kalsow Prarie",
        r"Kalsow",
        r"Kearney",
        r"Keim Hall",
        r"Konza Praire",
        r"Konza Prairie",
        r"Konza Prarie",
        r"La Selva Biological Station",
        r"Laboratory specimen",
        r"Lamoille county",
        r"Larmine",
        r"Lava Mountain",
        r"Lava",
        r"Leadplant",
        r"Lincoln County Club",
        r"Lincoln",
        r"Long's Peak",
        r"Mead pasture",
        r"Middle Loup River",
        r"Minnesota",
        r"Missouri",
        r"Montana",
        r"Mount Rushmore",
        r"Nance county",
        r"Niobrara River",
        r"NMSU",
        r"Oahu",
        r"Ord",
        r"Pachaug State Forest",
        r"Pammel woods",
        r"Perkins County",
        r"Poteet",
        r"Redbud",
        r"Reichelt Remant Prarie",
        r"Rich County",
        r"Rocky Mountain Nat'l Park",
        r"San Jaun",
        r"Schluckebier Prairie",
        r"Scotch Pine",
        r"Sheeder Prairie",
        r"Siver Falls State Park",
        r"Texas potato field",
        r"Texas",
        r"UC Davis",
        r"University of Washington Arboretum Seattle",
        r"USDA",
        r"Utah",
        r"Waldo",
        r"Williams Prairie",
        r"Wisconsin"
    ]
    for i in List:
        if i in text:
            return i
    return ""

def GetView(text):
    List = [
        r"body",
        r"anterior",
        r"tail",
        r"head",
        r"lateral field",
        r"tail tip",
        r"basal esophagus",
        r"vulva",
        r"median bulb",
        r"esophagus",
        r"compare",
        r"spermatheca",
        r"spicules",
        r"ovary",
        r"basal bulb",
        r"anus",
        r"amphid",
        r"cuticle",
        r"corpus",
        r"probolae",
        r"phasmid",
        r"longitudinal lines",
        r"dorsal gland oriface",
        r"basal pharynus",
        r"testis",
        r"dorsal gland nucleus",
        r"sperm",
        r"supplements",
        r"fascicles",
        r"DN/DO",
        r"S1O/S2O",
        r"pharynx",
        r"pharyngeal bulb",
        r"posterior",
        r"guiding ring",
        r"lips",
        r"intestinal junction",
        r"lateral pores",
        r"egg",
        r"testes",
        r"boby",
        r"odontostyle",
        r"cardia",
        r"ovaries",
        r"gut(prerectum)",
        r"stoma",
        r"midbody",
        r"stylet",
        r"esophageal intestinal junstion",
        r"cardiae glands",
        r"esophageal musculature",
        r"reproductive tract",
        r"esophageal contriction",
        r"esophaheal bulb",
        r"anterior esophagus",
        r"dorsal gland nuclei",
        r"anterior ovary",
        r"z-organ",
        r"parasites",
        r"amphid ",
        r"amphid aperature",
        r"bode",
        r"labial region-crenation",
        r"annule membranes",
        r"cuticle anterior",
        r"cuticle posterior",
        r"head / scales",
        r"tail / vulva flap",
        r"scales",
        r"tail dorsal view",
        r"tail lateral view",
        r"anterior annules",
        r"head/stoma/tooth",
        r"posterior esophagus",
        r"intestine",
        r"posterior midbody",
        r"anterior testis",
        r"reproductive system",
        r"lateral lines",
        r"anterior cuticle",
        r"amour",
        r"esophageal bulb",
        r"armor",
        r"dorsal gland orafice",
        r"oesophageal overlap"
    ]
    for i in List:
        if i in text:
            return i
    return ""

def GetHost(text):
    List = [
        r"Little bluestem/ Scribner's panicum",
        r"Little bluestem/Seribner's panicum",
        r"Big bluestem/Scribner's panicum",
        r"Big bluestem/Seribner's panicum",
        r"Scribner's panicum/ Bluegrass",
        r"Big bluestem/|_ittle bluestem",
        r"Big bluestem/Little bluestem",
        r"Seribner's panicum/Bluegrass",
        r"Big bluestem/Senbner's panicum",
        r"Little bluestem/Sporobolus",
        r"Big bluestem/Blluegrass",
        r"Big bluestem/Bluegrass",
        r"Caucasian bluestem",
        r"forest floor litter",
        r"Scribner's panicum",
        r"Laboratory specimen",
        r"Seribner's panicum",
        r"Serbner's panicum",
        r"Little bluestem",
        r"Big bluestem",
        r"Bigbluesten/",
        r"Attemesia",
        r"Sporobolus",
        r"Switchgrass",
        r"Dead pig B",
        r"Junegrass",
        r"Dead pig A",
        r"Dead pig",
        r"Bluegrass",
        r"Blucgess",
        r"Leadplant",
        r"in oasis",
        r"in oasis",
        r"In oasis"
    ]
    for i in List:
        if i in text:
            return i
    return ""

def getImage(df):

    magset = {"1000X", "100X", "200X", "400X", "40X", "50X"}
    image_dir = r"X:\WebSiteMirrors\TomPowers\images\\"

    count = 0
    for index, row in df.iterrows():
        ImageName = str(row['ImageName']).strip()
        GenderDf = str(row['Gender']).strip()
        ViewDf = str(row['View']).strip()
        MagnificationDf = str(row['Magnification']).strip()
        LocationDf = str(row['Location']).strip()
        Hostdf = str(row['Host']).strip()
        image_path = image_dir + ImageName
        count = count + 1
        print (count)
        #if count > 100:
        #    break

        try:
            text = ocr(image_path)
            text = os.linesep.join([s for s in text.splitlines() if s])
            host = ""
            gender = ""
            view = ""
            location = ""
            mag = ""
            lines = text.splitlines()
            #for i in lines:
            i = text
            if len(host) < 1 :
                host = GetHost(i)
            if len(gender) < 1 :
                gender = GetGender(i)
            if len(view) < 1 :
                view = GetView(i)
            if len(location) < 1 :
                location= GetLocation(i)
            if len(mag) < 1 :
                mag =  GetMag(i)

            GenderDf = str(row['Gender']).strip()
            ViewDf = str(row['View']).strip()
            MagnificationDf = str(row['Magnification']).strip()
            LocationDf = str(row['Location']).strip()
            Hostdf = str(row['Host']).strip()
            if len(Hostdf) < 1 :
                df.loc[index, 'Host'] = host
            if len(GenderDf) < 1 :
                df.loc[index, 'Gender'] = gender
            if len(ViewDf) < 1 :
                df.loc[index, 'View'] = view
            if len(LocationDf) < 1 :
                df.loc[index, 'Location'] = location
            if len(MagnificationDf) < 1 :
                df.loc[index, 'Magnification'] = mag
            df.loc[index, 'ImageText'] = text

            if view == 'vulva':
                df.loc[index, 'Gender'] = 'female'
            if view == 'spicules':
                df.loc[index, 'Gender'] = 'male'
        except:
                print("An exception occurred")
                print(image_path)
    fn = "../Metadata/ManualEdits/KeepMetadata_003_test.csv"
    df.to_csv(fn)
    return df

def ocr(image):
    # Defining paths to tesseract.exe
    # and the image we would be using
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = image

    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract
    # executable location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to
    # image_to_string() function
    # This function will
    # extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text

    return(text)

def main():
    df = read_metadata()
    getImage(df)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

