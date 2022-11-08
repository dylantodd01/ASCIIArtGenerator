# This script will take an image and output a .txt file
# with a simple ASCII representation of the image

from PIL import Image

img = Image.open("DogImage.jpg")
img = img.resize((120, 70), Image.ANTIALIAS)
pix = img.load()


def main():
    with open('ASCII_Art.txt', 'w') as f:
        txtFileString = ""
        for y in range(img.size[1]):
            txtFileString += '\n'
            for x in range(img.size[0]):
                greyscaleValue = RGBToGreyscale(x, y)
                txtFileString += ASCIIOutput(greyscaleValue)
        
        f.write(txtFileString)


def RGBToGreyscale(x: int, y: int) -> int:
    RGB = pix[x,y]
    greyscaleValue = (RGB[0] + RGB[1] + RGB[2]) // 3
    return greyscaleValue

def ASCIIOutput(greyscaleValue: int) -> str:
    if greyscaleValue > 200:
        return '#'
    elif greyscaleValue > 150:
        return '<'
    elif greyscaleValue > 100:
        return '~'
    elif greyscaleValue > 50:
        return "'"
    else:
        return ' '
