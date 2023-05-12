from copy import deepcopy



class GraphException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Graph:
    def __init__(self,n):
        self._size=n
        self._din={}
        self._dout={}
        self._costs={}

    def undirected_converter(self):
        for x in self.parse_vertices():
            for el in self.parse_inbounds(x):
                if el!=x:
                    c=self.get_cost(el,x)
                    self._dout[x].append(el)
                    self._costs.update({(x,el): c})
                else:
                    self.remove_edge(x,el)



    def get_cost(self,x,y):
        """
        :param x: origin
        :param y: destination
        :return: cost of (x,y) edge
        """
        return self._costs[(x,y)]

    def add_vertex(self, x):
        """
        Adds a vertex to the dictionary of inbounds and dictionary of outbounds
        :param x: vertex to add
        """
        if self.is_vertex(x):
            raise GraphException("The vertex is already among us!")
        else:
            self._dout[x] = []
            self._din[x] = []

    def add_edge(self,x,y,c):
        """
        Adds edge to dictionary of inbounds, outbounds and dictionary of costs
        :param x: origin
        :param y: destination
        :param c: cost
        """
        if self.is_edge(x,y):
            raise GraphException("The edge is already among us!")
        else:
            self._dout[x].append(y)
            self._din[y].append(x)
            self._costs[(x,y)]=c

    def is_vertex(self, vertex):
        """
        Validator for vertices
        :param vertex: vertex to check if exists
        :return: True if it exists, False otherwise
        """
        if vertex in self.parse_vertices():
            return True
        else:
            return False

    def is_edge(self,x,y):
        """
        Validator for edges
        :param x: origin
        :param y: destination
        :return: True if (x,y) generates an edge, False otherwise
        """
        if self.is_vertex(x) is True and self.is_vertex(y) is True:
            return y in self._dout[x]
        else:
            return False

    def edge_info(self,tuple):
        """
        Retrieves information about an edge and its cost
        :param tuple: tuple where the first element is the origin, and the second one is the destination node
        :return: string containing edge information
        """
        if self.is_edge(tuple[0], tuple[1]) is False:
            return "No edge!"
        if tuple[0]==tuple[1]:
            return f"{tuple[0]} {-1}"
        else:
            return f"{tuple[0]} {tuple[1]} {self._costs[(tuple[0],tuple[1])]}"
    @property
    def get_costs(self):
        """
        :return: dictionary of costs
        """
        return self._costs
    def remove_vertex(self,x):
        """
        Deletes vertex from all the dictionaries
        :param x: vertex to remove
        """
        if self.is_vertex(x):
            for destination in self._dout[x]:
                self._din[destination].remove(x)
                del self._costs[(x, destination)]
            for origin in self._din[x]:
                self._dout[origin].remove(x)
                del self._costs[(origin,x)]
            del self._din[x]
            del self._dout[x]
    def remove_edge(self,x,y):
        """
        Deletes edge from all the dictionaries
        :param x: origin
        :param y: destination
        """
        if self.is_edge(x,y):
            del self._costs[(x,y)]
            self._dout[x].remove(y)
            self._din[y].remove(x)
    def change_cost(self,x,y,new_cost):
        """
        Modifies an edge
        :param x: origin
        :param y: destination
        :param new_cost: cost to modify with
        """
        if self.is_edge(x,y):
            self._costs[(x,y)]=new_cost
        else:
            return "No edge!"
    def degree_inbounds(self,x):
        """
        :param x: vertex used for finding in degree
        :return: inbounds of vertex x
        """
        if self.is_vertex(x):
            return len(self._din[x])
    def degree_outbounds(self,x):
        """
        :param x: vertex used for finding out degree
        :return: outbounds of vertex x
        """
        if self.is_vertex(x):
            return len(self._dout[x])
    def number_of_vertices(self):
        """
        :return: number of vertices
        """
        return self._size
    def number_of_edges(self):
        """
        :return: number of edges
        """
        return len(self.get_costs)
    def parse_vertices(self):
        """
        :return: iterable structure that contains the vertices
        """
        #myKeys=list(self._dout.keys())
        #myKeys.sort()
        return iter(self._dout.keys())
    def parse_outbounds(self,vertex):
        """
        :param vertex: vertex used for finding outbounds
        :return: iterable object containing outbound vertices
        """

        return iter(self._dout[vertex])

    def parse_inbounds(self,vertex):
        """
        :param vertex: vertex used for finding inbounds
        :return: iterable object containing inbound vertices
        """

        return iter(self._din[vertex])
    def make_copy(self):
        """
        :return: copy of the grap
        """
        return deepcopy(self)
    def print_dict(self):
        """
        Prints all 3 dictionaries.
        """
        print(self._din, "\n")
        print(self._dout, "\n")
        print(self._costs, "\n")

    def print_undirected(self):
        print("Dictionary of outbounds:\n")
        print(self._dout, "\n\n")
        print("Edges:\n")
        print(self._costs, "\n")

    """
      FLOYD-WARSHALL ALGORITHM
      """

    def to_matrix(self):
        """
        Function that creates two matrices of dimension n*n where n is the number of vertices.
        The indexes are the vertices of the graph.
        :return: dist - matrix where each cell dist[v1][v2] is filled with the cost corresponding to the edge (i,j)
                        if the edge doesn't exist, the value will be INF=9999
                 path - matrix where each cell path[v1][v2] is filled with a list [i,j]
                        if the edge doesn't exist, the value will be an empty list []
        """
        INF=9999
        vertices=self._size
        dist=[[INF for _ in range(vertices)] for _ in range(vertices)]
        path = [[[] for _ in range(vertices)] for _ in range(vertices)]
        for v1 in range(vertices):
            for v2 in range(vertices):
                if self.is_edge(v1,v2):
                    dist[v1][v2]=self.get_cost(v1,v2)
                    path[v1][v2]=[v1,v2]
        for v in range(vertices):
            dist[v][v]=0
        for i in range(len(dist)):
            for j in range(len(dist[i])):
                if dist[i][j] == 9999:
                    print("∞", end=" ")
                else:
                    print(path[i][j], end=" ")
            print()

        print("\n")

        return dist,path
    def floyd_warshall(self):
        """
        Floyd Warshall algorithm for computing the minimum cost distance and the paths between all vertices.

        :return:

        """
        dist,path=self.to_matrix()
        vertices = self._size
        for k in range(vertices):
            for i in range(vertices):
                for j in range(vertices):
                    if dist[i][j]>dist[i][k]+dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path[i][j] = path[i][k] + path[k][j][1:]
            print(f"Intermediate matrix {k+1}: \n")
            for i in range(len(dist)):
                for j in range(len(path[i])):
                    if dist[i][j]==9999:
                        print("∞", end=" ")
                    else:
                        print(dist[i][j], end=" ")
                print()
            print("\n")

        return dist,path
    def shortest_path(self,x,y):
        dist, path = self.floyd_warshall()
        return dist[x][y],path[x][y]