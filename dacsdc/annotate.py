import os
import cv2
import json
import argparse

import yolox
from yolox.data import get_yolox_datadir

from dacsdc import DACSDC_CLASSES

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Annotate output image.")
    parser.add_argument(
        "--image_index", type=str, default='08000', help="image index without .jpg file type"
    )
    args = parser.parse_args()

    # Read JSON label file
    with open(f'{get_yolox_datadir()}label/{args.image_index}.json', 'r') as f:
        label_data = json.load(f)

    # Load the image
    image = cv2.imread(f'{get_yolox_datadir()}JPEGImages/{args.image_index}.jpg')

    # Draw bounding boxes on the image
    for obj in label_data:
        x, y, w, h = obj['x'], obj['y'], obj['width'], obj['height'], 
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle

        # Add text on the rectangle
        if obj['type'] > 7:
            continue
        text = DACSDC_CLASSES[obj['type']]  # Replace with the desired text
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Save the annotated image
    print(yolox.__path__[0])
    output_dir = os.path.dirname(yolox.__path__[0])
    output_filename = f'{output_dir}/dacsdc/{args.image_index}_annotated.jpg'
    cv2.imwrite(output_filename, image)

    print(f"Annotated image saved as {output_filename}")
