#1
# class PrintSpooling:
#     def __init__(self):
#         self.print_queue = []

#     def addPrintJObs(self, job):
#         self.print_queue.append(job)
#         print(f"print job {job} added to the queue")

#     def printThePrintJobs(self):
#         while self.print_queue:
#             job = self.print_queue.pop(0)
#             print(f"Printing: {job}")
#             print(f"Print JOb {job} complted")

# p = PrintSpooling()

# p.addPrintJObs("resume.txt")
# p.addPrintJObs("nature.jpg")
# p.addPrintJObs("report.txt")
# p.addPrintJObs("data.csv")

# print("printing The Print Jobs: ")
# p.printThePrintJobs()


#2
# class Queue:
#     def __init__(self,size):
#         self.queue = []
#         self.size = size

#     def ifEmpty(self):
#         return len(self.queue) == 0
    
#     def isFull(self):
#         return len(self.queue) == self.size
    
#     def enqueue(self,item):
#         if self.isFull():
#             return("Queue is full, please delete some items to add item")
#         else:
#             self.queue.append(item)

#     def dequeue(self):
#         if self.ifEmpty():
#             return("Queue is empty, add some to delete")
#         else:
#             self.queue.pop(0)

#     def peek(self):
#         if self.ifEmpty():
#             return("Queue is empty, add some to peek")
#         else:
#             print(self.queue[0])
    
#     def displayQueue(self):
#         print(self.queue)   
# q = Queue(5)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(4)
# q.peek()
# q.displayQueue()
# q.dequeue()
# q.enqueue(2)
# q.dequeue()
# q.enqueue(4)
# q.peek()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(4)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(4)
# print(q.isFull())
# print(q.ifEmpty())
# q.displayQueue()