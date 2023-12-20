import cv2
import tifffile as tiff
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from PIL import Image


class ImageObj:

    def __init__(self, directory_location: Path, image_name: str):
        images_path = self.get_images_path(directory_location, image_name)
        self.green_channel = self.get_image(images_path[0])
        self.red_channel = self.get_image(images_path[1])
        self.tumor_location = None
        self.bbbd_location = None

    @staticmethod
    def get_images_path(directory_location: Path, image_name: str) -> list:
        """
        return images path for green and red channels
        directory_location: Path
        image_name: str
        green_image_path: Path
        red_image_path: Path
        """
        image_path = directory_location / image_name
        files = [x for x in image_path.glob('**/*') if x.is_file()]
        files_names = [files[i].name for i in range(len(files))]
        green_image_path = [files[loc] for loc, i in enumerate(files_names) if 'FITC' in i][0]
        red_image_path = [files[loc] for loc, i in enumerate(files_names) if 'CY' in i][0]

        return [green_image_path, red_image_path]

    @staticmethod
    def get_image(image_path: Path) -> np.ndarray:
        """
        return image from path
        image_path: Path
        image: np.ndarray
        """
        image = tiff.imread(image_path)[::-1, ::-1].transpose()
        #image2 = Image.open(image_path)
        #plt.figure()
        #plt.imshow(image, cmap='Greys')
        #plt.show()
        return image

    def find_tumor(self):
        pass








