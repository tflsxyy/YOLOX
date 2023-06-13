# DACSDC

 ## Prepare dataset
 ```bash
 bash YOLOX/dacsdc/gdrive.sh
 unzip train.zip
 export YOLOX_DATADIR=/work/yanzhi_group/datasets/yanyue/train/ # write this in ~/.bashrc
 cd YOLOX
 pip install -e .
 ```
 ```python
 python dacsdc/dacsdc_prepare_dataset.py
 python tools/train.py -f dacsdc/yolox_dacsdc_nano.py -d 4 -b 16 --fp16 -c dacsdc/yolox_nano.pth --cache
 ```