from math import ceil
from typing import Any, Optional

class MyQueue:

    def __init__(self, initial_array:list = None) -> None:
        self.array = [] if initial_array is None else initial_array[:]

    def insert(self, element: Any):
        self.array.insert(0, element) 

    def pop(self):
        try:
            return self.array.pop()
        except Exception:
            return "Stop"

    def show(self, prefix: Optional[str] = ""):
        print(f"{prefix}{self.array}")

class MyArray:

    def __init__(self, initial_array:list = None) -> None:
        self.array = [] if initial_array is None else initial_array[:]

    def pop(self):
        self.array.pop()

    def insert(self, element: Any):
        self.array.append(element) 

    def get(self, index: int):
        return self.array[index]

    def show(self, prefix: Optional[str] = ""):
        print(f"{prefix}{self.array}")

    def invert_show(self, prefix: Optional[str] = ""):
        # Poderia retornar self.stack[::-1]
        size: int = len(self.array)
        inverted_array = []
        for i in range(size):
            inverted_array.append(self.array[size-1-i])

        print(f"{prefix}{inverted_array}")
    
    def binary_search(self, element: Any):
        """
        Supondo 
        """

        array_size = len(self.array)

        lower_index = 0
        upper_index = array_size - 1
        for _ in range(array_size):

            middle_index = int(ceil((upper_index + lower_index)/2))

            if self.array[middle_index] == element:
                return middle_index
            elif self.array[middle_index] > element:
                upper_index = middle_index - 1
            else:
                lower_index = middle_index

        return None

    def find_mode(self):
        dicio = {}

        for elem in self.array:
            if elem in dicio:
                dicio[elem] += 1
            else: 
                dicio[elem] = 1

        map_list = [(key, value) for key, value in dicio.items()]

        max_key, max_value = map_list[0]

        for key, value in map_list:
            if value > max_value:
                max_key = key
                max_value = value
            
        return max_key, max_value

class MyStack:

    def __init__(self, initial_stack:list = None) -> None:
        self.stack = [] if initial_stack is None else initial_stack[:]

    def pop(self):
        try:
            return self.stack.pop()
        except Exception:
            return "Stop"

    def insert(self, element: Any):
        self.stack.append(element) 

    def show(self, prefix: Optional[str] = ""):
        print(f"{prefix}{self.stack}")


if __name__ == "__main__":
    array = MyArray([1,2,3,4,5,6,7,8,9,10])

    resp = array.binary_search(10)
    print(array.get(resp), resp)