import cv2
import matplotlib.pyplot as plt

# Read the grayscale image
img = cv2.imread('/content/grayscale_image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Negative transformation
negative = 255 - img

# Display images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(negative, cmap='gray')
plt.title("Negative Image")
plt.axis('off')

plt.show()
