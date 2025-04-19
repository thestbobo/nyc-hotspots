import copy
import random

import networkx as nx

from database.DAO import DAO
from geopy.distance import geodesic

class Model:
    def __init__(self):
        self._myGraph = nx.Graph()
        self._idMap = {}

        self._best_path = []

        pass

    def _getV0(self, strNode, vf):
        v0 = None
        while v0 is None:
            n = random.choice(list(self._myGraph.nodes))
            if strNode not in n.locName and n.locName != vf.locName:
                v0 = n
        return v0

    def getPath(self, strNode, selected_loc):
        allLoc = list(self._myGraph.nodes)

        vf = selected_loc
        v0 = self._getV0(strNode, vf)
        if not nx.has_path(self._myGraph, v0, vf):
            return False

        partial = [v0]
        self._best_path = []
        self._recursion(partial, vf, strNode)

        return self._best_path

    def _recursion(self, partial, vf, strNode):
        current_node = partial[-1]

        print(len(partial))

        if current_node == vf:
            if len(partial) > len(self._best_path):
                self._best_path = copy.deepcopy(partial)

            return

        for n in self._myGraph.neighbors(partial[-1]):
            if n not in partial and strNode not in n.locName:
                partial.append(n)
                self._recursion(partial, vf, strNode)
                partial.pop()



    def analyzeGraph(self):
        nodes = list(self._myGraph.nodes)
        for n in nodes:
            n.neighbors = len(list(self._myGraph.neighbors(n)))
        return sorted(nodes, key=lambda n: n.neighbors, reverse=True)


    def buildGraph(self, provider, maxD):
        self._myGraph.clear()
        self._idMap.clear()
        nodes = self.getNodes(provider)
        for n in list(nodes):
            self._idMap[n.locName] = n
        self._myGraph.add_nodes_from(nodes)

        self.addEdges(maxD)


        pass

    def addEdges(self, maxD):
        for n in list(self._myGraph.nodes):
            for n2 in list(self._myGraph.nodes):
                if self.getDistance(n,n2) <= maxD and not self._myGraph.has_edge(n,n2) and not n == n2:
                    self._myGraph.add_edge(n, n2, weigth=self.getDistance(n,n2))

        pass

    def getNodes(self, provider):
        return DAO.getLocationProvider(provider)

    def getDistance(self, l1, l2):
        point1 = (l1.latitude, l1.longitude)
        point2 = (l2.latitude, l2.longitude)
        return geodesic(point1, point2).kilometers


    def getProviders(self):
        return DAO.getAllProvider()




