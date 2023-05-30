import os

for index in range(12001):
    if index >= 10000:
        if os.path.isfile(f'/work/yanzhi_group/datasets/yanyue/train/JPEGImages/{index:06d}.jpg'):
            continue
        else:
            print(f'image {index:06d}.jpg not existed')
    else:
        if os.path.isfile(f'/work/yanzhi_group/datasets/yanyue/train/JPEGImages/{index:05d}.jpg'):
            continue
        else:
            print(f'image {index:05d}.jpg not existed')

