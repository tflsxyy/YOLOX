# DACSDC

## Prepare dataset
```bash
export YOLOX_DATADIR=/work/yanzhi_group/datasets/yanyue/train/ # write this in ~/.bashrc
bash gdrive.sh
unzip train.zip -f $YOLOX_DATADIR
```
```python
python dacsdc/dacsdc_prepare_dataset.py
```