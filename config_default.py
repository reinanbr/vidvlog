import os

IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY','usr/bin.convert')
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"  # Adjust path if needed


