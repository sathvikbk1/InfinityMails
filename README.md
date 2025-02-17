# InfinityMails

**InfinityMails** is an email automation tool that helps you find and send personalized emails to contacts at different companies, while tracking email opens. The application integrates with Hunter.io to search for emails based on name and company and sends personalized emails with tracking pixels to monitor email opens.

## Features

- Find email addresses using Hunter.io
- Send personalized emails to contacts
- Track email opens with a tracking pixel
- Simple and efficient to use

## Installation

To install and use this project locally, clone the repository and install the required dependencies:

```bash
git clone https://github.com/sathvikbk1/InfinityMails.git
cd InfinityMails

## Install the required Python packages:

pip install -r requirements.txt

Usage
Running the Server with Flask
Start the Flask tracking server:

Run the Flask application to start the server locally:

python tracking_server.py
Expose the server with ngrok:

Ngrok is required to expose the local server to the internet so you can track email opens. If you haven't installed ngrok yet, download it here and follow the installation instructions.

Once ngrok is installed, run the following command to start the tunnel:

ngrok http 5000
Ngrok will generate a public URL (e.g., https://<your-ngrok-id>.ngrok-free.app), which you will use in the email tracking URL.

Update the Tracking URL in the Code:

Replace the tracking URL in the script with the newly generated ngrok URL. For example:

python
tracking_url = f"https://<your-ngrok-id>.ngrok-free.app/track_open/{to_email}"
Run the email lookup script:

Use the following script to find email addresses and send personalized emails with the tracking pixel:

python hunter_email_lookup.py
ngrok Considerations
ngrok is required to tunnel your local Flask server to a public URL. This is necessary for tracking email opens.
ngrok URL changes each time you start a new ngrok session, so you must update the tracking URL in the code after restarting ngrok.
## Usage
Run the script to find emails and send personalized emails with tracking: 
python hunter_email_lookup.py

#License
This project is licensed under the MIT License.

### What’s New:
- **Installation**: Instructions on installing and using **ngrok**.
- **Usage**: Explains how to use **ngrok** to expose your local Flask server and generate a public URL.
- **Considerations**: A note on ngrok URL changes each time it restarts, and the need to update the tracking URL accordingly.

### Steps to Update:
1. Open your `README.md` file.
2. Copy and paste the above content (or modify it as needed).
3. Add any additional details about **ngrok** that might be specific to your project setup.
4. Save the file.

Once you're done, stage, commit, and push the updated `README.md` to your GitHub repository:

```bash
git add README.md
git commit -m "Update README to include ngrok setup"
git push origin main