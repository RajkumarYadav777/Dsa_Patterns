
# TWO POINTERS
# we simulate stack kind approach and whn found item we reuce the count and 
# start comparing until end of the loop
# key step is assign s[j] = s[i]


# in-place
def remove_adj_dups_tp(s):
    ls = list(s)
    j = 0

    for i in range(len(ls)):
        ls[j] = ls[i]

        # check condition and j must > 0

        if j > 0 and ls[j] == ls[j-1]:
            j -= 1
        else:
            j += 1
    return ''.join(ls[:j])  # 0 to j-1
print(remove_adj_dups_tp('abbaca'))



# using real stack which is 0(n)
# push items to stack and compare it with top element
# if same pop it from stack 

def remove_adjs_dups_stack(s):
    ls = list(s)
    stack = []

    for ch in ls:
        # stack should not empty
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            # just append to stack
            stack.append(ch)
    return ''.join(stack)
print(remove_adjs_dups_stack('abbaca'))
