import os
os.system('cls')

'''
Nama    : Ibra Hasan Suraya
Kelas   : IF-B
NIM     : 2010511053
Sumber: https://www.tutorialspoint.com/python_data_structure/python_graphs.htm#:~:text=A%20graph%20is%20a%20pictorial,the%20vertices%20are%20called%20edges.
'''

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def getgraph(self):
        return (self.gdict)

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())
    
    def edges(self):
        return self.findedges()

    # Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def getVertices(self):
        return list(self.gdict.keys())

    # Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []
    
    # Add the new edge
    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    # List the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"],
          "f" : ["a"]
         }
g = graph(graph_elements)

# Print the graph 		 
print("Graph\t: ", g.getgraph())

# Print the vertex 		 
print("Vertex\t: ", g.getVertices())

# Print the Edges 		 
print("Edges\t: ",g.edges())

print()
print("Add new vertex z")
# Add new vertex
g.addVertex("z")
print("Graph\t: ", g.getgraph())
print("Vertex\t: ", g.getVertices())


print()
print("Add new edges {'a','e'}")
# Add new edges
g.AddEdge({'a','e'})
print("Graph\t: ", g.getgraph())
print("Edges\t: ",g.edges())

print()
print("Add new edges {'b','e'}")
# Add new edges
g.AddEdge({'b','e'})
print("Graph\t: ", g.getgraph())
print("Edges\t: ",g.edges())