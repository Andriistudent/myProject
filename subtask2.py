def seq_op (set_x):
    if len(set_x)==0:
        print("Empty set!")
        n = 0
        m = -1
        a = -1
        print(n, m, a)
    elif set_x[-1] != -1 or (len(set_x)==1 and set_x[0]==-1):
        print("Sequence isn't defined!")
    else:
        set_x.remove(-1)
        n = len(set_x)
        s = sum(set_x)
        m = min(set_x)
        a = s/n
        print(n, s, m, a)

seq_op ([3, 4, 0, 2, 1, 8, -1])
seq_op ([12, 3, 3])
seq_op ([-1])
seq_op ([])

# it looks like I learned how to use git today