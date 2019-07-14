from graph import Vertex, Graph
import unittest

class VertexTest(unittest.TestCase):
    
    def test_init(self):
        label = "Sugar"
        vertex = Vertex(label)
        # Should tell us that this vertex is called Sugar
        assert vertex.id == "Sugar"
        # Should tell us that Sugar has no neighbors ;(
        assert any(vertex.neighbors) is False

    def test_addNeighbor(self):
        label = "Sugar"
        vertex = Vertex(label)

        vertex.addNeighbor("Kevin", weight = 0)

        # Should tell us that Sugar has a neighbor
        assert any(vertex.neighbors) is True
        # Should tell us that Sugar's neighbor is Kevin
        assert vertex.neighbors == {"Kevin": 0}

    def test_getNeighbors(self):
        label = "Sugar"
        vertex = Vertex(label)

        vertex.addNeighbor("Kevin", weight = 0)
        vertex.addNeighbor("Chewie", weight = 4)
        vertex.addNeighbor("Maggie", weight = 8)
        vertex.addNeighbor("Duckie", weight = 2)

        # Should tell us Sugar has 4 neighbors
        assert len(vertex.neighbors) == 4
        # Should tell us Sugar's neighbors are Kevin, Chewie, Maggie, Duckie
        assert vertex.getNeighbors() == {"Kevin", "Chewie", "Maggie", "Duckie"}


    def test_getId(self):
        label = "Sugar"
        vertex = Vertex(label)
        # Should tell us that this vertex is called Sugar
        assert vertex.id == "Sugar"

    def test_getEdgeWeight(self):
        label = "Sugar"
        vertex = Vertex(label)

        vertex.addNeighbor("Kevin", weight = 0)
        vertex.addNeighbor("Chewie", weight = 4)
        vertex.addNeighbor("Maggie", weight = 8)
        vertex.addNeighbor("Duckie", weight = 2)

        # TODO: This doesn't work ¯\_(ツ)_/¯
        # Should raise ValueError telling us "Rainbow Unicorn" is not a neighbor
        # self.assertRaises(ValueError, vertex.getEdgeWeight("Rainbow Unicorn"))        

        # Should tell us Sugar has 4 neighbors
        assert len(vertex.neighbors) == 4
        # Should tell us Sugar's neighbors have a weight of 0, 4, 8, or 2
        assert 0 in vertex.getEdgeWeight(label)
        assert 4 in vertex.getEdgeWeight(label)
        assert 8 in vertex.getEdgeWeight(label)
        assert 2 in vertex.getEdgeWeight(label)

class GraphTest(unittest.TestCase):
    
    def test_init(self):
        graph = Graph()
        assert any(graph.vertList) == False
        assert graph.numVertices == 0

    def test_addVertex(self):
        graph = Graph()
        graph.addVertex("Sugar")
        assert graph.numVertices == 1
        assert "Sugar" in graph.vertList.keys()

        graph.addVertex("Kevin")
        graph.addVertex("Chewie")
        graph.addVertex("Maggie")
        graph.addVertex("Duckie")
        assert graph.numVertices == 5

        # Should be 5 as duplicate vertex names aren't allowed
        graph.addVertex("Sugar")
        assert graph.numVertices == 5
        # Double checking that vertList has the same count as numVertices
        assert len(graph.vertList) == 5



    def test_getVertex(self):
        graph = Graph()
        graph.addVertex("Sugar")
        
        assert graph.getVertex("Sugar")
        # TODO: Does not work
        # assert self.assertRaises(ValueError, graph.getVertex("Rainbow Unicorn"))        

    def test_addEdge(self):
        pass

    def test_getVertices(self):
        pass