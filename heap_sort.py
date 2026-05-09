random_numbers = [6, 3, 5, 8, 4, 2, 9, 1, 5]  
# consider array as a compelete binary tree, so we can use it as a heap-tree :
    # so parent of "i" is "(i//2)-1", left child of "i" is "(2*i)+1", right child of "i" is "(2*i)+2"
print(random_numbers)

def heap(array:list):
    sorted_part = len(array)
    while(sorted_part>0):  # while we have more than 0 element in sorted part (we can not sort 0 element :D)
        parent = (sorted_part//2)-1  # last parent index
        child = sorted_part-1  # last child index

        if(len(array)%2==0):
            if(array[parent]<array[child]):
                array[parent], array[child] = array[child], array[parent]
            parent-=1; child-=1

        while(parent>=0):
            for _ in range(2):  # for left and right child
                if(array[parent]<array[child]):
                    array[parent], array[child] = array[child], array[parent]
                child-=1
            parent-=1
        array[0], array[sorted_part-1] = array[sorted_part-1], array[0]  # replace max with last element
        sorted_part-=1  # decrease sorted part

heap(random_numbers)
print(random_numbers)
#MadMad_28