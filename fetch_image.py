import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for URL
    url = input("Enter the image URL: ").strip()

    # Create directory for fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image from the web
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        # Extract filename from URL or generate one if not found
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If filename is empty, generate a unique one
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Full path to save the image
        filepath = os.path.join(save_dir, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✅ Image successfully saved as {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Failed to connect. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
# fetch_image.py