from rymscraper import rymscraper, RymUrl
from PIL import Image
import pytesseract
import pandas as pd
import json
import pyautogui

'''
    can use get artist infos to get the info

'''

network = rymscraper.RymNetwork()

pytesseract.pytesseract.tesseract_cmd = r''

#artist_infos = network.get_artist_infos(name="Aaron Is Sarah")

#print(json.dumps(artist_infos, indent=2, ensure_ascii=False))

