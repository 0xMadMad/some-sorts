random_numbers = [6, 3, 5, 8, 4, 2, 9, 1, 5]
print(random_numbers)

def slice_to_merge(left:list, right:list):
    l=r=0; tmp_array=[] 
    while(l<len(left) and r<len(right)):  # check pointers
        if(left[l]<=right[r]):  # compare value of pointers
            tmp_array.append(left[l])  # add value to result array
            l+=1  # moving pointer forward
        elif(right[r]<left[l]):  # compare value of pointers
            tmp_array.append(right[r])  # add value to result array
            r+=1  # moving pointer forward
    return tmp_array + left[l:] + right[r:]  # result array plus remains

def merge(array:list):
    if(len(array) == 1):  # it is alone </3
        return array
    
    middle_point = len(array)//2  # middle of array
    left_side = merge(array[:middle_point])  # make array lonelier </3
    right_side = merge(array[middle_point:])  # make array lonelier </3
    
    return slice_to_merge(left_side, right_side)  # merge loneliers <3

print(merge(random_numbers))
#MadMad_26