class LinkedList(object):

    def __init__(self, initial_data=[]):
        if initial_data == []:
            self._head = None
            return

        self._head = {'data': initial_data[0], 'next': None}

        current_node = self._head
        for data in initial_data[1:len(initial_data)]:
            new_node = {'data': data, 'next': None}
            current_node['next'] = new_node

            current_node = new_node

    def print_values(self):
        values = []
        current_node = self.get_head()
        while current_node['next'] is not None:
            values.append(str(current_node['data']))
            current_node = current_node['next']
        values.append(str(current_node['data']))

        return ','.join(values)

    def get_head(self):
        return self._head
