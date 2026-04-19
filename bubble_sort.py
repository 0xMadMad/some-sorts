random_numbers = [6, 3, 5, 8, 4, 2, 9, 1]
print(random_numbers)

def bubble(array:list):
    replaced = -1  # to enter at while at least once (we have not do-while here..)
    while(replaced != 0):  # while we have no replacement at one cycle
        replaced = 0  # reinitialize
        for i in range(len(array)-1):  # from index 0 to end-1
            if(array[i]>array[i+1]):  # if current is bigger than it nextone
                array[i], array[i+1] = array[i+1], array[i]  # replace it
                replaced += 1

bubble(random_numbers)
print(random_numbers)
#MadMad_15