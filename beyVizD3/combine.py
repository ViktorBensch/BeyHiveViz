import shutil
import glob
import os

root = "D:/Misra/output_january/"
outfilename = "whole_month.json"
with open(outfilename, 'wb') as outfile:
    for path, subdirs, files in os.walk(root):
        for filename in files:
            if filename == outfilename:
                # don't want to copy the output into the output
                continue
            with open(path + "/" + filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)