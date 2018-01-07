# Wrapper function for minimum sub array, returns only subarray
def min_subarray_finder(inpArr):
    sum,first_index,second_index = minimum_subarray(inpArr,0,len(inpArr)-1)
    return inpArr[first_index:second_index+1]

# Main function to solve minimum subarray problem. Returns minimum sub,first index of it,last index of it
# To find minimum sum subarray, first we have to look from middle to left and right side, to reach minimum sum
# from middle. Then we have to calculate left side and right side separately recursively. If middle combined minimum
# is less than left or right seperate result our minimum sub, here its our minimum sub, or we have to compare
# left and right seperate sums and return the minimum sum. I am tracking indexes to return minimum subarray rather than
# minimum sum for wrapper funtion. Therefore we are splitting the array/2 every time, this comes with logn complexity,
# and we also traversing array in all repeatition, this comes with n complexity. Therefore our worst case will be n.logn
def minimum_subarray(array,start,end):
    if start == end:                                # if array has one element return that
        return array[start],start,end
    middle = (start+end) // 2                       # else calculate middle element
    min_index_left = middle                         # combined results indexes
    max_index_right = middle+1
    # print(start,middle, end,array[start:end+1])
    min_left = 9999999999999999
    min_right = 9999999999999999
    summation_left = 0
    summation_right = 0
    # looking for left-right combined minimum sum
    for left_index,right_index in zip(range(middle,start-1,-1),range(middle+1,end+1)):
        # print(left_index,right_index)
        summation_left += array[left_index]
        summation_right += array[right_index]
        if summation_left < min_left:
            min_left = summation_left
            min_index_left = left_index
        if summation_right < min_right:
            min_right = summation_right
            max_index_right = right_index

    minimum_combined = min_left+min_right
    # print("Min combined:", minimum_combined)

    min_sub_left,index_left_first,index_left_second = minimum_subarray(array,start,middle)  # getting seperate min sums
    min_sub_right,index_right_first,index_right_second = minimum_subarray(array,middle+1,end)

    minimum_seperate = min_sub_right                # if right seperate sum is lesser
    result_first_index = index_right_first
    result_second_index = index_right_second

    if min_sub_left < min_sub_right:                # if left seperate sum is lesser
        minimum_seperate = min_sub_left
        result_first_index = index_left_first
        result_second_index = index_left_second

    return_minimum = minimum_combined             # if combined sum is lesser
    return_index_first = min_index_left
    return_index_second = max_index_right

    if minimum_seperate < minimum_combined:       # if seperate sum is lesser
        return_minimum = minimum_seperate
        return_index_first = result_first_index
        return_index_second = result_second_index
    return return_minimum,return_index_first,return_index_second    # return


inpArr = [1, -4, -7, 5, -13, 9, 23, -1]
msa = min_subarray_finder(inpArr)
print(msa)
# Output: [-4, -7, 5, -13]
print(sum(msa))