from flask import Flask, send_file
import io
from PIL import Image

app = Flask(__name__)

@app.route('/track_open/<email>', methods=['GET'])
def track_open(email):
    print(f"Request for {email} received.")
    print(f"Email opened by {email}")  # This will print to your Flask server logs
    
    # Create a 1x1 transparent pixel (tracking image)
    img = Image.new('RGB', (1, 1), color=(255, 255, 255))  # white pixel
    byte_io = io.BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)

    # Return the tracking image (1x1 pixel)
    return send_file(byte_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

