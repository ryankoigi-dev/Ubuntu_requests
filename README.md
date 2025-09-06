# Ubuntu_requests
A python tool that downloads images from any URL, saves them into an organized folder, and handles errors gracefully following ubuntu principles of community, respect, sharing, and practicality. 
# Ubuntu_Requests

A simple Python script that fetches images from any given URL and saves them into a local directory called **Fetched_Images**.  
The project applies the **Ubuntu principles** of Community, Respect, Sharing, and Practicality.

---

## ✨ Features
- Prompts the user for an image URL
- Creates a `Fetched_Images/` directory if it doesn’t exist
- Downloads and saves the image in binary mode
- Extracts the filename from the URL (or generates one if missing)
- Handles errors gracefully:
  - Invalid URL
  - Connection errors
  - HTTP errors (404, 500, etc.)
  - Timeouts

---

## ⚡ Ubuntu Principles
- **Community**: Connects to the wider web by fetching resources.  
- **Respect**: Handles errors gracefully without crashing.  
- **Sharing**: Saves images in an organized folder for future use.  
- **Practicality**: Provides a tool that solves a real need.  

---

## 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Ubuntu_Requests.git
   cd Ubuntu_Requests
2. Install dependencies:
   pip install requests
3. Run the script:
   python fetch_image.py
4. Enter any valid image URLmage URL (e.g., https://example.com/picture.jpg).
The image will be saved in the Fetched_Images/ folder.
