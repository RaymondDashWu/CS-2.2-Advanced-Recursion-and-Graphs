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

    def test_add_neighbor(self):
        label = "Sugar"
        vertex = Vertex(label)

        vertex.add_neighbor("Kevin", weight = 0)

        # Should tell us that Sugar has a neighbor
        assert any(vertex.neighbors) is True
        # Should tell us that Sugar's neighbor is Kevin
        assert vertex.neighbors == {"Kevin": 0}

    def test_get_neighbors(self):
        label = "Sugar"
        vertex = Vertex(label)

        vertex.add_neighbor("Kevin", weight = 0)
        vertex.add_neighbor("Chewie", weight = 4)
        vertex.add_neighbor("Maggie", weight = 8)
        vertex.add_neighbor("Ducky", weight = 2)

        # Should tell us Sugar has 4 neighbors
        assert len(vertex.neighbors) == 4
        # Should tell us Sugar's neighbors are Kevin, Chewie, Maggie, Ducky
        assert vertex.get_neighbors() == {"Kevin", "Chewie", "Maggie", "Ducky"}


    def test_getId(self):
        label = "Sugar"
        vertex = Vertex(label)
        # Should tell us that this vertex is called Sugar
        assert vertex.id == "Sugar"

    def test_get_edge_weight(self):
        label = "Sugar"
        vertex = Vertex(label)

        vertex.add_neighbor("Kevin", weight = 0)
        vertex.add_neighbor("Chewie", weight = 4)
        vertex.add_neighbor("Maggie", weight = 8)
        vertex.add_neighbor("Ducky", weight = 2)

        # Should raise ValueError telling us "Rainbow Unicorn" is not a neighbor
        self.assertRaises(ValueError, vertex.get_edge_weight, "Rainbow Unicorn")        

        # Should tell us Sugar has 4 neighbors
        assert len(vertex.neighbors) == 4
        # Should tell us Sugar's neighbors have a weight of 0, 4, 8, or 2
        assert vertex.get_edge_weight("Kevin") == 0
        assert vertex.get_edge_weight("Chewie") == 4
        assert vertex.get_edge_weight("Maggie") == 8
        assert vertex.get_edge_weight("Ducky") == 2

class GraphTest(unittest.TestCase):
    
    def test_init(self):
        graph = Graph()
        assert any(graph.vertList) == False
        assert graph.numVertices == 0

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("Sugar")
        assert graph.numVertices == 1
        assert "Sugar" in graph.vertList.keys()

        graph.add_vertex("Kevin")
        graph.add_vertex("Chewie")
        graph.add_vertex("Maggie")
        graph.add_vertex("Ducky")
        assert graph.numVertices == 5

        # Should be 5 as duplicate vertex names aren't allowed
        graph.add_vertex("Sugar")
        assert graph.numVertices == 5
        # Double checking that vertList has the same count as numVertices
        assert len(graph.vertList) == 5



    def test_get_vertex(self):
        graph = Graph()
        graph.add_vertex("Sugar")
        
        assert graph.get_vertex("Sugar")
        self.assertRaises(ValueError, graph.get_vertex, "Rainbow Unicorn")        

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("Sugar")
        graph.add_vertex("Kevin")

        graph.add_edge("Sugar", "Kevin", weight = 4)

        vertex_sugar = graph.get_vertex("Sugar")
        vertex_kevin = graph.get_vertex("Kevin")

        # Kevin and Sugar should be neighbors to one another
        assert "Kevin" in vertex_sugar.neighbors
        assert "Sugar" in vertex_kevin.neighbors

        # Kevin and Sugar should not be neighbors to themselves
        assert "Kevin" not in vertex_kevin.neighbors
        assert "Sugar" not in vertex_sugar.neighbors

        # Checking edge weights
        assert vertex_sugar.get_edge_weight("Kevin") == 4
        assert vertex_kevin.get_edge_weight("Sugar") == 4

        # Should raise errors because these vertexes don't exist
        self.assertRaises(ValueError, graph.add_edge, "Rainbow Unicorn", "Silver Salamander")

        # Should raise error because you can't have two of the same vertexes connected
        self.assertRaises(ValueError, graph.add_edge, "Sugar", "Sugar")


    def test_get_vertices(self):
        graph = Graph()
        graph.add_vertex("Sugar")
        graph.add_vertex("Kevin")
        graph.add_vertex("Chewie")
        graph.add_vertex("Maggie")
        graph.add_vertex("Ducky")

        assert "Sugar" in graph.get_vertices()
        assert "Kevin" in graph.get_vertices()
        assert "Chewie" in graph.get_vertices()
        assert "Maggie" in graph.get_vertices()
        assert "Ducky" in graph.get_vertices()

        assert "Rainbow Unicorn" not in graph.get_vertices()

    def test_get_edges(self):
        # TODO
        graph = Graph()
        graph.add_vertex("Sugar")
        graph.add_vertex("Kevin")
        graph.add_vertex("Chewie")
        graph.add_vertex("Maggie")
        graph.add_vertex("Ducky")

        # Sugar knows everyone
        graph.add_edge("Sugar", "Kevin", weight = 4)
        graph.add_edge("Sugar", "Chewie", weight = 9)
        graph.add_edge("Sugar", "Maggie", weight = 12)
        graph.add_edge("Sugar", "Ducky", weight = 1)

        # Kevin only knows Sugar
        graph.add_edge("Kevin", "Sugar", weight = 4)

        # Chewie knows Sugar and Maggie
        graph.add_edge("Chewie", "Sugar", weight = 9)
        graph.add_edge("Chewie", "Maggie", weight = 8)

        # Maggie knows Sugar, Chewie, and Ducky
        graph.add_edge("Maggie", "Sugar", weight = 12)
        graph.add_edge("Maggie", "Chewie", weight = 8)
        graph.add_edge("Maggie", "Ducky", weight = 15)

        # Ducky knows Sugar and Maggie
        graph.add_edge("Ducky", "Sugar", weight = 1)
        graph.add_edge("Ducky", "Maggie", weight = 15)

        assert ("Sugar", "Kevin", 4) in graph.get_edges()