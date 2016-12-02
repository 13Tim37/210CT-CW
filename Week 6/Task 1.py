class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 
 
def in_order(tree):
    
    stack = []
    done = False

    while not done:
        if tree != None:
            # Check current node is not null, switch to that node's left node until it is null.
            stack.append(tree)
            tree = tree.left
        elif len(stack) > 0:
            # If left node is null we remove centre node from the stack and print it and do the same with the right node.
            tree = stack.pop()
            print(tree.value)
            tree = tree.right
        else:
            # If we have removed all items from our stack we are done.
            done = True
            
        
def count_children(tree):
    count = 0
    if tree.left!=None:
        count = count + 1
    if tree.right!=None:
        count = count + 1
    return count

def tree_sort(a):
    t = tree_insert(None, a[0])
    for item in a[1:]:
        tree_insert(t,item)
    in_order(t)
    
 
if __name__ == '__main__':
   
  t=tree_insert(None,10);
  tree_insert(t,8)
  tree_insert(t,14)
  tree_insert(t,5)
  tree_insert(t,9)
  tree_insert(t,12)
  tree_insert(t,12)
  tree_insert(t,13)
  tree_insert(t,17)
  in_order(t)

  def init():
      try:
          int_list = list(map(int, input("Enter a list of integers seperated by ',': ").split(',')))
      except ValueError or SyntaxError:
          print('Only enter a list of integers!')
          int_list = init()
      return int_list

  int_list = init()

  print('----')
  tree_sort(int_list)
