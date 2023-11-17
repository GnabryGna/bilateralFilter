import cv2
import numpy as np
import random
from scipy import ndimage


def add_gaussian(image, sigma):
    noise = np.random.normal(0, sigma, image.shape)
    output = np.clip(image + noise, 0, 255)
    output = output.astype('uint8')
    return output


def bilateral_filter(image, width, height):

    pass

input_img = cv2.imread('./dgu_gray.png', 0)
input_img = add_gaussian(input_img, 0.1*255)
width, height = input_img.shape

output_img = bilateral_filter(input_img, width, height)
cv2.imshow('inputImg', input_img)
cv2.waitKey()
