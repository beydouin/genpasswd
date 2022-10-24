#!/usr/bin/python
#title           : genpassword3.py
#description     : Generates password for the specified userid or string
#author          : Khurram Subhani
#date            : 20191223
#version         : 2.0
#usage           : python pyscript.py [string] [string] [string] ...
#notes           : Default string is 'root', if string is not provided
#notes           : Substring used to extract the first 8 characters
#notes           : there are no limits as to how many userids you put
#python_version  : 3.8.0

import hashlib,sys,os

userinput = []
userid = ""
passwd = ""

def getInput():
    global userinput
    if len(sys.argv) > 1:
        userinput = list(sys.argv[1:])
    else:
        userinput.append('root')

def genpassword():
    global userid, passwd
    passwd = hashlib.md5("mut97:" + userid.encode('utf-8')).hexdigest()

def printpass(x,y):
    print("USERID   : %s\nPASSWORD : %s\n" % (x,y[:8]))

def clearscreen():
    os.system('clear')

def generate():
    global userid
    getInput()
    for id in userinput:
        userid = id
        genpassword()
        printpass(userid,passwd)

def main():
    clearscreen()
    generate()

main()
