# 1. Introduction
This simple Python-script processes multiple images stored in the subdirectory `/data` of this script
using tesseract-ocr. For more information concerning tesseract visit
[https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract).
It uses no preprocessing on the images, it works with them as they are.

# 2. Installation
At first you need of course tesseract and the data for the needed languages. To install tesseract on Ubuntu
just use the command `sudo apt install tesseract-ocr`. This will install the OCR engine and automatically
the needed files for English language.

My provided script uses `eng+deu` as parameter. This means you also need the data for the German language. You can
easily get them through `sudo apt install tesseract-ocr-deu`.

Concerning Python there is only one non-standard library used in this script. So you also need to install `pytesseract`.
You can do this using your IDE or via `sudo -H pip3 install pytesseract` on Ubuntu.

# 3. Usage
Create a directory and put the script in it. Then create a subdirectory called `data` and put all the things in
you want to be processed. It is okay, if this dataset has directories as well.

Head to the directory of the script via command line and start the script. It will go through the directories and files
under `data` and will open every file. If the actual file is no image, the file will be skipped. If it is an image,
the script tries to perform the optical character recognition.

If it recognizes text, it will create a textfile named nearly like the original filename. E. g. `image.jpg` would 
result in `image.jpg.txt`. The recognized text will be stored in there.

So afterwards you can use `grep` - if you want to - to look through the results. Additionally a csv-file is created,
which contains information about **all** processed files. No matter what the result was. So you can also open this
file in Excel etc. and use filters to look through the information.

Each time you execute the script, a logfile will be created, and the start time will be a part of the filename.
Starting and ending time will be written in the logfile, as well as the duration and a count of the
processed and skipped files. For each file in the provided directory `data` there will be one line in the logfile,
stating if the file was processed or if the file was skipped because it was no image.