# The following file shows all the list functions and the use

mylist = ['9', '2', '15', '48', '1', '9']

# performing the following functions on the example list

"""Methods for a list are
    append
    insert
    extend
    remove
    pop
    clear
    index
    count
    sort
    reverse
    copy"""

mylist.append('64')
print(mylist)

mylist.insert(0, '100')
print(mylist)

mylist.remove('100')
print(mylist)

mylist.pop(5)
print(mylist)

print(mylist.index('9'))

print(mylist.count('9'))

"""Using list as stack (Last-in,first-out)  PUSH/POP"""

print("------------------------------------------------")

stack = ['1','2', '3', '4']

print("inital stack")
print(stack)

stack.append('5')
stack.append('6')
stack.append('8')

print("Pushed elements with the initial stack is ")
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print("stack after poping 3 items")
print(stack)

"""Using list as Queues (First-in,First-out) ENQUEUE/DEQUEUE"""

print("------------------------------------------------")
my_queue = []

my_queue.append('Apple')
print(my_queue)

my_queue.append('Banana')
print(my_queue)

my_queue.append('Orange')
print(my_queue)


my_queue.pop(0)
print(my_queue)

my_queue.pop(0)
print(my_queue)

my_queue.pop(0)
print(my_queue)

joining two list using extend() method

my_list1 = ['1', '2', '3']
my_list2 = ['Apple', 'Banana', 'Mango']

my_list1.extend(my_list2)
print(my_list1)
