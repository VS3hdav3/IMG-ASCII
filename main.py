import PIL.Image
import os

# ASCII characters array
ASCII_chars = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "?", "!", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_"]

# resize picture based on new_width
def resize_img(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_img = image.resize((new_width, new_height))
    return(resized_img)


# convert each pixel to grayscale
def gray(image):
    grayscaled_img = image.convert("L")
    return(grayscaled_img)

# convert each pixel to ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_chars[pixel//25] for pixel in pixels])
    return(characters)

def main():
    path  = os.path.join("images", "mario_2.png")
    image = PIL.Image.open(path)
    new_width = 100
    width, height = image.size
    
    # convert image to ASCII
    new_image_data = pixels_to_ascii(gray(resize_img(image, new_width)))
    
    # format new image
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))
    
    # print result
    print(ascii_image)
    
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()