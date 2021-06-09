def binary_search(sorted_list, num):
    low = 0
    high = len(sorted_list) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if sorted_list[mid] < num:
            low = mid + 1

        elif sorted_list[mid] > num:
            high = mid - 1

        else:
            return mid

    return None
