import sys
import tt
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
        self.size=0
        self.edge=data
        self.multi_add=0
    def bfactor(self):
        return self.left.height-self.right.height
    
def Rotate_Left(Node):
 #   print "Rotate Left"
    Parent=Node.parent
    Node5=Node
    Node4=Node.left
    Node3=Node.left.left
    A=Node3.left
    B=Node3.right
    C=Node4.right
    D=Node5.right
    if Parent !=None:
        if Parent.left==Node5:
            Parent.left=Node4
        else:
            Parent.right=Node4
    Node4.parent=Parent
    Node4.left=Node3
    Node3.parent=Node4
    Node4.right=Node5
    Node5.parent=Node4
    Node5.right=D
    D.parent=Node5
    Node5.left=C
    C.parent=Node5
    Node3.right=B
    B.parent=Node3
    #Modify heads and tails
    if A.external!=1:
        Node3.head=A.head
    else:
        Node3.head=A
    if B.external!=1:
        Node3.tail=B.tail
    else:
        Node3.tail=B
    if C.external!=1:
        Node5.head=C.head
    else:
        Node5.head=C
    if D.external!=1:
        Node5.tail=D.tail
    else:
        Node5.tail=D

    Node4.head=Node3.head
    Node4.tail=Node5.tail
    Node3.size=1+Node3.left.size+Node3.right.size
    Node5.size=1+Node5.left.size+Node5.right.size
    Node4.size=1+Node4.left.size+Node4.right.size
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    Node4.height=max(Node4.left.height+1,Node4.right.height+1)
    while Parent!=None:
        Parent.height=max(Parent.left.height+1,Parent.right.height+1)
        if Parent.left.parent==Parent:
            Parent.head=Parent.left.head
        Parent=Parent.parent
        
def Rotate_Left_Right(Node):
#    print "Rotate Left Right"
    Parent=Node.parent
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
    Node3.right=B
    B.parent=Node3
    Node4.right=C
    C.parent=Node4
    #modify head and tails
    if A.external!=1:
        Node3.head=A.head
    else:
        Node3.head=A
    if B.external!=1:
        Node3.tail=B.tail
    else:
        Node3.tail=B
    Node4.head=Node3.head
    if C.external!=1:
        Node4.tail=C.tail
    else:
        Node4.tail=C
    Node5.head=Node4.head
    if D.external!=1:
        Node5.tail=D.tail
    else:
        Node5.tail=D
    Node3.size=1+Node3.left.size+Node3.right.size
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    Node4.size=1+Node4.left.size+Node4.right.size
    Node4.height=max(Node4.left.height+1,Node4.right.height+1)
    Node5.size=1+Node5.left.size+Node5.right.size
    while Node5!=None:
        Node5.height=max(Node5.left.height+1,Node5.right.height+1)
        if Node5.left.parent==Node5:
            Node5.head=Node5.left.head
        Node5=Node5.parent
    
    Rotate_Left(Node)
    
def Rotate_Right_Left(Node):
  #  print "Rotate Right Left"
    Parent=Node.parent
    Node3=Node
    Node5=Node.right
    Node4=Node.right.left
    A=Node3.left
    B=Node4.left
    C=Node4.right
    D=Node5.right
    Node3.right=Node4
    Node4.parent=Node3
    Node4.left=B
    B.parent=Node4
    Node4.right=Node5
    Node5.parent=Node4
    Node5.left=C
    C.parent=Node5
    Node5.right=D
    D.parent=Node5
    #modify Head and Tails
    if C.external!=1:
        Node5.head=C.head
    else:
        Node5.head=C
    if D.external!=1:
        Node5.tail=D.tail
    else:
        Node5.tail=D
    if B.external!=1:
        Node4.head=B.head
    else:
        Node4.head=B
    Node4.tail=Node5.tail
    if A.external!=1:
        Node3.head=A.head
    else:
        Node3.head=A
    Node3.tail=Node4.tail
    Node5.size=1+Node5.left.size+Node5.right.size
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)

    Node4.size=1+Node4.left.size+Node4.right.size
    Node4.height=max(Node4.left.height+1,Node4.right.height+1)
    Node3.size=1+Node3.left.size+Node3.right.size
    while Node3!=None:
        Node3.height=max(Node3.left.height+1,Node3.right.height+1)
        if Node3.right.parent==Node3:
            Node3.tail=Node3.right.tail
        Node3=Node3.parent
    Rotate_Right(Node)

def Rotate_Right(Node):
 #   print "Rotate Right"
    Parent=Node.parent
    Node3=Node
    Node4=Node.right
    Node5=Node.right.right
    A=Node3.left
    B=Node4.left
    C=Node5.left
    D=Node5.right
    if Parent!=None:
        if Parent.left==Node3:
            Parent.left=Node4
        else:
            Parent.right=Node4
    Node4.parent=Parent
    Node4.left=Node3
    Node3.parent=Node4
    Node4.right=Node5
    Node5.parent=Node4
    Node3.left=A
    A.parent=Node3
    Node3.right=B
    B.parent=Node3
    Node5.left=C
    C.parent=Node5
    Node5.right=D
    D.parent=Node5
    #modify head and tails
    if A.external!=1:
        Node3.head=A.head
    else:
        Node3.head=A
    if B.external!=1:
        Node3.tail=B.tail
    else:
        Node3.tail=B
    if C.external!=1:
        Node5.head=C.head
    else:
        Node5.head=C
    if D.external!=1:
        Node5.tail=D.tail
    else:
        Node5.tail=D
    Node4.head=Node3.head
    Node4.tail=Node5.tail
    Node3.size= 1+ Node3.left.size + Node3.right.size
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    Node5.size= 1+ Node5.left.size + Node5.right.size
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)
    Node4.size=1+Node4.left.size+Node4.right.size
    Node4.height=max(Node4.left.height+1,Node4.right.height+1)
    while Parent !=None:
        Parent.height=max(Parent.left.height+1,Parent.right.height+1)
        if Parent.right.parent==Parent:
            Parent.tail=Parent.right.tail
        Parent=Parent.parent

def Link(u,v,w):
    Node1=Tree[u]
    Node2=Tree[v]
    while Node1.parent!=None:
        Node1=Node1.parent
    while Node2.parent!=None:
        Node2=Node2.parent
    if Node1.external==1 and Node2.external==1:
        newNode=InNode(w)
        newNode.left=Node1
        Node1.parent=newNode
        newNode.right=Node2
        Node2.parent=newNode
        newNode.head=Node1
        newNode.tail=Node2
        newNode.size=1
        newNode.height=2
#	print_tree(Find_Root(u))
    elif Node1.external!=1 and Node2.external==1:
        while Node1.external!=1 and Node1.height!=2:
            Node1=Node1.right
        if Node1.parent==None:
            newNode=InNode(w)
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1.head
            newNode.tail=Node2
            newNode.size=2
            newNode.height=3
#	    print_tree(Find_Root(u))
        elif Node1.external==1:
            Parent=Node1.parent
            newNode=InNode(w)
            Parent.right=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1
            newNode.tail=Node2
            newNode.size=1
            newNode.height=2
            while Parent!=None:
                Parent.tail=Parent.right.tail
                Parent.size=1+Parent.left.size+Parent.right.size
                Parent.height=max(Parent.left.height+1,Parent.right.height+1)
                Parent=Parent.parent
            while newNode.parent!=None and newNode.bfactor()!=-2:
                newNode=newNode.parent
            if newNode.bfactor()==-2:
                if newNode.right.bfactor()==1:
                    Rotate_Right_Left(newNode)
                elif newNode.right.bfactor()==-1:
                    Rotate_Right(newNode)
#	    print_tree(Find_Root(u))        
        else:
            Parent=Node1.parent
            newNode=InNode(w)
            Parent.right=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1.head
            newNode.tail=Node2
            newNode.size=1+Node1.size
            newNode.height=1+Node1.height
            while Parent!=None:
                Parent.tail=Parent.right.tail
                Parent.size=1+Parent.left.size+Parent.right.size
                Parent.height=max(Parent.left.height+1,Parent.right.height+1)
                Parent=Parent.parent
            while newNode.parent!=None and newNode.bfactor()!=-2:
                newNode=newNode.parent
            if newNode.bfactor()==-2:
                if newNode.right.bfactor()==1:
                    Rotate_Right_Left(newNode)
                elif newNode.right.bfactor()==-1:
                    Rotate_Right(newNode)
#	    print_tree(Find_Root(u))
    elif Node2.external!=1 and Node1.external==1:
        while Node2.external!=1 and Node2.height!=2:
            Node2=Node2.left
        if Node2.parent==None:
            newNode=InNode(w)
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1
            newNode.tail=Node2.tail
            newNode.size=2
            newNode.height=3
#	    print_tree(Find_Root(u))
        elif Node2.external==1:
            Parent=Node2.parent
            newNode=InNode(w)
            Parent.left=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1
            newNode.tail=Node2
            newNode.size=1
            newNode.height=2
            while Parent!=None:
                Parent.head=Parent.left.head
                Parent.size=1+Parent.left.size+Parent.right.size
                Parent.height=max(Parent.left.height+1,Parent.right.height+1)
                Parent=Parent.parent
            while newNode.parent!=None and newNode.bfactor()<2:
                newNode=newNode.parent
            if newNode.bfactor()>=2:
                if newNode.left.bfactor()==-1:
                    Rotate_Left_Right(newNode)
                elif newNode.left.bfactor()==1:
                    Rotate_Left(newNode)        
#	    print_tree(Find_Root(u))        
	else:
            Parent=Node2.parent
            newNode=InNode(w)
            Parent.left=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1
            newNode.tail=Node2.tail
            newNode.size=1+Node2.size
            newNode.height=1+Node2.height
            while Parent!=None:
                Parent.head=Parent.left.head
                Parent.size=1+Parent.left.size+Parent.right.size
                Parent.height=max(Parent.left.height+1,Parent.right.height+1)
                Parent=Parent.parent
	    
            while newNode.parent!=None and newNode.bfactor()!=2:
                newNode=newNode.parent
            if newNode.bfactor()==2:
                if newNode.left.bfactor()==-1:
                    Rotate_Left_Right(newNode)
                elif newNode.left.bfactor()==1:
                    Rotate_Left(newNode)
 #           print_tree(Find_Root(u))        
    elif Node1.height > Node2.height:
        while  Node1.height!=Node2.height+1 and Node1.height!=Node2.height:
            Node1=Node1.right
        if  Node1.parent==None:
            #print "here"
            newNode=InNode(w)
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1.head
            newNode.tail=Node2.tail
            newNode.height=max(newNode.left.height+1,newNode.right.height+1)
            newNode.size=1+newNode.left.size+newNode.right.size
#	    print_tree(Find_Root(u))
        else:
            newNode=InNode(w)
            Parent=Node1.parent
            Parent.right=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1.head
            newNode.tail=Node1.tail
            newNode.size=1 + newNode.left.size+newNode.right.size
            newNode.height=max(newNode.left.height+1,newNode.right.height+1)
            while Parent!=None:
                Parent.tail=Parent.right.tail
                Parent.size=1+Parent.left.size+Parent.right.size
                Parent.height=max(Parent.left.height+1,Parent.right.height+1)
                Parent=Parent.parent
            while newNode.parent!=None and newNode.bfactor()!=-2:
                newNode=newNode.parent
            if newNode.bfactor()==-2:
                if newNode.right.bfactor()==1:
                    Rotate_Right_Left(newNode)
                elif newNode.right.bfactor()==-1:
                    Rotate_Right(newNode)
#	    print_tree(Find_Root(u))
    else:
        #print Node2.height
        while Node2.height!=Node1.height+1 and Node2.height!=Node1.height :
            #if v==4:
 #           print Node2.height,Node1.height
            Node2=Node2.left
        
        if Node2.parent==None:
            newNode=InNode(w)
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1.head
            newNode.tail=Node2.tail
            newNode.height=max(newNode.left.height+1,newNode.right.height+1)
            newNode.size=1+newNode.left.size+newNode.right.size
#	    print_tree(Find_Root(u))        
	else:
            newNode=InNode(w)
            Parent=Node2.parent
            Parent.left=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1.head
            newNode.tail=Node2.tail
            newNode.size=1+newNode.left.size+newNode.right.size
            newNode.height=max(newNode.left.height+1,newNode.right.height+1)
            while Parent!=None:
                Parent.head=Parent.left.head
                Parent.size=1+Parent.left.size+Parent.right.size
                Parent.height=max(Parent.left.height+1,Parent.right.height+1)
                Parent=Parent.parent
            while newNode.parent!=None and newNode.bfactor()!=2:
                newNode=newNode.parent
            if newNode.bfactor()==2:
                if newNode.left.bfactor()==-1:
                    Rotate_Left_Right(newNode)
                elif newNode.left.bfactor()==1:
                    Rotate_Left(newNode)
#	    print_tree(Find_Root(u))


def Find_Root(u):
    Node1=Tree[u]
    while Node1.parent !=None:
        Node1=Node1.parent    
    return Node1


count=0   
def print_tree(node):
    ##InOrder traversal on InNodes and for each InNode we find the rightmost ExNode of its left
    ##subtree and leftmost ExNode of its right subtree.
    global count
    #When the node is only vertex in the path:
    if node==None:
        return
    elif(node.external==1):
        print node.data    
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
        if  count==0:
            g.write( str(str(itrl.data) + '---'+ str(node.edge)+'--->>>>>'+str(itrr.data)))
            count=1
        else:
            g.write(  str( '---'+ str(node.edge)+'--->>>>>'+str(itrr.data)))
        if not node.right==None and node.right.external==0:
            print_tree(node.right)
            

#def print_tree(node):
    ##InOrder traversal on InNodes and for each InNode we find the rightmost ExNode of its left
    ##subtree and leftmost ExNode of its right subtree.

    #When the node is only vertex in the path:
 #   if node==None:
#        return
    #when # of vertices in path are greater than 1
  #  else:
   #     if not node.left==None and node.left.external==0 :
    #        print_tree(node.left)
        ##Now get the rightmost element of left subtree and leftmost element of right subtree
     #   itrl=node.left
    #    while itrl.right!=None :
     #       itrl=itrl.right
      #  itrr=node.right
       # while itrr.left!=None :
     #       itrr=itrr.left
      #  print itrl.data,"--",node.height,"(",node.left.height,",",node.right.height,")","---",node.size,"(",node.left.size,"+",node.right.size,")","--",itrr.data
       # if not node.right==None and node.right.external==0:
        #    print_tree(node.right)







#global start
if __name__ == "__main__" :  
#     global start=time.time() 
     f=open(sys.argv[1],'r')
     g=open(sys.argv[2],'w')
     cases=f.readlines()
 #    start_time=time.time
     for x in cases:
        splitcases=x.split()
        if(splitcases[0]=='L') :  
            Link(int(splitcases[1]),int(splitcases[2]),int(splitcases[3]))
        elif(splitcases[0]=='C') :
            Cut(int(splitcases[1]),int(splitcases[2]))
        elif(splitcases[0]=='I'):
            Is_Reachable(int(splitcases[1]),int(splitcases[2]))
        else:
            Tree={}
            total=int(splitcases[0])    
            for i in range(int(splitcases[0])+1):                                                     
                 Tree[i]=ExNode(i)
     print_tree(Find_Root(1))   
     f.close()    
     g.close()

#print time.time() - start,"sec"

