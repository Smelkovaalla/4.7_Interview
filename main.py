class Stack:
  def __init__(self):
    self.stack = [] 

  def isEmpty(self):
    if len(self.stack) == 0:
      return 'True'
    else:
      return 'False'

  def push(self, new_element):
    self.stack.insert(0, new_element)

  def pop(self):
    self.stack.pop(0)
    return self.stack[0]

  def peek(self):
    return self.stack[0]

  def size(self):
    return len(self.stack)


example = Stack()

print(example.stack)
print(example.isEmpty())
print('----' * 9)
example.stack.append(1)
example.stack.append('jiksjd')
example.stack.append('54fddf')
print(example.stack)
print(example.isEmpty())
print('----' * 9)

example.push(123)
print(example.stack)
print('----' * 9)
print(example.pop())
print(example.stack)
print('----' * 9)
print(example.peek())
print(example.stack)
print('----' * 9)
print(example.size())
print(example.stack)