# DACSDC

## Prepare dataset
```bash
bash YOLOX/dacsdc/gdrive.sh
unzip train.zip
export YOLOX_DATADIR=/work/yanzhi_group/datasets/yanyue/train/ # write this in ~/.bashrc
cd YOLOX
```
```python
pip install -e . # install YOLOX
python dacsdc/dacsdc_prepare_dataset.py
```
