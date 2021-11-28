class queue:
    """
        class queue:
            first elem is stored at the top of the array and the last elem at the 0
            FIFO: First in First out


    """
    def __init__(self) :
        """
            __init__:
                creates an empty array

        """
        self.queue=[]

        return


    def push(self,elem):
        """
            push:
                appends an elem at the end of the queue

        """
        self.queue.append(elem)

        return 


    def pop(self):
        """ 
            pop:
                removes the first element of the queue

        """
        if(self.empty()):

            return

        x=self.front()

        del self.queue[0]

        return x
    

    def front(self):
        """
            front:
                gets the first element in the queue


        """
        return self.queue[0]


    def rear(self):
        """
            rear:
                gets the last element in the queue
        
        """
        return self.queue[len(self.queue)-1]
    

    def empty(self):
        """
            empty:
                checks if the len of the array is equal to zero
        
        """
        if len(self.queue)==0:

            return True

        return False


    def has_elem(self,elem):
        """
            has_elem:
                checks if the count of the element is higher than zero 
        
        
        """
        if(self.queue.count(elem)>0):

            return True

        return False
     
       
    def print(self):
        """
            print:
                sorts the array printing each value
        
        """
        for i in self.queue:

            print("Element: ",i)

        return

if __name__=="__main__":

    q=queue()

    #Pruebas unitarias para verificar el correcto funcionamiento del TAD queue:
    print("Probando queue is empty y eliminar un elemento de un queue vacio: ")

    print("\nqueue is empty: ", q.empty())

    print("The element extracted is: ",q.pop())

    print("\nAñadiendo varios elementos y probando la funcion print: ")

    print("El queue es: ")

    q.push(1)

    q.push(2)

    q.push(3)

    q.print()

    print(q.queue)

    print("\nVerificando si funciona la funcion has_elem, front y rear: ")

    print("Does the queue have the element 3: ",q.has_elem(3))

    print("Does the queue have the element 5: ",q.has_elem(5))

    print("Front of the queue: ", q.front())

    print("Rear of the queue: ", q.rear())

    print("\nExtracting elements from queue: ")

    print("Extracted element: ",q.pop())

    print("Extracted element: ",q.pop())

    print("Extracted element: ",q.pop())
