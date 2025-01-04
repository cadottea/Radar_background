import requests
import os
import time
import subprocess
from PIL import Image, ImageEnhance

def download_radar_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded radar image to {save_path}")
    except Exception as e:
        print(f"An error occurred while downloading the radar image: {e}")

def process_image(image_path, output_path, brightness_factor, contrast_factor):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")  # Convert to RGB mode for processing
            
            # Apply brightness enhancement
            brightness_enhancer = ImageEnhance.Brightness(img)
            img = brightness_enhancer.enhance(brightness_factor)

            # Apply contrast enhancement
            contrast_enhancer = ImageEnhance.Contrast(img)
            img = contrast_enhancer.enhance(contrast_factor * 1.5)  # Increased contrast multiplier

            img.save(output_path, format='GIF')  # Save as GIF
            print(f"Processed image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")

def set_desktop_background(image_path):
    try:
        script = f'''
        tell application "System Events"
            set desktopCount to count of desktops
            repeat with i from 1 to desktopCount
                set desktopImage to POSIX file "{image_path}"
                tell desktop i to set picture to desktopImage
            end repeat
        end tell
        '''
        subprocess.run(['osascript', '-e', script])
        print("Desktop background updated.")
    except Exception as e:
        print(f"An error occurred while setting the desktop background: {e}")

def main():
    url = "https://radar.weather.gov/ridge/standard/CONUS-LARGE_1.gif"
    download_path = os.path.expanduser("~/Desktop/radar_image.gif")  # Change this if needed
    processed_path = os.path.expanduser("~/Desktop/processed_radar_image.gif")  # Change this if needed

    # Get user input for brightness and contrast levels
    while True:
        try:
            brightness_factor = float(input("Enter a brightness factor (0.0 to 1.0, where 0.0 is black and 1.0 is original brightness): "))
            if 0.0 <= brightness_factor <= 1.0:
                break
            else:
                print("Please enter a value between 0.0 and 1.0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    while True:
        try:
            contrast_factor = float(input("Enter a contrast factor (1.0 for no change, >1.0 to increase contrast): "))
            if contrast_factor > 0:
                break
            else:
                print("Please enter a value greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    while True:
        download_radar_image(url, download_path)
        process_image(download_path, processed_path, brightness_factor, contrast_factor)
        set_desktop_background(processed_path)
        time.sleep(300)  # Wait for 5 minutes

if __name__ == "__main__":
    main()