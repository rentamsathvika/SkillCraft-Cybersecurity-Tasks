from PIL import Image

# Function to encrypt image
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()  # Access pixel data

    for i in range(img.size[0]):  # width
        for j in range(img.size[1]):  # height
            r, g, b = pixels[i, j]
            # Simple encryption: add key value to each RGB component
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save("encrypted_image.png")
    print("✅ Image Encrypted Successfully! Saved as 'encrypted_image.png'")

# Function to decrypt image
def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # Reverse operation to decrypt
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save("decrypted_image.png")
    print("🔓 Image Decrypted Successfully! Saved as 'decrypted_image.png'")


# Main Program
if __name__ == "__main__":
    print("=== Image Encryption & Decryption Tool ===")
    path = input("Enter image path (e.g., sample.png): ")
    key = int(input("Enter key (integer value): "))

    print("\n1. Encrypt Image\n2. Decrypt Image")
    choice = int(input("Choose an option: "))

    if choice == 1:
        encrypt_image(path, key)
    elif choice == 2:
        decrypt_image(path, key)
    else:
        print("Invalid choice!")