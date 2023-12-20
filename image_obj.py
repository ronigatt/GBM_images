import numpy as np
from pathlib import Path
from PIL import Image


class ImageObj:

    def __init__(self, directory_location: Path, image_name: str):
        green_image_path, red_image_path = self.get_images_path(directory_location, image_name)
        self.green_channel = self.get_image(green_image_path)
        self.red_channel = None
        self.tumor_location = None
        self.bbbd_location = None

    def get_images_path(self, directory_location: Path, image_name: str):
        # return images path for green and red channels
        # directory_location: Path
        # image_name: str
        # green_image_path: Path
        # red_image_path: Path
        image_path = directory_location / image_name
        files = [x for x in image_path.glob('**/*') if x.is_file()]
        files_names = [files[i].name for i in range(len(files))]
        green_image_path = [files[loc] for loc, i in enumerate(files_names) if 'FITC' in i]
        red_image_path = [files[loc] for loc, i in enumerate(files_names) if 'CY' in i]

        return green_image_path, red_image_path

    def get_image(self, green_image_path: Path):
        # return image from path
        # green_image_path: Path
        # image:




        """
    def find_string(self, list_of_strings: list, string: str):
        # return index of substring in list of strings
        for i in range(len(list_of_strings)):
            if string in list_of_strings[i]:
                return i
"""





