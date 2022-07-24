import pandas as pd
#import xlrd
import openpyxl
import os
import json
from sortedcontainers import SortedList, SortedSet, SortedDict
#import Pillow
from PIL import Image
from pytesseract import pytesseract

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn)
    df = df.fillna('')
    return df


def getImage(df):

    magset = {"1000X", "100X", "200X", "400X", "40X", "50X"}
    image_dir = r"X:\WebSiteMirrors\TomPowers\images\\"

    count = 0
    for index, row in df.iterrows():
        ImageName = str(row['ImageName']).strip()

        Genus = str(row['Genus']).strip()
        image_path = image_dir + ImageName
        count = count + 1
        print (count)
        #if count > 100:
        #    break

        try:
            text = ocr(image_path)
            text = os.linesep.join([s for s in text.splitlines() if s])
            lines = text.splitlines()
            for i in lines:
                Species = str(i).strip()
                if Genus in str(i):
                    print(i)
                    SpeciesArr = Species.split(" ")
                    if len(SpeciesArr) > 2:
                        Species = SpeciesArr[0] + " " + SpeciesArr[1]
                    print(Species)
                    df.loc[index, 'Species'] = Species

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

