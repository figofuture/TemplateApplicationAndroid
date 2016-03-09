#!/usr/bin/env python
import os,re,sys
import platform
import webpconvertor
from webpconvertor import webpconvertor

def getdrawables(root):
    dirList = os.listdir(root)
    for filename in dirList:
        m = re.match('drawable|mipmap',filename)
        if m:
            print os.path.join(root, filename)
            webpconvertor(os.path.join(root, filename))

if __name__=="__main__":
    print(platform.architecture())
    print(platform.platform())
    print(platform.system())
    print(platform.python_version())
    outputDir = sys.argv[1]
    getdrawables(sys.argv[1])
    
