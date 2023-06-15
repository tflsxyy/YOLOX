# DACSDC

### Prepare dataset
```bash
bash YOLOX/dacsdc/gdrive.sh
unzip train.zip
export YOLOX_DATADIR=/work/yanzhi_group/datasets/yanyue/train/ # write this in ~/.bashrc
cd YOLOX
pip install -e .
```

### Training
```python
python dacsdc/dacsdc_prepare_dataset.py
python tools/train.py -f dacsdc/yolox_dacsdc_nano.py -d 4 -b 32 --fp16 -c dacsdc/yolox_nano.pth --cache
```

### Export
```python
python tools/export_onnx.py --output-name YOLOX_outputs/yolox_dacsdc_nano/yolox_dacsdc_nano_relu.onnx -f dacsdc/yolox_dacsdc_nano.py -c YOLOX_outputs/yolox_dacsdc_nano/last_epoch_ckpt.pth
```

### Note
The `cv2.imread()` function in OpenCV returns a NumPy array that represents the image. If the image is a color image in RGB or BGR format, the return array will have shape `(height, width, 3)`, where the last dimension represents the three color channels (Red, Green, Blue).

Note that OpenCV reads the image in BGR order by default. If you need the image in RGB format, you can use `cv2.cvtColor()` to convert the image from BGR to RGB. DACSDC score function has the following code to convert image from BGR to RGB format.

```python
bgr_img = cv2.imread(str(image_path), cv2.IMREAD_COLOR) # Use the flag cv2.IMREAD_COLOR or not does not change color image output!
rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
```