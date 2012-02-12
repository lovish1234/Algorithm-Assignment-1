class ExNode :
	def __init__(self,data):
		self.data=data
		self.external=1
		self.parent(None)
	def	height(self):
		return 0
	def parent(self,parent):
		self.parent=parent
	
class InNode :
	def __init__(self,left,right):
		self.left=left
		self.right=right
		self.external=0
		self.parent=None
		self.head=None
		self.tail=None
		left.parent=self
		right.parent=self
	def height(self):
		lheight=0
		if self.left :
			lheight=self.left.height()
		rheight=0
		if self.right :
			rheight=self.right.height()
		return 1 + max(lheight,rheight)
	def bfactor(self):
		lheight=0
		if self.left :
			lheight=self.left.height()
		rheight=0
		if self.right:
			rheight=self.right.height()	
		return (lheight - rheight)
	def rotate_left(self):
		pivot=self.right
		root=self

		self.right=self.right.left
		pivot.left.parent=root

		pivot.left=self
		nparent=root.parent
		root.parent=pivot

		pivot.parent=nparent
	def rotate_right(self):
		pivot=self.left
		root=self

		self.left=self.left.right
		pivot.right.parent=root

		pivot.right=self
		nparent=root.parent
		root.parent=pivot
	
		pivot.parent=nparent
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

def Merge (tree1,tree2):
	if( (tree1.height()-tree2.height()) < (2) and (tree1.height()-tree2.height()) > (-2)):
		dummy=InNode(tree2,tree1)
		tree2.parent=dummy
		tree1.parent=dummy
	elif( (tree1.height() - tree2.height()) <= (-2) ):
		it=tree2
		while not (it.height() == tree1.height() +1 or it.height() == tree1.height() ):
			it=it.right	
		itparent=it.parent	
		dummy=InNode(it,tree1)
		it.parent=dummy
		itparent.right=dummy		 
		dummy.parent=itparent
## Not balancing here ?
	else:
 		it = tree1	  
		while not (it.height() == tree2.height() +1 or it.height() == tree2.height() ):
			it=it.left
		itparent=it.parent	
		dummy=InNode(tree2,it)
		it.parent=dummy
		itparent.left=dummy
		dummy.parent=itparent
## Not balanced ?
		
if __name__ == "__main__" :	
#Two test trees and checking if they are getting merged 
#first tree.Rotation working correctly
	one=ExNode(1)
	two=ExNode(2)
	onei=InNode(one,two)
	three=ExNode(3)
	twoi=InNode(onei,three)
	twoi.balance()
	four=ExNode(4)
	threei=InNode(twoi,four)
	threei.balance()
#second tree.
	one1=ExNode(5)
	two1=ExNode(6)
	onei1=InNode(one1,two1)
	three1=ExNode(7)
	twoi1=InNode(onei1,three1)
	twoi1.balance()
	four1=ExNode(8)
	threei1=InNode(twoi1,four1)
	threei1.balance()
	Merge(threei,threei1)
#third tree.
	one2=ExNode(9)
	Merge(one2,threei1)

