import random

#Defining a Node
class Node:
    def __init__(self,data):
    	self.data=data
        self.in_edge=0 # stores weight of incoming edge on vertex
        self.out_edge=0 #stores weight of outgoing edge from vertex
        self.left=None # stores pointer to vertex left for a vertex
        self.right=None # stores pointer to vertex right for a vertex

#Linked_List implementation of Link
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
        return 0   
    while Node1.right!= None and Node1!=Node2:
        Node1=Node1.right
    if Node1 != Node2:
        while Node2.left!= None :
            Node2=Node2.left
     #       print "Hello1"    
        Node1.right=Node2
        Node2.left=Node1
        Node1.out_edge=w
        Node2.in_edge=w
        return 1
    else:
        return 0

#Linked_List implementation of Cut.Would help in determining and making random test cases for our new implementation.
def Cut(u,v):
    Node1=Tree[u]
    Node2=Tree[v]
    if Node1.right==Node2:
        Node1.right=None
        Node2.left=None
        Node1.out_edge=0
        Node2.in_edge=0
	return 1
    else:
        #print "Their is no Edge between ",u, " and ",v
	return 0

if __name__ == "__main__" :
# Initialise the Tree dictionary to a particular range(default:1000)
    Tree = {}	
    for i in range(1000):
	Tree[i]= Node(i)


#Dict={1:'Link',2:'Cut',3:'Multi_Add_Element',4:'Reverse_Path',5:'Report_Min',6:'Is_Reachable'}
Dict={1:'Link',2:'Cut',3:'Is_Reachable'}
List=[1,2,3]
f=open('testcases.txt','w')
for i in range (1000):
    s=random.randint(1,10)
    t=random.randint(1,10)
    u=random.randint(1,1000)
    v=random.sample(List,1)
    w=v.pop(0)
    if w==2:
        if (Cut(s,t)==1):
    	    f.write('Cut'+'('+str(s)+','+str(t)+')')
            f.write('\n')
    elif w==3:
        f.write ('Is_Reachable'+'('+str(s)+','+str(t)+')')
        f.write('\n')
    else:
            if(Link(s,t,u)==1):    
                f.write('Link'+'('+str(s)+','+str(t)+','+str(u)+')')
                f.write('\n')
f.close()
