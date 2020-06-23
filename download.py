
import requests
import os
import shutil
import img2pdf
from pathlib import Path
from bs4 import BeautifulSoup

DOWNLOAD_DIRECTORY = Path("./downloads/")

URL = str(input("Enter KissManga URL: "))

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# find title of the manga
title = soup.select(".bigChar")[0].text

# create a direcotry
if not(os.path.isdir(DOWNLOAD_DIRECTORY / title)):
    os.mkdir(DOWNLOAD_DIRECTORY / title)

chapters_html = soup.select(".episodeList div h3 a")

# build chapter list
chapters = {}

for a in chapters_html:
    chapter_number = float(a["href"].split("/")[-1].split("_")[-1])
    chapter_url = "https://kissmanga.org/" + a["href"]
    chapters[chapter_number] = chapter_url


# sort chapter list
chapters = dict(sorted(chapters.items()))

# loop through sorted chapters
for chapter_number, chapter_url in chapters.items():

    # chapter name
    chapter_name = "chapter_" + str(chapter_number)

    # make chapter dir
    chapter_directory = DOWNLOAD_DIRECTORY / title / chapter_name
    chapter_image_directory = chapter_directory / "img"

    if not(os.path.isdir(chapter_directory)):
        os.mkdir(chapter_directory)

    if not(os.path.isdir(chapter_image_directory)):
        os.mkdir(chapter_image_directory)

    # grab chapter images
    response = requests.get(chapter_url)
    soup = BeautifulSoup(response.text, "html.parser")
    imgs = soup.select("#centerDivVideo img")

    # downlaoded img path list for pdf building
    downloaded_img_paths = []

    # downlaod each chapter iamge
    for img in imgs:
        image_url = img["src"]
        image_name = os.path.basename(image_url)
        image_path = chapter_image_directory / image_name

        downloaded_img_paths.append(str(image_path))

        # check if already downloaded
        if (os.path.isfile(image_path)):
            continue

        print("Log: Downloading: " + chapter_name + " : " + image_name)

        response = requests.get(image_url, stream=True)

        # save image
        with open(image_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

    # path for chapter pdf file
    chapter_pdf_path = chapter_directory / (chapter_name + ".pdf")

    # build the pdf
    with open(chapter_pdf_path, "wb") as f:
        f.write(img2pdf.convert(downloaded_img_paths))

    print("Log: PDF " + str(chapter_pdf_path) + " created")