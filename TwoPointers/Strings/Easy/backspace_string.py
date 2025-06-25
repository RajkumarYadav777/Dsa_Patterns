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



# TWO POINTERS
