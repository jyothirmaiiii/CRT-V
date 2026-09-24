    def count_nodes(self):
        if self.head is None:
            return 0
        if self.head.next is None:
            return 1
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
