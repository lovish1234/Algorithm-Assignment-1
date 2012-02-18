import sys
import tt
inf=float('inf')
class ExNode :
    def __init__(self,data):
        self.data=data
        self.size=0
        self.left=None
        self.right=None
        self.external=1
        self.height=0
        self.parent=None
        
class InNode :
    def __init__(self,data):
        self.left=None
        self.right=None
        self.external=0
        self.parent=None
        self.head=None
        self.tail=None
        self.height=0
        self.size=0
        self.edge=data
        self.multi_add=0
	self.min_wt=inf
    def bfactor(self):
        return self.left.height-self.right.height
    
def Rotate_Left(Node):
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
    Node3.left=A
    A.parent=Node3
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
    #Modify Multi_adds
    add4=Node4.multi_add
    add5=Node5.multi_add
    Node4.multi_add=add4+add5
    Node5.multi_add=add5-Node4.multi_add
    if C.external!=1:
	C.multi_add=C.multi_add+add4
    
    Node4.head=Node3.head
    Node4.tail=Node5.tail
    Node3.size=1+Node3.left.size+Node3.right.size
    Node5.size=1+Node5.left.size+Node5.right.size
    Node4.size=1+Node4.left.size+Node4.right.size
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    Node4.height=max(Node4.left.height+1,Node4.right.height+1)

    #changes in min_weight while rotation
    if C.external==0 and D.external==0:
        Node5.min_weight=min(C.min_weight,D.min_weight,Node5.min_weight)
    else:
        if C.external==1 and D.external==0:
            Node5.min_weight=min(D.min_weight,Node5.min_weight)
        elif C.external==0 and D.external==1:
            Node5.min_weight=min(C.min_weight,Node5.min_weight)
        else:
            Node5.min_weight=Node5.min_weight
    Node3.min_weight=min(Node4.min_weight(),Node5.min_weight(),Node3.min_weight())
    #changes end

    while Parent!=None:
        Parent.height=max(Parent.left.height+1,Parent.right.height+1)
        if Parent.left.parent==Parent:
            Parent.head=Parent.left.head
        Parent=Parent.parent
        
def Rotate_Left_Right(Node):
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
    Node3.left=A
    A.parent=Node3
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
    add3=Node3.multi_add
    add4=Node4.multi_add
    add5=Node5.multi_add
    Node4.multi_add=add3+add4
    Node3.multi_add=add3-Node4.multi_add
    if B.external  !=1: 
	 B.multi_add=B.multi_add+add4
    Node3.size=1+Node3.left.size+Node3.right.size
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    Node4.size=1+Node4.left.size+Node4.right.size
    Node4.height=max(Node4.left.height+1,Node4.right.height+1)
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)
    Node5.size=1+Node5.left.size+Node5.right.size

   # added for min_weight
    if A.external==0 and B.external==0:
        Node3.min_weight=min(A.min_weight,B.min_weight,Node3.min_weight)
    else:
        if A.external==1 and B.external==0:
            Node3.min_weight=min(B.min_weight,Node3.min_weight)
        elif A.external==0 and B.external==1:
            Node3.min_weight=min(A.min_weight,Node3.min_weight)
        else:
            Node3.min_weight=Node3.min_weight
    if C.external==1 :
        Node4.min_weight=min(Node3.min_weight,Node4.min_weight)
    else:
        Node4.min_weight=min(C.min_weight,Node3.min_weight,Node4.min_weight)
    if D.external==1:
        Node5.min_weight=min(Node4.min_weight,Node5.min_weight)
    else:
        Node5.min_weight=min(Node4.min_weight,D.min_weight,Node5.min_weight)
    #changes end

    while Parent!=None:
        Parent.height=max(Parent.left.height+1,Parent.right.height+1)
        if Parent.left.parent==Parent:
            Parent.head=Parent.left.head
        Parent=Parent.parent
    
    Rotate_Left(Node)
    
def Rotate_Right_Left(Node):
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
    add3=Node3.multi_add
    add4=Node4.multi_add
    add5=Node5.multi_add
    Node4.multi_add=add4+add5
    Node5.multi_add=add5-Node4.multi_add
    if C.external!=1:
	C.multi_add=C.multi_add+add4
    Node3.tail=Node4.tail
    Node5.size=1+Node5.left.size+Node5.right.size
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)

    Node4.size=1+Node4.left.size+Node4.right.size
    Node4.height=max(Node4.left.height+1,Node4.right.height+1)
    Node3.size=1+Node3.left.size+Node3.right.size
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)

   
    #added for min-weight 
    if C.external==0 and D.external==0:
        Node5.min_weight=min(C.min_weight,D.min_weight,Node5.min_weight)
    else:
        if C.external==1 and D.external==0:
            Node5.min_weight=min(D.min_weight,Node5.min_weight)
        elif C.external==0 and D.external==1:
            Node5.min_weight=min(C.min_weight,Node3.min_weight)
        else:
            Node5.min_weight=Node5.min_weight
    if B.external==1 :
        Node4.min_weight=min(Node5.min_weight,Node4.min_weight)
    else:
        Node4.min_weight=min(B.min_weight,Node3.min_weight,Node4.min_weight)
    if A.external==1:
        Node3.min_weight=min(Node4.min_weight,Node5.min_weight)
    else:
        Node3.min_weight=min(Node4.min_weight,A.min_weight,Node5.min_weight)
    #changes end    


    while Parent!=None:
        Parent.height=max(Parent.left.height+1,Parent.right.height+1)
        if Parent.right.parent==Parent:
            Parent.tail=Parent.right.tail
        Parent=Parent.parent
    Rotate_Right(Node)

def Rotate_Right(Node):
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
    add3=Node3.multi_add
    add4=Node4.multi_add
    add5=Node5.multi_add
    Node4.multi_add=add3+add4
    Node3.multi_add=add3-Node4.multi_add
    if B.external!=1:
    	B.multi_add=B.multi_add+add4
    Node4.head=Node3.head
    Node4.tail=Node5.tail
    Node3.size= 1+ Node3.left.size + Node3.right.size
    Node3.height=max(Node3.left.height+1,Node3.right.height+1)
    Node5.size= 1+ Node5.left.size + Node5.right.size
    Node5.height=max(Node5.left.height+1,Node5.right.height+1)
    Node4.size=1+Node4.left.size+Node4.right.size
    Node4.height=max(Node4.left.height+1,Node4.right.height+1)


    #for min_weight
    if A.external==0 and B.external==0:
        Node3.min_weight=min(A.min_weight,B.min_weight,Node3.min_weight)
    else:
        if A.external==1 and B.external==0:
            Node3.min_weight=min(B.min_weight,Node3.min_weight)
        elif A.external==0 and B.external==1:
            Node3.min_weight=min(A.min_weight,Node3.min_weight)
        else:
            Node3.min_weight=Node3.min_weight
    Node4.min_weight=min(Node3.min_weight,Node5.min_weight,Node4.min_weight)
    #end changing

    while Parent !=None:
        Parent.height=max(Parent.left.height+1,Parent.right.height+1)
        if Parent.right.parent==Parent:
            Parent.tail=Parent.right.tail
        Parent=Parent.parent

def Merge(u,v,w):
    Node1=u
    Node2=v
    while Node1.parent!=None:
        Node1=Node1.parent
    while Node2.parent!=None:
        Node2=Node2.parent
    add=0
    if Node1.external==1 and Node2.external==1:
        newNode=InNode(w)
        newNode.left=Node1
        Node1.parent=newNode
        newNode.right=Node2
        Node2.parent=newNode
        newNode.head=Node1
        newNode.tail=Node2
        newNode.size=1
        newNode.height=max(newNode.left.height+1,newNode.right.height+1)
    elif Node1.external!=1 and Node2.external==1:
	
        while Node1.external!=1 and Node1.height!=1:
		add=add+Node1.multi_add            
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
            newNode.height=max(newNode.left.height+1,newNode.right.height+1)
        elif Node1.external==1:
            Parent=Node1.parent
            newNode=InNode(w)
	    newNode.multi_add= -add
            Parent.right=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1
            newNode.tail=Node2
            newNode.size=1
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
        else:
            Parent=Node1.parent
            newNode=InNode(w)
	    newNode.multi_add=-add
            Parent.right=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1.head
            newNode.tail=Node2
            newNode.size=1+Node1.size
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
    elif Node2.external!=1 and Node1.external==1:
        while Node2.external!=1 and Node2.height!=1:
	    add=add+Node2.multi_add
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
            newNode.height=max(newNode.left.height+1,newNode.right.height+1)
        elif Node2.external==1:
            Parent=Node2.parent
            newNode=InNode(w)
	    newNode.multi_add=-add
            Parent.left=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1
            newNode.tail=Node2
            newNode.size=1
            newNode.height=max(newNode.left.height+1,newNode.right.height+1)
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
	else:
            Parent=Node2.parent
            newNode=InNode(w)
            newNode.multi_add=-add
	    Parent.left=newNode
            newNode.parent=Parent
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1
            newNode.tail=Node2.tail
            newNode.size=1+Node2.size
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
    elif Node1.height > Node2.height:
        while  Node1.height!=Node2.height+1 and Node1.height!=Node2.height:
		add=add+Node1.multi_add            
		Node1=Node1.right
        if  Node1.parent==None:
            newNode=InNode(w)
            newNode.left=Node1
            Node1.parent=newNode
            newNode.right=Node2
            Node2.parent=newNode
            newNode.head=Node1.head
            newNode.tail=Node2.tail
            newNode.height=max(newNode.left.height+1,newNode.right.height+1)
            newNode.size=1+newNode.left.size+newNode.right.size
        else:
            newNode=InNode(w)
	    newNode.multi_add=-add
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
    else:
        while Node2.height!=Node1.height+1 and Node2.height!=Node1.height :
	    add=add+Node2.multi_add         
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
	else:
            newNode=InNode(w)
	    newNode.multi_add=-add
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

   
def Link(u,v,w):
	Node1=Tree[u]
	Node2=Tree[v]
	Merge(Node1,Node2,w)
def Cut(u,v):
	Node1=Tree[u]
	Node2=Tree[v]
   	Root1= Find_Root(u)
   	Root2 = Find_Root(v)
   	if Root1 != Root2:
       		return -1
   	else:
		while Node1.parent!=None and Node1.parent.left!=Node1:
       			Node1 = Node1.parent
       		
		Node1= Node1.parent
		Parent=Node1.parent
		A=Node1.left
		B=Node1.right
                if B.external!=1 and A.external!=1:
                	A.multi_add+=Node1.multi_add
                	B.multi_add+=Node1.multi_add
		elif B.external==1 and A.external!=1:
                	A.multi_add+=Node1.multi_add
                elif B.external!=1 and A.external==1:
			B.multi_add+=Node1.multi_add
		A.parent=None
		B.parent=None
       		while Parent != None:
           		if Parent.left==Node1:
               			Parent.right.parent = None
				if Node1.right.external!=1 and Parent.right.external!=1:                                
					Parent.right.multi_add +=Parent.multi_add
					Node1.right.multi_add +=Node1.multi_add+Parent.multi_add
               				Merge(B,Parent.right,Parent.edge)
				elif Node1.right.external==1 and Parent.right.external!=1:                                
					Parent.right.multi_add+=Parent.multi_add
               				Merge(B,Parent.right,Parent.edge+Parent.multi_add)
             			elif Node1.right.external!=1 and Parent.right.external==1:                                
					Node1.right.multi_add+=Parent.multi_add+Node1.multi_add
               				Merge(B,Parent.right,Parent.edge+Parent.multi_add)
				else:
					Merge(B,Parent.right,Parent.edge+Parent.multi_add)
					
				Node1= Parent
               			Parent = Parent.parent
           		else:
               			Parent.left.parent = None
				if Node1.left.external!=1 and Parent.left.external!=1:                                
					Parent.left.multi_add +=Parent.multi_add
					Node1.left.multi_add +=Node1.multi_add+Parent.multi_add
               				Merge(Parent.left,A,Parent.edge)
				elif Node1.left.external==1 and Parent.left.external!=1:                                
					Parent.left.multi_add+=Parent.multi_add
               				Merge(Parent.left,A,Parent.edge+Parent.multi_add)
             			elif Node1.left.external!=1 and Parent.left.external==1:                                
					Node1.left.multi_add+=Parent.multi_add+Node1.multi_add
               				Merge(Parent.left,A,Parent.edge+Parent.multi_add)
				else:
					Merge(Parent.left,A,Parent.edge+Parent.multi_add)
               			Node1= Parent
               			Parent = Parent.parent

def Is_Reachable(u,v):
        root1=Find_Root(u)
        root2=Find_Root(v)
        if root1==root2:
		count1,count2=Count(u,v)
        	if count1 <= count2:
		        h.write("1\n")
		else:
			h.write("0\n")
        else:
		h.write("0\n")


def Count(u,v):
	Node1=Tree[u]
	Node2=Tree[v]
	a=b=0
        while Node1.parent!=None:
        	if Node1.parent.right==Node1:         
        	     a=a+Node1.parent.left.size+1
        	Node1=Node1.parent
        while Node2.parent!=None:
        	if Node2.parent.right==Node2:
        	     b=b+Node2.parent.left.size+1
        	Node2=Node2.parent
        return a,b


#Find Lowest  Common Ancestor

def Find_LCA(ucount,vcount,root):        
       
	if root.left.size >ucount and root.left.size>vcount:
                
               return   Find_LCA(ucount,vcount,root.left)
        elif root.left.size >=ucount and vcount>=root.left.size:
		return root
        else:
		return  Find_LCA(ucount-root.left.size-1,vcount-root.left.size-1,root.right)



def Multi_add(u,v,w):
	root1=Find_Root(u)
        root2=Find_Root(v)
        if root1!=root2:
                return
        ucount,vcount=Count(u,v)
	Node1=Tree[u]
	Node2=Tree[v]
	while Node1.parent!=None:
		Node1=Node1.parent
   	root=Node1
   	LCA=Find_LCA(ucount,vcount,root)
        if v==2:
                print LCA
	Node1=Tree[u]
	Node2=Tree[v]
        while Node1.parent!=LCA:
		if Node1.parent.left==Node1:
			if Node1.parent.right.external!=1:
				Node1.parent.right.multi_add +=w
				Node1.parent.edge +=w
				Node1.parent.right.min_wt+=w
			else:
      				Node1.parent.edge +=w
		if Node1.parent.left.external!=1 and Node1.parent.right.external!=1: 
			Node1.parent.min_wt=min(Node1.parent.left.min_wt,Node1.parent.edge,Node1.parent.right.min_wt)
		if Node1.parent.left.external==1 and Node1.parent.right.external!=1: 
			Node1.parent.min_wt=min(Node1.parent.edge,Node1.parent.right.min_wt)
		else:
			Node1.parent.min_wt=Node1.parent.edge
		Node1=Node1.parent

        while Node2.parent!=LCA:
		if Node2.parent.right==Node1:
			if Node2.parent.left.external!=1:
				Node2.parent.left.multi_add +=w
				Node2.parent.edge +=w
			else:
      				Node2.parent.edge +=w
		if Node2.parent.left.external!=1 and Node2.parent.right.external!=1: 
			Node2.parent.min_wt=min(Node2.parent.left.min_wt,Node2.parent.edge,Node2.parent.right.min_wt)
		elif Node2.parent.left.external==1 and Node2.parent.right.external!=1: 
			Node2.parent.min_wt=min(Node2.parent.edge,Node2.parent.right.min_wt)
		else:
			Node2.parent.min_wt=Node2.parent.edge

		Node2=Node2.parent
        #print  LCA
      	LCA.edge =LCA.edge+w
	if LCA.left.external!=1 and LCA.right.external!=1: 
			LCA.min_wt=min(LCA.left.min_wt,LCA.edge,LCA.right.min_wt)
	elif LCA.left.external==1 and LCA.right.external!=1: 
			LCA.min_wt=min(LCA.edge,LCA.right.min_wt)
        elif LCA.left.external!=1 and LCA.right.external==1:
                        LCA.min_wt=min(LCA.edge,LCA.left.min_wt)
	else:
			LCA.min_wt=LCA.edge
	temp=LCA.parent
	#Update Minimum upto root
	while temp!=None:
		if temp.left.external!=1 and temp.right.external!=1:		
			temp.min_wt=min(temp.left.min_wt,temp.right.min_wt,temp.edge)
		elif temp.left.external==1 and temp.right.external!=1:
			temp.min_wt=min(temp.right.min_wt,temp.edge)		
		else:
			temp.min_wt=temp.edge
		temp=temp.parent

def Find_Root(u):
    Node1=Tree[u]
    while Node1.parent !=None:
        Node1=Node1.parent    
    return Node1


count=0   
def print_tree(node,GA):
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
            print_tree(node.left,GA+node.multi_add)
        ##Now get the rightmost element of left subtree and leftmost element of right subtree
        itrl=node.left
        while itrl.right!=None :
            itrl=itrl.right
        itrr=node.right
        while itrr.left!=None :
            itrr=itrr.left
        if  count==0:
            g.write( str(str(itrl.data) + '---'+ str(node.edge+GA)+'--->>>>>'+str(itrr.data)))
            count=1
        else:
            g.write(  str( '---'+ str(node.edge+GA)+'--->>>>>'+str(itrr.data)))
        if not node.right==None and node.right.external==0:
            print_tree(node.right,GA+node.multi_add)
      

 

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



if __name__ == "__main__" :  
     f=open(sys.argv[1],'r')
     g=open(sys.argv[2],'w')
     h=open(sys.argv[3],'w')
     cases=f.readlines()
     for x in cases:
        splitcases=x.split()
        if(splitcases[0]=='L') :  
            Link(int(splitcases[1]),int(splitcases[2]),int(splitcases[3]))
        elif(splitcases[0]=='C') :
            Cut(int(splitcases[1]),int(splitcases[2]))
        elif(splitcases[0]=='I'):
            Is_Reachable(int(splitcases[1]),int(splitcases[2]))
        elif(splitcases[0]=='A'):
            Multi_add(int(splitcases[1]),int(splitcases[2]),int(splitcases[3]))
        else:
            Tree={}
            total=int(splitcases[0])    
            for i in range(int(splitcases[0])+1):                                                     
                 Tree[i]=ExNode(i)
     print_tree(Find_Root(1),0)   
     f.close()    
     g.close()
     h.close()   


