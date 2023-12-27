import cv2
import tifffile as tiff
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from PIL import Image


class ImageObj:

    def __init__(self, directory_location: Path, image_name: str):
        images_path = self.get_images_path(directory_location, image_name)
        self.green_channel = None
        self.red_channel = None
        self.get_image(images_path)
        self.max_val = self.red_channel.max()
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
        if len ([files[loc] for loc, i in enumerate(files_names) if 'Merge' in i]):
            image_path = [files[loc] for loc, i in enumerate(files_names) if 'Merge' in i][0]
        else:
            green_image_path = [files[loc] for loc, i in enumerate(files_names) if 'FITC' in i][0]
            red_image_path = [files[loc] for loc, i in enumerate(files_names) if 'CY' in i][0]
            image_path = [green_image_path, red_image_path]
        return image_path

    def get_image(self, image_path: Path or list):
        """
        return image from path
        image_path: Path
        image: np.ndarray
        """
        if isinstance(image_path, list):
            self.green_channel = tiff.imread(image_path[0])[::-1, ::-1].transpose()
            self.red_channel = tiff.imread(image_path[1])[::-1, ::-1].transpose()
        else:
            image = tiff.imread(image_path)
            self.green_channel = image[:, :, 1][::-1, ::-1].transpose()
            self.red_channel = image[:, :, 0][::-1, ::-1].transpose()

    def find_roi(self, tumor=False, bbbd=False):
        """
        find roi in image
        tumor: bool
        bbdd: bool
        """
        image = self.green_channel if tumor or not bbbd else self.red_channel
        # convert the image to binary image
        _, image = cv2.threshold(image, 0.1*self.max_val, self.max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        denoised = cv2.morphologyEx(np.uint8(image), cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8), iterations=11)
        if tumor:
            self.tumor_location = denoised < 255
        if bbbd:
            self.bbbd_location = denoised < 255

    def find_brain(self):
        """
        find brain in image
        """
        image = self.green_channel
        # convert the image to binary image
        _, image = cv2.threshold(image, 254, self.max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        denoised = cv2.morphologyEx(np.uint8(image), cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8), iterations=11)
        self.brain_location = denoised < 255

    def median_red_intensity(self, roi: np.ndarray) -> float:
        """
        return median red intensity in roi
        roi: np.ndarray
        median_red_intensity: float
        """
        self.red_channel[roi]
        return np.median(self.red_channel[roi])







