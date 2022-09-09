


import os
from PIL import Image
from colorama import Fore


#def console():
#    print("Type copy to copy to clipboard your ascii text\nType 'quit' to close the program\n\nMade by Mattia Raffaele :)")
#    code = input()
#    
#    if code == "copy":
#        fh = open("_TXT/" + artName)






# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "." , "\\"]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    # attempt to open image from user-input
    print(Fore.RED + "Your image MUST be copyright free, you will be responsible for all legal actions that the author of the image will make, type I confirm to accept")
    confirm = input(Fore.WHITE)
    if confirm == "I confirm":

        path = input("\nEnter a valid pathname to an image:\n")
        try:
            image = Image.open(path)
        except:
            print(path, " is not a valid pathname to an image.")
            return()
    
        # convert image to ascii    
        new_image_data = pixels_to_ascii(grayify(resize_image(image)))
        
        # format
        pixel_count = len(new_image_data)  
        ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
        
        # print result
        print(ascii_image)
        
        # save result to "ascii_image.txt"
        with open("TXT/ascii_image.txt", "w") as f:
            f.write(ascii_image)

        print("Give a name to your artwork")
        artName = input()
        os.rename("TXT/ascii_image.txt" , "TXT/" + artName + ".txt")
        #console()
    
 
# run program
main()