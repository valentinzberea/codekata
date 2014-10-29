class InsertionSort(object):

    def sort(self, array):
        if len(array) <= 1:
            return array

        for i in range(1, len(array)):
            aux = array[i]
            for j in reversed(range(0, i)):
                if aux > array[j]:
                    array[j+1] = aux
                    break
                else:
                    array[j+1] = array[j]
                    array[j] = aux

        return array
