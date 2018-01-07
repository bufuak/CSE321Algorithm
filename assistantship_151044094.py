
# This function finds all permutations of given list This functions work time is O(n!)
#
def permutation_recur(given_list, permutations):
    if len(given_list) == 1:                                        # If given list's size is 1
        permutations.append(given_list)                             # Put it to permutations list's end
    else:                                                           # Else
        for i in range(0, len(given_list)):                         # iterate given list
            element = given_list[i]                                 # take element from given list
            copy_given_list = []                                    # create a new copy list
            for j in range(0, len(given_list)):                     # append elements except given_list[i] to copy list
                if j != i:
                    copy_given_list.append(given_list[j])
            subpermutations = []
            permutation_recur(copy_given_list, subpermutations)     # take these elements permutations
            for subpermutation in subpermutations:                  # iterate these permutations
                result = [element] + subpermutation                 # combine with our first chosen element
                permutations.append(result)                         # insert it to permutations list's end



# This functions is just a wrapper for permutation_recur. Also work time is O(n!)
def permutation_finder(given_list):
    permutations = []
    permutation_recur(given_list, permutations)
    return list(permutations)


# This function handles the situation when course number is less than assistants
# Creating indexes list from course numbers and filling -1 until course number and assistant number is equal
# Also work time is O(n!)
def gettingPermutations(inputTable):
    indexes = list(range(len(inputTable[0])))   # Ex' 0 1 2
    while len(indexes) < len(inputTable):
        indexes.append(-1)                      # Ex -1 -1 0 1 2
    permutations = permutation_finder(indexes)  # Find all permutations of this list
    return permutations


# This function's work time is O(n!*n)
def assistantship_problem_solver(inputTable):
    permutations = gettingPermutations(inputTable)  # Getting all the permutations
    min_hours = 169                                 # One week has 168 hours :)
    min_hours_assistants = permutations[0]          # Default result of return value
    for permutation in permutations:                # Looking for one possible result at a time , iterating n! times
        permutation_hours = 0
        index = 0
        for hour in permutation:                    # Traversing result which ex. { -1 2 0 1} , iterating n times
            if hour == -1:                          # if hour is -1 : this assistant spend 6 hours
                permutation_hours += 6
            else:                                   # else spends inputTable[index][hour]
                permutation_hours += inputTable[index][hour]
            index += 1

        if min_hours > permutation_hours:           # if permutation_hours is less than min_hours
            min_hours = permutation_hours           # Result of min_hours will be this permutations_hours
            min_hours_assistants = permutation      # Result of assistants will be this permutation

    return min_hours_assistants, min_hours


def assistantship_problem_solver_tester():
    matrix = [[65, 51, 33, 44], [61, 61, 76, 17],[14, 98, 65, 2], [9, 28, 61, 68]]

    assistants,min_hour = assistantship_problem_solver(matrix)
    print(assistants)
    print(min_hour)   # goo.gl/yvpbvD You can check result in hungarianalgorithm.com


assistantship_problem_solver_tester()






