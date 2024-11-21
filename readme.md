# Image to ASCII Converter

This project converts an image into an ASCII art representation using Python. It utilizes the `Pillow` library to handle image processing and maps pixel values to ASCII characters to create a text-based version of the image.

## **Overview**
The program reads an image, resizes it to fit a specified width, converts it to grayscale, and then maps each pixel to an ASCII character based on its intensity. The result is then printed to the console and saved to a file named `ascii_image.txt`.

## **Components**

### **1. Main Script (`main.py`)**
The `main.py` script performs the following tasks:
- **Image Loading:** Opens an image from the `images` directory, specifically `mario_2.png`.
- **Image Resizing:** Resizes the image to a new width while maintaining the aspect ratio.
- **Grayscale Conversion:** Converts the image to grayscale, where each pixel’s brightness is represented as a single value.
- **ASCII Conversion:** Maps each pixel to an ASCII character based on its intensity (brightness).
- **Output:** The ASCII representation is printed to the terminal and written to a text file (`ascii_image.txt`).

### **2. Functions**

#### **`resize_img(image, new_width)`**
- Resizes the input image to a new width while maintaining the aspect ratio.
- Calculates the new height based on the aspect ratio and resizes the image accordingly.

#### **`gray(image)`**
- Converts the input image to grayscale using the `convert("L")` method, which transforms the image into a mode where each pixel represents its lightness level (grayscale value).

#### **`pixels_to_ascii(image)`**
- Converts each pixel in the grayscale image to an ASCII character. The pixel value is divided by 25 (since there are 10 ASCII characters in `ASCII_chars` that correspond to pixel values from 0-255).
- The ASCII characters range from the darkest (`Ñ`) to the lightest (`_`).

## **Functionality**
1. **Resize and Grayscale Conversion:** The image is resized to a specified width (default is 100 pixels) to fit the terminal window and maintain visual coherence. The image is then converted to grayscale to simplify the color-to-character mapping.
2. **ASCII Mapping:** The grayscale intensity of each pixel is mapped to a character in the `ASCII_chars` list, where darker pixels are represented by denser characters like `Ñ` or `@`, and lighter pixels by characters like `_`.
3. **Output:** The ASCII art is displayed in the console and saved to a file (`ascii_image.txt`) for further use.

This project is a simple yet fun way to explore image manipulation and ASCII art creation in Python. It demonstrates how to process images with the `Pillow` library and convert them into text-based representations for display or storage.
