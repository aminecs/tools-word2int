# word2int

These four python scripts are used to translate a graph of strings by translating them to a graph of integers and therefore be able to use the graph of integers in Deepwalk and node2vec.

- parser.py: Using regular expressions, this python scripts sanitises your graph of strings, leaving it containing only the string and its edges
- fromStrToInt.py: As the name of the file indicates it, it translates the graph from a graph of strings to a graph of integers and stores the mapping in a file map.json. It uses the python library called NetworkX.
- extractListOfDic.py: It extracts the mapping of strings to integers from the map.json file, creating a new file with a tuple of the string and the integer.
- mapIntToWordv3.py: It uses the output generated by deepwalk and node2vec to replace the integers by the strings they represent.
