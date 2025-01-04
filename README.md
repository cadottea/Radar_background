# Radar Background

This project allows users to download, crop, and set a radar image as their desktop wallpaper on macOS. The radar images are sourced from a customizable URL, and the user can select a specific region based on state boundaries. Additionally, the process can be run in the background using the terminal for continuous updates.

## Features

- **Radar Image Downloading**: Downloads radar images from a user-defined URL. The default source is `https://radar.weather.gov/ridge/standard/CONUS-LARGE_1.gif`.
- **Cropping**: Users can crop the radar image by selecting specific states for the north, south, east, and west boundaries.
- **Desktop Wallpaper**: The program automatically sets the downloaded radar image as the desktop wallpaper on macOS.
- **Background Process**: The process runs in the background and refreshes the radar image every 5 minutes.
- **Customizable Source**: Users can choose any radar image URL.

## Future

- **Animation**: I would like to add an animation flag - although I personally don't find a significant use for it.

## Requirements

- Python 3.x
- `requests` library
- `Pillow` (PIL) library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/radar_background.git
    cd radar_background
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python radar_background.py
    ```

2. Enter the names of states for cropping or type 'null' to avoid cropping. Available states are:
    - Ohio
    - Michigan
    - Georgia
    - Kansas
    - Massachusetts
    - Hawaii
    - Alabama
    - Alaska
    - Arizona
    - Arkansas
    - California
    - Colorado
    - Connecticut
    - Delaware
    - Florida
    - Idaho
    - Illinois
    - Indiana
    - Iowa
    - Kentucky
    - Louisiana
    - Maine
    - Maryland
    - Minnesota
    - Mississippi
    - Missouri
    - Montana
    - Nebraska
    - Nevada
    - New Hampshire
    - New Jersey
    - New Mexico
    - New York
    - North Carolina
    - North Dakota
    - Ohio
    - Oklahoma
    - Oregon
    - Pennsylvania
    - Rhode Island
    - South Carolina
    - South Dakota
    - Tennessee
    - Texas
    - Utah
    - Vermont
    - Virginia
    - Washington
    - West Virginia
    - Wisconsin
    - Wyoming

3. The script will download the radar image, crop it if needed, and set it as your wallpaper.

4. The process will repeat every 5 minutes to update the wallpaper.

## Customizing Radar Source

The default radar source URL is `https://radar.weather.gov/ridge/standard/CONUS-LARGE_1.gif`. You can change this URL in the script to use a different source for radar images.

## Running in the Background

You can run the script in the background on the terminal to continuously update your wallpaper without needing to keep the terminal window open. Simply execute the script and leave it running.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.