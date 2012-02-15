class ExNode :
    def __init__(self,data):
        self.data=data
        self.size=0
        self.left=None
        self.right=None
        self.external=1
        self.height=1
        self.parent=None

class InNode :
    def __init__(self,data):
        self.left=None
        self.right=None
        self.external=0
        self.parent=None
        self.head=None
        self.tail=None
        self.height=1
        self.size=1
        self.edge=data
    def bfactor(self):
        return self.left.height-self.right.height

def Rotate_Left(Node):
    print "Rotate Left"
    Node1=Node.parent
    Node2=Node
    Node3=Node.left
    Node4=Node.left.right
    if Node1 ==None:
        Node3.parent=None
        Node3.right=Node2
        Node2.parent=Node3
        Node2.left=Node4
        if Node4 != None:
            Node4.parent=Node2
    else:
        Node1.left=Node3
        Node3.parent=Node1  
        Node2.parent=Node3
        Node3.right=Node2
        Node2.left=Node4
        if Node4 != None:
            Node4.parent=Node2
        if Node4.external !=1:
            Node2.head=Node4.head
        else:
            Node2.head=Node4
    Node2.size=Node4.size+Node2.right.size+1
    Node3.size=Node3.left.size+Node2.size+1
    Node2.height=max(Node2.left.height+1,Node2.right.height+1)
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    while Node1!=None and Node1.parent != None:
        Node1.height=max(Node1.left.height+1,Node1.right.height+1)
        Node1=Node1.parent
    if Node1!=None:
        Node1.height=max(Node1.left.height+1,Node1.right.height+1)
    #print Tree[7].parent.parent.size
def Rotate_Left_Right(Node):
    print "Rotate Left Right"
    Node5=Node
    Node3=Node.left
    Node4=Node.left.right
    A=Node3.left
    B=Node4.left
    C=Node4.right
    D=Node5.right
    Node5.left=Node4
    Node4.parent=Node5
    Node4.left=Node3
    Node3.parent=Node4
    Node3.left=A 
    if A!=None:
        A.parent=Node3
    Node3.right=B
    if B!=None:
        B.parent=Node3
    
    if B.external!=1:
        Node3.tail=B.tail
    else:
        Node3.tail=B
    if A.external!=1:
        Node4.head=A.head
    else:
        Node4.head=A
    Node3.size=A.size+B.size+1
    Node4.size=Node3.size+C.size+1
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    Node4.height=max(Node4.right.height+1,Node4.left.height+1)
    #print Tree[7].parent.edge
    Rotate_Left(Node)
    
def Rotate_Right_Left(Node):
    print "Rotate Right Left"
    Node3=Node
    Node5=Node.right
    Node4=Node.right.left
    A=Node3.left
    B=Node4.left
    C=Node4.right
    D=Node5.right
    Node3.right=Node4
    Node4.parent=Node3
    Node4.right=Node5
    Node5.parent=Node4
    Node3.left=A
    if A!=None:
        A.parent=Node3
    Node5.left=C
    if C!=None:
        C.parent=Node5
    if D.external!=1:
        Node4.tail=D.tail
    else:
        Node4.tail=D
    if C.external!=1:
        Node5.head=C.head
    else:
        Node5.head=C  
    Node5.size=C.size+D.size+1
    Node4.size=Node5.size+B.size+1
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)
    Node4.height=max(Node4.right.height+1,Node4.left.height+1)
    #print Node3.parent
    Rotate_Right(Node)
    
def Rotate_Right(Node):
    print "Rotate Right"
    Node1=Node.parent
    Node2=Node
    Node3=Node.right
    Node4=Node.right.left
    if Node1 ==None:
        #Node1.right=Node3
        #Node3.parent=Node1
        Node3.parent=None
        Node3.left=Node2
        Node2.parent=Node3
        Node2.right=Node4
        if Node4 != None:
            Node4.parent=Node2
    else:
        Node1.right=Node3
        Node3.parent=Node1  
        Node2.parent=Node3
        Node3.left=Node2
        Node2.right=Node4
        if Node4 != None:
            Node4.parent=Node2
    Node3.head=Node2.head
    if Node4.external !=1:
        Node2.tail=Node4.tail
    else:
        Node2.tail=Node4
    Node2.size=Node2.left.size+Node4.size+1
    Node3.size=Node2.size+Node3.right.size+1
    Node2.height=max(Node2.left.height+1,Node2.right.height+1)
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    while Node1!=None and Node1.parent != None:
        Node1.height=max(Node1.left.height+1,Node1.right.height+1)
        Node1=Node1.parent
    if Node1!=None:
        Node1.height=max(Node1.left.height+1,Node1.right.height+1)
    
def Cut(u,v):
    Node1=Tree[u] 
    Node=Tree[v]
    # Check if Tree containing U and Tree containing V has only U and V as vertice 
    if Node.parent == None or Node1.parent==None:
        print "Their is No edge between ", u ," and ",v
        return
    while Node1.parent!=None:
        Node1=Node1.parent
    while Node.parent!=None:
        Node=Node.parent
    #Che
    if Node1!=Node:
        print u," and ",v," belongs to different trees"
        return
    #Go upwards untill their is a left turn form U because we know that V will be left most element of its right subtree iff their is an edge between U and V exists 
    while  Node1.parent.left!=Node1 :
        Node1=Node1.parent
    while Node.parent.right!=Node:
        Node=Node.parent
    if Node.parent!=Node1.parent:
        print "Their is No edge between ", u ," and ",v
        return 
    Node2=Node1.parent
    Node3=Node2.parent
    if Node3!=None:
       # print "here"
        if Node3.left == Node2:
            Node3.left=Node2.right
            Node2.right.parent=Node3
            Node2.left.parent=None
            while Node3.parent !=None:
                if Node3.left.external !=1:
                    Node3.head=Node3.left.head
                else:
                    Node3.head=Node3.left
                Node3.size=Node3.left.size+Node3.right.size
                Node3.height=max(Node3.left.height+1,Node3.right.height+1)
                Node3=Node3.parent
            if Node3.left.external !=1:
                Node3.head=Node3.left.head
            else:
                Node3.head=Node2.left
            Node3.size=Node3.left.size+Node3.right.size
            Node3.height=max(Node3.left.height+1,Node3.right.height+1)
            while Node3.parent!=None and Node3.bfactor()!=-2:
                Node3=Node3.parent
            if Node3.bfactor()==-2:
                if Node3.right.bfactor()==1:
                    Rotate_Right_Left(Node3)
                else:
                    Rotate_Right(Node3)
                
        else:
           # print "here"
            Node3.right=Node2.left
            Node2.left.parent=Node3
            Node2.right.parent=None
            while Node3.parent !=None:
                if Node3.right.external!=1:
                    Node3.tail=Node3.right.tail
                else:
                    Node3.tail=Node3.right
                Node3.size=Node3.left.size+Node3.right.size
                Node3.height=max(Node3.left.height+1,Node3.right.height+1)
            if Node3.right.external!=1:
                Node3.tail=Node3.right.tail
            else:
                Node3.tail=Node3.right
            Node3.size=Node3.left.size+Node3.right.size
            Node3.height=max(Node3.left.height+1,Node3.right.height+1)
            while Node3.parent!=None and Node3.bfactor()!=2:
                Node3=Node3.parent
            if Node3.bfactor()==2:
                if Node3.right.bfactor()==-1:
                    Rotate_Left_Right(Node3)
                else:
                    Rotate_Left(Node3)
    else:
        Node1.parent=None
        Node2.right.parent=None
    print "Cut Done"

        


def Link(u,v,w):
    Node1=Tree[u]
    Node2=Tree[v]
   # print "linked"
    while Node1.parent !=None:
        #print "nh"
        Node1=Node1.parent
    #print Node1.external

   # print "linked"
    while Node2.parent !=None:
        Node2=Node2.parent
    #print Node2.external

    if Node1==Node2:
        print "Vertex",u," and " , v , " are alreday linked"
       # print "linked"
    else:
       # print "linked"
        #print "linked"
        if Node1.external==1 and Node2.external==1:
            #print "linked"
            Node=InNode(w)
            Node.left=Node1
            Node1.parent=Node
            Node.right=Node2
            Node2.parent=Node
            Node.head=Node1
            Node.tail=Node2
            #Node.bfactor=0
            Node.size=1+Node1.size+Node2.size
            Node.height=Node1.height+Node2.height
            print "Linked 1"
        elif Node1.external==1 and Node2.external ==0:
           # print "here"
            while Node2.external != 1 and Node2.height != 2:
                Node2=Node2.left
            if Node2.parent == None:
                rootNode=InNode(w)
                rootNode.left=Node1
                Node1.parent=rootNode
                rootNode.right=Node2
                Node2.parent=rootNode
                rootNode.head=Node1
                rootNode.tail=Node2.tail
                rootNode.height=1+Node2.height
                rootNode.size=1+Node2.size
             #   rootNode.bfactor=-1
                print "linked 2"
            else:
                 a=Node2.parent
                 b=Node2
                 c=Node1
                 newNode=InNode(w)
                 newNode.left=c
                 c.parent=newNode
                 newNode.right=b
                 b.parent=newNode
                 if Node2.external !=1:
                     newNode.head=c
                     newNode.tail=b.tail
                     newNode.height=1+b.height
                     newNode.size=1+b.size
                  #   newNode.bfactor=-1
                     a.left=newNode
                     newNode.parent=a
                     a.head=newNode.head
                     while a.parent!=None:
                         a.head=newNode.head
                         a.size=a.size+1
                         a.height=max(a.left.height+1,a.right.height+1)
                         a=a.parent
                     a.head=newNode.head
                     a.size=a.size+1
                     a.height=max(a.left.height+1,a.right.height+1)
                     
                     x=Node2.parent
                     while x.bfactor()!=2 and x.parent != None:
                         x=x.parent
                     if  x.bfactor()==2:
                         if x.left.bfactor()==-1 :
                             Rotate_Left_Right(x)
                         else:
                             Rotate_Left(x)
                     
                     print "Linked 3"
                 else:
                     newNode.head=c
                     newNode.tail=b
                     newNode.height=1+b.height
                     newNode.size=1+Node2.size
                   #  newNode.bfactor=0
                     a.left=newNode
                     newNode.parent=a
                     a.head=newNode.head
                     while a.parent!=None:
                         a.head=newNode.head
                         a.size=a.size+1
                         a.height=max(a.left+1,a.right+1)
                         a=a.parent
                     a.head=newNode.head
                     a.size=a.size+1
                     a.height=max(a.left+1,a.right+1)
                     #print "there"
                     x=Node2.parent
                     while x.bfactor()!=2 and x.parent!=None:
                         x=x.parent
                     if  x.bfactor()==2:
                         if x.left.bfactor()==-1 :
                             Rotate_Left_Right(x)
                         else:
                             Rotate_Left(x)

                     print "linked 4"
        elif Node2.external==1 and Node1.external ==0:
            #print Node1.edge
            #print "there"
            while Node1.external!=1 and Node1.height != 2 :
                Node1=Node1.right
            if Node1.parent == None:
                rootNode=InNode(w)
                rootNode.left=Node1
                Node1.parent=rootNode
                rootNode.right=Node2
                Node2.parent=rootNode
                rootNode.head=Node1.head
                rootNode.tail=Node2
                rootNode.height=1+Node1.height
                rootNode.size=1+Node2.size
                #rootNode.bfactor=1
                print "linked 5"
            else:
                 a=Node1.parent
                 b=Node1
                 c=Node2
                # print w
                 newNode=InNode(w)
                 newNode.left=b
                 b.parent=newNode
                 #print b.parent.edge
                 newNode.right=c
                 c.parent=newNode
                 if Node1.external !=1:
                     newNode.head=b.head
                     newNode.tail=c
                     newNode.height=1+b.height
                     newNode.size=1+b.size
                 #    newNode.bfactor=-1
                     a.right=newNode
                     newNode.parent=a
                     a.tail=newNode.tail
                     while a.parent!=None:
                         a.tail=newNode.tail
                         a.size=1+a.size
                         a.height=1+max(a.left.height,a.right.height)
                         a=a.parent
                     a.tail=newNode.tail
                     a.size=1+a.size
                     a.height=1+max(a.left.height,a.right.height)
                     x=Node1.parent
                     #print newNode.bfactor()
                     while x.bfactor()!=-2 and x.parent !=None:
                         x=x.parent
                     if  x.bfactor()==-2:
                         if x.right.bfactor()==1 :
                             Rotate_Right_Left(x)
                         else:
                             Rotate_Right(x)

                     print "Linked 6"
                 else:
                     newNode.head=b
                     newNode.tail=c
                     newNode.height=1+Node1.height
                     newNode.size=1+Node2.size
                  #   newNode.bfactor=0
                     a.right=newNode
                     newNode.parent=a
                     a.tail=newNode.tail
                     while a.parent!=None:
                         a.tail=newNode.tail
                         a.size=1+a.size
                         a.height=1+max(a.left.height,a.right.height)
                         a=a.parent
                     a.tail=newNode.tail
                     a.height=1+max(a.left.height,a.right.height)
                     a.size=1+a.size
                     x=Node1.parent
                     while x.bfactor()!=-2 and x.parent !=None:
                         x=x.parent
                     if  x.bfactor()==-2:
                         if x.right.bfactor()==1 :
                             Rotate_Right_Left(x)
                         else:
                             Rotate_Right(x)
                     print "linked 7"
                 
        else:
            
            if Node2.height >= Node1.height:
                while Node2.height != Node1.height+1 and Node2.height != Node1.height:
                    Node2=Node2.left
                if Node2.parent == None:
                    rootNode=InNode(w)
                    rootNode.left=Node1
                    Node1.parent=rootNode
                    rootNode.right=Node2
                    Node2.parent=rootNode
                    rootNode.head=Node1.head
                    rootNode.tail=Node2.tail
                    rootNode.height=1+Node2.height
                    rootNode.size=1+Node1.size+Node2.size
##                    if Node2.height!=Node1.height:
##                        rootNode.bfactor=-1
##                    else:
##                        rootNode.bfactor=0
                    print "Linked 8"
                else:
                     a=Node2.parent
                     b=Node2
                     c=Node1
                     newNode=InNode(w)
                     newNode.left=c
                     c.parent=newNode
                     newNode.right=b
                     b.parent=newNode
                     newNode.head=c.head
                     newNode.tail=b.tail
                     newNode.height=1+b.height
                     newNode.size=1+c.size+b.size
##                     if Node2.height!=Node1.height:
##                        rootNode.bfactor=-1
##                     else:
##                        rootNode.bfactor=0
##                     a.left=newNode
                     newNode.parent=a
                     a.head=newNode.head
                     while a.parent!=None:
                        a.head=newNode.head
                        a.size=1+a.size+c.size
                        a.height=1+max(a.left.height,a.right.height)
                        a=a.parent
                     a.head=newNode.head
                     a.size=1+a.size+c.size
                     a.height=1+max(a.left.height,a.right.height)
                     x=newNode.parent
                     while x.bfactor()!=2 and x.parent !=None:
                         x=x.parent
                     if  x.bfactor()==2:
                         if x.right.bfactor()==-1 :
                             Rotate_Left_Right(x)
                         else:
                             Rotate_Left(x)
                   #  print "linked 7"
                     print "Linked 9"
            else:
               # print "here"
                while Node1.height != Node2.height+1 :
                    Node1=Node1.right
                #print Node1.external
                #print Node1.parent
                if Node1.parent == None:
                    rootNode=InNode(w)
                    rootNode.left=Node1
                    Node1.parent=rootNode
                    rootNode.right=Node2
                    Node2.parent=rootNode
                    rootNode.head=Node1.head
                    rootNode.tail=Node2.tail
                    rootNode.height=1+Node1.height
                    rootNode.size=1+Node1.size+Node2.size
                    print "Linked 10"
                else:
                     #print_tree(Find_Root(2))
                     a=Node1.parent
                     b=Node2
                     c=Node1
                     newNode=InNode(w)
                     newNode.left=c
                     c.parent=newNode
                     newNode.right=b
                     b.parent=newNode
                     newNode.head=c.head
                     newNode.tail=b.tail
                     newNode.height=1+c.height
                     newNode.size=1+c.size+b.size
                     a.right=newNode
                     newNode.parent=a
                     a.tail=newNode.tail
                     while a.parent!=None:
                        a.tail=newNode.tail
                        a.size=1+a.size+c.size
                        a.height=1+max(a.left.height,a.right.height)
                        a=a.parent
                     a.tail=newNode.tail
                     a.size=1+a.size+c.size
                     a.height=1+max(a.left.height,a.right.height)
                     x=newNode.parent
                    # print_tree(Find_Root(2))
                     while x.bfactor()!=-2 and x.parent !=None:
                         x=x.parent
                     if  x.bfactor()==-2:
                         if x.right.bfactor()==1 :
                             Rotate_Right_Left(x)
                         else:
                             Rotate_Right(x)
                    # print "linked 7"
                     print "Linked 11"


def Find_Root(u):
    #print "here"
    Node1=Tree[u]
   # print Node1.parent.edge
    while Node1.parent !=None:
        #print "here"
        Node1=Node1.parent
        #print Node1.edge
   # print "here"
    
    return Node1

def Is_Reachable(u,v):
    Node1=Tree[u]
    Node2=Tree[v]
    while Node1.parent != None:
        #print "here"
        Node1=Node1.parent
    #print Node1.right.size
    while Node2.parent != None:
        #print "there"
        Node2=Node2.parent
    if Node1!=Node2:
        print v," is NOT Reachable from  " ,u
        return
    Node1=Tree[u]
    Node2=Tree[v]
    a=b=0
    while Node1.parent!=None:
       # print "here"
        if Node1.parent.left==Node1:
           # if Node1.external!=1:
             
             a=a+Node1.parent.right.size+1
        Node1=Node1.parent
    #a=a+1
    while Node2.parent!=None:
        #print "there"
        if Node2.parent.left==Node2:
           # if Node2.external!=1:
             b=b+Node2.parent.right.size+1
        Node2=Node2.parent
    print a,b    
    if a >= b:
        print v ," is reachable from  ", u
        
    
def print_tree(node):
    ##InOrder traversal on InNodes and for each InNode we find the rightmost ExNode of its left
    ##subtree and leftmost ExNode of its right subtree.

    #When the node is only vertex in the path:
    if node==None:
        return
    #when # of vertices in path are greater than 1
    else:
        if not node.left==None and node.left.external==0 :
            print_tree(node.left)
        ##Now get the rightmost element of left subtree and leftmost element of right subtree
        itrl=node.left
        while itrl.right!=None :
            itrl=itrl.right
        itrr=node.right
        while itrr.left!=None :
            itrr=itrr.left
        print itrl.data, node.edge,itrr.data
        if not node.right==None and node.right.external==0:
            print_tree(node.right)


if __name__ == "__main__" :
    Tree = {}
    for i in range(1000):
        Tree[i]= ExNode(i)

   # Link(7,5,191)
    #Link(5,9,170)
   # Link(1,7,455)    
    #print_tree(Find_Root(5))
    #Is_Reachable(1,9)
    	 
