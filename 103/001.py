A = []
B = []
while 1:
    mov = int(input())
    if mov == 0:
        break
    elif mov == 1:
        A = []
        print('A:%s B:%s' % (A, B))
    elif mov == 2:
        B = []
        print('A:%s B:%s' % (A, B))
    elif mov == 3:
        insert = int(input())
        A.append(insert)
        print('A:%s B:%s' % (A, B))
    elif mov == 4:
        insert = int(input())
        B.append(insert)
        print('A:%s B:%s' % (A, B))
    elif mov == 5:
        remove = int(input())
        if remove in A:
            A.remove(remove)
        print('A:%s B:%s' % (A, B))
    elif mov == 6:
        remove = int(input())
        if remove in B:
            B.remove(remove)
        print('A:%s B:%s' % (A, B))
    elif mov == 7:
        print(sorted(list(set().union(A, B))))
    elif mov == 8:
        print(list(set(A).intersection(B)))
    elif mov == 9:
        print(0 if ''.join(map(str, B)) in ''.join(map(str, A)) else 1)
