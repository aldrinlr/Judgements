__author__ = 'Aldrin'

from os import listdir
from os.path import isfile, join
import re


def openfile(filename, classname):
    filehandler = open(filename, 'r')
    file_content = filehandler.read()
    pattern = r'<[A-Za-z/]*>'
    file_content = re.sub(pattern, '', file_content)
    words = file_content.split()


def classify():
    mypath = 'C:\\Users\\Aldrin\\Downloads\\Interview Test Problem\\Judgements\\'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    mypath2 = 'C:\\Users\\Aldrin\\Downloads\\Interview Test Problem\\'
    f = open(mypath2 + 'Interview_Mapping.csv')
    for line in f:
        filename = line.split(',')[0].strip('"')
        classname = line.split(',')[1].strip('"')[:-2]
        # print filename
        if filename != 'Judgements':
            openfile(mypath + filename + '.txt', classname)


if __name__ == '__main__':
    classify()