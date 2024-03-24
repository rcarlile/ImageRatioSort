# Image Ratio Sort

**Author:** Robert Carlile  
**Creation Date:** 2024-03-23

## Requirements:
  Python 3  
  Pip command: pip install pillow

## Description
It analyses images in a folder calculates the aspect ratio, then creates a folder for that ratio and ove the image in that folder. I have it calculate to one decimal place to cut down on the number of folders to deal with.

## Directions
  1. Create a directory
  2. Copy script to that folder
  3. Make another folder named what is set in the _unsorted_directory_ variable
  4. Copy the images that need sorting in to the _unsorted_directory_ folder
  5. Run the script: python3 ImageRatioSort.py

## Notes
Popular ratios and what I call them.
| Proportions | Decimal Ratio | What I Call It |
| --- | --- | --- |
|16x9 | 1.77 | Widescreen |
|4x3 | 1.33 | Square |
|21x9 | 2.33 | Ultra Widescreen |

## History
| Date | Author | Description |
| --- | --- | --- |
| 2024-03-23 | RC | Initial Creation |
| 2024-03-24 | RC | Added image extension check |
