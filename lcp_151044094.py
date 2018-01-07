# Wrapper for longest common postfix finder, return common postfix string
def longest_common_postfix(inpStrings):
    return longest_common_postfix_finder(inpStrings,0,len(inpStrings)-1)

# Main function to solve longest common postfix string find. Returns common postfix string. To find common postfix
# we must firstly look left and right of strings' common postfixes recursively. And then we look for common postfixes
# of these. To look common postfixes of 2 string, we have to look strings from last characters until there is a not
# equality. Return this string as a result. Therefore we splitting our array of strings by 2, there will be logn
# complexity. And we are iterating most of lenght of common postfix string if we call it m, our complexity will be
# logn.m
def longest_common_postfix_finder(inpStrings,start,end):
    if start == end:                        # If there is left only one string
        return inpStrings[start]            # Return it

    middle = (start + end) // 2             # Find middle index
    # print (start,middle,end)
    left_common_string = longest_common_postfix_finder(inpStrings,start,middle) # Look for left common postfix string
    right_common_string = longest_common_postfix_finder(inpStrings,middle+1,end)# Look for right common postfix string
    # print(left_common_string,right_common_string)
    left_index = len(left_common_string)-1
    right_index = len(right_common_string)-1
    result_common = ''
    # Look for two strings equality until there is a inequality or our indexes will be out of range
    while (left_common_string[left_index] == right_common_string[right_index]) and left_index >= 0 and right_index >= 0:
        result_common += left_common_string[left_index]
        left_index -= 1
        right_index -= 1
    # print(result_common[::-1])
    return result_common[::-1]  # Return result

inpStrings =  ["absorptivity", "circularity", "electricity", "importunity", "humanity"]

lcp = longest_common_postfix(inpStrings)
print(lcp)
#Output: ity