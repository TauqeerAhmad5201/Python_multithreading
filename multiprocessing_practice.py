import multiprocessing

arr = [5,7.4,6.07,4,7.89,0.001]

def square(numbers):
    for i in numbers: 
        print('Square : ',i*i)

def cube(numbers):
    for i in numbers: 
        print('Cube : ',i*i*i)

# square(arr)
# cube(arr)

if __name__=='__main__':
    t1 = multiprocessing.Process(target=square, args=(arr,))
    t2 = multiprocessing.Process(target=cube, args=(arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('I hope so that your job has been done. :)')

  
