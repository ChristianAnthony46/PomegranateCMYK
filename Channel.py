from PIL import Image

class Channel:

    def __init__(self, channelLabel, size):

        self.channelLabel = channelLabel
        self.channel = Image.new("CMYK", (size[0], size[1]), "black")
        self.pixelMap = self.channel.load()

    def save(self, filename):

        self.channel.save(filename)