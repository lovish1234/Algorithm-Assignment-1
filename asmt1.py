class ExNode :
    def __init__(self,data):
        self.data=data
        self.size=0
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
    Node1.left=Node3
    Node3.parent=Node1    
    Node2.left=Node4
    if Node4 != None:
        Node4.parent=Node2
    Node2.parent=Node3
    Node3.right=Node2
    Node3.tail=Node2.tail
    if Node4.external !=1:
        Node2.head=Node4.head
    else:
        Node2.head=Node4
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
        B.parent=B
    if B.external!=1:
        Node3.tail=B.tail
    else:
        Node3.tail=B
    if A.external!=1:
        Node4.head=A.head
    else:
        Node4.head=A  
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    Node4.height=max(Node4.right.height+1,Node4.left.height+1)
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
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)
    Node4.height=max(Node4.right.height+1,Node4.left.height+1)
    Rotate_Right(Node)
    
def Rotate_Right(Node):
    print "Rotate Right"
    Node1=Node.parent
    Node2=Node
    Node3=Node.right
    Node4=Node.right.left
    Node1.right=Node3
    Node3.parent=Node1    
    Node2.right=Node4
    if Node4 != None:
        Node4.parent=Node2
    Node2.parent=Node3
    Node3.left=Node2
    Node3.head=Node2.head
    if Node4.external !=1:
        Node2.tail=Node4.tail
    else:
        Node2.tail=Node4
##def rotate_left(node):
##    pivot=node.right
##    root=node
##
##    node.right=node.right.left
##    pivot.node.parent=root
##
##    pivot.node=node
##    nparent=root.parent
##    root.parent=pivot
##
##    pivot.parent=nparent
##def Rotate_Right(self):
##    pivot=self.left
##    root=self
##
##    self.left=self.left.right
##    pivot.right.parent=root
##
##    pivot.right=self
##    nparent=root.parent
##    root.parent=pivot
##
##    pivot.parent=nparent
def rotate_left_right(self):
    rotate_right(self.left)
    rotate_left(self)
def rotate_right_left(self):
    rotate_left(self.right)
    rotate_right(self)
def balance(self):
    value=self.bfactor()
    if value >= 2:
        if self.left.bfactor() > 0:
            self.rotate_right()
        else:
            self.rotate_left_right()
    elif value<=(-2):
        if self.right.bfactor() < 0:
            self.rotate_left()
        else:
            self.rotate_right_left()


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
                     while x.bfactor()!=2:
                         x=x.parent
                     if x.left.bfactor()==-1:
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
                     x=Node2.parent
                     while x.bfactor()!=2:
                         x=x.parent
                     if x.left.bfactor()==-1:
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
                 newNode=InNode(w)
                 newNode.left=b
                 b.parent=newNode
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
                     x=Node2.parent
                     while x.bfactor()!=-2:
                         x=x.parent
                     if x.right.bfactor()==1:
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
                     while x.bfactor()!=-2:
                         x=x.parent
                     if x.right.bfactor()==1:
                         Rotate_Right_left(x)
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
                     a.left=newNode
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
                     print "Linked 11"


def Find_Root(u):
    Node1=Tree[u]
    while Node1.parent !=None:
        Node1=Node1.parent
    return Node1
if __name__ == "__main__" :
     Tree={0:ExNode(0),1:ExNode(1) , 2:ExNode(2), 3:ExNode(3) , 4:ExNode(4),5:ExNode(5),6:ExNode(6)}
     Link(1,2,12)
     Link(2,3,15)
     Link(4,5,100)
     Link(3,5,50)
     Link(0,1,69)
     #Link(3,4,20)
     #Link(5,6,30)
     #Link(2,6,100)
     x=Find_Root(3)
     print x.bfactor()
     
