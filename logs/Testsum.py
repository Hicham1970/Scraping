import unittest
# from Generate_unit_tests import sum

# TODO: Ask CodeWhisperer to write unit tests.

def sum(a, b):
    """
    Function to sum two numbers.

    Args:
    - a: First number.
    - b: Second number.

    Returns:
    - Sum of the two numbers.
    """
    return a + b

# Write a test case for the above function.

class TestSum(unittest.TestCase):

    def test_sum_two_positives(self):
        if (self.assertEqual(sum(2, 3), 5)):
            print('Operation  1 reussi')
        else:
            print('Erreur dans l\'addition de deux nombres positifs')

        
        return True # Return True if the test fails and False otherwise

    def test_sum_two_negatives(self):
        if (self.assertEqual(sum(-2, -3), -5)):
            print('Operation 2 reussi')
        else:
            print('Erreur dans l\'addition de deux nombres negatifs')    
        

    def test_sum_positive_negative(self):
        if(self.assertEqual(sum(2, -3), -1)):
            print('Operation 3 reussi')
        else:
            print('Erreur dans l\'addition d\'un nombre positif et un nombre negatif')    

    def test_sum_zeroes(self):
        if(self.assertEqual(sum(0, 0), 0)):
            print('Operation 4 reussi')
        else:
            print('Erreur dans l\'addition de deux nombres nuls')    


print(TestSum().test_sum_two_positives(2, 6)) 
print(TestSum().test_sum_zeroes(0, 0))


if __name__ == '__main__':
    unittest.main()