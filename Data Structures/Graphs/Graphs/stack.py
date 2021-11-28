class stack:
    """
        class stack:
            This is a stack implemented in a certain way where the top of the stack is the value 0 of the array and the bottom of the stack is the len elem
            This is made cause in my opinion it fits better the representation of stack

    """
    def __init__(self) :
        """
            __init__:
                Creates an empty array

        """
        self.stack=[]

        return


    def push(self,elem):
        """
            push:
                inserts in the 0 elem the element

        """
        self.stack.insert(0,elem)

        return


    def pop(self):
        """
            pop:
                gets the value of the firs element then remove it with del

        """
        if(self.empty()):

            return

        x=self.top()

        del self.stack[0]

        return x


    def top(self):
        """
            top:
                gets the value of the top element in the stack
            
        """

        return self.stack[0]
    

    def empty(self):
        """
            empty:
                checks if the len of the stack is 0
        
        """
        if len(self.stack)==0:

            return True

        return False


    def has_elem(self,elem):
        """
            has_elem:
                checks if the count of the element is more than 0

        """
        if(self.stack.count(elem)>0):

            return True

        return False


    def print(self):
        """
            print:
                sorts the stack printing each value

        """
        for i in self.stack:

            print("Element: ",i)

        return
        
if __name__=="__main__":

    s=stack()

    #Pruebas unitarias para verificar el correcto funcionamiento del TAD Stack:
    print("Probando stack is empty y eliminar un elemento de un stack vacio: ")

    print("\nStack is empty: ", s.empty())

    print("The element extracted is: ",s.pop())

    print("\nAñadiendo varios elementos y probando la funcion print: ")

    print("El stack es: ")

    s.push(1)

    s.push(2)

    s.push(3)

    s.print()

    print(s.stack)

    print("\nVerificando si funciona la funcion has_elem y top: ")

    print("Does the stack have the element 3: ",s.has_elem(3))

    print("Does the stack have the element 5: ",s.has_elem(5))

    print("\nExtracting elements from stack: ")

    print("Extracted element: ",s.pop())

    print("Extracted element: ",s.pop())

    print("Extracted element: ",s.pop())



