"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist =((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**(1/2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    r_av=0
    g_av=0
    b_av=0
    for i in range(len(pixels)):
        r_av += pixels[i].red
    r_av //= len(pixels)

    for i in range(len(pixels)):
        g_av += pixels[i].green
    g_av //= len(pixels)

    for i in range(len(pixels)):
        b_av += pixels[i].blue
    b_av //= len(pixels)

    return [r_av,g_av,b_av]



def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    r_av = get_average(pixels)[0]
    g_av = get_average(pixels)[1]
    b_av = get_average(pixels)[2]
    best_d = 100000000000 # initialize best_d a very large word
    best_p = 0
    for i in range(len(pixels)):
        d =((r_av - pixels[i].red)**2 +(g_av - pixels[i].green)**2 + (b_av - pixels[i].blue)**2)**(1/2)
        if d < best_d:
            best_d = d
            best_p = i
    return pixels[best_p]






def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    pixel_lst = []




    for i in range(width):
        for j in range(height):
            for image in images:
                pixel = image.get_pixel(i,j)
                pixel_lst.append(pixel)
            pixel = get_best_pixel(pixel_lst)
            pixel_result = result.get_pixel(i,j)
            pixel_result.red = pixel.red
            pixel_result.green = pixel.green
            pixel_result.blue = pixel.blue
            pixel_lst = []





    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
