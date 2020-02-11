#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
import numpy as np
import cv2


def int_to_bin(rgb):
        r=rgb[0]
        g=rgb[1]
        b=rgb[2]

        return ('{0:08b}'.format(r),
                '{0:08b}'.format(g),
                '{0:08b}'.format(b))


def bin_to_int(rgb):
    #convert string tuple to integer tuple
    r,g,b=rgb
    return [int(r, 2),
            int(g, 2),
            int(b, 2)]


def merge_rgb(rgb1, rgb2):
    #merge two RGB tuples
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    rgb = (r1[:4] + r2[:4],
            g1[:4] + g2[:4],
            b1[:4] + b2[:4])
    return rgb


def merge(img1, img2):
        #merge two images
        #check the images img1>img2?
        if img2.shape[0] > img1.shape[0] or img2.shape[1] > img1.shape[1]:
            raise ValueError('Image 2 should not be larger than Image 1!')


        #create new merged image
        new_image = np.zeros(img1.shape, np.uint8)

        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                rgb1 = int_to_bin(img1[i, j])

                #use black pixel as default
                rgb2 = int_to_bin([0,0,0])

                #check if the pixel map position is valid for img2
                if i < img2.shape[0] and j < img2.shape[1]:
                    rgb2 = int_to_bin(img2[i, j])

                #merge the two pixels and convert it to a integer tuple
                rgb =  merge_rgb(rgb1, rgb2)

                new_image[i, j] = bin_to_int(rgb)
        print("Merged two images successfully...")
        return new_image




def unmerge(img):
        #create the new image
        new_image = np.zeros(img.shape, np.uint8)

        #list used to store the image original size
        original_size = img.shape[:2]

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                #get RGB from the current pixel
                r, g, b = int_to_bin(img[i, j])

                #extract the last 4 bits 
                #concatenate 4 zero bits
                rgb = (r[4:] + '0000',
                       g[4:] + '0000',
                       b[4:] + '0000')

                #convert it to an integer array with r,g,b values
                new_image[i, j] = bin_to_int(rgb)

                #if valid store as the last valid position
                if new_image[i, j][0]!=0 and new_image[i, j][1]!=0 and new_image[i, j][2]!=0:
                    original_size = [i + 1, j + 1]

        #crop the image based on valid pixels

        crop_img = new_image[0: original_size[0], 0: + original_size[1]]
        print("Hidden image extracted successfully...")
        return crop_img







