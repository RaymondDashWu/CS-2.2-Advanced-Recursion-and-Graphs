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

        # Should tell us Sugar has 4 neighbors
        assert len(vertex.neighbors) == 4
        # Should tell us Sugar's neighbors are Kevin, Chewie, Maggie, Duckie
        assert vertex.getEdgeWeight(label) == {0, 4, 8, 2}

class GraphTest(unittest.TestCase):
    
    def test_init(self):
        pass

    def test_addVertex(self):
        pass

    def test_getVertex(self):
        pass

    def test_addEdge(self):
        pass

    def test_getVertices(self):
        pass