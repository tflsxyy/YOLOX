import sys
import cv2
import json

if len(sys.argv) != 2:
    sys.argv[1] = '08000'

# Read JSON label file
with open(f'/Users/yanyue/Downloads/train/label/{sys.argv[1]}.json', 'r') as f:
    label_data = json.load(f)

# Load the image
image = cv2.imread(f'/Users/yanyue/Downloads/train/JPEGimages/{sys.argv[1]}.jpg')

# Draw bounding boxes on the image
for obj in label_data:
    x, y, w, h = obj['x'], obj['y'], obj['width'], obj['height'], 
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle

# Save the annotated image
output_filename = f'/Users/yanyue/YOLOX/output/{sys.argv[1]}_annotated.jpg'
cv2.imwrite(output_filename, image)

print(f"Annotated image saved as {output_filename}")
