import numpy as np
from PIL import Image

# Load the image
image = Image.open("images/birds.jpg")
image_array = np.array(image)

def flip_image(img_array):
    return np.flipud(np.fliplr(img_array))

def add_noise(img_array):
    noise = np.random.randint(0, 50, img_array.shape, dtype=np.uint8)
    return np.clip(img_array + noise, 0, 255)

def brighten_channels(img_array, brightness=40):
    return np.clip(img_array + brightness, 0, 255)

def apply_mask(img_array, mask_size=(100, 100)):
    h, w, _ = img_array.shape
    center_x, center_y = w // 2, h // 2
    x1, y1 = center_x - mask_size[0] // 2, center_y - mask_size[1] // 2
    x2, y2 = x1 + mask_size[0], y1 + mask_size[1]
    img_array[y1:y2, x1:x2] = [0, 0, 0]
    return img_array


flipped = flip_image(image_array)
noisy = add_noise(flipped)
brightened = brighten_channels(noisy)
masked = apply_mask(brightened)


final_image = Image.fromarray(masked.astype(np.uint8))
final_image.save("images/processed_birds.jpg")

print("Image processing complete. Saved as 'processed_birds.jpg'.")
