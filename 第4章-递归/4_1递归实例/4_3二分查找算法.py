def binary_search(data, target, low, height):
    """
    Return True if target is found in indicated portion of a Python list

    The search only considers the portion from data[low] to data[high] inclusive
    """
    if low > height:
        return False                   # interval is empty: not match
    else:
        mid = (low + height) // 2
        if target == mid:              # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, height)


if __name__ == '__main__':
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 9
    res = binary_search(data, target, 0, 9)
    print(res)
