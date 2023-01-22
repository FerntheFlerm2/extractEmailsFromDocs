#!/bin/bash
#https://stackoverflow.com/questions/5671988/how-to-extract-just-plain-text-from-doc-docx-files
libreoffice --headless --convert-to "txt:Text (encoded):UTF8" *.doc