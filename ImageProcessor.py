from PIL import Image
from Channel import *
import os

class ImageProcessor:

    def __init__(self, filename):

        self.filename = filename

        self.image = Image.open(self.filename)
        self.imagePixels = self.image.load()

        self.channels = [] # Cyan, Magenta, Yellow, Black

        # Create 4 color channels the size of the image being processed

        self.channels.append(Channel("CYAN",(self.image.size[0], self.image.size[1])))
        self.channels.append(Channel("MAGENTA",(self.image.size[0], self.image.size[1])))
        self.channels.append(Channel("YELLOW", (self.image.size[0], self.image.size[1])))
        self.channels.append(Channel("BLACK", (self.image.size[0], self.image.size[1])))

    def translateColor(self, value):

        # Find the K value

        k = min(255 - value[0], min(255 - value[1], 255 - value[2]))
        factor = 255 - k

        # Ensure a divide by 0 error does not occur
        if k == 255:
            factor = 1

        # RGB to CMYK conversion

        c = 255 * (255 - value[0] - k) / factor
        m = 255 * (255 - value[1] - k) / factor
        y = 255 * (255 - value[2] - k) / factor

        return [c, m, y, k]

    def processImage(self):

        for x in range(self.image.size[0]):
            for y in range(self.image.size[1]):
                for z in self.channels:

                    # Iterate through each channel, pixel by pixel
                    # Converting the RGB values to CMYK
                    # And outputting each value to its specified layer

                    translatedColor = self.translateColor(self.imagePixels[x, y])
                    if z.channelLabel == "CYAN":
                        self.channels[0].pixelMap[x, y] = (translatedColor[0], 0, 0 , 0)
                    elif z.channelLabel == "MAGENTA":
                        self.channels[1].pixelMap[x, y] = (0, translatedColor[1], 0, 0)
                    elif z.channelLabel == "YELLOW":
                        self.channels[2].pixelMap[x, y] = (0, 0, translatedColor[2], 0)
                    elif z.channelLabel == "BLACK":
                        self.channels[3].pixelMap[x, y] = (0, 0, 0, translatedColor[3])


        self.savePixelMaps()

    def savePixelMaps(self):

        strings = ['C', 'M', 'Y', 'K']

        os.chdir("../Output/")

        path = self.filename
        if not os.path.isdir(path):
            os.makedirs(path)

        for x in range(4):
            self.channels[x].save(path + "/" + self.filename + " - " + strings[x] + ".tif")