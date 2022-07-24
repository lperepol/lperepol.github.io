import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict
from PIL import Image
from pytesseract import pytesseract

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn)
    return df

def getImage(df):
    magset = {"1000X", "100X", "200X", "400X", "40X", "50X"}
    df = df.fillna(0)
    image_dir = r"X:\WebSiteMirrors\TomPowers\images\\"
    GenderSet = SortedSet()
    LocationSet = SortedSet()
    ViewSet = SortedSet()
    for index, row in df.iterrows():
        ImageName = str(row['ImageName'])
        Gender = str(row['Gender']).strip().upper()
        Location =str(row['Location']).strip().upper()
        View = str(row['View']).strip().upper()
        GenderSet.add(Gender)
        LocationSet.add(Location)
        ViewSet.add(View)

    df['View_2'] = ''
    df['Gender_2'] = ''
    df['Mag_2'] = ''
    df['Location_2'] = ''
    count = 0
    for index, row in df.iterrows():
        ImageName = str(row['ImageName']).strip()
        Gender = str(row['Gender']).strip().upper()
        Location = str(row['Location']).strip().upper()
        View = str(row['View']).strip().upper()
        image_path = image_dir + ImageName
        count = count + 1
        print (count)
        Gender_2 = ""
        View_2 = ""
        if count> 1000:
           break
        try:
            text = ocr(image_path)
            lines = text.splitlines()
            for l in lines:
                line = str(l).strip().upper()
                for vw in ViewSet:
                    if vw in line:
                        df.loc[index, 'View_2'] = str(vw).lower()
                        View_2 = str(vw).lower()
                if len(View_2) < 3 :
                    if '40X' in line:
                        df.loc[index, 'View_2'] = 'body'
                    if '50X' in line:
                        df.loc[index, 'View_2'] = 'body'
                    if 'MET EL SEEKS' in line:
                        df.loc[index, 'View_2'] = 'tail'
                for vw in GenderSet:
                    if vw in line:
                        df.loc[index, 'Gender_2'] = str(vw).lower()
                        Gender_2 = str(vw).lower()
                if len(Gender_2) < 3:
                    if 'MET EL SEEKS' in line:
                        df.loc[index, 'Gender_2'] = 'juvenile'
                    if 'VULVA' in line:
                        df.loc[index, 'Gender_2'] = 'female'
                    if 'SPICULE' in line:
                        df.loc[index, 'Gender_2'] = 'male'

                line = line.title()
                if 'Crater' in line:
                    df.loc[index, 'Location_2'] = 'Haughton Crater'
                if 'laboratory' in line:
                    df.loc[index, 'Location_2'] = 'laboratory specimen'
                if 'Konza' in line:
                    df.loc[index, 'Location_2'] = 'Konza Praire'
                if 'Nine Mile' in line:
                    df.loc[index, 'Location_2'] = 'Nine Mile'
                if 'Mead' in line:
                    df.loc[index, 'Location_2'] = 'Mead Pasture'
                if 'Jumbo' in line:
                    df.loc[index, 'Location_2'] = 'Jumbo Valley'
                if 'Costa' in line:
                    df.loc[index, 'Location_2'] = 'Costa Rica'
                if 'Lava' in line:
                    df.loc[index, 'Location_2'] = 'Lava Mountain'
                if "Long's" in line:
                    df.loc[index, 'Location_2'] = "Long's Peak"
                if 'Homestead' in line:
                    df.loc[index, 'Location_2'] = "Homestead Nat'l Monument"
                if 'Great Smoky' in line:
                    df.loc[index, 'Location_2'] = 'Great Smoky Mountains'
                if 'Half Moon' in line:
                    df.loc[index, 'Location_2'] = 'Half Moon Bay'
                if 'USDA' in line:
                    df.loc[index, 'Location_2'] = 'USDA'
                if 'Washington' in line:
                    df.loc[index, 'Location_2'] = 'George Washington Memorial'
                if 'Rocky Mountain' in line:
                    df.loc[index, 'Location_2'] = "Rocky Mountain Nat'l Park"
                if 'Kearney' in line:
                    df.loc[index, 'Location_2'] = 'Kearney'
                if 'Dalhart' in line:
                    df.loc[index, 'Location_2'] = 'Dalhart'
                if 'Bearberry' in line:
                    df.loc[index, 'Location_2'] = 'Bearberry'
                if 'Leadplant' in line:
                    df.loc[index, 'Location_2'] = 'Leadplant'
                if 'Jasper' in line:
                    df.loc[index, 'Location_2'] = 'Jasper county'
                if 'Grundy' in line:
                    df.loc[index, 'Location_2'] = 'Grundy county'
                if 'Texas' in line:
                    df.loc[index, 'Location_2'] = 'Texas potato field'
                if 'Poteet' in line:
                    df.loc[index, 'Location_2'] = 'Poteet'
                if 'Pachaug' in line:
                    df.loc[index, 'Location_2'] = 'Pachaug State Forest'
                if 'Great Smoky' in line:
                    df.loc[index, 'Location_2'] = 'Great Smoky Moutians'
                if 'Homestead' in line:
                    df.loc[index, 'Location_2'] = 'Homestead Restored Prarie'
                if 'Keim' in line:
                    df.loc[index, 'Location_2'] = 'Keim Hall'
                if 'Scotch' in line:
                    df.loc[index, 'Location_2'] = 'Scotch Pine'
                if 'Falls City' in line:
                    df.loc[index, 'Location_2'] = 'Falls City'
                if 'Sheeder' in line:
                    df.loc[index, 'Location_2'] = 'Sheeder Prairie'
                if 'Niobrara' in line:
                    df.loc[index, 'Location_2'] = 'Niobrara River'
                if 'Douglas' in line:
                    df.loc[index, 'Location_2'] = 'Douglas County'
                if 'Larmine' in line:
                    df.loc[index, 'Location_2'] = 'Larmine'
                if 'Redbud' in line:
                    df.loc[index, 'Location_2'] = 'Redbud'
                if 'Minnesota' in line:
                    df.loc[index, 'Location_2'] = 'Minnesota'
                if 'Rushmore' in line:
                    df.loc[index, 'Location_2'] = 'Mount Rushmore'
                if 'Ord, NE' in line:
                    df.loc[index, 'Location_2'] = 'Ord, NE'
                if 'Texas' in line:
                    df.loc[index, 'Location_2'] = 'Texas'
                if 'Lincoln' in line:
                    df.loc[index, 'Location_2'] = 'Lincoln County Club'
                if 'Brookings' in line:
                    df.loc[index, 'Location_2'] = 'Brookings'
                if 'Haughton' in line:
                    df.loc[index, 'Location_2'] = 'Haughton Crator'


                line = line.upper()

                if '1000X' in line:
                    df.loc[index, 'Mag_2'] = '1000X'
                if '400X' in line:
                    df.loc[index, 'Mag_2'] = '400X'
                if '200X' in line:
                    df.loc[index, 'Mag_2'] = '200X'
                if '100X' in line:
                    df.loc[index, 'Mag_2'] = '100X'
                if '40X' in line:
                    df.loc[index, 'Mag_2'] = '40X'
                if '50X' in line:
                    df.loc[index, 'Mag_2'] = '50X'
                if 'MET EL SEEKS' in line:
                    df.loc[index, 'Mag_2'] = '400x'



        except:
                print("An exception occurred")
                print(image_path)
    fn = "../Metadata/ManualEdits/KeepMetadata_002_test.csv"
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

