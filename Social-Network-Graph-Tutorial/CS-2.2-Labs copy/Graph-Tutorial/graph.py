#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # check if vertex is already a neighbor
        if vertex in self.neighbors:
            pass
        # if not, add vertex to neighbors and assign weight.
        else:
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        # return the neighbors
        return self.neighbors.keys()

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        # return the weight of the edge from this
        # vertex to the given vertex.
        
        return self.neighbors[vertex]
        # return self.neighbors.values()

        # TODO: Fix this + ValueError test
        # if vertex in self.neighbors:
        #     return self.neighbors.values()
        # else:
        #     raise ValueError("{} not found".format(vertex))


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # duplicate checking
        if key in self.vertList:
            return

        # create a new vertex
        new_vertex = Vertex(key)        
        # add the new vertex to the vertex list
        self.vertList[key] = new_vertex
        # increment the number of vertices
        self.numVertices += 1
        # return the new vertex
        return new_vertex

    def getVertex(self, key):
        """return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vertList:
            return self.vertList[key] 
        else:
            raise ValueError("{} vertex does not exist".format(key))

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """

        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if f not in self.vertList:
            raise ValueError("{} vertex does not exist".format(f))
        elif t not in self.vertList:
            raise ValueError("{} vertex does not exist".format(t))

        # Edge case where vertex f & t are the same
        elif f == t:
            raise ValueError("Both vertexes can not have the same name")

        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].
        else:
            # Adds edge to both vertList dictionary entries f & t
            self.vertList[f].addNeighbor(t, cost)
            self.vertList[t].addNeighbor(f, cost)

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def getEdges(self):
        """return all the edges in the graph"""
        # TODO
        edge_dict = {}

        # Night cap. I can't envision what the output looks like for my edge dict
        # My guess is it should look something like this {edge1 : {edge2: weight1
        #                                                          edge3: weight2            
        #                                                         }}
        for vertex in self.vertList:
            for neighbor in vertex.getNeighbors():
                edge_dict.update({vertex.id: neighbor})


    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Friend 1")
    g.addVertex("Friend 2")
    g.addVertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Friend 1", "Friend 2")
    g.addEdge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
