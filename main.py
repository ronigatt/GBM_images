
from pathlib import Path

from image_obj import ImageObj


def print_hi(name):
    pass


if __name__ == '__main__':
    directory_location = Path(r'G:\My Drive\Ilovitsh Lab\Export images')
    image_name = 'GBM4_S3_3_fl'
    image = ImageObj(directory_location, image_name)
    image.find_roi(tumor=True)
    image.find_roi(bbbd=True)

