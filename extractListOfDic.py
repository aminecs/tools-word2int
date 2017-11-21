import json

def readFileMap(fileArg):
    with open(fileArg) as fileInput:
        return fileInput.read()

def returnListofDico(fileArg):
    map = readFileMap(fileArg)
    myJson = json.loads(map)
    return myJson ['nodes']

def writeTo(fileArg):
    list = returnListofDico(fileArg)
    with open('listofDico', 'xt') as fileOutput:
        for dico in list:
            fileOutput.write("%s\n" % dico)

def main(fileArg):
    writeTo(fileArg)

main('map.json')
