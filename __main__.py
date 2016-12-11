from ImageProcessor import *
import shutil
import os

print("PomegranateCMYK")

def verify_integrity():

    paths = ["Input", "Input/Processed", "Output"]

    for x in paths:
        if not os.path.isdir(x):
            print(x + " not found. Creating " + x)
            os.mkdir(x)

verify_integrity()

os.chdir("Input/")

print("Beginning image processing - Do not close the program.")

for filename in os.listdir(os.curdir):
    if filename.endswith(".jpg") or filename.endswith(".png"):

        img = ImageProcessor(filename)

        print("Processing " +filename+"...")

        img.processImage()

        os.chdir("../Input")

        shutil.move(filename, "Processed")

print("Finished processing all images. You may now exit.")