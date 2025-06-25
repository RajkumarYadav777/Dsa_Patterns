# BRUTE FORCE
# here two strings are given s and t havin # in it 
# so when we click backspace on keyboard one letter will remove 
# by simulating that we compare two stings at the end both are equal or not
# s = ab#c t = ab#c
# Only call .pop() if the stack is not empty
# So no crash if the input starts with '#' or has multiple '#'s in a row

def backspace_stirng_brute(s, t):
    ls = list(s)
    s_stack = []
    for ch in s:
        if s_stack and ch == '#':
            
            s_stack.pop()
            
        else:
            
            s_stack.append(ch)
    t_stack = []

    for ch in t:
        if t_stack and ch == '#':
            t_stack.pop()
        else:
            t_stack.append(ch)
    
    # return True if ''.join(s_stack) == ''.join(t_stack) else False
    return s_stack == t_stack



#  TWO POIINTERS

# we use two pointers rom right
# and use seperate loop to find backspace and removing chars by 
# by reducing backspace count when it exceeds 0
# if backspace ==0 and ch != # we will break means we found alid one 


def backspace_string_tp(s,t):
    p1 = len(s)-1
    p2 = len(t)-1

    while p1 >= 0 and p2 >= 0:
        # for s
        backspace_s = 0

        while p1 >= 0:
            if s[p1] == '#':
                backspace_s += 1
                p1 -= 1
            elif backspace_s > 0:
                backspace_s -= 1  # simulating the removing item
                p1 -= 1
            else:
                break   # we found valid one that is not equal to # and backspace=0
        
        # same for t
        backspace_t = 0

        while p2 >= 0:
            if t[p2] == '#':
                backspace_t += 1
                p2 -= 1
            elif backspace_t > 0:
                backspace_t -= 1
                p2 -= 1
            else:
                break
    
    # we now compare current valid ones

    if p1 >= 0 and p2 >= 0:  # both are valid pointers i.e it goes to left so no negatives
        if s[p1] != [p2]:
            return False
    elif p1 >=0 or p2 >= 0: # if only one pointer is still valid
        return False  # one string finished early
    
    p1 -= 1
    p2 -= 1
    return True

'''
while p1 >= 0 or p2 >= 0:

    # Step 1: Move p1 to next valid character (skip # and deleted chars)
    # Step 2: Move p2 to next valid character

    # Step 3: Now compare current characters at p1 and p2 move pointers


'''