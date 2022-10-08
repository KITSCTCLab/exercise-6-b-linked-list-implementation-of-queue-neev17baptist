class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, data) -> None:
    n=Node(data)
    if self.rear==None and self.front==None:
      self.rear=n
      self.front=n
    else:
      self.rear.next=n
      self.rear=n

  def dequeue(self) -> None:
    if self.rear==self.front:
      self.rear=None
      self.front=None
    else:
      self.front=self.front.next

  def status(self) -> None:
    if self.rear==None and self.front==None:
      print("None")
    else:
      t=self.front
      while(t!=None):
        print(t.data, end="=>")
        t=t.next
      print("None")

# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
