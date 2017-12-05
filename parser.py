import re

def readFile(path):
    with open(path) as fileInput:
        with open('networkUnweighted.edgelist', 'xt') as fileOutput:
            for line in fileInput:
                lineWithoutW = matchInt(line)
                fileOutput.write(lineWithoutW[0] + '\n')

def matchW(oneLine):
    theRegex = r'.+?(?=\tw$)'
    p = re.compile(theRegex)
    return p.findall(oneLine)

def matchInt(oneLine):
    theRegex = r'.+?(?=\t[0-9]*\tw$)'
    p = re.compile(theRegex)
    return p.findall(oneLine)

def main(path):
    readFile(path)


main('network')
