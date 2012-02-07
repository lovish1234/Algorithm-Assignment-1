#Class Node having the essential functions 
class Node :
	def _init_(self,data):
		self.data=data
		self.child(self,None,None)
	def child(self,leftchild,rightchild):
		self.left=leftchild
		self.right=rightchild
	def bfactor(self):
		if self.left:
			lheight=self.left.height()
		if self.right:
			rheight=self.right.height()	
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
	def balance(self):
		value=self.bfactor()
		if value >= 2:
			if self.left.balance() >0:
				self.rotate_right()
			else:
				self.rotate_left_right()
		elif value<=(-2):
			if self.right.balance() > 0:
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
  
	def inorder(self):
		inorder(self.left)
		print self.data
		inorder(self.right) 		


				
			







			



		
			
		
 		 

