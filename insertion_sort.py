random_numbers = [6, 3, 5, 8, 4, 2, 9, 1]
print(random_numbers)

def insertion(array:list):
    for i in range(1, len(random_numbers)):  # from index 1 to end
        current = random_numbers[i]  # save current pointer value
        j = i-1  # create a pointer at one step behind
        while(j>=0 and random_numbers[j]>current):  # while 0th index got checked  and  behind value is more than current value
            random_numbers[j+1] = random_numbers[j]  # moving behind values to front
            j-=1
        random_numbers[j+1] = current  # replace targeted value to first repetitive place

insertion(random_numbers)
print(random_numbers)
#MadMad_15