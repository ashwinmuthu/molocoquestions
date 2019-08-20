def equalsWhenOneCharRemoved(x, y):
    if len(x) == len(y):
        return False

    sizex = len(x)
    sizey = len(y)
    if abs(sizey - sizex) > 1:
        return False

    chosen_word = None
    compare_word = None
    if sizex > sizey:
        chosen_word = x
        compare_word = y
    else:
        chosen_word = y
        compare_word = x

    i = j = 0
    num_mismatches = 0
    while i < len(chosen_word) and j < len(compare_word):
        char1 = chosen_word[i]
        char2 = compare_word[j]

        if char1 == char2:
            i += 1
            j += 1
            continue

        elif char1 != char2:
            if num_mismatches > 0:
                return False
            i += 1
            num_mismatches += 1
            continue
            
    return True