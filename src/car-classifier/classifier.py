import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision

# Define a function to visualize detection results on the image
def visualize(image, detection_result):
    for detection in detection_result.detections:
        bbox = detection.bounding_box
        start_point = (int(bbox.origin_x), int(bbox.origin_y))
        end_point = (int(bbox.origin_x + bbox.width), int(bbox.origin_y + bbox.height))
        cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)

        category = detection.categories[0]
        label = category.category_name
        score = round(category.score, 2)
        label_text = f'{label} ({score})'
        text_location = (start_point[0] + 10, start_point[1] + 20)
        cv2.putText(image, label_text, text_location, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Print the detection info
        print(f"Detected: {label} with score: {score} at {start_point} to {end_point}")

    return image

# Main function to setup and run the object detector
def main():
    model_path = 'efficientdet_lite0.tflite'
    image_path = 'cars.png'
    output_image_path = 'processed.png'

    # Create an ObjectDetector object
    base_options = mp.tasks.BaseOptions(model_asset_path=model_path)
    options = vision.ObjectDetectorOptions(base_options=base_options, score_threshold=0.5)
    detector = vision.ObjectDetector.create_from_options(options)

    # Load the input image as a MediaPipe Image object
    mp_image = mp.Image.create_from_file(image_path)

    # Detect objects in the input image
    detection_result = detector.detect(mp_image)

    # Convert MediaPipe Image to a numpy array for visualization
    image_array = np.copy(mp_image.numpy_view())
    annotated_image = visualize(image_array, detection_result)

    # Output image
    cv2.imwrite(output_image_path, annotated_image)

if __name__ == '__main__':
    main()


