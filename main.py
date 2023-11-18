import cv2
import numpy as np
import random
from scipy import ndimage


def add_gaussian(image, sigma):
    noise = np.random.normal(0, sigma, image.shape)
    output = np.clip(image + noise, 0, 255)
    output = output.astype('uint8')
    return output


def bilateral_filter(image, width, height, sigma_d=50, sigma_r=20):
    #sigma_r = np.uint8(sigma_r)
    kernel_size = 5
    h_xy = np.zeros([kernel_size, kernel_size], dtype=np.float64)
    pad_size = kernel_size//2
    image = np.pad(image, ((pad_size, pad_size), (pad_size, pad_size)), mode='constant')
    output = np.zeros([width,height])
    for x in range(0, height):
        for y in range(0, width):
            for k in range(-pad_size, pad_size+1):
                for l in range(-pad_size, pad_size+1):
                    h_xy[l][k] = np.exp(-1 * (k**2 + l**2) / (2 * (sigma_d**2))) * \
                                 np.exp(-1 * ((int(image[y+2][x+2]) - int(image[y+2+l][x+2+k]))**2) / (2 * (sigma_r ** 2)))
            h_xy = h_xy / np.sum(h_xy)
            output[y][x] = np.sum(image[y:y+(2*pad_size)+1, x:x+(2 * pad_size)+1] * h_xy)
    return output

input_img = cv2.imread('./dgu_gray.png', 0)
input_img = add_gaussian(input_img, 0.1*255)
width, height = input_img.shape

output_img = bilateral_filter(input_img, width, height)

cv2.imshow('inputImg', input_img)
cv2.imshow('outputImg', output_img.astype('uint8'))
cv2.waitKey()
