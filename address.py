class Address:
    def __init__(self, left, right, count=1):
        self.left = left
        self.right = right
        self.count = count

    def __str__(self):
        return "left:{},right:{},count:{}".format(self.left, self.right, self.count)

    def add_count(self, n):
        self.count += n

    def is_adjacent(self, address_b):
        if self.left >= address_b.right or self.right <= address_b.left:
            return False
        return True

    def merge_address(self, address_b):
        self.left = min(self.left, address_b.left)
        self.right = max(self.right, address_b.right)
        self.count = self.count + address_b.count
