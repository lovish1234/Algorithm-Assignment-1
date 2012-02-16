import sys
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
        self.size=1
        self.edge=data
        self.multi_add=0
    def bfactor(self):
        return self.left.height-self.right.height
def Link(u,v,x):
##When both are external nodes
    a=Find_Root(u)
    b=Find_Root(v)
    if a.external==1 and b.external==1:
        Node=InNode(x)
        Node.left=a
        Node.right=b
        Node.head=a
        Node.tail=b
        Node.height=1
        a.parent=Node
        b.parent=Node
        Node.size=1
        #No Balancing required in this case
    elif a.external==1 and b.external==0:    
        while  b.left.external==1:
            b=b.left  
        c=b.parent              
        Node=InNode(x)
        Node.left=a
        Node.head=a
        a.parent=Node
        Node.right=b 
        b.parent=Node       
        Node.tail=b.tail
        Node.height=1+max(b.height,a.height)
        Node.size=b.size+1
        Node.parent=c.parent
        #Do balance
    elif a.external==0 and b.external==1:
        while a.right==1:
            a=a.right
        c=a.parent
        Node=InNode(x)
        Node.right=b
        Node.tail=b
        b.parent=Node
        Node.left=a
        a.parent=Node
        Node.head=a.head
        Node.height=1+max(a.height,b.height)
        Node.size=a.size+1
        Node.parent=c.parent
        #Do Balance
     else:
        if a.height==b.height or a.height==b.height+1 or a.height+1==b.height:
            Node=InNode(x)
            Node.left=a
            Node.right=b
            Node.head=a.head
            Node.tail=b.tail
            Node.size=1+b.size+a.size
            Node.height=1+max(a.height,b.height)
            a.parent=Node
            b.parent=Node
            # No balancing required in this case too
        elif a.height>b.height+1:
            while b.left!=None :
                if b.height==a.height+1 or b.height==a.height:
                    break
                else:
                    b=b.left
            c=b.parent
            Node=InNode(x)
            Node.left=a
            Node.right=b
            Node.head=a.head
            Node.tail=b.tail
            Node.size=1+a.size+b.size
            Node.height=1+max(a.height,b.height)
            Node.parent=c
            #Do balance    
        else:
            while a.right!=None:
                if a.height==b.height+1 or a.height==b.height:
                    break
                else:
                    a=a.right
            c=a.parent
            Node=InNode(x)
            Node.left=a
            Node.right=b
            Node.head=a.head
            Node.tail=b.tail
            Node.size= =1+a.size+b.size
            Node.height=1+max(a.height,b.height)
            Node.parent=c
            #do balance
               
def Find_Root(u):
    Node=Tree[u]
    while Node.parent !=None:
        Node=Node1.parent
    return Node



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
            

if __name__ == "__main__" :
     f=open(sys.argv[1],'r')
     g=open(sys.argv[2],'w')
     cases=f.readlines()
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
            for i in range(int(splitcases[0])+1):                                                              Tree[i]=ExNode(i)
     print_tree(Find_Root(1))   
     f.close()    
     g.close()
