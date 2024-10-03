import cv2
import time
from datetime import datetime
from pathlib import Path

# Configuration
capture_interval_seconds = 300
save_directory = Path("/driveway-mon-data/photos")

# Ensure the save directory exists
save_directory.mkdir(parents=True, exist_ok=True)

# Open the camera (usually 0 is the default camera, or 1 for the second camera, etc.)
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

try:
    while True:
        # Capture a single frame (screenshot)
        ret, frame = camera.read()

        if ret:
            # Generate a unique filename using the current timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = save_directory / f"driveway_{timestamp}.jpg"
            
            # Save the screenshot to the specified path
            cv2.imwrite(str(image_path), frame)  # Convert Path object to string for OpenCV
            print(f"Screenshot saved to {image_path}")
        else:
            print("Error: Could not capture image.")

        # Wait for the specified interval before capturing the next screenshot
        time.sleep(capture_interval_seconds)

except KeyboardInterrupt:
    print("Terminating the process...")

finally:
    # Release the camera when the loop is terminated
    camera.release()
    cv2.destroyAllWindows()

