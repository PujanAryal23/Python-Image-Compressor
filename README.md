# Image Compression Script

This Python script compresses an image file to a target file size by adjusting the JPEG quality level.

## Prerequisites

- Python 3.x
- Pillow (PIL) library

## Usage

1. Save the script to a directory of your choice.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

<python compress_image.py my_image.jpg my_compressed_image.jpg 500000>

Replace `[input_path]` with the path to the input image file, `[output_path]` with the desired path for the compressed output file, and `[target_size]` with the target file size in bytes.

For example, to compress an image named `my_image.jpg` to a file size of 500 KB and save the compressed image as `my_compressed_image.jpg`, you would run the following command:


The script will compress the image by adjusting the JPEG quality level until the resulting file size is less than or equal to the target size. The compressed image will be saved to the specified output path.

