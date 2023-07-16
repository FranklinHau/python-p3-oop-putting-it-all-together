#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition=None):
        self.brand=brand
        self.size=size
        self.condition=condition
        

    def get_brand(self):
        return self._brand 
    def get_size(self):
        return self._size 
    def get_condition(self):
        return self._condition
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size=size 
        else:
            print('size must be an integer')
    
    def set_condition(self, condition):
        self._condition=condition

    def cobble(self):
        print('Your shoe is as good as new!')
        self._condition = 'New'
    
    size=property(get_size, set_size)
    condition=property(get_condition, set_condition)

shoe=Shoe('Addidas', 9)
shoe.cobble()
print(shoe.get_condition())
