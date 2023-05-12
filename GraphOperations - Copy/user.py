import random
from queue import Queue
from graph import Graph
#TODO: check outbound edges of removed vertices
#TODO: REMOVE ON 1K
#TEST FUNCTOINALITIES ON 1K
class UI:
    def __init__(self):

        self._graph=None
        self.read_from_file("input.txt")
        self.start_menu()


    @staticmethod
    def print_menu():
        from colorama import Fore
        pr = ""
        pr += "1. get the number of vertices\t8. modify edge\t\t\t\t15. create example graphs\n"
        pr += "2. parse the set of vertices\t"
        pr += "9. add\t\t\t\t\t\t16. find the connected components \n"
        pr += "3. is there an edge\t\t\t\t"
        pr += "10. remove\t\t\t\t\t17. Get shortest cost path\n"
        pr += "4. get degree of a vertex\t\t"
        pr += "11. make a copy\t\t\t\t0. exit\n"
        pr += "5. parse  outbound edges\t\t"
        pr += "12. read graph\n"  # vertex, is vertex edge, reading
        pr += "6. parse inbound edges\t\t\t"
        pr += "13. write to file\n"
        pr += "7. retrieve info about an edge\t"
        pr += "14. create random graph\t\t"
        pr += "\n\n"
        print(Fore.BLUE+"Menu loading...\n\n")
        print(Fore.CYAN+"Options:\n")
        print(Fore.LIGHTMAGENTA_EX+pr)
    @staticmethod
    def print_add():
        pr=""
        pr += "1.Add Vertex\n"
        pr += "2.Add Edge\n"
        print(pr)
    @staticmethod
    def print_remove():
        pr=""
        pr += "1. Remove Vertex\n"
        pr += "2. Remove Edge\n"
        print(pr)
    def start_menu(self):

        running=True

        while running:

            self.print_menu()
            command = int(input("What should I do?\n"))
            commands=[]
            for i in range(18):
                commands.append(i)

            while command not in commands:
                command=int(input("Insert a valid command!\n"))

            if command==0:
                running=False
            else:
                try:
                    match command:
                        case 1:
                            print(self._graph.number_of_vertices())
                        case 2:
                            self.parse_vertices()
                        case 3:
                            x=int(input("Origin: "))
                            y=int(input("Destination: "))
                            if self._graph.is_edge(x,y):
                                print("Found it!\n"+self._graph.edge_info((x,y)))
                            else:
                                print("No edge between these vertices!")
                        case 4:
                            x = int(input("Vertex: "))
                            print("Inbound degree: ", self._graph.degree_inbounds(x))
                            print("Outbound degree: ",self._graph.degree_outbounds(x))
                        case 5:
                            x = int(input("Vertex: "))
                            if self._graph.is_vertex(x):
                                self.parse_in(x)
                            else:
                                print("No inbounds!\n")
                        case 6:
                            x = int(input("Vertex: "))
                            if self._graph.is_vertex(x):
                                self.parse_out(x)
                            else:
                                print("No inbounds!\n")

                        case 7:
                            x = int(input("Origin: "))
                            y = int(input("Destination: "))
                            print(self._graph.edge_info((x,y)))
                        case 8:
                            x = int(input("Origin: "))
                            y = int(input("Destination: "))
                            c = int(input("Cost: "))
                            mess=self._graph.change_cost(x,y,c)
                            if mess=="No edge!":
                                print(mess)
                        case 9:
                            self.print_add()
                            command2=int(input("Choose option: "))
                            if command2==2:
                                x = int(input("Origin: "))
                                y = int(input("Destination: "))
                                c = int(input("Cost: "))
                                self._graph.add_edge(x,y,c)
                            elif command2==1:
                                x = int(input("Vertex: "))
                                self._graph.add_vertex(x)

                        case 10:
                            self.print_remove()
                            command2 = int(input("Choose option: "))
                            if command2 == 2:
                                x = int(input("Origin: "))
                                y = int(input("Destination: "))
                                self._graph.remove_edge(x,y)
                            elif command2 == 1:
                                x = int(input("Vertex: "))
                                self._graph.remove_vertex(x)
                        case 11:
                            new_graph=self._graph.make_copy()
                            self._graph=new_graph
                        case 12:
                            file_name=input("Insert file name: ")
                            self.read_from_file(file_name)
                        case 13:
                            self.write_to_file()
                        case 14:
                            self._graph=self.create_random()
                        case 15:

                            self._graph = self.create_random(7,20)
                            self.write_to_file_1()
                            self._graph = self.create_random(6,40)
                            self.write_to_file_2()
                        case 16:
                            #turn into undirected graph
                            self._graph.undirected_converter()
                            self._graph.print_dict()
                            result=self.list_connected_components()
                            print(f"The number of connected components is {len(result)}, consisting of the following subgraphs:\n\n")
                            i=0
                            for obj in result:
                                i+=1
                                print(f"Subgraph nb.{i}\n")
                                obj.print_undirected()
                        case 17:
                            # print("Lab3\n")
                            # dist,path=self._graph.floyd_warshall()
                            # print("distance:\n")
                            # for i in range(len(dist)):
                            #     for j in range(len(dist[i])):
                            #         print(dist[i][j], end=" ")
                            #     print()
                            # print("\n\n")
                            # print("path:\n")
                            # for i in range(len(path)):
                            #     for j in range(len(path[i])):
                            #         print(path[i][j], end=" ")
                            #     print()
                            # print("\n\n")

                            x = int(input("Origin: "))
                            y = int(input("Destination: "))
                            cost,way=self._graph.shortest_path(x,y)

                            if cost==9999:
                                with open("output3.txt", "w") as file:
                                    file.write("No path!")
                                file.close()
                                print("No path!")
                            else:
                                with open("output3.txt", "w") as file:
                                    file.write(f"The cost is {cost} and the vertices are {way}\n\n")
                                file.close()
                                print(f"The cost is {cost} and the vertices are {way}\n\n")





                except Exception as e:
                    print(e)





    """
    ASSIGNMENT 2: CONNECTED COMPONENTS
    """
    """
    BFS visists nodes in layers. Each layer <=> vertices at the same distance
    from the starting node. Keeps track of all visited vertices to add them to the same
    component.More efficient for short paths of similar lenght.
    1st: all neighbours at distance 1
    2nd: all neighbours at distance 2
    ....
    nth: all connected nodes visited
    SPACE COMPLEXITY: uses more memory bcs of the queue
    TIME COMPLEXITY: O(vertices+edges) bcs they visit each node and edge at most once
    def accessible(g, s):
        Returns the set of vertices of the graph g that are accessible
        from the vertex s
        acc = set()
        acc.add(s)
        list = [s]
        while len(list) > 0:
            x = list[0]
            list = list[1 : ]
            for y in g.parseNout(x):
                if y not in acc:
                    acc.add(y)
                    list.append(y)
        return acc
        
        2 manual executions of the algorithm for 2 graphs with at least 5 vertices and 8 edges: 
        one having 3 connected components (with one isolated vertex) 
        and the other one having 1 connected component. 

    """
    def list_connected_components(self):
        """
        Iterates over all nodes in the graph to apply BFS to each unvisited node.
        The created component for each vertex is added to a list.
        :return: list containing Graph objects representing the connected components
        """
        connected_components=[]
        visited={}
        for vertex in self._graph.parse_vertices():
            #for every vertex in the graph
            if not vertex in visited.keys():
                #the vertex has not been visited yet
                component=self.breadth_first(vertex,visited)
                connected_components.append(component)
        return connected_components
    """
    
    """
    def breadth_first(self,source, visited):
        """
        Explores the component starting at source. The algorithm
        dequeues vertices from que one by one and adds their unvisited
        neighbours to que until there are no more unvisited verices.
        :param source: source vertex representing the starting point for perfoming a breadth first search
        :param visited: dictionary for keeeping track of visited vertices, keys: vertices, values: boolean values
        :return: graph object reresenting a connected component
        """
        vertices=[] #vertices of connected component
        edges=[] #edges of connected component
        que = Queue() #empty queue for performing bfs
        que.put(source) #FIFO: enqueue the source vertex
        visited[source]=True #the source is visited first
        vertices.append(source) #the source is part of the connected component
        while not que.empty():
            first=que.get() #dequeue the first node
            for neigh in self._graph.parse_outbounds(first):
                if not neigh in visited.keys():
                    visited[neigh]=True #mark the neighbours as visited
                    que.put(neigh) #enqueue the neighbour
                    # if self._graph.is_edge(neigh,neigh):
                    #     edges.append((neigh,neigh,self._graph.get_cost(neigh,neigh)))
                    for vertex in vertices:
                        x, y = neigh, vertex
                        if self._graph.is_edge(x,y) and ((x,y,self._graph.get_cost(x,y)) not in edges):
                            edges.append((x,y,self._graph.get_cost(x,y)))
                    vertices.append(neigh)
        obj=Graph(len(vertices))
        self.unfold_graph(obj,vertices,edges)
        return obj

    def unfold_graph(self,G,vertices,edges):
        """
        Adds corresponding vertices and edges to the connected component graph object.
        :param G: graph object representing subgraph equivalent to a  connected component
        :param vertices: vertices to add to the subgraph
        :param edges: edges to add to the subgrap
        """
        for vertex in vertices:
            G.add_vertex(vertex)
        for edge in edges:
            G.add_edge(edge[0],edge[1],edge[2])
            G.add_edge(edge[1],edge[0],edge[2])




    """
    FILE OPERATIONS
    """
    def read_from_file(self,file_name):
        with open(file_name, 'r') as file:
            prop = file.readline().split()
            print(prop)
            if len(prop)==2 and prop[1]!='-1':
                n=int(prop[0])
                m=int(prop[1])
                self._graph = Graph(n)
                coordinates= [line for line in file.read().strip().split("\n")]

                for coord in coordinates:
                    coord=coord.split()

                    x=int(coord[0])
                    y=int(coord[1])
                    c=int(coord[2])
                    try:
                        self._graph.add_vertex(x)
                    except:
                        pass

                    try:
                        self._graph.add_vertex(y)
                    except:
                        pass

                    self._graph.add_edge(x,y,c)

                self._graph.print_dict()

            else:
                n=len(file.readlines())
                self._graph=Graph(n)
                if len(prop)==1:
                    try:
                        self._graph.add_vertex(int(prop[0]))
                    except:
                        pass
                elif len(prop)==3:
                    for i in range(2):
                        self._graph.add_vertex(int(prop[i]))
                    self._graph.add_edge(int(prop[0]),int(prop[1]),int(prop[2]))
                coordinates = [line for line in file.read().strip().split("\n")]
                for coord in coordinates:
                    coord = coord.split()
                    if len(coord)>2:
                        x = int(coord[0])
                        y = int(coord[1])
                        c = int(coord[2])
                    else:
                        x = int(coord[0])
                        y = x
                        c = -1


                    try:
                        self._graph.add_vertex(x)
                    except:
                        pass

                    try:
                        self._graph.add_vertex(y)
                    except:
                        pass

                    self._graph.add_edge(x, y, c)

                copy_graph=self._graph.make_copy()
                copy_graph.print_dict()

    def write_to_file(self):
        if len(self._graph.get_costs) > self._graph.number_of_vertices() ** 2:
            with open("output.txt", "w") as file:
                file.write("Impossible to create such graph!" + "\n")
        with open("output.txt", "w") as file:
            for element in self._graph.get_costs.keys():
                file.write(self._graph.edge_info(element)+ "\n")
        file.close()
    def write_to_file_1(self):
        with open("random_graph1.txt", "w") as file:
            for element in self._graph.get_costs.keys():
                file.write(self._graph.edge_info(element) + "\n")
        file.close()
    def write_to_file_2(self):
        with open("random_graph2.txt", "w") as file:
                file.write(self._graph+ "\n")
        file.close()


    """
        EXTERNAL FUNCTIONS
    """
    def create_random(self,*args):
        """

        :param creator: Class Object Graph for generating a random graph
        :return: Randomly generated graph
        """
        creator = Graph
        if len(args)==0:
            n=random.randint(1,10)
            m = random.randint(0, n * n)
        else:
            n=args[0]
            m=args[1]
        graph=creator(n)
        added_edges=0
        failed_edges=0
        if m>n*n:
            return f"Impossible to create {n} vertices graph with {m} edges!!!"
        while added_edges<m:
            x=random.randrange(n)
            y=random.randrange(n)
            c=random.randint(1,10)
            try:
                graph.add_vertex(x)
            except:
                pass
            try:
                graph.add_vertex(y)
            except:
                pass
            try:
                graph.add_edge(x,y,c)
                added_edges+=1
            except:
                failed_edges+=1
        print(f"Vertices: {n}, Edges: {m}, "
              f"Added edges: {added_edges}, "
              f"Failed attempts: {failed_edges}")
        print("\n")
        graph.print_dict()
        return graph

    """
        PARSE FUNCTIONS
    """
    def parse_in(self,x):
        if len(list(self._graph.parse_inbounds(x))) == 0:
            print("No inbounds!\n")
        else:
            for element in self._graph.parse_inbounds(x):
                print(str(element))

    def parse_out(self,x):
        if len(list(self._graph.parse_outbounds(x)))==0:
            print("No oubtounds!\n")
        else:
            for element in self._graph.parse_outbounds(x):
                print(str(element))
    def parse_vertices(self):
        for element in self._graph.parse_vertices():
            print(str(element))



