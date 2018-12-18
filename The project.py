from PIL import Image
#img = Image.open('TARGET.jpg')
#img.show()
import cv2

def get_main_color1(file):
    file = "blue.jpg"
    img = Image.open(file)
    colors = img.getcolors(256) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        print(most_present)
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

def get_main_color2(file):
    file = "red.jpg"
    img = Image.open(file)
    colors = img.getcolors(256) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        print(most_present)
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

def get_main_color3(file):
    file = "green.jpg"
    img = Image.open(file)
    colors = img.getcolors(256) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        print(most_present)
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

def get_main_color4(file):
    file = "yellow.jpg"
    img = Image.open(file)
    colors = img.getcolors(256) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        print(most_present)
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")


get_main_color1("")
get_main_color2("")
get_main_color3("")
get_main_color4("")
