#1 - Reverse Integer
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        rev = rev * sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

#2 - Multiply Strings
class Solution(object):
    def multiply(self, num1, num2):
        
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                position = i + j + 1
                carry_position = i + j

                total = product + result[position]

                result[position] = total % 10
                result[carry_position] += total // 10

    
        while len(result) > 1 and result[0] == 0:
            result.pop(0)

        return ''.join(str(x) for x in result)
            
