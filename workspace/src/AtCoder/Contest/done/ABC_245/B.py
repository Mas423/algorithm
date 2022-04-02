def binary_search(sorted_list, search_value):
    left_index = 0
    right_index= len(sorted_list) - 1
    while left_index <= right_index:
        middle_index= (left_index + right_index) // 2
        middle_value= sorted_list[middle_index]
 
        if search_value < middle_value:
            right_index = middle_index - 1
            continue
        if search_value > middle_value:
            left_index = middle_index + 1
            continue
 
        return True
