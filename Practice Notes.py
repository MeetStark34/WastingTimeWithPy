# Pattern Problems:
# > Square Star Pattern
# > Hollow Square Pattern
# > Right L Triangle Star Pattern
# > Right R Triangle Star Pattern
# > Inverted Right L Triangle Star Pattern
# > Inverted Right R Triangle Star Pattern
# > Diamond Star Pattern
# > Butterfly Pattern
# > Downward Triangle Star Pattern
# > Hollow Diamond Star Pattern
# > Cross Star Pattern
# > Hollow Pyramid Star Pattern


# > Square Star Pattern
def Square(n):
    print("\n\n1. Square Star Pattern\n")
    for i in range(n):
        print('* ' * n)

# > Hollow Square Pattern
def HollowSquare(n):
    print("\n\n2. Hollow Square Pattern:\n")
    for i in range(n):
        if i == 0 or i == n - 1:
            print('* ' * n)
        else:
            print('* ' + '  ' * (n - 2) + '*')

# > Hollow Pyramid Star Pattern
def XAndOBox(n):
    print("\n\n3. X & O Patterns:\n")    
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

# > Right L Triangle Star Pattern
def RightLTriangle(n):
    print("\n\n4. Right L Triangle Star Pattern:\n")
    for i in range(1, n+1):
        print('* ' * i)

# > Right R Triangle Star Pattern
def RightRTriangle(n):
    print("\n\n5. Right R Triangle Star Pattern:\n")
    for i in range(1, n+1):
        print('  ' * (n - i) + '* ' * i)

# > Inverted Right L Triangle Star Pattern
def InvertedRightL(n):
    print("\n\n6. Inverted Right L Triangle Star Pattern:\n")
    for i in range(n, 0, -1):
        print('* ' * i)

# > Inverted Right R Triangle Star Pattern
def InvertedRightR(n):
    print("\n\n7. Inverted Right R Triangle Star Pattern:\n")
    for i in range(n, 0, -1):
        print('  ' * (n - i) + '* ' * i)

# > Triangle Star Pattern
def StraightTriangle(n):
    print("\n\n8. Triangle Star Pattern:\n")
    for i in range(1, n+1):
        print(' ' * (n - i) + '* ' * i)

# > Hollow Triangle Pattern
def HollowStraightTriangle(n):
    print("\n\n9. Hollow Triangle Star Pattern:\n")
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# > Downward Triangle Star Pattern
def InvertedTriangle(n):
    print("\n\n10. Downward Triangle Star Pattern:\n")
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '* ' * i)

# > Inverted Hollow Triangle Pattern
def InvertedHollowTriangle(n):
    print("\n\n11. Inverted Hollow Triangle Star Pattern:\n")
    for i in range(n):
        for j in range(i):
            print(' ', end='')
        for j in range(2 * (n - i) - 1):
            if j == 0 or j == 2 * (n - i) - 2 or i == 0:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# > Diamond Star Pattern
def Diamond(n):
    print("\n\n12. Diamond Star Pattern:\n")
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

# > Hollow Diamond Star Pattern
def HollowDiamond(n):
    print("\n\n13. Hollow Diamond Star Pattern:\n")
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))

# > Butterfly Pattern
def Butterfly(n):
    print("\n\n14. Butterfly Pattern:\n")
    for i in range(1, n + 1):
        print('*' * i + ' ' * (2 * (n - i)) + '*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

# > Cross Star Pattern
def Cross(n):
    print("\n\n15. Cross Star Pattern:\n")
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# Directly call each pattern function with n = 9
n = 4
Square(n)
HollowSquare(n)
XAndOBox(n)
RightLTriangle(n)
RightRTriangle(n)
InvertedRightL(n)
InvertedRightR(n)
StraightTriangle(n)
HollowStraightTriangle(n)
InvertedTriangle(n)
InvertedHollowTriangle(n)
Diamond(n)
HollowDiamond(n)
Butterfly(n)
Cross(n)