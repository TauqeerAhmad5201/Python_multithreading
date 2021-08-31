import multiprocessing


def square(numbers,array_):
    # global square_result 
    for index, i in enumerate(numbers): 
        array_[index] = i*i
    print('Inside Function Result :-',array_[:])


def cube(numbers):
    for i in numbers: 
        print("Cube : ",i*i*i)

if __name__ == "__main__":
    my_data = [5,5,3]

    #creating an array named array_ with data type integer and capacity = 3 
    array_ = multiprocessing.Array('i',3) #multiprocessing.Array('data type', data list capacity)
    t1 = multiprocessing.Process(target=square, args=(my_data,array_,))
    # t2 = multiprocessing.Process(target=cube, args=(my_data, ))
    t1.start()
    t1.join()

    print('Result = ',array_[:])
    print('Done')

