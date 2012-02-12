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
			if self.left.balance() >0:
				self.rotate_right()
			else:
				self.rotate_left_right()
		elif value<=(-2):
			if self.right.balance() < 0:
				self.rotate_left()
			else:
				self.rotate_right_left()
		
if __name__ == "__main__" :	
	one=ExNode(1)
	two=ExNode(2)
	onei=InNode(one,two)
	three=ExNode(3)
	twoi=InNode(onei,three)
	twoi.balance()

