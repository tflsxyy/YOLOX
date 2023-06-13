import os
import shutil
import glob

from yolox.data import get_yolox_datadir

def prepare_dataset(yolox_dir):
    # Define paths
    jpeg_images_dir = os.path.join(yolox_dir, 'JPEGImages')
    labels_dir = os.path.join(yolox_dir, 'Annotations')
    train_dir = os.path.join(yolox_dir, 'train')
    val_dir = os.path.join(yolox_dir, 'val')
    train_label_dir = os.path.join(yolox_dir, 'train_label')
    val_label_dir = os.path.join(yolox_dir, 'val_label')

    # Create train and validation directories
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(train_label_dir, exist_ok=True)
    os.makedirs(val_label_dir, exist_ok=True)
    
    # Create train and validation file lists
    train_file = open(os.path.join(yolox_dir, 'train.txt'), 'w')
    val_file = open(os.path.join(yolox_dir, 'val.txt'), 'w')

    # Copy the first 8000 images to the train directory
    train_images = glob.glob(os.path.join(jpeg_images_dir, '0[0-9][0-9][0-9][0-9].jpg'))
    for image_path in train_images:
        image_name = os.path.basename(image_path)
        shutil.copy(image_path, os.path.join(train_dir, image_name))
        train_file.write(image_name.split('.')[0] + '\n')

    # Copy the last 2000 images to the validation directory
    val_images = glob.glob(os.path.join(jpeg_images_dir, '01[0-9][0-9][0-9][0-9].jpg'))
    for image_path in val_images:
        image_name = os.path.basename(image_path)
        shutil.copy(image_path, os.path.join(val_dir, image_name))
        val_file.write(image_name.split('.')[0] + '\n')

    # Copy the corresponding label files to the train_label directories
    train_labels = glob.glob(os.path.join(labels_dir, '0[0-9][0-9][0-9][0-9].xml'))
    for label_path in train_labels:
        label_name = os.path.basename(label_path)
        shutil.copy(label_path, os.path.join(train_label_dir, label_name))

    # Copy the corresponding label files to the val_label directories
    val_labels = glob.glob(os.path.join(labels_dir, '01[0-9][0-9][0-9][0-9].xml'))
    for label_path in val_labels:
        label_name = os.path.basename(label_path)
        shutil.copy(label_path, os.path.join(val_label_dir, label_name))

    train_file.close()
    val_file.close()

    print("Dataset preparation complete.")


if __name__ == "__main__":
    # Replace 'yolox_dir' with the actual path to your YOLOX codebase
    yolox_dir = get_yolox_datadir()  # Replace with your own implementation

    # Call the function to prepare the dataset
    prepare_dataset(yolox_dir)
