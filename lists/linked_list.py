from .list_node import ListNode


class LinkedList(object):

    def __init__(self, initial_data=[]):
        if initial_data == []:
            self._head = None
            return

        self._head = ListNode(initial_data[0])

        current_node = self._head
        for data in initial_data[1:len(initial_data)]:
            new_node = ListNode(data)
            current_node.next_link = new_node

            current_node = new_node

    def print_values(self):
        values = []
        current_node = self.get_head()
        while current_node.next_link is not None:
            values.append(str(current_node.data))
            current_node = current_node.next_link
        values.append(str(current_node.data))

        return ','.join(values)

    def get_head(self):
        return self._head
