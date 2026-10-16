#PATTERNS
##1,Pyramid
'''def p08_pyramid(n=5):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))
p08_pyramid()'''

##2,Inverted Pyramid
'''def p09_inverted_pyramid(n=5):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "*" * (2*i-1))
p09_inverted_pyramid()'''

##3,Hollow Pyramid
'''def p10_hollow_pyramid(n=5):
    for i in range(1, n+1):
        row = ""
        for j in range(1, 2*i):
            if j == 1 or j == 2*i-1 or i == n:
                row += "*"
            else:
                row += " "
        print(" " * (n-i) + row)
p10_hollow_pyramid()'''

##4,Diamond
'''def p11_diamond(n=5):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "*" * (2*i-1))
p11_diamond()'''

##5,Hollow Diamond
'''def p12_hollow_diamond(n=5):
    def row(i):
        row = ""
        for j in range(1, 2*i):
            row += "*" if j == 1 or j == 2*i-1 else " "
        return " " * (n-i) + row

    for i in range(1, n+1):
        print(row(i))

    for i in range(n-1, 0, -1):
        print(row(i))
p12_hollow_diamond()'''

##6,Hourglass
'''def p13_hourglass(n=5):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "*" * (2*i-1))
    for i in range(2, n+1):
        print(" " * (n-i) + "*" * (2*i-1))
p13_hourglass()'''

##7,Floyd's Triangle
'''def p14_floyds_triangle(n=5):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
p14_floyds_triangle()'''

##8,Number Triangle
'''def p15_number_triangle(n=5):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
p15_number_triangle()'''

##9,Inverted Number Triangle
'''def p16_inv_number_triangle(n=5):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
p16_inv_number_triangle()'''

##10,Repeated Number Triangle
def p17_repeated_number_triangle(n=5):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()
p17_repeated_number_triangle()
