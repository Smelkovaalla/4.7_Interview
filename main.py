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

test = '[([])((([[[]]])))]{()}'
skobki = [*test]
# print(skobki)
len_skobki = len(skobki)


if len_skobki % 2 == 0:
  print('Четное число')
  a = len_skobki - 1
  while a >= 0:
    example.push(skobki[a])
    a = a - 1
  a = 0
  b = example.size() / 2
  skoba = example.peek()
  print(example.stack)   
  while a < b:
    skoba = example.peek()   
    if example.isEmpty() == 'False':        
      example.pop()
    # print(skoba)
    # print(example.stack)    
    if skoba == '(':
      if ')' in example.stack:
        example.stack.remove(')')
      else:
        print("Несбалансированно")
        break      
    elif skoba == '[':
      if ']' in example.stack:
        example.stack.remove(']')
      else:
        print("Несбалансированно")
        break
    elif skoba == '{':
      if '}' in example.stack:
        example.stack.remove('}')
      else:
        print("Несбалансированно")
        break      
    # print(example.stack)     
    a = a + 1
else:
  print("Несбалансированно")


if example.isEmpty() == 'True':   
  print("Сбалансировано")     


# example.stack.append(test)
# print(example.stack())
# example.stack() = [*'(((([{}]))))']
# print(example.stack())
# if len()

# print(example.stack)
# print(example.isEmpty())
# print('----' * 9)
# example.stack.append(1)
# example.stack.append('jiksjd')
# example.stack.append('54fddf')
# print(example.stack)
# print(example.isEmpty())
# print('----' * 9)

# example.push(123)
# print(example.stack)
# print('----' * 9)
# print(example.pop())
# print(example.stack)
# print('----' * 9)
# print(example.peek())
# print(example.stack)
# print('----' * 9)
# print(example.size())
# print(example.stack)