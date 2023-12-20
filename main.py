
from pathlib import Path

from image_obj import ImageObj


def print_hi(name):
    pass


if __name__ == '__main__':
    directory_location = Path(r'G:\My Drive\Ilovitsh Lab\Export images')
    image_name = 'GBM4_S3_3_fl'
    ImageObj(directory_location, image_name)
    print(type(directory_location))

