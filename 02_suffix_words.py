import unittest

question_02 = """
Given sides of rectangle, return area of rectangle. 
example:
input:
width=10
height=5
output:
50

"""

# Implement the below function and run the program


def area_rectangle(width, height):
    area = width * height
    return area
    pass
width = int(input("Enter the width of the rectangle:"))
height = int(input("Enter the height of the rectangle:"))

print(area_rectangle(width, height))


# do not touch this code
class Area_Rectangle(unittest.TestCase):

    def test_1(self):
        self.assertEqual(area_rectangle(10, 5), 50)

    def test_2(self):
        self.assertEqual(area_rectangle(100, 50), 5000)


if __name__ == '__main__':
    unittest.main(verbosity=2)
