import requests
from PIL import Image, ImageEnhance
import io
import os
import time

# Define the state coordinates (left, upper, right, lower)
state_coordinates = {
    "Ohio": (300, 200, 450, 350),
    "Michigan": (200, 150, 500, 400),
    "Georgia": (400, 350, 700, 600),
    "Kansas": (100, 300, 400, 600),
    "Massachusetts": (600, 150, 800, 300),
    "Hawaii": (1000, 500, 1200, 700),
    "Alabama": (350, 400, 550, 500),
    "Alaska": (0, 700, 800, 1200),
    "Arizona": (200, 300, 600, 600),
    "Arkansas": (300, 350, 500, 500),
    "California": (0, 250, 800, 450),
    "Colorado": (200, 250, 600, 500),
    "Connecticut": (600, 150, 800, 300),
    "Delaware": (600, 200, 700, 300),
    "Florida": (400, 450, 700, 700),
    "Idaho": (0, 200, 300, 450),
    "Illinois": (300, 200, 600, 400),
    "Indiana": (300, 200, 600, 350),
    "Iowa": (200, 200, 600, 350),
    "Kentucky": (300, 200, 600, 400),
    "Louisiana": (300, 400, 600, 600),
    "Maine": (600, 100, 800, 250),
    "Maryland": (600, 200, 700, 300),
    "Minnesota": (200, 150, 600, 400),
    "Mississippi": (350, 400, 600, 500),
    "Missouri": (300, 300, 600, 500),
    "Montana": (0, 200, 600, 400),
    "Nebraska": (200, 300, 600, 500),
    "Nevada": (0, 250, 800, 400),
    "New Hampshire": (600, 150, 800, 300),
    "New Jersey": (600, 200, 800, 300),
    "New Mexico": (200, 300, 600, 500),
    "New York": (600, 200, 800, 300),
    "North Carolina": (350, 400, 700, 600),
    "North Dakota": (200, 200, 600, 400),
    "Ohio": (300, 250, 600, 400),
    "Oklahoma": (200, 300, 600, 500),
    "Oregon": (0, 100, 800, 300),
    "Pennsylvania": (600, 200, 800, 300),
    "Rhode Island": (600, 150, 800, 300),
    "South Carolina": (350, 400, 700, 600),
    "South Dakota": (200, 200, 600, 400),
    "Tennessee": (300, 350, 600, 500),
    "Texas": (100, 400, 800, 600),
    "Utah": (200, 200, 600, 400),
    "Vermont": (600, 150, 800, 300),
    "Virginia": (350, 400, 600, 500),
    "Washington": (0, 100, 800, 300),
    "West Virginia": (300, 250, 600, 400),
    "Wisconsin": (200, 200, 600, 400),
    "Wyoming": (0, 200, 600, 400),
}

# Function to set desktop wallpaper on macOS
def set_wallpaper(image_path):
    try:
        script = f'''
        tell application "System Events"
            set desktopCount to count of desktops
            repeat with i from 1 to desktopCount
                set desktopPicture of desktop i to POSIX file "{image_path}"
            end repeat
        end tell
        '''
        os.system(f'osascript -e \'{script}\'')
    except Exception as e:
        print(f"Error setting wallpaper: {e}")

# Function to download the radar image
def download_radar_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(io.BytesIO(response.content))

# Function to crop the image based on user input
def crop_image(image, coordinates):
    return image.crop(coordinates)

# Main function
def main():
    radar_url = "https://radar.weather.gov/ridge/standard/CONUS-LARGE_1.gif"
    
    while True:
        # Get user input for state cropping
        print("Available states: " + ", ".join(state_coordinates.keys()) + ", or enter 'null' for no cropping.")
        state_north = input("Enter the north state (or 'null'): ").strip()
        state_east = input("Enter the east state (or 'null'): ").strip()
        state_south = input("Enter the south state (or 'null'): ").strip()
        state_west = input("Enter the west state (or 'null'): ").strip()

        # Initialize cropping coordinates
        cropping_coordinates = (0, 0, 0, 0)  # Default to (0, 0, 0, 0)
        north, east, south, west = None, None, None, None

        # Set cropping coordinates based on user input
        if state_north in state_coordinates:
            north = state_coordinates[state_north][1]
        if state_east in state_coordinates:
            east = state_coordinates[state_east][2]
        if state_south in state_coordinates:
            south = state_coordinates[state_south][3]
        if state_west in state_coordinates:
            west = state_coordinates[state_west][0]

        # Determine cropping coordinates
        if north is not None and east is not None and south is not None and west is not None:
            cropping_coordinates = (west, north, east, south)
        elif state_north == 'null' and state_east == 'null' and state_south == 'null' and state_west == 'null':
            print("No cropping will be applied. Displaying full image.")
        else:
            # Use only specified states for cropping
            cropping_coordinates = (west if west is not None else 0,
                                    north if north is not None else 0,
                                    east if east is not None else 800,  # Use default image width
                                    south if south is not None else 800)  # Use default image height

        # Debugging statements
        print(f"North: {north}, East: {east}, South: {south}, West: {west}")
        print(f"Cropping coordinates: {cropping_coordinates}")

        # Download and crop the radar image
        try:
            radar_image = download_radar_image(radar_url)
            if cropping_coordinates != (0, 0, 0, 0):
                radar_image = crop_image(radar_image, cropping_coordinates)

            # Save the processed image
            image_path = "/Users/thor/Desktop/radar_image.gif"
            radar_image.save(image_path)
            print(f"Downloaded and cropped radar image to {image_path}")

            # Set the desktop wallpaper
            set_wallpaper(image_path)
            print("Desktop background updated.")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 5 minutes before updating again
        time.sleep(300)

if __name__ == "__main__":
    main()