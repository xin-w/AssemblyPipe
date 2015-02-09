__author__ = 'sungshine'
#!/usr/bin/python3
#Run FastQC on raw reads

import os
import sys
import subprocess
import getopt

inputDirectory = '' #raw reads directory

#parse command line options
def parseOpts(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:")
    except getopt.GetoptError:
        print 'usage: ./assemblyMagic.py -i <Raw reads Directory>\n'
        sys.exit()
    for opt, arg in opts:
        if opt == 'h':
            print 'usage: ./assemblyMagic.py -i <Raw reads Directory>\n'
            sys.exit()
        elif opt in ('i')
            inputDirectory = arg

if __name__ == "__parseOpts__":
    parseOpts(sys.argv[1:])
    
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

#Invokes fastqc on raw read files passing in the files in as an argument
def moduleFastQC(file):
    subprocess.call(['fastqc', file])

#Invokes prinseq-lite on raw read files using default settings passing files in as argument
def modulePrinseq(file):
    subprocess.call(['prinseq-lite', '-verbose', '-fastq',file,'-out_format','3',])

for file in paths:
    keyname = os.path.basename(file)
    moduleFastQC(file)
    modulePrinseq(file)

