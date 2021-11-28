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
        self._stack=[]

        return


    def push(self,elem):
        """
            push:
                inserts in the 0 elem the element

        """
        self._stack.insert(0,elem)
        print("setting")
        return


    def pop(self):
        """
            pop:
                gets the value of the firs element then remove it with del

        """
        if(self.empty()):

            return




    def top(self):
        """
            top:
                gets the value of the top element in the stack
            
        """

        return self._stack[0]
    

    def empty(self):
        """
            empty:
                checks if the len of the stack is 0
        
        """
        if len(self._stack)==0:

            return True

        return False


    def has_elem(self,elem):
        """
            has_elem:
                checks if the count of the element is more than 0

        """
        if(self._stack.count(elem)>0):

            return True

        return False

    def get_full_stack(self):
        """
            print_full_stack:
                prints the full value of the stack
        
        """
        return self._stack

    def print(self):
        """
            print:
                sorts the stack printing each value

        """
        for i in self._stack:

            print("Element: ",i)

        return
    
    stack=property(get_full_stack,push)


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

    s._stack[0]=3

    s.print()

    print(s.stack)

    print("\nVerificando si funciona la funcion has_elem y top: ")

    print("Does the stack have the element 3: ",s.has_elem(3))

    print("Does the stack have the element 5: ",s.has_elem(5))

    print("\nExtracting elements from stack: ")

    print("Extracted element: ",s.pop())

    print("Extracted element: ",s.pop())

    print("Extracted element: ",s.pop())



