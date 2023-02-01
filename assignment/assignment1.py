

def q2(): # print hello world
    print("Hello World")
    
def q3(): # multiplication table
    print('    ', end='')
    for i in range(1, 13):
        print(i, end='   ' if i<10 else '  ')
    print()
    for i in range(1, 13):
        print(i, end='   ' if i<10 else '  ')
        for j in range(1, 13):
            if i*j < 10:
                print(i*j, end='   ')
            elif i*j < 100:
                print(i*j, end='  ')
            else:
                print(i*j, end=' ')
        print()
        
def q4(s):  # determine if it's palindrom
    if len(s)<2:
        return True
    left, right = 0, len(s)-1
    while left<right:
        if s[left] != s[right]:
            return False
        left, right = left+1, right-1
    return True

print("123321", "12321", "123322")
print(q4("123321"), q4("12321"), q4("123322"))
# True True False

def q5(l1, l2): # merge
    res = []
    for i in range(len(l1)):
        res += [l1[i], l2[i]]
    return res

print("First", ['a', 'b', 'c'])
print("Second", [1,2,3])
print("Merge", q5(['a', 'b', 'c'], [1,2,3]))

def q6(): # fibonacci sequence
    fib = {i:-1 for i in range(1, 101)}
    fib[1], fib[2] =1, 1
    for i in range(3, 101):
        fib[i] = fib[i-1]+fib[i-2]
    return fib

def q7(year): # determine if it's leap year
    if year%100 == 0:
        if year%400 == 0:
            return True
        else:
            return False
    else:
        if year%4 == 0:
            return True
        else:
            return False

print("Year 1900", q7(1900))
print("Year 2000", q7(2000))
print("Year 2003", q7(2003))
print("Year 2004", q7(2004))
    


