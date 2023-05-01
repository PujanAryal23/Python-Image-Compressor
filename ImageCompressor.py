import os
import sys
import multiprocessing
import io
from PIL import Image

def compress_image(filepath, max_size, quality):
    # Open the image and get its current size and format
    with Image.open(filepath) as im:
        current_size = os.path.getsize(filepath)
        format = im.format

        # Reduce the quality of the image until its size is less than or equal to the desired size
        while current_size > max_size:
            quality = int(quality * 0.9)
            buffer = io.BytesIO()
            im.save(buffer, format=format, optimize=True, quality=quality)
            buffer_size = buffer.getbuffer().nbytes
            current_size = buffer_size

        # Save the compressed image to a new file
        new_filepath = f"{os.path.splitext(filepath)[0]}_compressed.{format.lower()}"
        with open(new_filepath, 'wb') as f:
            f.write(buffer.getvalue())

    return new_filepath

if __name__ == '__main__':
    # Get the filepath, max_size, and quality from command line arguments
    filepath = sys.argv[1]
    max_size = int(sys.argv[2])
    quality = int(sys.argv[3])

    # Create a pool of worker processes
    num_cpus = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_cpus)

    # Split the input image into smaller chunks
    chunk_size = int(os.path.getsize(filepath) / num_cpus)
    chunks = [(filepath, max_size, quality)] * num_cpus

    # Run the compression process in parallel on each chunk
    results = pool.starmap(compress_image, chunks)

    # Print the paths to the compressed image files
    for result in results:
        print(result)
