#!python

from collections import deque
from queue import PriorityQueue

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
        return f'{self.id} adjacent to {[x for x in self.neighbors]}'

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

        # Edge case where vertex key1 & key2 are the same
        elif key1 == key2:
            raise ValueError("Both vertexes can not have the same name")

        # if both vertices in the graph, add the
        # edge by making key2 a neighbor of key1
        # and using the add_neighbor method of the Vertex class.
        # Hint: the vertex key1 is stored in self.vert_list[key1].
        else:
            # Adds edge to both vert_list dictionary entries key1 & key2
            self.vert_list[key1].add_neighbor(key2, weight)
            self.vert_list[key2].add_neighbor(key1, weight)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_list.keys()

    # def get_edges(self):
    # TODO: Optional function
    #     """return all the edges in the graph"""
    #     edge_dict = {}

    #     # PSEUDO BRAINSTORM
    #     # Output should look something like this {vertex1 : {vertex2: weight1
    #     #                                                    vertex3: weight2            
    #     #                                                   }}

    #     for vertex in self:
    #         print("vertex:", vertex)
    #         for neighbor in vertex.get_neighbors():
    #             print("neighbor", neighbor)
    #             edge_dict.update({vertex.id: {neighbor: vertex.get_edge_weight(neighbor)}})
    #             print("edge_dict:", edge_dict)
    #     return edge_dict

    def BFS(self, vertex, n):
        # Make sure the input node is actually in the graph
        if vertex not in self.vert_list:
            raise ValueError("Input node is not in the graph")

        # Should not be able to traverse negative levels
        if n < 0:
            raise ValueError("The number of levels being traversed is lower than 0")

        # Run BFS starting from the input node and going `n` levels deep
        queue = deque()
        level = 0
        visited = []
        
        queue.append(self.vert_list[vertex])
        visited.append(vertex)

        while len(queue) > 0 and level <= n:
            node = queue.popleft()
            
            # get neighbors to the vertex
            neighbors = node.get_neighbors()

            # append all neighbors to queue
            for neighbor in neighbors:
                if neighbor not in visited:
                    # visit node by appending it to queue
                    queue.append(self.vert_list[neighbor])
                    visited.append(neighbor)
            level += 1

        # Return all nodes found at the `n`th level
        return visited

    def find_shortest_path(self, from_vert, to_vert):
        # Make sure that both nodes from_vert and to_vert are actually in the graph
        if from_vert not in self.vert_list or to_vert not in self.vert_list:
            raise ValueError("Input node is not in the graph")
        queue = PriorityQueue()
        
        # Setting vertexes to ∞
        for node in self.vert_list:
            # NOTE these are graph objects whereas in my BFS function they were dict keys
            queue.put({float('inf'), self.vert_list[node], None})
            print("queue.get(node)", queue.get(node))

        # starting vertex starts at {0, start, path}
        queue.put({0, self.vert_list[from_vert], None})
        
        # Run BFS starting from from_vert
        while queue:
            node = queue.get()
            print("node", node)
            neighbors = node.get_neighbors()
            print(neighbors)
        # PSEUDO BRAINSTORM
        # other vertexes start at ∞
        # for every vertex traversed update weight with from, to vert (weight, from_vert, to_vert)


# Figure out a way to keep track of each path you take
        # Once you find to_vert, end the search.
        # Since you've been tracking the paths, find the path that goes from from_vert to to_vert
        # Return the path, in the order of nodes visited starting with from_vert and ending with to_vert



        # while len(queue) > 0:
        #     node = queue.get()
            
        #     # get neighbors to the vertex
        #     neighbors = node.get_neighbors()

        #     # append all neighbors to queue
        #     for neighbor in neighbors:
        #         if neighbor not in visited:
        #             # visit node by appending it to queue
        #             queue.put(self.vert_list[neighbor])
        #             visited.append(neighbor)

        # # Return all nodes found at the `n`th level
        # return visited
        
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