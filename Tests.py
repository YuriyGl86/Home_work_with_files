class StackObj:

    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new):
        self.__data = new

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new):
        self.__next = new


class Stack:

    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            temp = self.top
            while temp.next:
                temp = temp.next
            temp.next = obj

    def pop_back(self):
        temp = self.top
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def __add__(self, other):
        self.push_back(StackObj(other))
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self

st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st += 5
st *= [3,7,8]
# st.push_back(StackObj('3'))
print(st.top.next.next.next.next.next.data)





