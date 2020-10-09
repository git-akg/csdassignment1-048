import unittest

question_01 = """
Given three numbers a,b,c, return sum of all these numbers
Example:
input:
a=2
b=3
c=5
output:
10
"""

# Implement the below function and run the program


def sum_of_num(a, b, c):
    # write your code here
    sum  = a + b + c
    return sum
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

print(sum_of_num(a, b, c))


# do not touch below code

class Sum_of_Num(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sum_of_num(2,3,5),10)

    def test_2(self):
        self.assertEqual(sum_of_num(10, 3, 5), 18)


if __name__ == '__main__':
    unittest.main(verbosity=2)
