random_numbers = [6, 3, 5, 8, 4, 2, 9, 1, 5]
print(random_numbers)

def quick(array:list):
    pivot = array[len(array)-1]  # a random item:  first=array[0], last=array[len(array)-1], mid=array[len(array)//2], random=random.choice(array)
    green=0  # i
    orange=-1  # j
    # orange & green because of visualization-video that i watched =)

    while(green<(len(array)-1)):
        if(array[green]<pivot):
            orange+=1
            array[orange], array[green] = array[green], array[orange]
        green+=1
    orange+=1
    array[orange], array[len(array)-1] = array[len(array)-1], array[orange]
    # orange is pivot index now

    if(len(array[:orange])>1):
        print(f"[:o] {array[:orange]}")
        array[:orange] = quick(array[:orange])

    if(len(array[orange+1:])>1):
        print(f"[o+1:] {array[orange+1:]}")
        array[orange+1:] = quick(array[orange+1:])
    
    return array

quick(random_numbers)
print(random_numbers)
#MadMad_31