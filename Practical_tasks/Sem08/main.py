def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        if b != 0:
            return a / b
        else:
            print('На ноль делить нельзя!')
    elif ch == '*':
        return a * b

def calc_level3(m):
    m2 = [m[0]]
    result = 0
    j = 1
    for i in range(1, len(m)):
        if m[i-1] == '*' or m[i-1] == '/':
            continue
        if m[i] == '*' or m[i] == '/':
            result = calc(int(m2[j-1]), int(m[i+1]), m[i])
            del m2[j-1]
            m2.append(result)
        else:
            m2.append(m[i])
            j += 1
    result = int(m2[0])
    for i in range(1, len(m2) - 1, 2):
        result = calc(result, int(m2[i + 1]), m2[i])
    return result

def calc_level4(string):
    x = string.split()
    y = []
    i = 0
    while i < len(x):
        if x[i] == '(':
            i+=1
            while x[i] != ')':
                y.append(x[i])
                del x[i-1]
            del x[i]
            z = " ".join(y)
            x[i-1] = calc_level3(y)
            y = []
        i+=1
    return x

def calculation(string):
    return calc_level3(calc_level4(string))

example = '20 - 4 * ( 2 + 6 ) / 2'  
    
print(f'{example} = {calculation(example)}')