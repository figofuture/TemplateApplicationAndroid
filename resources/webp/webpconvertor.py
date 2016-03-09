#!/usr/bin/env python
import os,re,sys
import platform
#outputDir = 'webp'

def isInWhiteList( whitelist, filename ):
    for line in whitelist:
        if filename == line.rstrip():
            return True
    return False

def webpconvertor(root):
    outputDir = root
    dirList = os.listdir(root)

    sysstr = platform.system()
    if(sysstr =="Darwin"):
        cwebp = os.path.join(os.path.dirname(os.path.abspath(__file__)),"mac/cwebp")
    elif(sysstr == "Linux"):
        cwebp = os.path.join(os.path.dirname(os.path.abspath(__file__)),"linux/cwebp")
    elif(sysstr == "Windows"):
        cwebp = os.path.join(os.path.dirname(os.path.abspath(__file__)),"cwebp.exe")

    whitelistfile = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"webpconvertor_whitelist.txt"),"r")
    whitelist = whitelistfile.readlines()
    whitelistfile.close()

    for filename in dirList:
        m = re.match('([\w\-]+).(|jpg|jpeg|jp2|png|)$',filename)
        if m:
            if isInWhiteList( whitelist, filename ):
                continue
            cmd = '%s -q 50 -quiet %s -o %s/%s.webp'%( cwebp,os.path.join(root,filename), outputDir, m.group(1) )
            result = os.system(cmd)
            if 0 == result:
                os.remove(os.path.join(root, filename))

if __name__=="__main__":
    #try:
    #    os.mkdir(outputDir)
    #except:
    #    pass
    print(platform.architecture())
    print(platform.platform())
    print(platform.system())
    print(platform.python_version())
    webpconvertor(sys.argv[1])
    
