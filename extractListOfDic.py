import json

def readFileMap(fileArg):
    with open(fileArg) as fileInput:
        return fileInput.read()

def listofDico(path):
    map = readFileMap(path)
    myJson = json.loads(map)
    return myJson ['nodes']

def writeTo(path):
    list = listofDico(path)
    with open('listofDico', 'xt') as fileOutput:
        for dico in list:
            fileOutput.write("%s\n" % dico)

def main(path):
    writeTo(path)

main('map.json')
