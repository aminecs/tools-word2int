import linecache, ast, re

def readFileWE(fileArg):
    with open(fileArg) as fileInput:
        with open('wikiStr.embeddings', 'xt') as fileOutput:
            for line in fileInput:
                repl = matchInt(line)
                fileOutput.write(repl)

def getLabel(index):
    line = linecache.getline('listofDico', int(index[0]) +1)
    dicRep = ast.literal_eval(line)
    return dicRep['label']

def matchInt(line):
    theRegex = '^[0-9]+'
    p = re.compile(theRegex)
    found = p.findall(line)
    string = getLabel(found)
    return p.sub(string, line)

def main(fileArg):
    readFileWE(fileArg)

main('sampleEmb.embeddings')
