#PATTERNS
##1,Basic
'''for i in range(1, 6):
    print("*" * i)'''

##2,Solid Square
'''def solid_square(n=5):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
solid_square()'''

##3,Hollow Square
'''def hollow_square(n=5):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hollow_square()'''

##4,Right Triangle
'''def right_triangle(n=5):
    for i in range(1, n+1):
        print("* " * i)
right_triangle()'''

##5,Inverted Right Triangle
'''def inverted_right_triangle(n=5):
    for i in range(n, 0, -1):
        print("* " * i)
inverted_right_triangle()'''

##6,Mirrored Triangle
'''def mirrored_triangle(n=5):
    for i in range(1, n+1):
        print("  " * (n-i) + "* " * i)
mirrored_triangle()'''

##7,Inverted Mirrored Triangle
'''def inverted_mirrored_triangle(n=5):
    for i in range(n, 0, -1):
        print("  " * (n-i) + "* " * i)
inverted_mirrored_triangle()'''

##8,Hollow Right Triangle
'''def hollow_right_triangle(n=5):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if j == 1 or j == i or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hollow_right_triangle()'''
