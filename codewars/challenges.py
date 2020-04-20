#####################################################################################################
# 1
# Create fibonacci sequence with n elements and ouptut it in a list. If n == 0 return empty list.
#  0 1 1 2 3 5 8 11 19 ...etc
# [0, 1, 1, 2, 3, 5,]

def fib_sequence(n):
    base = [0, 1]
    if n == 0:
        return []
    if n == 1: 
        return [base[0]]
    if n == 2:
        return base
    if n > 2:
        counter = 2
        while counter < n:
            print('looping')
            base.append(base[counter - 1] + base[counter - 2])
            print(counter)
            counter += 1
    return base

# print(fib_sequence(7))

#####################################################################################################
# 2
# Create a tribonacci sequence with n elements and ouptut it in a list. If n == 0 return empty list.
# 0 1 1 2 4 7 13 24 ...etc
# [0, 1, 1, 2, 4, 7, 13, 24,]

def trib_sequence(n):
    base = [0, 1, 1]
    if n == 0:
        return []
    if n == 1:
        return [base[0]]
    if n == 2:
        return [base[0], base[1]]
    if n == 3:
        return base
    if n > 3:
        counter = 3
        # only for first time!!!
        # base.append(base[0] + base[1] + base[2])
        # base.append(0 + 1 + 1)
        while counter < n:
            base.append(base[counter - 3] + base[counter - 2] + base[counter - 1])
            counter += 1

        return base

print(trib_sequence(4))




        