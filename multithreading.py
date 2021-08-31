import time
import threading
arr = [5,6,3,4]

def square(numbers):
    for i in numbers:
        time.sleep(1)
        print('Square: ',i*i)

def cube(numbers):
    for i in numbers:
        time.sleep(1)
        print('Cube: ',i*i*i)

# square(arr)
# cube(arr)

t1 = threading.Thread(target=square, args=(arr,))  #since args is a tuple so we can't leave it with single argument
t2 = threading.Thread(target=cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print('I think process in done ! Right?')