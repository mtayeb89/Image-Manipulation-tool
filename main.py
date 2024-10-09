from PIL import Image, ImageFilter
import os


# Function to load an image
def load_image(image_path):
    try:
        img = Image.open(image_path)
        print(f"Image '{image_path}' loaded successfully.")
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


# Function to resize an image
def resize_image(image, size):
    resized_img = image.resize(size)
    print(f"Image resized to {size}.")
    return resized_img


# Function to rotate an image
def rotate_image(image, angle):
    rotated_img = image.rotate(angle)
    print(f"Image rotated by {angle} degrees.")
    return rotated_img


# Function to convert an image to grayscale
def grayscale_image(image):
    grayscale_img = image.convert("L")
    print("Image converted to grayscale.")
    return grayscale_img


# Function to save the image
def save_image(image, output_path):
    try:
        image.save(output_path)
        print(f"Image saved as '{output_path}'.")
    except Exception as e:
        print(f"Error saving image: {e}")


# Main function
def main():
    # Load the image
    image_path = input("Enter the image file path: ")
    img = load_image(image_path)

    if img is not None:
        # Resize the image
        width = int(input("Enter the new width: "))
        height = int(input("Enter the new height: "))
        resized_img = resize_image(img, (width, height))

        # Rotate the image
        angle = int(input("Enter the rotation angle in degrees: "))
        rotated_img = rotate_image(resized_img, angle)

        # Convert to grayscale
        grayscale_img = grayscale_image(rotated_img)

        # Save the final image
        output_path = input("Enter the output file path (with extension): ")
        save_image(grayscale_img, output_path)


if __name__ == "__main__":
    main()
