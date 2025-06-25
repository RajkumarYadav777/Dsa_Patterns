def reverse_only_letters(s):
    ls = list(s)

    left = 0
    right = len(ls) - 1

    while left < right:
        if ls[left].isapha() and ls[right].isalpha():
            ls[left], ls[right] = ls[right], ls[left]
            left += 1
            right -= 1
        
        elif not ls[left].isalpha():
            left += 1
        elif not ls[right].isalpha():
            right -= 1
    return ''.join(ls)

# BRUTE FORCE

# simulate stack and if ch == ch pop from stack and push it result 
# if no ch just push it result


def revers_only_letters_brute(s):
    letters = [ch for ch in s if ch.isalpha()]
    result = []

    for ch in s:
        if ch.isalpha():
            result.append(letters.pop())
        else:
            result.append(ch)
    return ''.join(result)
