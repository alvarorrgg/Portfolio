import random
from stack import stack
import showGraph


class graph:

    """
        A graph is defined by a group of vertex which are connected by edges

        In this case of graph, edges have direction that means that an edge that joins vertex [1] with vertex[2] only joins them in this direction 1--->2

        But they are not joined in this direction 2--->1

        Also the vertex are only defined as a number and a state, the number represents an Id and the state represents if the vertex has been visited or not. Edges are represented by a array containing both vertex: the edge between 1 and 2 is [1,2]

    """ 
    
    def __init__(self):
        """

            Defines both the lists of vertex and connections

                Vertex will be only a one dimension array

        """
        self.vertex=[]

        self.connections=[]

        return


    def create_vertex(self,id,state):
        """

            Creates a vertex with the Id and state given only if the state is or 0 or 1
        
        """

        if state!=0 and state!=1:

            return None

        vertex=[id,state]

        return vertex


    def add_vertex(self,v):
        """
        
        Searchs if the vertex is in the graph, if its not in the graph it appends the vertex
        
        """
        
        
        for i in self.vertex:

            for j in i:

                if j == v[0]:

                    return 

        self.vertex.append(v)

        return  

     
    def remove_vertex(self,v):
        """
        
            Searchs the vertex then removes it 
        
        """


        if self.vertex.count(v)>0:
            
            del self.vertex[self.find_vertex_by_id(v[0])]

            self.remove_connections(v)

        return


    def get_number_vertex(self):
        """

        gets the len of the vertex
        
        """

        return len(self.vertex)


    def get_total_connections(self):
        """
        
        gets the len of the connections
        
        """

        return len(self.connections)


    def remove_connections(self,v):
        """
        searches the connection then removes it
        
        """

        k=0

        l=len(self.connections)

        while k<l:

            i=self.connections[k]

            for j in i:

                if j==v[0]:

                    del self.connections[k]

                    k-=1

                    l=len(self.connections)

            k+=1       

        return

    def connection_exists(self,id1,id2):
        """
        
        calls function find_connection_index and checks if the return is different from -1 which its the value it returns if it doesnt find the connection
        
        """

        if self.find_connection_index(id1,id2)!=-1:

            return True

        return False
            

    def find_connection_index(self,idfrom,idto):
        """
        
        checks if any connection is equal to the connection[idfrom,idto]
        
        """

        k=0

        for i in self.connections:

            if i == [idfrom,idto]:

                return k

            k+=1

        return -1
                

    def find_vertex_by_id(self,id):
        """
            finds the vertex index by an id given -1 if nothing is found

        """
        l=0
        for i in self.vertex:

            for j in i:

                if id==j:

                    return l

            l+=1
            

        return -1


    def add_connection(self,id1,id2):
        """
        
        adds a connection to the graph if both ids exist and the connection doesnt exist alredy
        
        """

        l=0
        if id1==id2: 

            return

        if self.connections.count([id1,id2])>0:

            return

        for i in self.vertex:
            k=0

            for j in i:

                if k==0:

                    if j==id1 or j==id2:
                        
                        l+=1

            k+=1

        if l==2:

            connection=[id1,id2]

            self.connections.append(connection)

        return


    def remove_connection(self,id1,id2):
        """
        
        removes an existant connection
        
        """

        if self.connections.count([id1,id2])>0:

            del self.connections[self.find_connection_index(id1,id2)]


    def find_connections_by_id(self,id):
        """
        
        given an id finds its connections
        
        """
        connections=[]

        for i in self.connections:

            k=0

            for j in i:

                if k==0:

                    if j==id:

                        connections.append(i)
                        
                k+=1

        return connections


    def find_connections_by_index(self,index):
        """
        
        given an index finds its connections
        
        """

        vertex=self.vertex[index]

        id=vertex[0]

        return self.find_connections_by_id(id)


    def get_number_connections_from_id1(self,id):
        """
        
        gets the number of connections an id has
        
        """
        l=0

        for i in self.connections:

            k=0

            for j in i:

                if k==0:

                    if j==id:

                        if self.vertex[self.find_vertex_by_id(i[1])][1]==0:

                             l+=1
                        
                k+=1

        return l

    def get_number_connections_from_index(self,index):

        """
        
        gets the number of connections of an index
        
        """
            
        vertex=self.vertex[index]

        id=vertex[0]

        return self.get_number_connections_from_id1(id)


    def print_graf(self):
        """
        
        prints all the information of the graph
        
        """
        j=0

        for i in self.vertex:
            if self.get_number_connections_from_index(j)!=0:
                print("vertex: ",i," has ",self.get_number_connections_from_index(j),"connections.\n\n",i,": ",self.find_connections_by_index(j),"\n")
            else:
                print("vertex: ",i," has ",self.get_number_connections_from_index(j),"connections.\n",i,":")
            j+=1
            
        return


    def create_graf_from_file(self,filename):

        """
        
        given a file with vertex and connections, creates a graph out of it
        
        """

        f=open(filename,"r")

        vertex_num=f.readline()

        vertex_num=vertex_num[:-1]

        i=0

        j=0

        item=["",""]

        item2=0

        vertex=["",""]

        while i<int(vertex_num):

            vertex[0]=f.readline()

            if vertex[0][len(vertex[0])-1]=="\n":

                vertex[0]=vertex[0][:-1]

                vertex[0]=int(vertex[0])

            vertex[1]=0
            vertexR=vertex.copy()
            self.add_vertex(vertexR)
            i+=1

        connections_num=f.readline()

        connections_num=connections_num[:-1]

        i=0

        while i<int(connections_num):

            j=0

            connection=f.readline()

            for item2 in connection.split(" "):

                item[j]=item2

                j+=1

            if item[1][len(item[1])-1]=="\n":

                item[1]=item[1][:-1]

            self.add_connection(int(item[0]),int(item[1]))

            i+=1

        f.close()
            

    def create_random_graf(self):
        """
        
        randomly creates a graph. Depending on the number of vertex it will create more or less connections 
        
        """

        number=int(input("How many vertex do you want in your graph: "))


        for i in range(1,number+1):

            v=self.create_vertex(i,0)

            self.add_vertex(v)

        for i in range(number):

            for j in range(number):

                n=random.random()*5

                if n<=0.3:

                    self.add_connection(self.vertex[i][0],self.vertex[j][0])

        return


    def graph_depth_search_method1(self,from_id,to_id):

        """
        
        finds a path between the ids given
        
        """

        vertexB=[] #we will keep the path here

        ids=[]

        id_temp=[]

        id_aux=from_id

        aux=0

        i=0

        k=0

        comp=False

        for i in range(len(self.vertex)): #sets all states to 0 to make sure no vertex have been visited

            self.vertex[i][1]=0

        while id_aux!=to_id and id_aux!=-1: #condition to keep up with the loop

            self.vertex[self.find_vertex_by_id(id_aux)][1]=1 #changes the state to visited

            if self.connection_exists(id_aux,to_id): #if there is a connection between the aux id and the to id then we ve found a path

                vertexB.append(self.vertex[self.find_vertex_by_id(id_aux)]) #adds the vertex to the list where the path is kept

                id_aux=to_id

                break

            aux=self.get_number_connections_from_id1(id_aux) #gets the connection of the vertex

            if len(ids)==0 and aux==0: #this is the end if this happens there is no path between those vertex

                id_aux=-1

                break

            if aux==0:

                id_aux=ids.pop()

                i-=1

            else:

                vertexB.append(self.vertex[self.find_vertex_by_id(id_aux)]) #adds the vertex to the path

                id_temp=self.find_connections_by_id(id_aux) #an array with the connections of id_aux

                k=0

                while k<aux:

                    if self.vertex[self.find_vertex_by_id(id_temp[k][1])][1]==0: #checks that the vertex state is 0

                        self.vertex[self.find_vertex_by_id(id_temp[k][1])][1]=1 #changes the state to 1 in order to not visit it again

                        ids.append(id_temp[k][1]) #adds the vertex to an array with the connections found

                        i+=1 #adds one to the number of connections in ids list

                    k+=1

                if len(ids)!=0:

                    id_aux=ids.pop() #gets next id of the ids list

                    i-=1 #removes one to the number of connections in ids list

                else:

                    print("There is no path between those vertex")

        if id_aux==-1: #no path found

            print("There is no path between those vertex")

            return

        else:#path found

            for i in vertexB: #the path is stored in vertexB

                print (i)

        print(self.vertex[self.find_vertex_by_id(id_aux)])# prints last vertex

        return 


    def graph_depth_search_method2(self,from_id,to_id):

        """
        
        finds a path between the ids given
        
        The algorithm works like first method but using a stack instead of a array to keep the ids of the connections

        """

        j=0

        vf=self.find_vertex_by_id(from_id)

        v=0

        vo=0

        st=0

        id=[]

        s=stack()

        for i in range(len(self.vertex)):

            self.vertex[i][1]=0

        self.vertex[vf][1]=1

        s.push(self.vertex[vf])

        while s.empty()==False and st==0:

            vo=s.pop()[0]

            if vo==-1:

                print("Error in graph search algorithim")   

                return

            print(self.vertex[self.find_vertex_by_id(vo)])

            if vo==to_id:

                st=1


            else:

                id=self.find_connections_by_id(vo)
                
                for j in id:

                    if j[1]==to_id:

                        self.vertex[self.find_vertex_by_id(j[1])][1]=1

                        print(self.vertex[self.find_vertex_by_id(j[1])])

                        st=1
                
                for j in range(self.get_number_connections_from_id1(vo)):

                    if st==0:

                        v=self.vertex[self.find_vertex_by_id(id[j][1])]

                        if v[1]==0:

                            self.vertex[self.find_vertex_by_id(id[j][1])][1]=1

                            s.push(self.vertex[self.find_vertex_by_id(id[j][1])])

        return

    def show_graf():

        showGraph.show_graph(graph)

        return 
        

if __name__=="__main__":
    
    g=graph()

    g.create_random_graf()

    g.print_graf()

    g.graph_depth_search_method1(1,100)





    
