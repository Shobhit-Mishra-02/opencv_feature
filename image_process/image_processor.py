import cv2 as cv
import numpy as np

class image_convertor:
    def __init__(self, filename):
        self.filename = filename
        self.result = None

    def color_to_gray(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        return self.result

    def color_to_red(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))
        img[:,:,2] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img

        return self.result

    def color_to_blue(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))

        img[:,:,0] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img

        return self.result
    
    def color_to_green(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))

        img[:,:,1] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img

        return self.result
    
    def color_to_black(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))

        edges = cv.Canny(img, 100,200)

        self.result = edges

        return self.result

        

    def show(self):
        cv.imshow('frame', self.result)
        cv.waitKey(0)

class save_file:
    def __init__(self,image, location):
        self.image = image
        self.location = location

    def save_image(self):
        cv.imwrite(f"{self.location}", self.image)

class Merging_interface:
    def __init__(self):
        pass
        

if __name__=="__main__":
    x=image_convertor('image_1.jpg')
    x.color_to_gray()
    x.show()
    # x.save_image()
