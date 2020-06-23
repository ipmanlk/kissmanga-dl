## kissmanga-dl
_Download manga from KissManga and build PDFs easily!._

### Features
- Download all chapters as images.
- Build PDF for each chapter.

### Prerequisites
- Python 3 or above ([Download](https://www.python.org/)).
- pipenv ([Download](https://pipenv.pypa.io/en/latest/)).

### Instructions
1. Download this repository using ``git clone`` or zip download option.
2. Navigate to downloaded directory in your terminal.
3. Run ``pipenv shell`` and then ``pipenv install`` to install dependencies.
4. **(optional)** If you want to use a custom download directory, simply change the value of ``DOWNLOAD_DIRECTORY``.
5. Run ``python3 download.py`` (or ``python download.py``) to start the script. 
6. It will ask for a KissManga url. Provide the url of the manga you want to download (url of the page with chapter list) and hit ENTER.
7. Specify which chapters you want to download. 

- You can specify chapters as below,
    - All chapters : ``*``
    - Specific chapter: ``1`` (just the chapter number)
    - Multiple chapters: ``1,2,3,4`` (chapter numbers seperated by commas)
    - Chapter range: ``1-3`` (from 1st chapter to 3rd chapter)

### Notes
Currently only works for manga with JPG formatted chapters.

### Example
```bash
$ python3 download.py

Enter KissManga URL: https://kissmanga.org/manga/example
Enter chapters: 1

Log: Downloading: chapter_1.0 : 1.jpg
Log: Downloading: chapter_1.0 : 2.jpg
Log: Downloading: chapter_1.0 : 3.jpg
Log: Downloading: chapter_1.0 : 4.jpg
Log: Downloading: chapter_1.0 : 5.jpg
Log: Downloading: chapter_1.0 : 6.jpg

Log: PDF downloads/example/chapter_1.0/chapter_1.0.pdf created
```