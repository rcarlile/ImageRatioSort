# Program Name: ImageRatioSort.py
# Author: Robert Carlile
# Creation Date: 2024-03-23
# Requirements:
#   Python 3
#   Pip command: pip install pillow

# Description
# It analyses images in a folder calculates the aspect ratio,
# then creates a folder for that ratio and ove the image in that folder.
# I have it calculate to one decimal place to cut down on the number of folders to deal with.

# Directions
#   Create a directory
#   Copy script to that folder
#   Make another folder named what is set in the unsorted_directory variable
#   Run the script: python3 ImageRatioSort

# Notes:
# Popular ratios and what I call them.
# 16x9 - 1.77 - Widescreen
# 4x3  - 1.33 - Square
# 21x9 - 2.33 - Ultra Widescreen

# History:
# 2024-03-23    RC  Initial Creation
# 2024-03-24    RC  Added image extension check

from PIL import Image
import os
import shutil

# This is the directory for the unsorted images
unsorted_directory = 'Unsort'
image_ext = ('.jpg','.png','.bmp','.jpeg', '.gif')

#Lets loop through the unsorted folder
for filename in os.listdir(unsorted_directory):

    # Build Full path of file
    full_file_path = os.path.join(unsorted_directory, filename)

    # If the file is a file and not a directory
    if os.path.isfile(full_file_path):

        # Lets not process .DS_Store on mac
        if filename.lower().endswith(image_ext):

            #Lets get some variables going.
            file_image = Image.open(full_file_path)
            ratio_number = file_image.width / file_image.height
            ratio_string = "%.1f" % ratio_number
            base_filename = os.path.basename(full_file_path)
            new_file_path = os.path.join(ratio_string, base_filename)

            # Lets print some image info to the screen.
            print('Filename: ', full_file_path)
            print('Width: ', file_image.width)
            print('Height: ', file_image.height)
            print('Ratio: ', ratio_string)
            print(new_file_path)

            # If the ratio folder does not exist then make it. Needs to be flipped.
            if os.path.isdir(ratio_string) == False:
                os.mkdir(ratio_string)

            # Move the image to the proper ratio folder
            shutil.move(full_file_path, new_file_path)
