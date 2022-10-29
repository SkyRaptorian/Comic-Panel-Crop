#Import required Image library
import os.path
from PIL import Image

page_count = 1
page_path = "page-{}.png"
panel_count = 1
panel_path = "final/{}-{}.png"
panel_size = {
  "1": (76, 87, 610, 465),
  "2": (76, 499, 610, 877),
  "3": (76, 908, 610, 1292),
  "4": (76, 1323, 610, 1705),
  "5": (666, 87, 1200, 465),
  "6": (666, 499, 1200, 877),
  "7": (666, 908, 1200, 1292),
  "8": (666, 1323, 1200, 1705)
}

#Loop for incremental value (until it runs out of pages)
while os.path.exists(page_path.format(page_count)):
    page = Image.open(page_path.format(page_count))
    while panel_count < 9:
        panel = page.crop(panel_size["%s" % panel_count])
        panel.save(panel_path.format(page_count, panel_count))
        panel_count += 1
    panel_count = 1
    page_count += 1

#Get page
#Retreive panels loop six times

#left, upper, right, lowe
#Crop
#cropped = im.crop((1,2,300,300))

#Display the cropped portion
#cropped.show()

#Save the cropped image


#1-(76, 87, 610, 465)
#2-(76, 499, 610, 877)
#3-(76, 908, 610, 1292)
#4-(76, 1323, 610, 1705)
#5-(666, 87, 1200, 465)
#6-(666, 499, 1200, 877)
#7-(666, 908, 1200, 1292)
#8-(666, 1323, 1200, 1705)
