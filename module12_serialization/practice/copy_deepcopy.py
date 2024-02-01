from copy import copy, deepcopy

original_list = [1,[2, 3], [4, 5]]

# Using copy

shallow_copy_list = copy(original_list)
shallow_copy_list[1][0] = 'X' # changes copy
shallow_copy_list.append(3) # should not change copy
print(original_list)

print(shallow_copy_list == original_list)
# Using deepcopy

deepcopy_list = deepcopy(original_list)
deepcopy_list[1][0] = 'Y' # should not change copy
print(original_list)