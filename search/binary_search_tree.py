class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
      pass


    def breadth_first_for_each(self, cb):
      # Initialize the queue
      queue = [self]
      # while loop as long as there is a length to the queue
      while len(queue):
        # Remove and save first element
        current = queue.pop(0)
        print(current.value)
        # if node has a left, add to queue
        if current.left:
          queue.append(current.left)
        # if node has a right, add to queue.
        if current.right:
          queue.append(current.right)
        # run the function on current.
        cb(current.value)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value


