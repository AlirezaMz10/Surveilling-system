# Surveilling System for News Images

This project is a Python-based application that monitors news websites, extracts the latest article URLs, and downloads the main images associated with those articles. The downloaded images are stored in a structured directory for easy access and organization.

## Features
- Automatically scrapes news URLs from a specified website.
- Downloads main images for each news article.
- Organizes downloaded images into an `images/` directory.

## How It Works
1. **`download_urls()`**: Continuously fetches article URLs from the website's homepage and adds them to a processing queue.
2. **`get_images_url()`**: Processes the URLs to locate and download main images.
3. **Image Storage**: Saves the downloaded images into the `images/` directory, creating the folder if it doesn't exist.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/AlirezaMz10/Surveilling-system.git
   cd surveilling-system-images
   
2. Install required dependencies:

Requirements

	•	Python: Version 3.8 or higher
	•	Libraries:
	•	requests
	•	beautifulsoup4

Usage

Run the script as follows:

``python main.py``


The script will:

 - Continuously monitor the website for new articles.
 - Download the main images associated with each article.

Notes

 - The images/ directory will be created automatically if it does not already exist.
 - Modify the web_url variable in the code to target a different news website.
 - Ensure the website permits web scraping by reviewing its terms of service.


Contributing

Contributions are welcome! If you have suggestions for improving the script or adding new features, feel free to open an issue or submit a pull request.