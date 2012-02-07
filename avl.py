#Class Node having the essential functions 
class Node :
	def __init__(self,data):
		self.data=data
		self.child(None,None)
	def child(self,leftchild,rightchild):
		self.left=leftchild
		self.right=rightchild
	def bfactor(self):
		lheight=0
		if self.left:
			lheight=self.left.height()
		rheight=0
		if self.right:
			rheight=self.right.height()
#		print lheight
#		print rheight	
		return (lheight - rheight)
	def height(self):
		lheight=0
		if self.left :
			lheight=self.left.height()
		rheight=0
		if self.right :
			rheight=self.right.height()
		return 1 + max(lheight,rheight)
#See wikipedia for "Tree Rotation" for better understanding of the below rotate_ functions	
	def rotate_left(self):
		temp=self.data
		self.data = self.right.data
		self.right.data=temp
		temp1=self.left
		self.child(self.right,self.right.right)
		self.left.child(temp1,self.left.left)
	def rotate_right(self):
		temp=self.data
		self.data=self.left.data
		self.left.data=self.data
		temp1=self.right
		self.child(self.left.left,self.left)
		self.right.child(self.right.right,temp1)
	def rotate_left_right(self):
 		self.left.rotate_left()
		self.rotate_right()
	def rotate_right_left(self):
 		self.right.rotate_right()
		self.rotate_left()	
# Balancing the tree using above set of rotations		 
	def balance(self):
		value=self.bfactor()
#		print value
		if value >= 2:
			if self.left.balance() >0:
				self.rotate_right()
			else:
				self.rotate_left_right()
		elif value<=(-2):
			if self.right.balance() < 0:
				self.rotate_left()
			else:
				self.rotate_right_left()

#Essential operations in an avl tree ie Insert,Delete and Search

	def Insert(self,data):
		if data <= self.data:
			if not self.left:
				self.left =  Node(data)
			else:
				self.left.Insert(data)
		else:
			if not self.right :
				self.right = Node(data)
			else:
				self.right.Insert(data)
		self.balance()
  	
	def Search(self,data):
		if data==self.data:
			print "Yes it exists"
		elif data<=self.data and not self.left==None:
			self.left.Search(data)
		elif data > self.data and not self.right==None:
			self.right.Search(data)
		else:
			print "It does not exist"

	def inorder(self):
#		print  str(self.data)
		if self.left:
			self.left.inorder()
		print  str(self.data)
		if self.right:
			self.right.inorder()	


#def Delete(self,datum):
#		if self.data==datum:
#Remove this node
#		elif self.data<=datum:
#			self.left.Delete(datum)
#		elif self.data>datum:
#			self.right.Delete(datum)
			
			
				
if __name__ == "__main__" :	
	tree = Node(14)
	tree.Insert(22)
	tree.Insert(27)
	tree.Insert(30)
	tree.Insert(33)
	tree.Insert(34)
	tree.Insert(35)
	tree.Insert(36)
	tree.Insert(40)
	tree.Insert(42)
	tree.Insert(55)
	tree.Insert(58)
	tree.Search(41)
	tree.Search(40)
	tree.inorder()
		


				
			







			



		
			
		
 		 

