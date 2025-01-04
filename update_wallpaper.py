import requests
import os
import time
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup

def get_radar_image_list():
    radar_url = "https://radar.weather.gov/ridge/standard/"
    print(f"Fetching radar images from {radar_url}...")  # Debug info

    try:
        response = requests.get(radar_url)
        response.raise_for_status()  # Raise an error for bad responses
        print("Radar images fetched successfully.")  # Debug info
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching radar images: {e}")
    return None

def extract_conus_image_url(html):
    # Find all links to GIF images in the directory listing
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    conus_images = []
    
    for link in links:
        href = link.get('href')
        if href and "CONUS" in href and href.endswith('.gif'):
            conus_images.append(href)

    # Sort images by name to get the latest
    conus_images.sort(reverse=True)  # Sort in descending order

    if conus_images:
        latest_image_url = f"https://radar.weather.gov/ridge/standard/{conus_images[0]}"
        print(f"Latest CONUS radar image URL: {latest_image_url}")
        return latest_image_url
    else:
        print("No CONUS radar images found.")
    return None

def save_radar_image(image_url, image_path):
    print(f"Downloading CONUS radar image from {image_url}...")  # Debug info
    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()  # Raise an error for bad responses
        with open(image_path, 'wb') as f:
            f.write(image_response.content)
        print(f"Saved image to {image_path}")  # Debug info
        return True
    except requests.RequestException as e:
        print(f"Error downloading radar image: {e}")
    return False

def set_desktop_background(image_path):
    print(f"Setting desktop background to {image_path}...")  # Debug info
    try:
        script = f'''
        tell application "System Events" to set picture of desktop 1 to "{image_path}"
        '''
        subprocess.call(['osascript', '-e', script])
        print(f"Desktop background updated with {image_path}")  # Debug info
    except Exception as e:
        print(f"An error occurred while setting background: {e}")

def main():
    radar_image_html = get_radar_image_list()
    
    if radar_image_html:
        latest_image_url = extract_conus_image_url(radar_image_html)

        if latest_image_url:
            # Define the path to save the radar image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = os.path.expanduser(f"~/Desktop/conus_radar_image_{timestamp}.gif")

            # Save the radar image
            if save_radar_image(latest_image_url, image_path):
                set_desktop_background(image_path)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(300)  # Wait for 5 minutes (300 seconds)