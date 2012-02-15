class Node:
    def __init__(self,data):
        self.data=data
        self.in_edge=0 # stores weight of incoming edge on vertex
        self.out_edge=0 #stores weight of outgoing edge from vertex
        self.left=None # stores pointer to vertex left for a vertex

        self.right=None # stores pointer to vertex right for a vertex

def Link(u,v,w):
    Node1=Tree[u]
    Node2=Tree[v]
 #checking for the case of cycle
    cycle1=Node1
    cycle2=Node2
    while cycle1.right!=None:
        cycle1=cycle1.right    
    while cycle2.right!=None:
        cycle2=cycle2.right
    if cycle1==cycle2: 
        print "cycle exists in your test cases"

    while Node1.right!= None and Node1!=Node2:
        Node1=Node1.right
    if Node1 != Node2:
        while Node2.left!= None :
            Node2=Node2.left
           
        Node1.right=Node2
        Node2.left=Node1
        Node1.out_edge=w
        Node2.in_edge=w
    else:
        print u, " and " ,v,"lies in same Tree"
def Cut(u,v):
    Node1=Tree[u]
    Node2=Tree[v]
    if Node1.right==Node2:
        Node1.right=None
        Node2.left=None
        Node1.out_edge=0
        Node2.in_edge=0

    else:
        print "Their is no Edge between ",u, " and ",v
def Multi_Add(u,v,w):
    Node1=Tree[u]
    Node2=Tree[v]
    if Is_Reachable(Node1,Node2) == 1:
        
        while Node1 != Node2:
            Node1.out_edge=Node1.out_edge+w
            Node1.right.in_edge=Node1.right.in_edge+w
            Node1=Node1.right
    else:
        print v ," is  Not Reachable from ",u
def Reverse(u):
    Node=Tree[u]
    while Node.right != None:
        Node=Node.right
    while Node != None:
        t1=Node.right
        t2=Node.left
        t3=Node
        in_edge=Node.in_edge
        out_edge=Node.out_edge
        Node.in_edge=out_edge
        Node.out_edge=in_edge
        Node.right=t2
        Node.left=t1
        Node=Node.right
def Is_Reachable(u,v):
    Node1=Tree[u]
    Node2=Tree[v]
    while Node1!=Node2 and Node1 !=None :
        Node1=Node1.right
    if Node1 != None:
        print v ," is Reachable from ",u
        return 1
    else:
        print v ," is Not Reachable from ",u
        return 0
def Report_Minimum(u,v):
    Node1=Tree[u]
    Node2=Tree[v]
    if Is_Reachable(u,v) == 1:
        Min_edge=Node1.out_edge
        while Node1 != Node2:
            if Min_edge > Node1.out_edge:
                Min_edge=Node1.out_edge
            else:
                pass
            Node1=Node1.right
        return Min_edge
    else:
        print v ," is Not Reachable from ",u
        return -1
def Traverse(index):
    tree=Tree[index]
    while tree.left!= None:
        tree=tree.left
    node=tree
    if node.right ==None:
        print node.data
    else:
        while node.right != None :
            print node.data ,"(",node.out_edge,")",node.right.data
            node=node.right
if __name__ == "__main__" :
 
    Tree={1:Node(1) , 2:Node(2), 3:Node(3) , 4:Node(4)}
    Cut(2,3)
    Link(1,2,10)
    Reverse(1)
    Link(3,4,12)
    Link(1,3,15)
    b=Report_Minimum(1,4)
    print b
    #Traverse(1)
    #Traverse(2)
    #print Tree[1].size
    Traverse(4)
    a=Is_Reachable(4,3)
    #Cut(1,2)
    #Traverse(1)
    #Traverse(3)
    #print Tree[1].size
    #Multi_Add(2,3,10)
    Reverse(4)
    Traverse(4)
