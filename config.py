import os
from enum import Enum


class Config(Enum):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Path to the root directory of the project
    IMG_DIR = os.path.join(ROOT_DIR, 'report', 'images')  # Path to the images directory
