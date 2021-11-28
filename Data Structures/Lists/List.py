"""
    Node:
        Each Node has a value and a 'pointer' to the next Node


"""
class list_node(object):

    def __init__(self):

        self.node=None

        self.value=None

    def set_node(self,node):

        self.node=node

        return True

    def set_value(self,value):

        self.value=value

        return True

    def get_node(self):

        return self.node

    def get_value(self):

        return self.value






"""
    Linked list:
        Inits the list, this list only has one item which is 'first' but first will be a Node so it has a 
        value and a 'pointer' to the next value

        Its not an special linked list so u can really only push elements from the front and from the back.
        The linked is not sorted and the elements will stay in the position you add them.
        There are few methods such as reverse lists.

"""

class list(object):

    def __init__(self):
        """
            Inits the list creating a first null node

        """
        self.first=list_node()

    
    def push_front(self,value):
        """
           push_front:
                We will call the new node added 1 and the first node 2 (before any type of change)
                So we have 1 that will point to 2
                then we will make that the first node of the list "self.first" is now 1
                that way self.first will be 1 that points to 2 and 2 points to the rest of nodes

        """
        if not value:
            
            return False

        node=list_node()

        node.set_node(self.first)

        node.set_value(value)

        self.first=node

        return True


    def remove_front(self):
        """
            remove_front:
                we store the value of the first element
                we make the first element to be the second one instead

        """
        
        value=self.first.value

        self.first=self.first.node

        return value


    def push_back(self,value):
        """
            push_back:
                There might be a much more efficient way to do this but this is a simple way:
                If the list is empty we simply add the Node to the list
                If its not empty we will sort the list and store each value in order in an array
                Then we will add at the end of the array the new value
                We will use the function push_front to create a new list with the array.

        """
        if not value:
            
            return False

        pn=list_node()

        pn.set_value(value)

        if self.list_isEmpty()==True:

            self.first=pn

        else:
            
            array=[]

            array.append(self.first.value)

            while self.first.node!=None:

               self.first=self.first.node

               array.append(self.first.value)

            array.append(value)

            self.first=list_node()

            for i in range(len(array)):

                self.push_front(array[len(array)-1-i])

            return True

    def remove_back(self):
        """
            Very similar to the push_back function but instead of adding the element at the end of the array we pop one
            then we create a new list with push_front and the array.
        
        """
        if self.list_isEmpty()==True:

            return False

        else:
            
            array=[]

            while self.first.node!=None:

               array.append(self.first.value)

               self.first=self.first.node

            value=array.pop()

            self.first=list_node()

            for i in range(len(array)):

                self.push_front(array[len(array)-1-i])

            return value
    

    def list_isEmpty(self):
        """
            list_isEmpty:
                Simply checks if first element is None or not
        """
        if self.first==None:

            return True

        return False



    def reverse_list(self):
        """
            reverse_list:
                reverses the list first elem will be last elem...
        
        """
        if self.first==None:

            return 

        else:
            value=self.first.value
            pn1=self.first
            pn2=pn1.node
            pn3=pn2.node
            pn1.node=None
            while pn3!=None:
                pn2.node=pn1
                pn1=pn2
                pn2=pn3
                pn3=pn2.node
            self.first=pn1
            self.push_back(value)
            self.remove_back()
            return 

    def print_list(self):

        """
            print_list:
                Sorts the list, creates an array with the list then print it.

        """
        qn=self.first

        array=[]

        while qn.node!=None:

            array.append(qn.value)

            qn=qn.node

        print(array)    

        return True




if __name__=="__main__":

    l=list()

    l.push_back(9)

    l.push_front(1)

    l.push_front(2)

    l.push_front(3)

    l.push_front(4)

    l.push_front(2)

    l.push_front(3)

    l.push_front(4)

    l.print_list()

    l.remove_front()

    l.print_list()

    l.push_back(5)

    l.push_back(12)

    l.push_back(15)

    l.print_list()

    l.print_list()

    l.reverse_list()

    l.print_list()
