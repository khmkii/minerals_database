"""
running this script decodes the url encoded filenames for the image files associated with the project
"""

import os
import shutil
from urllib import parse

BASE_DIR = os.path.abspath('..')

path_to_images_file = os.path.join(BASE_DIR, 'assets\static\images')


def url_decode(encoded_filename):
    return parse.unquote(encoded_filename)


def rename_files(original_filename, new_filename):
    old_path = os.path.join(path_to_images_file, original_filename)
    new_path = os.path.join(path_to_images_file, new_filename)
    shutil.move(old_path, new_path)


if __name__ == '__main__':
    for file in os.listdir(path_to_images_file):
        decoded_filename = url_decode(file)
        rename_files(file, decoded_filename)
