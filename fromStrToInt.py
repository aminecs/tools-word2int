import networkx as nx
from networkx.readwrite import json_graph
import json

def main():
    strEdgeList = nx.read_edgelist("/Users/Amine/uniProjects/deepwalk/example_graphs/networkUnweighted.edgelist", nodetype=str)
    intEdgeList = nx.convert_node_labels_to_integers(strEdgeList, label_attribute="label")

    data = json_graph.node_link_data(intEdgeList)
    with open('map.json', 'w') as outfile:
        json.dump(data, outfile)

    nx.write_edgelist(intEdgeList, "intNetwork.edgelist", data=False)

main()
