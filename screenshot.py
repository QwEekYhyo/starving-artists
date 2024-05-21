from PIL import Image, ImageGrab
import time

time.sleep(2)
screenshot = ImageGrab.grab()
print(screenshot.getpixel((1322, 458)))
