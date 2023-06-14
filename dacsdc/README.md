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
python tools/export_onnx.py --output-name YOLOX_outputs/yolox_dacsdc_nano/yolox_dacsdc_nano_relu.onnx -f dacsdc/yolox_dacsdc_nano.py -c YOLOX_outputs/yolox_dacsdc_nano/best_ckpt.pth
```