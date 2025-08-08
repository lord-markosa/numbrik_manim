import numpy as np
from collections import Counter
from PIL import Image


def pixelate_image(image_path, pixel_size=10):
    # Load the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = np.array(image)
    height, width, _ = pixels.shape

    # Create an output image
    output_pixels = np.zeros_like(pixels)

    for i in range(0, height, pixel_size):
        for j in range(0, width, pixel_size):
            # Extract block of pixels
            block = pixels[
                i : min(i + pixel_size, height), j : min(j + pixel_size, width)
            ]

            # Flatten the block and count occurrences of colors
            flat_block = block.reshape(-1, 3)
            most_common_color = Counter(map(tuple, flat_block)).most_common(1)[0][0]

            # Assign the most common color to the block in output image
            output_pixels[
                i : min(i + pixel_size, height), j : min(j + pixel_size, width)
            ] = most_common_color

    # Convert back to image and save
    output_image = Image.fromarray(output_pixels)
    return output_image


# Example usage
if __name__ == "__main__":
    input_image_path = "assets/complex_colors.webp"  # Replace with your image path
    output_image_path = "pixelated_output.webp"

    pixelated = pixelate_image(input_image_path, pixel_size=10)
    pixelated.save(output_image_path)

    pixelated.show()
