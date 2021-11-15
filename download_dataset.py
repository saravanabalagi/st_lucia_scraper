# from tqdm import tqdm
import subprocess


urls = [
    "https://cloudstor.aarnet.edu.au/plus/s/795TJ8WOw5ipM2p/download",
    "https://cloudstor.aarnet.edu.au/plus/s/G2QD4jAogGTIzYt/download",
    "https://cloudstor.aarnet.edu.au/plus/s/SmF1m1hBY5kj0db/download",
    "https://cloudstor.aarnet.edu.au/plus/s/8i8MMXaV6zVoGTF/download",
    "https://cloudstor.aarnet.edu.au/plus/s/wBPSt6WvcYQ332V/download",
    "https://cloudstor.aarnet.edu.au/plus/s/GkzEDUtN8h0qKmB/download",
    "https://cloudstor.aarnet.edu.au/plus/s/1BRFv7k9BDvtGeP/download",
    "https://cloudstor.aarnet.edu.au/plus/s/AY7PLl5ARQGFe1L/download",
    "https://cloudstor.aarnet.edu.au/plus/s/DQT31UhrXLfnETT/download",
    "https://cloudstor.aarnet.edu.au/plus/s/jccojB8OSW1mZV6/download",
    "https://cloudstor.aarnet.edu.au/plus/s/a9sEr9h4MyZcGSJ/download",
    "https://cloudstor.aarnet.edu.au/plus/s/VvYzQRZvfHBroYM/download",
    "https://cloudstor.aarnet.edu.au/plus/s/gIt8YF3M6CV8H6L/download",
    "https://cloudstor.aarnet.edu.au/plus/s/OnVlSmcYsKDOZPl/download",
    "https://cloudstor.aarnet.edu.au/plus/s/8oCWSdMT1WbZmrC/download",
    "https://cloudstor.aarnet.edu.au/plus/s/yx4Akph4smCr6fc/download",
    "https://cloudstor.aarnet.edu.au/plus/s/2Fa89HAm16PYMXt/download",
    "https://cloudstor.aarnet.edu.au/plus/s/jCGICgvFRrDS29W/download",
    "https://cloudstor.aarnet.edu.au/plus/s/U3FsGXIv4UO6JgG/download"
]

filenames = [
    "101215_153851_MultiCamera0.part01.rar",
    "101215_153851_MultiCamera0.part02.rar",
    "101215_153851_MultiCamera0.part03.rar",
    "101215_153851_MultiCamera0.part04.rar",
    "101215_153851_MultiCamera0.part05.rar",
    "101215_153851_MultiCamera0.part06.rar",
    "101215_153851_MultiCamera0.part07.rar",
    "101215_153851_MultiCamera0.part08.rar",
    "101215_153851_MultiCamera0.part09.rar",
    "101215_153851_MultiCamera0.part10.rar",
    "101215_153851_MultiCamera0.part11.rar",
    "101215_153851_MultiCamera0.part12.rar",
    "101215_153851_MultiCamera0.part13.rar",
    "101215_153851_MultiCamera0.part14.rar",
    "101215_153851_MultiCamera0.part15.rar",
    "101215_153851_MultiCamera0.part16.rar",
    "101215_153851_MultiCamera0.part17.rar",
    "101215_153851_MultiCamera0.part18.rar",
    "101215_153851_MultiCamera0.part19.rar"
]

for url, filename in zip(urls, filenames):
    print('Downloading: ', url)
    subprocess.run(f"wget {url} -O {filename}", shell=True)
