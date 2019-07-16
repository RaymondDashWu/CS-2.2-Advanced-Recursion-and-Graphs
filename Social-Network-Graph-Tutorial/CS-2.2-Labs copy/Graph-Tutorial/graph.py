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

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        # check if vertex is already a neighbor
        if vertex in self.neighbors:
            pass
        # if not, add vertex to neighbors and assign weight.
        else:
            self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        # return the neighbors
        return self.neighbors.keys()

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # return the weight of the edge from this
        # vertex to the given vertex.
        
        if vertex in self.neighbors:
            return self.neighbors[vertex]
        else:
            raise ValueError("{} not found".format(vertex))


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        # duplicate checking
        if key in self.vert_list:
            return

        # create a new vertex
        new_vertex = Vertex(key)        
        # add the new vertex to the vertex list
        self.vert_list[key] = new_vertex
        # increment the number of vertices
        self.num_vertices += 1
        # return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vert_list:
            return self.vert_list[key] 
        else:
            raise ValueError("{} vertex does not exist".format(key))

    def add_edge(self, key1, key2, weight=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a weight."""
        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if key1 not in self.vert_list:
            raise ValueError("{} vertex does not exist".format(key1))
        elif key2 not in self.vert_list:
            raise ValueError("{} vertex does not exist".format(key2))

        # Edge case where vertex f & t are the same
        elif key1 == key2:
            raise ValueError("Both vertexes can not have the same name")

        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the add_neighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vert_list[f].
        else:
            # Adds edge to both vert_list dictionary entries f & t
            self.vert_list[key1].add_neighbor(key2, weight)
            self.vert_list[key2].add_neighbor(key1, weight)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_list.keys()

    def get_edges(self):
        """return all the edges in the graph"""
        # TODO
        edge_dict = {}

        # PSEUDO BRAINSTORM
        # Output should look something like this {vertex1 : {vertex2: weight1
        #                                                    vertex3: weight2            
        #                                                   }}
        for vertex in self.vert_list:
            print("vertex:", vertex)
            for neighbor in vertex.get_neighbors():
                print("neighbor", neighbor)
                edge_dict.update({vertex.id: {neighbor: vertex.get_edge_weight(neighbor)}})
                print("edge_dict:", edge_dict)


    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vert_list.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))