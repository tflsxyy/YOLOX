import os
import os.path
import copy
import pickle
import xml.etree.ElementTree as ET

import cv2
import numpy as np

from ..dataloading import get_yolox_datadir
from yolox.data.datasets.datasets_wrapper import CacheDataset, cache_read_img
from .dacsdc_classes import DACSDC_CLASSES

