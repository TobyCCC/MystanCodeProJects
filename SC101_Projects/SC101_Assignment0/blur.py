"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: image, original picture.
    :return: image, the picture that has undergone blur processing.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = new_img.get_pixel(x,y)
            count = 0                                               #Count how many neighbors.
            avg_red = 0
            avg_blue = 0
            avg_green = 0
            for a in range(x-1, x+2):                               #Find neighbors.
                if a >= 0 and a < img.width:
                    for b in range(y-1, y+2):
                        if b >= 0 and b < img.height:
                            pixel_origin = img.get_pixel(a,b)
                            avg_red += pixel_origin.red
                            avg_green += pixel_origin.green
                            avg_blue += pixel_origin.blue
                            count += 1
            pixel.red = avg_red / count
            pixel.green = avg_green / count
            pixel.blue = avg_blue / count
    return new_img


def main():
    """
    TODO: This program will conduct blur processing.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
