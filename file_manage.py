import os
import shutil
from os import listdir
from os.path import isfile, join
import pathlib

def manage_file():
    print("START>>>>>>>>>>>>>>>")
    foldername='unmanagedfiles'
    path=os.path.join(os.getcwd(), foldername)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for i in onlyfiles:
        extension=pathlib.Path(i).suffix
        if extension:
            dir_path=os.path.join(os.getcwd(),extension)
            isdircheck=os.path.isdir(dir_path)
            if isdircheck:
                src_path=path+'\\'+i
                dst_path=os.getcwd()+'\\'+extension
                shutil.move(src_path, dst_path)
                print("Moved success....")
            else:
                os.mkdir(extension)
                src_path=path+'\\'+i
                dst_path=os.getcwd()+'\\'+extension
                shutil.move(src_path, dst_path)
                print("Moved success....")

manage_file()