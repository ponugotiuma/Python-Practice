#PATTERNS
##1,Palindrome Number Pyramid
'''def p18_number_pyramid(n=5):
    for i in range(1, n + 1):
        left = "".join(str(x) for x in range(1, i + 1))
        right = "".join(str(x) for x in range(i - 1, 0, -1))
        print(" " * (n - i) + left + right)
p18_number_pyramid()'''

##2,Pascal's Triangle
'''def p19_pascals_triangle(n=5):
    for i in range(n):
        num = 1
        print(" " * (n - i), end="")

        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)

        print()
p19_pascals_triangle()'''

##3,Binary (0–1) Triangle
'''def p20_binary_triangle(n=5):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print((i + j + 1) % 2, end=" ")
        print()
p20_binary_triangle()'''

##4,Alphabet Triangle
'''def p21_alphabet_triangle(n=5):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()
p21_alphabet_triangle()'''

##5,Alphabet Pyramid
'''def p22_alphabet_pyramid(n=5):
    for i in range(1, n + 1):
        left = "".join(chr(64 + x) for x in range(1, i + 1))
        right = "".join(chr(64 + x) for x in range(i - 1, 0, -1))
        print(" " * (n - i) + left + right)
p22_alphabet_pyramid()'''

##6,Butterfly Pattern
'''def p23_butterfly(n=5):
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

    for i in range(n, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
p23_butterfly()'''

##7,Cross (X) Pattern
'''def p24_cross(n=5):
    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
p24_cross()'''

##8,Plus (+) Pattern
'''def p25_plus(n=5):
    mid = n // 2

    for i in range(n):
        for j in range(n):
            if i == mid or j == mid:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
p25_plus()'''
