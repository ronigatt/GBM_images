import matplotlib.pyplot as plt
from pathlib import Path

from image_obj import ImageObj

if __name__ == '__main__':
    directory_location = Path(r'G:\My Drive\Ilovitsh Lab\Export images\with_merge')
    images_names = [x.name for x in directory_location.glob('**/*') if x.is_dir()]
    tumor_median_red_intensity = [0] * len(images_names)
    bbbd_median_red_intensity = [0] * len(images_names)
    for i, image_name in enumerate(images_names):
        image = ImageObj(directory_location, image_name)
        image.find_roi(tumor=True)
        image.find_roi(bbbd=True)
        tumor_median_red_intensity[i] = image.median_red_intensity(image.tumor_location)
        only_bbbd_location = image.bbbd_location * ~image.tumor_location
        bbbd_median_red_intensity[i] = image.median_red_intensity(only_bbbd_location)
        #image.find_brain()

    print(tumor_median_red_intensity)
    print(bbbd_median_red_intensity)
    '''
    plt.figure()
    plt.imshow(image.red_channel)
    plt.figure()
    plt.imshow(image.bbbd_location)
    '''


